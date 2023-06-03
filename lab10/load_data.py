import csv
import datetime
import os
import sys

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from create_database import Rental, Station


def validate():
    if len(sys.argv) != 3:
        print('Wrong number of arguments')
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('File with data does not exist')
        sys.exit(1)

    if not os.path.isfile(f'{sys.argv[2]}.sqlite3'):
        print('Database does not exist')
        sys.exit(1)


def load_data(file_name, db_name):
    try:
        with open(file_name, 'r') as file:
            data = csv.DictReader(file)
            validate_file(data)
            store_data(data, db_name)
    except FileNotFoundError:
        print('File with data does not exist')
        sys.exit(1)


def validate_file(data):
    required_columns = ['UID wynajmu', 'Numer roweru', 'Data wynajmu', 'Data zwrotu', 'Stacja wynajmu',
                        'Stacja zwrotu', 'Czas trwania']

    if not all(column in data.fieldnames for column in required_columns):
        print('File with data has wrong format')
        sys.exit(1)


def store_data(data, db_name):
    engine = create_engine(f'sqlite:///{db_name}.sqlite3')
    rentals = []
    stations = {}

    with Session(engine) as session:
        for row in data:
            rental = Rental(
                rental_id=int(row['UID wynajmu']),
                bike_number=int(row['Numer roweru']),
                start_time=datetime.datetime.strptime(row['Data wynajmu'], '%Y-%m-%d %H:%M:%S'),
                end_time=datetime.datetime.strptime(row['Data zwrotu'], '%Y-%m-%d %H:%M:%S'),
                rental_station=extract_station(row['Stacja wynajmu'], stations, session),
                return_station=extract_station(row['Stacja zwrotu'], stations, session),
            )
            rentals.append(rental)

        session.add_all(stations.values())
        session.add_all(rentals)
        session.commit()


def extract_station(name, stations, session):
    if name in stations:
        return stations[name]

    station = session.scalar(select(Station).where(Station.station_name == name))

    if station is None:
        station = Station(station_name=name)
        stations[name] = station

    return station


if __name__ == '__main__':
    validate()
    load_data(sys.argv[1], sys.argv[2])
