import os
import time

import eel
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from create_database import Station, Rental

eel.init("web")


@eel.expose
def get_all_stations(db_name):
    if not os.path.isfile(f'{db_name}.sqlite3'):
        return {'status': 'error', 'stations': []}

    engine = create_engine(f'sqlite:///{db_name}.sqlite3', echo=True)

    with Session(engine) as session:
        return {'status': 'success', 'stations': [ses.__dict__ for ses in session.query(Station).all()]}


@eel.expose
def calculate_statistics(db_name, station_id):
    engine = create_engine(f'sqlite:///{db_name}.sqlite3', echo=True)

    with Session(engine) as session:
        return {
            'mean_time_from': mean_time_from(station_id, session),
        }


def mean_time_from(station_id, session):
    select_statement = select(Rental).where(Rental.rental_station_id == station_id)
    rentals = session.execute(select_statement).all()

    return calc_mean_time(rentals)


def calc_mean_time(rentals):
    if len(rentals) == 0:
        return 0

    total_time = 0

    for rental in rentals:
        total_time += (rental[0].end_time - rental[0].start_time).total_seconds()

    return time.strftime('%H:%M:%S', time.gmtime(total_time / len(rentals)))


# Start the index.html file
eel.start("index.html", size=(800, 500))
