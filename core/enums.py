from enum import Enum

class Role(Enum):
    ADMIN:str = "admin"
    LEAD_MANAGER:str = "lead_manager"
    PROJECT_MANAGER:str = "project_manager"
    ACCOUNTANT:str = "account_manager"


class Status(Enum):
    NEW:str = "new"
    CONTACTED:str = "contacted"
    QULIFIED:str= "qualified"
    PROPOSAL:str= "proposal"
    NEGOTIATION:str= "negotiation"
    LOST:str= "lost"
    ACTIVE:str = "active"
    PAID:str = "paid"


class PaymentMethod(Enum):
    BANK_TRANSFER:str = "bank transfer"
    CASH:str = "cash"
    CHEQUE:str = "cheque"
    UPI:str = "upi"

class Permission(str, Enum):
    REPORT_CREATE = "report:create"
    REPORT_READ = "report:read"
    REPORT_UPDATE = "report:update"
    REPORT_DELETE = "report:delete"
    USER_READ = "user:read"
    USER_UPDATE = "user:update"
    USER_CREATE = "user:create"
    USER_DELETE = "user:delete"
    LEAD_CREATE = "lead:create"
    LEAD_READ = "lead:read"
    LEAD_UPDATE = "lead:update"
    LEAD_DELETE = "lead:delete"
    CUSTOMER_CREATE = "customer:create"
    CUSTOMER_READ = "customer:read"
    CUSTOMER_UPDATE = "customer:update"
    CUSTOMER_DELETE = "customer:delete"
    INVOICE_READ = "invoice:read"
    INVOICE_CREATE = "invoice:create"
    INVOICE_UPDATE = "invoice:update"
    INVOICE_DELETE = "invoice:DELETE"
    PRODUCT_READ = "product:read"
    PRODUCT_CREATE = "product:create"
    PRODUCT_UPDATE = "product:update"
    PRODUCT_DELETE = "product:delete"
    ROLE_CREATE = "role:create"
    ROLE_READ = "role:read"
    ROLE_UPDATE = "role:update"
    ROLE_DELETE = "role:delete"
    DASHBOARD = "dashboad:read"
    AI_CHAT = "ai:chat"
    NOTIFICATIONS = "notification:create"
    SITE_SETTINGS = "site:settings"
    IMPERSONITION = "user:impersonition"




