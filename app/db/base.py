from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from app.db.config import settings
from app.models.worker import worker

class DatabaseSession:

    def __init__(self):
        self.engine = None
        self.session_factory = None

    def init(self):
        self.engine = create_engine(settings.DATABASE_URL, echo=True)
        self.session_factory = sessionmaker(bind=self.engine)

    def create_all(self):
        metadata = MetaData()
        metadata.create_all(self.engine)

    def get_session(self):
        return scoped_session(self.session_factory)

    def close(self):
        # Close database session...
        if self.engine is None: # Check if engine is initialized
            raise Exception("Database engine is not initialized") # Raise an exception if not
        self.engine.dispose() # Close the engine

db = DatabaseSession()

def commit_rollback():
    try:
        session = db.get_session()
        # Zde můžete provádět operace s vaší databází pomocí `session`
        session.commit()
    except Exception as e:
        if 'session' in locals():
            session.rollback()
        raise e

