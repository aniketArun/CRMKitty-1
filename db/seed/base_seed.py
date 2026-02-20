from .seed_model import SeedModel

from db.session import SESSIONLOCAL

db = SESSIONLOCAL()

seeder = SeedModel(db=db)


def start_seeder():
    seeder.seed_companies()
    seeder.seed_roles()
    seeder.seed_users()
    seeder.seed_leads()
    seeder.seed_customers()
    seeder.seed_products()
