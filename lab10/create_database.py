import os
import sys
from datetime import datetime

from sqlalchemy import create_engine, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship


class Base(DeclarativeBase):
    pass


class Rental(Base):
    __tablename__ = 'rentals'
    rental_id: Mapped[int] = mapped_column(primary_key=True)
    bike_number: Mapped[int] = mapped_column(Integer)
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
    rental_station_id: Mapped[int] = mapped_column(ForeignKey('stations.station_id'))
    rental_station: Mapped['Station'] = relationship('Station', foreign_keys=[rental_station_id])
    return_station_id: Mapped[int] = mapped_column(ForeignKey('stations.station_id'))
    return_station: Mapped['Station'] = relationship('Station', foreign_keys=[return_station_id])

    def __repr__(self):
        return f'Rental(rental_id={self.rental_id!r}, bike_number={self.bike_number!r}, start_time={self.start_time!r} end_time={self.end_time!r})'


class Station(Base):
    __tablename__ = 'stations'
    station_id: Mapped[int] = mapped_column(primary_key=True)
    station_name: Mapped[str] = mapped_column(String(50))

    def __repr__(self):
        return f'Station(station_id={self.station_id!r}, station_name={self.station_name!r})'


def validate():
    if len(sys.argv) != 2:
        print('Wrong number of arguments')
        sys.exit(1)

    if os.path.isfile(f'{sys.argv[1]}.sqlite3'):
        print('File already exists')
        sys.exit(1)


def create_database():
    engine = create_engine(f'sqlite:///{sys.argv[1]}.sqlite3', echo=True)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    validate()
    create_database()
