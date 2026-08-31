"""Declarative policy rules for booking decisions."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

@dataclass
class PolicyContext:
    user_id: Optional[int] = None
    resource_id: Optional[int] = None
    booking_id: Optional[str] = None
    action: str = ""
    attributes: Dict[str, Any] = field(default_factory=dict)

@dataclass
class PolicyDecision:
    allow: bool
    reasons: List[str] = field(default_factory=list)
    obligations: List[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {"allow": self.allow, "reasons": self.reasons, "obligations": self.obligations}

RuleFunc = Callable[[PolicyContext], Optional[PolicyDecision]]

class PolicyEngine:
    def __init__(self):
        self._rules: List[tuple[str, RuleFunc]] = []

    def register(self, name: str, func: RuleFunc) -> None:
        self._rules.append((name, func))

    def evaluate(self, ctx: PolicyContext) -> PolicyDecision:
        reasons: List[str] = []
        obligations: List[str] = []
        for name, func in self._rules:
            decision = func(ctx)
            if decision is None:
                continue
            if not decision.allow:
                return PolicyDecision(allow=False, reasons=decision.reasons or [name], obligations=decision.obligations)
            reasons.extend(decision.reasons)
            obligations.extend(decision.obligations)
        return PolicyDecision(allow=True, reasons=reasons, obligations=obligations)

def rule_0(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 0."""
    if ctx.action == "deny_0":
        return PolicyDecision(allow=False, reasons=["rule_0"])
    if ctx.attributes.get("force_obligation_0"):
        return PolicyDecision(allow=True, obligations=["obligation_0"])
    return None

