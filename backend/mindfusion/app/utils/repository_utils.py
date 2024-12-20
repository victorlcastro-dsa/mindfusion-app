from sqlalchemy.orm import Session

def _add_and_commit(db: Session, entity):
    """Add an entity to the session and commit."""
    db.add(entity)
    db.commit()
    db.refresh(entity)

def _commit_and_refresh(db: Session, entity):
    """Commit the session and refresh the entity."""
    db.commit()
    db.refresh(entity)