from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Exhibition(Base):
    __tablename__ = 'exhibition'

    id = Column(Integer, primary_key=True)
    source = Column(String(32))
    code = Column(String(32))
    name = Column(String(32))
    start_time = Column(Date())
    end_time= Column(Date())
    address = Column(String(128))
    city = Column(String(32))
    url = Column(String(256))

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, item[key])
