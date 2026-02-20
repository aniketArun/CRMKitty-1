from db.models.user import User
from db.models.lead import Lead
from db.models.activity_log import ActivityLog
from db.models.customer import Customer
from db.models.product import Product
from db.models.invoice import Invoice
from db.models.report import Report
from db.models.role import Role
from db.models.company import Company
from db.models.follow_up import FollowUp

from datetime import datetime, date
from sqlalchemy.orm import Session
from core.enums import Permission, Status 
from core.enums import Role as eRole


class SeedModel():
    def __init__(self, db:Session):
        self.db = db

    def seed_companies(self):
        companies = [
            Company(
                name="TechNova Inc.",
                email="contact@technova.com",
                phone="+1-555-1234",
                logo="technova_logo.png",
                currency="USD",
                timezone="America/New_York",
                billing_email="billing@technova.com",
                tax_id="TN123456",
                billing_address="123 Innovation Drive, New York, NY",
                created_at=datetime.now(),
                updated_at=None,
                updated_by=None,
                plan_id=1,
                license_id=101
            ),
            Company(
                name="GreenLeaf Solutions",
                email="info@greenleaf.com",
                phone="+44-20-1234-5678",
                logo="greenleaf_logo.png",
                currency="GBP",
                timezone="Europe/London",
                billing_email="accounts@greenleaf.com",
                tax_id="GL987654",
                billing_address="45 Eco Street, London, UK",
                created_at=datetime.now(),
                updated_at=None,
                updated_by=None,
                plan_id=2,
                license_id=202
            ),
            Company(
                name="GlobalMart",
                email="support@globalmart.com",
                phone="+91-98765-43210",
                logo="globalmart_logo.png",
                currency="INR",
                timezone="Asia/Kolkata",
                billing_email="finance@globalmart.com",
                tax_id="GM567890",
                billing_address="78 Market Road, Bengaluru, India",
                created_at=datetime.now(),
                updated_at=None,
                updated_by=None,
                plan_id=3,
                license_id=303
            )
        ]

        self.db.bulk_save_objects(companies)
        self.db.commit()
        print("Company Seed data inserted successfully!")

    def seed_roles(self, company_id: int = 1, created_by: int = 1):
        roles = [
            Role(
                name=eRole.ADMIN.value,
                permissions=[
                    Permission.REPORT_CREATE,
                    Permission.REPORT_READ,
                    Permission.REPORT_UPDATE,
                    Permission.REPORT_DELETE,
                    Permission.USER_CREATE,
                    Permission.USER_READ,
                    Permission.USER_UPDATE,
                    Permission.USER_DELETE,
                    Permission.LEAD_CREATE,
                    Permission.LEAD_READ,
                    Permission.LEAD_UPDATE,
                    Permission.LEAD_DELETE,
                    Permission.CUSTOMER_CREATE,
                    Permission.CUSTOMER_READ,
                    Permission.CUSTOMER_UPDATE,
                    Permission.CUSTOMER_DELETE,
                    Permission.INVOICE_CREATE,
                    Permission.INVOICE_READ,
                    Permission.INVOICE_UPDATE,
                    Permission.INVOICE_DELETE,
                    Permission.PRODUCT_CREATE,
                    Permission.PRODUCT_READ,
                    Permission.PRODUCT_UPDATE,
                    Permission.PRODUCT_DELETE,
                    Permission.ROLE_CREATE,
                    Permission.ROLE_READ,
                    Permission.ROLE_UPDATE,
                    Permission.ROLE_DELETE,
                    Permission.DASHBOARD,
                    Permission.AI_CHAT,
                    Permission.NOTIFICATIONS,
                    Permission.SITE_SETTINGS,
                    Permission.IMPERSONITION
                ],
                description="Full access to all system features and settings.",
                created_by=created_by,
                updated_by=None,
                created_at=datetime.now(),
                updated_at=None,
                company_id=company_id
            ),
            Role(
                name=eRole.LEAD_MANAGER.value,
                permissions=[
                    Permission.LEAD_CREATE,
                    Permission.LEAD_READ,
                    Permission.LEAD_UPDATE,
                    Permission.LEAD_DELETE,
                    Permission.REPORT_READ,
                    Permission.REPORT_CREATE,
                    Permission.REPORT_UPDATE,
                    Permission.REPORT_DELETE
                ],
                description="Manages leads and related reports.",
                created_by=created_by,
                updated_by=None,
                created_at=datetime.now(),
                updated_at=None,
                company_id=company_id
            ),
            Role(
                name=eRole.PROJECT_MANAGER.value,
                permissions=[
                    Permission.REPORT_CREATE,
                    Permission.REPORT_READ,
                    Permission.REPORT_UPDATE,
                    Permission.REPORT_DELETE,
                    Permission.USER_READ,
                    Permission.USER_UPDATE,
                    Permission.LEAD_READ,
                    Permission.CUSTOMER_READ,
                    Permission.INVOICE_READ,
                    Permission.PRODUCT_READ
                ],
                description="Oversees projects, users, and reporting.",
                created_by=created_by,
                updated_by=None,
                created_at=datetime.now(),
                updated_at=None,
                company_id=company_id
            ),
            Role(
                name=eRole.ACCOUNTANT.value,
                permissions=[
                    Permission.INVOICE_CREATE,
                    Permission.INVOICE_READ,
                    Permission.INVOICE_UPDATE,
                    Permission.INVOICE_DELETE,
                    Permission.CUSTOMER_READ,
                    Permission.CUSTOMER_UPDATE,
                    Permission.REPORT_READ
                ],
                description="Handles financial records, invoices, and customer billing.",
                created_by=created_by,
                updated_by=None,
                created_at=datetime.now(),
                updated_at=None,
                company_id=company_id
            )
        ]

        self.db.bulk_save_objects(roles)
        self.db.commit()
        print("Roles seeded successfully!")


    def seed_users(self, company_id: int = 1):
        from core.hashing import Hasher
        users = [
            User(
                first_name="Alice",
                last_name="Johnson",
                email="alice.admin@example.com",
                mobile="+1-555-1111",
                location="New York, USA",
                role_id=1,  # Admin role
                avatar="alice_avatar.png",
                two_factor_auth=True,
                created_at=datetime.now(),
                updated_at=None,
                password=Hasher.get_password_hashed("securepassword123"),
                company_id=company_id,
                is_active=True
            ),
            User(
                first_name="Bob",
                last_name="Smith",
                email="bob.leads@example.com",
                mobile="+1-555-2222",
                location="London, UK",
                role_id=2,  # Lead Manager role
                avatar="bob_avatar.png",
                two_factor_auth=False,
                created_at=datetime.now(),
                updated_at=None,
                password=Hasher.get_password_hashed("leadmanagerpass"),
                company_id=company_id,
                is_active=True
            ),
            User(
                first_name="Carol",
                last_name="Williams",
                email="carol.pm@example.com",
                mobile="+1-555-3333",
                location="Bengaluru, India",
                role_id=3,  # Project Manager role
                avatar="carol_avatar.png",
                two_factor_auth=True,
                created_at=datetime.now(),
                updated_at=None,
                password=Hasher.get_password_hashed("projectmanagerpass"),
                company_id=company_id,
                is_active=True
            ),
            User(
                first_name="David",
                last_name="Brown",
                email="david.accountant@example.com",
                mobile="+1-555-4444",
                location="Toronto, Canada",
                role_id=4,  # Accountant role
                avatar="david_avatar.png",
                two_factor_auth=False,
                created_at=datetime.now(),
                updated_at=None,
                password=Hasher.get_password_hashed("accountantpass"),
                company_id=company_id,
                is_active=True
            )
        ]

        self.db.bulk_save_objects(users)
        self.db.commit()
        print("Users seeded successfully!")


    def seed_customers(self, created_by: int = 1):
        customers = [
            Customer(
                first_name="Emma",
                last_name="Stone",
                email="emma.stone@example.com",
                phone="+1-555-5551",
                company="Stone Consulting",
                category="Enterprise",
                assigned_user_id=1,  # Assigned to Alice (Admin)
                addrees="456 Business Ave, New York, USA",
                is_active=True,
                created_by=created_by,
                created_at=datetime.now(),
                updated_at=None,
                updated_by=None
            ),
            Customer(
                first_name="Raj",
                last_name="Kumar",
                email="raj.kumar@example.com",
                phone="+91-98765-11111",
                company="Kumar Industries",
                category="SMB",
                assigned_user_id=2,  # Assigned to Bob (Lead Manager)
                addrees="12 MG Road, Bengaluru, India",
                is_active=True,
                created_by=created_by,
                created_at=datetime.now(),
                updated_at=None,
                updated_by=None
            ),
            Customer(
                first_name="Sophia",
                last_name="Martinez",
                email="sophia.martinez@example.com",
                phone="+44-20-555-2222",
                company="Martinez Retail",
                category="Retail",
                assigned_user_id=3,  # Assigned to Carol (Project Manager)
                addrees="78 High Street, London, UK",
                is_active=True,
                created_by=created_by,
                created_at=datetime.now(),
                updated_at=None,
                updated_by=None
            ),
            Customer(
                first_name="Liam",
                last_name="Nguyen",
                email="liam.nguyen@example.com",
                phone="+61-400-555-333",
                company="Nguyen Finance",
                category="Finance",
                assigned_user_id=4,  # Assigned to David (Accountant)
                addrees="22 George Street, Sydney, Australia",
                is_active=True,
                created_by=created_by,
                created_at=datetime.now(),
                updated_at=None,
                updated_by=None
            )
        ]

        self.db.bulk_save_objects(customers)
        self.db.commit()
        print("Customers seeded successfully!")


    def seed_leads(self, created_by: int = 1):
        leads = [
            Lead(
                first_name="Michael",
                last_name="Green",
                dob=date(1990, 5, 14),
                email="michael.green@example.com",
                phone="+1-555-7771",
                company="GreenTech Solutions",
                source="Website",
                status=Status.NEW.name,
                lead_value=50000.0,
                notes="Interested in enterprise software solutions.",
                owned_by=2,  # Assigned to Bob (Lead Manager)
                refered_by=None,
                created_by=created_by,
                created_at=datetime.now(),
                updated_at=None,
                updated_by=None
            ),
            Lead(
                first_name="Anita",
                last_name="Sharma",
                dob=date(1985, 8, 22),
                email="anita.sharma@example.com",
                phone="+91-98765-22222",
                company="Sharma Textiles",
                source="Referral",
                status=Status.CONTACTED.name,
                lead_value=15000.0,
                notes="Looking for accounting software.",
                owned_by=4,  # Assigned to David (Accountant)
                refered_by=1,  # Referred by Alice (Admin)
                created_by=created_by,
                created_at=datetime.now(),
                updated_at=None,
                updated_by=None
            ),
            Lead(
                first_name="James",
                last_name="Taylor",
                dob=date(1992, 3, 10),
                email="james.taylor@example.com",
                phone="+44-20-555-3333",
                company="Taylor Retail",
                source="Cold Call",
                status=Status.PROPOSAL.name,
                lead_value=25000.0,
                notes="Proposal sent for retail management system.",
                owned_by=3,  # Assigned to Carol (Project Manager)
                refered_by=None,
                created_by=created_by,
                created_at=datetime.now(),
                updated_at=None,
                updated_by=None
            ),
            Lead(
                first_name="Chen",
                last_name="Li",
                dob=date(1988, 12, 5),
                email="chen.li@example.com",
                phone="+86-555-4444",
                company="Li Manufacturing",
                source="Conference",
                status=Status.NEGOTIATION.name,
                lead_value=75000.0,
                notes="Negotiating terms for manufacturing ERP solution.",
                owned_by=2,  # Assigned to Bob (Lead Manager)
                refered_by=3,  # Referred by Carol (Project Manager)
                created_by=created_by,
                created_at=datetime.now(),
                updated_at=None,
                updated_by=None
            )
        ]

        self.db.bulk_save_objects(leads)
        self.db.commit()
        print("Leads seeded successfully!")


    def seed_products(self, created_by: int = 1):
        products = [
            Product(
                product_name="Enterprise CRM Suite",
                sku_code="CRM-ENT-001",
                description="Comprehensive CRM solution for large enterprises.",
                category="Software",
                status=Status.ACTIVE.name,
                price=12000.0,
                stock=50,
                tax=18.0,
                owned_by=2,  # Owned by Bob (Lead Manager)
                created_by=created_by,
                updated_by=None,
                created_at=datetime.now(),
                updated_at=None
            ),
            Product(
                product_name="Retail POS System",
                sku_code="POS-RET-002",
                description="Point-of-sale system tailored for retail businesses.",
                category="Hardware",
                status=Status.ACTIVE.name,
                price=2500.0,
                stock=200,
                tax=12.0,
                owned_by=3,  # Owned by Carol (Project Manager)
                created_by=created_by,
                updated_by=None,
                created_at=datetime.now(),
                updated_at=None
            ),
            Product(
                product_name="Accounting Software Pro",
                sku_code="ACC-PRO-003",
                description="Advanced accounting software for SMBs.",
                category="Software",
                status=Status.ACTIVE.name,
                price=800.0,
                stock=500,
                tax=10.0,
                owned_by=4,  # Owned by David (Accountant)
                created_by=created_by,
                updated_by=None,
                created_at=datetime.now(),
                updated_at=None
            ),
            Product(
                product_name="Cloud Storage Package",
                sku_code="CLOUD-STOR-004",
                description="Secure cloud storage solution with scalable plans.",
                category="Service",
                status=Status.ACTIVE.name,
                price=150.0,
                stock=1000,
                tax=5.0,
                owned_by=1,  # Owned by Alice (Admin)
                created_by=created_by,
                updated_by=None,
                created_at=datetime.now(),
                updated_at=None
            )
        ]

        self.db.bulk_save_objects(products)
        self.db.commit()
        print("Products seeded successfully!")

