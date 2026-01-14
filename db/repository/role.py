from sqlalchemy.orm import Session
from db.models.role import Role
from schemas.role import CreateRole



def create_new_role(role:CreateRole, db:Session):
    new_role = Role(
        name = role.name,
        permissions = role.permissions,
        description = role.description,
        created_by = role.created_by
    )

    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return new_role


def get_all_role(db:Session):
    queryset = db.query(Role).filter().all()

    return queryset