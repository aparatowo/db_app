import os
from database.credentials import get_secret
from database.models import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event, create_engine


ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../")
)

secrets = get_secret()

def _fk_pragma_on_connect(dbapi_con, con_record):
    """
    Turns on foreign keys while connecting to database. Used in SQLAlchemy event listener.
    :param dbapi_con:
    :return:
    """
    dbapi_con.execute('pragma foreign_keys=ON')


def get_session(secrets=None, echo=False):
    """
    Establishes and maintain connection with production PosgreSQL database.
    :param echo:
    :return:
    """

    db_user = secrets["username"]
    db_pass = secrets["password"]
    db_name = secrets["dbname"]
    db_address = secrets["host"]
    # db_port = secrets['port']
    db_path = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_address}:5432/{db_name}"
    engine = create_engine(db_path, echo=echo)
    db_session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    event.listen(engine, "connect", _fk_pragma_on_connect)

    return db_session()
