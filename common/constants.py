"""Central constants and enumerations for the booking platform."""
from __future__ import annotations

from enum import Enum, IntEnum

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    REJECTED = "rejected"
    NO_SHOW = "no_show"
    DRAFT = "draft"
    HOLD = "hold"

BOOKINGSTATUS_LABELS = {
    BookingStatus.PENDING: "Pending",
    BookingStatus.CONFIRMED: "Confirmed",
    BookingStatus.CANCELLED: "Cancelled",
    BookingStatus.COMPLETED: "Completed",
    BookingStatus.REJECTED: "Rejected",
    BookingStatus.NO_SHOW: "No Show",
    BookingStatus.DRAFT: "Draft",
    BookingStatus.HOLD: "Hold",
}

def is_valid_bookingstatus(value: str) -> bool:
    try:
        BookingStatus(value)
        return True
    except ValueError:
        return False

class ResourceStatus(str, Enum):
    ACTIVE = "active"
    MAINTENANCE = "maintenance"
    INACTIVE = "inactive"
    RETIRED = "retired"
    HIDDEN = "hidden"

RESOURCESTATUS_LABELS = {
    ResourceStatus.ACTIVE: "Active",
    ResourceStatus.MAINTENANCE: "Maintenance",
    ResourceStatus.INACTIVE: "Inactive",
    ResourceStatus.RETIRED: "Retired",
    ResourceStatus.HIDDEN: "Hidden",
}

def is_valid_resourcestatus(value: str) -> bool:
    try:
        ResourceStatus(value)
        return True
    except ValueError:
        return False

class UserRole(str, Enum):
    ADMIN = "admin"
    STAFF = "staff"
    USER = "user"
    GUEST = "guest"
    MANAGER = "manager"
    VIEWER = "viewer"

USERROLE_LABELS = {
    UserRole.ADMIN: "Admin",
    UserRole.STAFF: "Staff",
    UserRole.USER: "User",
    UserRole.GUEST: "Guest",
    UserRole.MANAGER: "Manager",
    UserRole.VIEWER: "Viewer",
}

def is_valid_userrole(value: str) -> bool:
    try:
        UserRole(value)
        return True
    except ValueError:
        return False

