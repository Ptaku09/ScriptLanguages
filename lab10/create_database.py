import os
import sys
from datetime import datetime

from sqlalchemy import create_engine, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class Rentals(Base):
    __tablename__ = 'rentals'
    rental_id: Mapped[int] = mapped_column(primary_key=True)
    bike_number: Mapped[int] = mapped_column(Integer)
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
    rental_station: Mapped[int] = mapped_column(ForeignKey('stations.station_id'))
    return_station: Mapped[int] = mapped_column(ForeignKey('stations.station_id'))


class Stations(Base):
    __tablename__ = 'stations'
    station_id: Mapped[int] = mapped_column(primary_key=True)
    station_name: Mapped[str] = mapped_column(String(50))


def validate():
    if len(sys.argv) != 2:
        print('Wrong number of arguments')
        sys.exit(1)

    if os.path.isfile(sys.argv[1]):
        print('File already exists')
        sys.exit(1)


def create_database():
    engine = create_engine(f'sqlite:///{sys.argv[1]}.sqlite3')
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    validate()
    create_database()
