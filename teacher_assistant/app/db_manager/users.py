from sqlalchemy.orm import Session

from doctor_assistant.app.database import User


def get_items(db: Session):
    return db.query(User).all()


def get_item(db: Session, item_id: int):
    return db.query(User).filter(User.id == item_id).first()


def delete_item(db: Session, item: User):
    db.delete(item)
    db.commit()
