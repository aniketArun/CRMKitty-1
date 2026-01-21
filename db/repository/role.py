from sqlalchemy.orm import Session
from db.models.role import Role
from schemas.role import CreateRole, UpdateRole
from db.models.user import User
from datetime import datetime

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


def update_role_by_id(id, role:UpdateRole, by_user:User, db:Session):
    role_in_db = db.query(Role).filter(Role.id == id).first()
    
    if role_in_db is None:
        return
    
    update_data = role.model_dump(exclude_unset=True)  # only provided keys
    
    for key, value in update_data.items():
        setattr(role_in_db, key, value)

    role_in_db.updated_at = datetime.now()
    role_in_db.updated_by = by_user.id
    
    db.add(role_in_db)
    db.commit()
    db.refresh(role_in_db)
    return role_in_db