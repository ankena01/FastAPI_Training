from sqlalchemy import Integer, String, Boolean , Column
from database import Base

class Todos(Base):

    __tablename__ = 'todos'

    # columns names in table
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    description = Column(String)
    priorty = Column(Integer)
    complete = Column(Boolean, default=False)




