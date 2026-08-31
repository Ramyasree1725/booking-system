
"""Recurring booking expansion using a simplified RRULE subset."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Iterator, List, Optional, Set

from django.utils import timezone


FREQ_DAILY = "DAILY"
FREQ_WEEKLY = "WEEKLY"
FREQ_MONTHLY = "MONTHLY"


@dataclass
class RecurrenceRule:
    freq: str = FREQ_WEEKLY
    interval: int = 1
    count: Optional[int] = None
    until: Optional[datetime] = None
    byweekday: Optional[Set[int]] = None  # 0=Mon .. 6=Sun

    @classmethod
    def parse(cls, rrule: str) -> "RecurrenceRule":
        """Parse a subset of RRULE: FREQ, INTERVAL, COUNT, UNTIL, BYDAY."""
        parts = {}
        for piece in rrule.upper().replace("RRULE:", "").split(";"):
            if "=" in piece:
                k, v = piece.split("=", 1)
                parts[k.strip()] = v.strip()
        freq = parts.get("FREQ", FREQ_WEEKLY)
        interval = int(parts.get("INTERVAL", "1"))
        count = int(parts["COUNT"]) if "COUNT" in parts else None
        until = None
        if "UNTIL" in parts:
            raw = parts["UNTIL"]
            # YYYYMMDD or YYYYMMDDTHHMMSSZ
            if "T" in raw:
                until = datetime.strptime(raw.replace("Z", ""), "%Y%m%dT%H%M%S")
                until = timezone.make_aware(until)
            else:
                until = datetime.strptime(raw, "%Y%m%d")
                until = timezone.make_aware(until)
        byweekday = None
        if "BYDAY" in parts:
            mapping = {"MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4, "SA": 5, "SU": 6}
            byweekday = set()
            for token in parts["BYDAY"].split(","):
                token = token.strip()
                # strip leading ordinal like 1MO or -1FR
                letters = "".join(c for c in token if c.isalpha())
                if letters in mapping:
                    byweekday.add(mapping[letters])
        return cls(freq=freq, interval=interval, count=count, until=until, byweekday=byweekday)

    def to_rrule(self) -> str:
        parts = [f"FREQ={self.freq}", f"INTERVAL={self.interval}"]
        if self.count is not None:
            parts.append(f"COUNT={self.count}")
        if self.until is not None:
            parts.append(f"UNTIL={self.until.strftime('%Y%m%dT%H%M%SZ')}")
        if self.byweekday:
            inv = {0: "MO", 1: "TU", 2: "WE", 3: "TH", 4: "FR", 5: "SA", 6: "SU"}
            days = ",".join(inv[d] for d in sorted(self.byweekday))
            parts.append(f"BYDAY={days}")
        return ";".join(parts)


def iter_occurrences(
    start: datetime,
    end: datetime,
    rule: RecurrenceRule,
    max_occurrences: int = 365,
) -> Iterator[tuple]:
    """Yield (occ_start, occ_end) pairs."""
    duration = end - start
    current_start = start
    emitted = 0
    hard_limit = max_occurrences if rule.count is None else min(max_occurrences, rule.count)

    while emitted < hard_limit:
        if rule.until and current_start > rule.until:
            break
        if rule.byweekday is None or current_start.weekday() in rule.byweekday:
            yield current_start, current_start + duration
            emitted += 1
            if rule.count is not None and emitted >= rule.count:
                break

        if rule.freq == FREQ_DAILY:
            current_start = current_start + timedelta(days=rule.interval)
        elif rule.freq == FREQ_WEEKLY:
            current_start = current_start + timedelta(weeks=rule.interval)
        elif rule.freq == FREQ_MONTHLY:
            # naive month increment
            month = current_start.month + rule.interval
            year = current_start.year + (month - 1) // 12
            month = (month - 1) % 12 + 1
            day = min(current_start.day, _days_in_month(year, month))
            current_start = current_start.replace(year=year, month=month, day=day)
        else:
            break


def _days_in_month(year: int, month: int) -> int:
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    this_month = datetime(year, month, 1)
    return (next_month - this_month).days


def expand_booking_dates(
    start: datetime,
    end: datetime,
    rrule_str: str,
    max_occurrences: int = 52,
) -> List[tuple]:
    rule = RecurrenceRule.parse(rrule_str)
    return list(iter_occurrences(start, end, rule, max_occurrences=max_occurrences))
