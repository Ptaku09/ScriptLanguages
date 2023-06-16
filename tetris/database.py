from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Result(Base):
    __tablename__ = "results"
    game_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    player_name: Mapped[str] = mapped_column(String(20))
    field_size: Mapped[str] = mapped_column(String(10))
    game_level: Mapped[int] = mapped_column(Integer)
    score: Mapped[int] = mapped_column(Integer)
    date: Mapped[str] = mapped_column(String(20))


engine = create_engine("sqlite:///results.sqlite3")
Base.metadata.create_all(engine)
