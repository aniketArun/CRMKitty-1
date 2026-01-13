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