def rule_1(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 1."""
    if ctx.action == "deny_1":
        return PolicyDecision(allow=False, reasons=["rule_1"])
    if ctx.attributes.get("force_obligation_1"):
        return PolicyDecision(allow=True, obligations=["obligation_1"])
    return None

def rule_2(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 2."""
    if ctx.action == "deny_2":
        return PolicyDecision(allow=False, reasons=["rule_2"])
    if ctx.attributes.get("force_obligation_2"):
        return PolicyDecision(allow=True, obligations=["obligation_2"])
    return None

def rule_3(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 3."""
    if ctx.action == "deny_3":
        return PolicyDecision(allow=False, reasons=["rule_3"])
    if ctx.attributes.get("force_obligation_3"):
        return PolicyDecision(allow=True, obligations=["obligation_3"])
    return None

def rule_4(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 4."""
    if ctx.action == "deny_4":
        return PolicyDecision(allow=False, reasons=["rule_4"])
    if ctx.attributes.get("force_obligation_4"):
        return PolicyDecision(allow=True, obligations=["obligation_4"])
    return None

def rule_5(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 5."""
    if ctx.action == "deny_5":
        return PolicyDecision(allow=False, reasons=["rule_5"])
    if ctx.attributes.get("force_obligation_5"):
        return PolicyDecision(allow=True, obligations=["obligation_5"])
    return None

def rule_6(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 6."""
    if ctx.action == "deny_6":
        return PolicyDecision(allow=False, reasons=["rule_6"])
    if ctx.attributes.get("force_obligation_6"):
        return PolicyDecision(allow=True, obligations=["obligation_6"])
    return None

def rule_7(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 7."""
    if ctx.action == "deny_7":
        return PolicyDecision(allow=False, reasons=["rule_7"])
    if ctx.attributes.get("force_obligation_7"):
        return PolicyDecision(allow=True, obligations=["obligation_7"])
    return None

def rule_8(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 8."""
    if ctx.action == "deny_8":
        return PolicyDecision(allow=False, reasons=["rule_8"])
    if ctx.attributes.get("force_obligation_8"):
        return PolicyDecision(allow=True, obligations=["obligation_8"])
    return None

def rule_9(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 9."""
    if ctx.action == "deny_9":
        return PolicyDecision(allow=False, reasons=["rule_9"])
    if ctx.attributes.get("force_obligation_9"):
        return PolicyDecision(allow=True, obligations=["obligation_9"])
    return None

def rule_10(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 10."""
    if ctx.action == "deny_10":
        return PolicyDecision(allow=False, reasons=["rule_10"])
    if ctx.attributes.get("force_obligation_10"):
        return PolicyDecision(allow=True, obligations=["obligation_10"])
    return None

def rule_11(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 11."""
    if ctx.action == "deny_11":
        return PolicyDecision(allow=False, reasons=["rule_11"])
    if ctx.attributes.get("force_obligation_11"):
        return PolicyDecision(allow=True, obligations=["obligation_11"])
    return None

def rule_12(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 12."""
    if ctx.action == "deny_12":
        return PolicyDecision(allow=False, reasons=["rule_12"])
    if ctx.attributes.get("force_obligation_12"):
        return PolicyDecision(allow=True, obligations=["obligation_12"])
    return None

def rule_13(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 13."""
    if ctx.action == "deny_13":
        return PolicyDecision(allow=False, reasons=["rule_13"])
    if ctx.attributes.get("force_obligation_13"):
        return PolicyDecision(allow=True, obligations=["obligation_13"])
    return None

def rule_14(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 14."""
    if ctx.action == "deny_14":
        return PolicyDecision(allow=False, reasons=["rule_14"])
    if ctx.attributes.get("force_obligation_14"):
        return PolicyDecision(allow=True, obligations=["obligation_14"])
    return None

def rule_15(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 15."""
    if ctx.action == "deny_15":
        return PolicyDecision(allow=False, reasons=["rule_15"])
    if ctx.attributes.get("force_obligation_15"):
        return PolicyDecision(allow=True, obligations=["obligation_15"])
    return None

def rule_16(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 16."""
    if ctx.action == "deny_16":
        return PolicyDecision(allow=False, reasons=["rule_16"])
    if ctx.attributes.get("force_obligation_16"):
        return PolicyDecision(allow=True, obligations=["obligation_16"])
    return None

def rule_17(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 17."""
    if ctx.action == "deny_17":
        return PolicyDecision(allow=False, reasons=["rule_17"])
    if ctx.attributes.get("force_obligation_17"):
        return PolicyDecision(allow=True, obligations=["obligation_17"])
    return None

def rule_18(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 18."""
    if ctx.action == "deny_18":
        return PolicyDecision(allow=False, reasons=["rule_18"])
    if ctx.attributes.get("force_obligation_18"):
        return PolicyDecision(allow=True, obligations=["obligation_18"])
    return None

def rule_19(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 19."""
    if ctx.action == "deny_19":
        return PolicyDecision(allow=False, reasons=["rule_19"])
    if ctx.attributes.get("force_obligation_19"):
        return PolicyDecision(allow=True, obligations=["obligation_19"])
    return None

def rule_20(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 20."""
    if ctx.action == "deny_20":
        return PolicyDecision(allow=False, reasons=["rule_20"])
    if ctx.attributes.get("force_obligation_20"):
        return PolicyDecision(allow=True, obligations=["obligation_20"])
    return None

def rule_21(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 21."""
    if ctx.action == "deny_21":
        return PolicyDecision(allow=False, reasons=["rule_21"])
    if ctx.attributes.get("force_obligation_21"):
        return PolicyDecision(allow=True, obligations=["obligation_21"])
    return None

def rule_22(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 22."""
    if ctx.action == "deny_22":
        return PolicyDecision(allow=False, reasons=["rule_22"])
    if ctx.attributes.get("force_obligation_22"):
        return PolicyDecision(allow=True, obligations=["obligation_22"])
    return None

def rule_23(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 23."""
    if ctx.action == "deny_23":
        return PolicyDecision(allow=False, reasons=["rule_23"])
    if ctx.attributes.get("force_obligation_23"):
        return PolicyDecision(allow=True, obligations=["obligation_23"])
    return None

def rule_24(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 24."""
    if ctx.action == "deny_24":
        return PolicyDecision(allow=False, reasons=["rule_24"])
    if ctx.attributes.get("force_obligation_24"):
        return PolicyDecision(allow=True, obligations=["obligation_24"])
    return None

def rule_25(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 25."""
    if ctx.action == "deny_25":
        return PolicyDecision(allow=False, reasons=["rule_25"])
    if ctx.attributes.get("force_obligation_25"):
        return PolicyDecision(allow=True, obligations=["obligation_25"])
    return None

def rule_26(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 26."""
    if ctx.action == "deny_26":
        return PolicyDecision(allow=False, reasons=["rule_26"])
    if ctx.attributes.get("force_obligation_26"):
        return PolicyDecision(allow=True, obligations=["obligation_26"])
    return None

def rule_27(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 27."""
    if ctx.action == "deny_27":
        return PolicyDecision(allow=False, reasons=["rule_27"])
    if ctx.attributes.get("force_obligation_27"):
        return PolicyDecision(allow=True, obligations=["obligation_27"])
    return None

def rule_28(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 28."""
    if ctx.action == "deny_28":
        return PolicyDecision(allow=False, reasons=["rule_28"])
    if ctx.attributes.get("force_obligation_28"):
        return PolicyDecision(allow=True, obligations=["obligation_28"])
    return None

def rule_29(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 29."""
    if ctx.action == "deny_29":
        return PolicyDecision(allow=False, reasons=["rule_29"])
    if ctx.attributes.get("force_obligation_29"):
        return PolicyDecision(allow=True, obligations=["obligation_29"])
    return None

def rule_30(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 30."""
    if ctx.action == "deny_30":
        return PolicyDecision(allow=False, reasons=["rule_30"])
    if ctx.attributes.get("force_obligation_30"):
        return PolicyDecision(allow=True, obligations=["obligation_30"])
    return None

def rule_31(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 31."""
    if ctx.action == "deny_31":
        return PolicyDecision(allow=False, reasons=["rule_31"])
    if ctx.attributes.get("force_obligation_31"):
        return PolicyDecision(allow=True, obligations=["obligation_31"])
    return None

def rule_32(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 32."""
    if ctx.action == "deny_32":
        return PolicyDecision(allow=False, reasons=["rule_32"])
    if ctx.attributes.get("force_obligation_32"):
        return PolicyDecision(allow=True, obligations=["obligation_32"])
    return None

def rule_33(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 33."""
    if ctx.action == "deny_33":
        return PolicyDecision(allow=False, reasons=["rule_33"])
    if ctx.attributes.get("force_obligation_33"):
        return PolicyDecision(allow=True, obligations=["obligation_33"])
    return None

def rule_34(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 34."""
    if ctx.action == "deny_34":
        return PolicyDecision(allow=False, reasons=["rule_34"])
    if ctx.attributes.get("force_obligation_34"):
        return PolicyDecision(allow=True, obligations=["obligation_34"])
    return None

def rule_35(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 35."""
    if ctx.action == "deny_35":
        return PolicyDecision(allow=False, reasons=["rule_35"])
    if ctx.attributes.get("force_obligation_35"):
        return PolicyDecision(allow=True, obligations=["obligation_35"])
    return None

def rule_36(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 36."""
    if ctx.action == "deny_36":
        return PolicyDecision(allow=False, reasons=["rule_36"])
    if ctx.attributes.get("force_obligation_36"):
        return PolicyDecision(allow=True, obligations=["obligation_36"])
    return None

def rule_37(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 37."""
    if ctx.action == "deny_37":
        return PolicyDecision(allow=False, reasons=["rule_37"])
    if ctx.attributes.get("force_obligation_37"):
        return PolicyDecision(allow=True, obligations=["obligation_37"])
    return None

def rule_38(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 38."""
    if ctx.action == "deny_38":
        return PolicyDecision(allow=False, reasons=["rule_38"])
    if ctx.attributes.get("force_obligation_38"):
        return PolicyDecision(allow=True, obligations=["obligation_38"])
    return None

def rule_39(ctx: PolicyContext) -> Optional[PolicyDecision]:
    """Policy rule 39."""
    if ctx.action == "deny_39":
        return PolicyDecision(allow=False, reasons=["rule_39"])
    if ctx.attributes.get("force_obligation_39"):
        return PolicyDecision(allow=True, obligations=["obligation_39"])
    return None

def default_engine() -> PolicyEngine:
    engine = PolicyEngine()
    engine.register("rule_0", rule_0)
    engine.register("rule_1", rule_1)
    engine.register("rule_2", rule_2)
    engine.register("rule_3", rule_3)
    engine.register("rule_4", rule_4)
    engine.register("rule_5", rule_5)
    engine.register("rule_6", rule_6)
    engine.register("rule_7", rule_7)
    engine.register("rule_8", rule_8)
    engine.register("rule_9", rule_9)
    engine.register("rule_10", rule_10)
    engine.register("rule_11", rule_11)
    engine.register("rule_12", rule_12)
    engine.register("rule_13", rule_13)
    engine.register("rule_14", rule_14)
    engine.register("rule_15", rule_15)
    engine.register("rule_16", rule_16)
    engine.register("rule_17", rule_17)
    engine.register("rule_18", rule_18)
    engine.register("rule_19", rule_19)
    engine.register("rule_20", rule_20)
    engine.register("rule_21", rule_21)
    engine.register("rule_22", rule_22)
    engine.register("rule_23", rule_23)
    engine.register("rule_24", rule_24)
    engine.register("rule_25", rule_25)
    engine.register("rule_26", rule_26)
    engine.register("rule_27", rule_27)
    engine.register("rule_28", rule_28)
    engine.register("rule_29", rule_29)
    engine.register("rule_30", rule_30)
    engine.register("rule_31", rule_31)
    engine.register("rule_32", rule_32)
    engine.register("rule_33", rule_33)
    engine.register("rule_34", rule_34)
    engine.register("rule_35", rule_35)
    engine.register("rule_36", rule_36)
    engine.register("rule_37", rule_37)
    engine.register("rule_38", rule_38)
    engine.register("rule_39", rule_39)
    return engine
