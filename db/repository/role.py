from sqlalchemy.orm import Session
from db.models.role import Role
from schemas.role import CreateRole
from db.models.user import User


def create_new_role(user:User, role:CreateRole, db:Session):
    new_role = Role(
        name = role.name,
        permissions = role.permissions,
        description = role.description,
        created_by = user.id,
        company_id = user.company_id
    )

    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return new_role


def get_all_role(user:User, db:Session):
    queryset = db.query(Role).filter(Role.company_id == user.company_id).all()

    return queryset