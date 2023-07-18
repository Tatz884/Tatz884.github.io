from sqlalchemy import create_engine

from api.models.task import Base

DB_URL = "mysql+pymysql://FullStackToDoApp_knownpair:741a23bc1f5556ffb05fcfd2e722458ad9a66bcb@6-u.h.filess.io:3307/FullStackToDoApp_knownpair"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()