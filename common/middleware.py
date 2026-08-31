
"""Custom middleware: request timing, correlation IDs, and soft rate hints."""
from __future__ import annotations

import logging
import time
import uuid
from typing import Callable

from django.http import HttpRequest, HttpResponse

logger = logging.getLogger("booking.request")


class RequestIDMiddleware:
    """Attach X-Request-ID to every request/response."""

    HEADER = "HTTP_X_REQUEST_ID"
    RESPONSE_HEADER = "X-Request-ID"

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        request_id = request.META.get(self.HEADER) or str(uuid.uuid4())
        request.request_id = request_id  # type: ignore[attr-defined]
        response = self.get_response(request)
        response[self.RESPONSE_HEADER] = request_id
        return response


class RequestTimingMiddleware:
    """Log slow requests and set Server-Timing style header."""

    SLOW_MS = 1000

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        start = time.perf_counter()
        response = self.get_response(request)
        elapsed_ms = (time.perf_counter() - start) * 1000
        response["X-Response-Time-Ms"] = f"{elapsed_ms:.1f}"
        if elapsed_ms >= self.SLOW_MS:
            logger.warning(
                "slow_request path=%s method=%s ms=%.1f user=%s",
                request.path,
                request.method,
                elapsed_ms,
                getattr(request.user, "pk", None),
            )
        return response


class SecurityHeadersMiddleware:
    """Add conservative security headers for API + HTML responses."""

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = self.get_response(request)
        response.setdefault("X-Content-Type-Options", "nosniff")
        response.setdefault("X-Frame-Options", "DENY")
        response.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.setdefault("Permissions-Policy", "geolocation=(), microphone=(), camera=()")
        return response
