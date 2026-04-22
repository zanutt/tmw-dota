# %%
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass
# %%
from sqlalchemy.orm import Mapped, mapped_column

class Match(Base):
    __tablename__ = "match"
    match_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    duration:  Mapped[int]
    start_time: Mapped[int]  
    radiant_team_id: Mapped[int] = mapped_column(nullable=True) 
    radiant_name: Mapped[str] = mapped_column(nullable=True)
    dire_team_id: Mapped[str] = mapped_column(nullable=True)
    dire_name: Mapped[str] = mapped_column(nullable=True)  #Breeki Cheeki,
    leagueid: Mapped[int] = mapped_column(nullable=True) #19532,
    league_name: Mapped[str] = mapped_column(nullable=True) #DreamLeague Division 2 Season 4,
    series_id: Mapped[int] = mapped_column(nullable=True)  #1089557,
    series_type: Mapped[int] = mapped_column(nullable=True) #1,
    radiant_score: Mapped[int]  #6,
    dire_score: Mapped[int]  #28,
    radiant_win: Mapped[bool]  #false,
    version: Mapped[int] = mapped_column(nullable=True) #null

# %%