class NotificationChannel(str, Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
    SLACK = "slack"
    WEBHOOK = "webhook"
    IN_APP = "in_app"

NOTIFICATIONCHANNEL_LABELS = {
    NotificationChannel.EMAIL: "Email",
    NotificationChannel.SMS: "Sms",
    NotificationChannel.PUSH: "Push",
    NotificationChannel.SLACK: "Slack",
    NotificationChannel.WEBHOOK: "Webhook",
    NotificationChannel.IN_APP: "In App",
}

def is_valid_notificationchannel(value: str) -> bool:
    try:
        NotificationChannel(value)
        return True
    except ValueError:
        return False

class ExportFormat(str, Enum):
    CSV = "csv"
    JSON = "json"
    ICAL = "ical"
    XLSX = "xlsx"
    PDF = "pdf"

EXPORTFORMAT_LABELS = {
    ExportFormat.CSV: "Csv",
    ExportFormat.JSON: "Json",
    ExportFormat.ICAL: "Ical",
    ExportFormat.XLSX: "Xlsx",
    ExportFormat.PDF: "Pdf",
}

def is_valid_exportformat(value: str) -> bool:
    try:
        ExportFormat(value)
        return True
    except ValueError:
        return False

class WebhookEventType(str, Enum):
    BOOKING_CREATED = "booking_created"
    BOOKING_UPDATED = "booking_updated"
    BOOKING_CANCELLED = "booking_cancelled"
    BOOKING_APPROVED = "booking_approved"
    BOOKING_REJECTED = "booking_rejected"
    RESOURCE_CREATED = "resource_created"
    RESOURCE_UPDATED = "resource_updated"
    USER_CREATED = "user_created"

WEBHOOKEVENTTYPE_LABELS = {
    WebhookEventType.BOOKING_CREATED: "Booking Created",
    WebhookEventType.BOOKING_UPDATED: "Booking Updated",
    WebhookEventType.BOOKING_CANCELLED: "Booking Cancelled",
    WebhookEventType.BOOKING_APPROVED: "Booking Approved",
    WebhookEventType.BOOKING_REJECTED: "Booking Rejected",
    WebhookEventType.RESOURCE_CREATED: "Resource Created",
    WebhookEventType.RESOURCE_UPDATED: "Resource Updated",
    WebhookEventType.USER_CREATED: "User Created",
}

def is_valid_webhookeventtype(value: str) -> bool:
    try:
        WebhookEventType(value)
        return True
    except ValueError:
        return False

class AuditActionType(str, Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    CANCEL = "cancel"
    APPROVE = "approve"
    REJECT = "reject"
    LOGIN = "login"
    LOGOUT = "logout"
    EXPORT = "export"
    IMPORT = "import"
    WEBHOOK = "webhook"
    SYSTEM = "system"
    VIEW = "view"
    DOWNLOAD = "download"

AUDITACTIONTYPE_LABELS = {
    AuditActionType.CREATE: "Create",
    AuditActionType.UPDATE: "Update",
    AuditActionType.DELETE: "Delete",
    AuditActionType.CANCEL: "Cancel",
    AuditActionType.APPROVE: "Approve",
    AuditActionType.REJECT: "Reject",
    AuditActionType.LOGIN: "Login",
    AuditActionType.LOGOUT: "Logout",
    AuditActionType.EXPORT: "Export",
    AuditActionType.IMPORT: "Import",
    AuditActionType.WEBHOOK: "Webhook",
    AuditActionType.SYSTEM: "System",
    AuditActionType.VIEW: "View",
    AuditActionType.DOWNLOAD: "Download",
}

def is_valid_auditactiontype(value: str) -> bool:
    try:
        AuditActionType(value)
        return True
    except ValueError:
        return False

DEFAULT_LIMIT_0 = 10
MAX_LIMIT_0 = 100
TIMEOUT_SECONDS_0 = 5
CACHE_TTL_0 = 60

DEFAULT_LIMIT_1 = 13
MAX_LIMIT_1 = 110
TIMEOUT_SECONDS_1 = 6
CACHE_TTL_1 = 120

DEFAULT_LIMIT_2 = 16
MAX_LIMIT_2 = 120
TIMEOUT_SECONDS_2 = 7
CACHE_TTL_2 = 180

DEFAULT_LIMIT_3 = 19
MAX_LIMIT_3 = 130
TIMEOUT_SECONDS_3 = 8
CACHE_TTL_3 = 240

DEFAULT_LIMIT_4 = 22
MAX_LIMIT_4 = 140
TIMEOUT_SECONDS_4 = 9
CACHE_TTL_4 = 300

DEFAULT_LIMIT_5 = 25
MAX_LIMIT_5 = 150
TIMEOUT_SECONDS_5 = 10
CACHE_TTL_5 = 360

DEFAULT_LIMIT_6 = 28
MAX_LIMIT_6 = 160
TIMEOUT_SECONDS_6 = 11
CACHE_TTL_6 = 420

DEFAULT_LIMIT_7 = 31
MAX_LIMIT_7 = 170
TIMEOUT_SECONDS_7 = 12
CACHE_TTL_7 = 480

DEFAULT_LIMIT_8 = 34
MAX_LIMIT_8 = 180
TIMEOUT_SECONDS_8 = 13
CACHE_TTL_8 = 540

DEFAULT_LIMIT_9 = 37
MAX_LIMIT_9 = 190
TIMEOUT_SECONDS_9 = 14
CACHE_TTL_9 = 600

DEFAULT_LIMIT_10 = 40
MAX_LIMIT_10 = 200
TIMEOUT_SECONDS_10 = 15
CACHE_TTL_10 = 660

DEFAULT_LIMIT_11 = 43
MAX_LIMIT_11 = 210
TIMEOUT_SECONDS_11 = 16
CACHE_TTL_11 = 720

DEFAULT_LIMIT_12 = 46
MAX_LIMIT_12 = 220
TIMEOUT_SECONDS_12 = 17
CACHE_TTL_12 = 780

DEFAULT_LIMIT_13 = 49
MAX_LIMIT_13 = 230
TIMEOUT_SECONDS_13 = 18
CACHE_TTL_13 = 840

DEFAULT_LIMIT_14 = 52
MAX_LIMIT_14 = 240
TIMEOUT_SECONDS_14 = 19
CACHE_TTL_14 = 900

DEFAULT_LIMIT_15 = 55
MAX_LIMIT_15 = 250
TIMEOUT_SECONDS_15 = 20
CACHE_TTL_15 = 960

DEFAULT_LIMIT_16 = 58
MAX_LIMIT_16 = 260
TIMEOUT_SECONDS_16 = 21
CACHE_TTL_16 = 1020

DEFAULT_LIMIT_17 = 61
MAX_LIMIT_17 = 270
TIMEOUT_SECONDS_17 = 22
CACHE_TTL_17 = 1080

DEFAULT_LIMIT_18 = 64
MAX_LIMIT_18 = 280
TIMEOUT_SECONDS_18 = 23
CACHE_TTL_18 = 1140

DEFAULT_LIMIT_19 = 67
MAX_LIMIT_19 = 290
TIMEOUT_SECONDS_19 = 24
CACHE_TTL_19 = 1200

DEFAULT_LIMIT_20 = 70
MAX_LIMIT_20 = 300
TIMEOUT_SECONDS_20 = 25
CACHE_TTL_20 = 1260

DEFAULT_LIMIT_21 = 73
MAX_LIMIT_21 = 310
TIMEOUT_SECONDS_21 = 26
CACHE_TTL_21 = 1320

DEFAULT_LIMIT_22 = 76
MAX_LIMIT_22 = 320
TIMEOUT_SECONDS_22 = 27
CACHE_TTL_22 = 1380

DEFAULT_LIMIT_23 = 79
MAX_LIMIT_23 = 330
TIMEOUT_SECONDS_23 = 28
CACHE_TTL_23 = 1440

DEFAULT_LIMIT_24 = 82
MAX_LIMIT_24 = 340
TIMEOUT_SECONDS_24 = 29
CACHE_TTL_24 = 1500

DEFAULT_LIMIT_25 = 85
MAX_LIMIT_25 = 350
TIMEOUT_SECONDS_25 = 30
CACHE_TTL_25 = 1560

DEFAULT_LIMIT_26 = 88
MAX_LIMIT_26 = 360
TIMEOUT_SECONDS_26 = 31
CACHE_TTL_26 = 1620

DEFAULT_LIMIT_27 = 91
MAX_LIMIT_27 = 370
TIMEOUT_SECONDS_27 = 32
CACHE_TTL_27 = 1680

DEFAULT_LIMIT_28 = 94
MAX_LIMIT_28 = 380
TIMEOUT_SECONDS_28 = 33
CACHE_TTL_28 = 1740

DEFAULT_LIMIT_29 = 97
MAX_LIMIT_29 = 390
TIMEOUT_SECONDS_29 = 34
CACHE_TTL_29 = 1800

DEFAULT_LIMIT_30 = 100
MAX_LIMIT_30 = 400
TIMEOUT_SECONDS_30 = 35
CACHE_TTL_30 = 1860

DEFAULT_LIMIT_31 = 103
MAX_LIMIT_31 = 410
TIMEOUT_SECONDS_31 = 36
CACHE_TTL_31 = 1920

DEFAULT_LIMIT_32 = 106
MAX_LIMIT_32 = 420
TIMEOUT_SECONDS_32 = 37
CACHE_TTL_32 = 1980

DEFAULT_LIMIT_33 = 109
MAX_LIMIT_33 = 430
TIMEOUT_SECONDS_33 = 38
CACHE_TTL_33 = 2040

DEFAULT_LIMIT_34 = 112
MAX_LIMIT_34 = 440
TIMEOUT_SECONDS_34 = 39
CACHE_TTL_34 = 2100

DEFAULT_LIMIT_35 = 115
MAX_LIMIT_35 = 450
TIMEOUT_SECONDS_35 = 40
CACHE_TTL_35 = 2160

DEFAULT_LIMIT_36 = 118
MAX_LIMIT_36 = 460
TIMEOUT_SECONDS_36 = 41
CACHE_TTL_36 = 2220

DEFAULT_LIMIT_37 = 121
MAX_LIMIT_37 = 470
TIMEOUT_SECONDS_37 = 42
CACHE_TTL_37 = 2280

DEFAULT_LIMIT_38 = 124
MAX_LIMIT_38 = 480
TIMEOUT_SECONDS_38 = 43
CACHE_TTL_38 = 2340

DEFAULT_LIMIT_39 = 127
MAX_LIMIT_39 = 490
TIMEOUT_SECONDS_39 = 44
CACHE_TTL_39 = 2400

DEFAULT_LIMIT_40 = 130
MAX_LIMIT_40 = 500
TIMEOUT_SECONDS_40 = 45
CACHE_TTL_40 = 2460

DEFAULT_LIMIT_41 = 133
MAX_LIMIT_41 = 510
TIMEOUT_SECONDS_41 = 46
CACHE_TTL_41 = 2520

DEFAULT_LIMIT_42 = 136
MAX_LIMIT_42 = 520
TIMEOUT_SECONDS_42 = 47
CACHE_TTL_42 = 2580

DEFAULT_LIMIT_43 = 139
MAX_LIMIT_43 = 530
TIMEOUT_SECONDS_43 = 48
CACHE_TTL_43 = 2640

DEFAULT_LIMIT_44 = 142
MAX_LIMIT_44 = 540
TIMEOUT_SECONDS_44 = 49
CACHE_TTL_44 = 2700

DEFAULT_LIMIT_45 = 145
MAX_LIMIT_45 = 550
TIMEOUT_SECONDS_45 = 50
CACHE_TTL_45 = 2760

DEFAULT_LIMIT_46 = 148
MAX_LIMIT_46 = 560
TIMEOUT_SECONDS_46 = 51
CACHE_TTL_46 = 2820

DEFAULT_LIMIT_47 = 151
MAX_LIMIT_47 = 570
TIMEOUT_SECONDS_47 = 52
CACHE_TTL_47 = 2880

DEFAULT_LIMIT_48 = 154
MAX_LIMIT_48 = 580
TIMEOUT_SECONDS_48 = 53
CACHE_TTL_48 = 2940

DEFAULT_LIMIT_49 = 157
MAX_LIMIT_49 = 590
TIMEOUT_SECONDS_49 = 54
CACHE_TTL_49 = 3000
