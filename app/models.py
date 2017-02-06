from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Table
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
import datetime

class Player(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    member_since = Column(Date, nullable=True)

    def __repr__(self):
        return "{0}".format(self.name)

    def register_date(self):
        return datetime.datetime(self.name, self.member_since, 1)

class Chall(Model):
    id = Column(Integer, primary_key=True)
    category = Column(String(50), unique = False, nullable=False)
    points = Column(Integer, nullable=False)
    solved_by = Column(String(50), ForeignKey('player.name'))
    player = relationship("Player")
    ctf_id = Column(Integer, ForeignKey('ctf.id'), nullable=False)
    ctf = relationship('Ctf')

    def __repr__(self):
        return "{0}".format(self.id)


class Ctf(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

    def __repr__(self):
        return self.name
