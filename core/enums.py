from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    LEAD_MANAGER = "lead_manager"
    PROJECT_MANAGER = "project_manager"
    ACCOUNTANT = "account_manager"


class Status(Enum):
    NEW = "new"
    CONTACTED = "contacted"
    QULIFIED= "qualified"
    PROPOSAL= "proposal"
    NEGOTIATION= "negotiation"
    LOST= "lost"