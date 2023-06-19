from datetime import datetime
from enum import Enum

import pygame
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from database import Result


def get_font(size):
    return pygame.font.Font("/Users/mateusz/Desktop/Studia/Semestr IV/[L] Języki skrytpowe/tetris/assets/fonts/tetris.ttf", size)


def extract_field_size(field_size):
    return int(field_size.split("x")[0]), int(field_size.split("x")[1])


def store_result(username, field_size, game_level, score):
    engine = create_engine("sqlite:///results.sqlite3")

    with Session(engine) as session:
        result = Result(
            player_name=username,
            field_size=field_size,
            game_level=game_level,
            score=score,
            date=datetime.today().date(),
        )
        session.add(result)
        session.commit()


def get_results(limit):
    engine = create_engine("sqlite:///results.sqlite3")

    with Session(engine) as session:
        return session.query(Result).order_by(Result.score.desc()).limit(limit)


class FieldSize(Enum):
    SMALL = "16x8"
    MEDIUM = "18x10"
    LARGE = "20x12"
