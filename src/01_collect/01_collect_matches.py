# %%
import sqlalchemy
import db_models
import requests
from sqlalchemy.orm import Session

db_path = "./../../data/database.db"

con = sqlalchemy.create_engine(f"sqlite:///{db_path}")

# db_models.Base.metadata.create_all(con)
# %%
class CollectorMatch():
    def __init__(self, engine):
        self.engine = engine
        self.url = "https://api.opendota.com/api/proMatches"

    def get_match(self):
        resp = requests.get(self.url)
        return resp
    
    def update_match(self, d, i):
        d.duration = i["duration"]
        d.start_time = i["start_time"]
        d.radiant_team_id = i["radiant_team_id"]
        d.radiant_name = i["radiant_name"]
        d.dire_team_id = i["dire_team_id"]
        d.dire_name = i["dire_name"]
        d.leagueid = i["leagueid"]
        d.league_name = i["league_name"]
        d.series_id = i["series_id"]
        d.series_type = i["series_type"]
        d.radiant_score = i["radiant_score"]
        d.dire_score = i["dire_score"]
        d.radiant_win = i["radiant_win"]
        d.version = i["version"]
        return d
    
    def save_match(self,data):
        with Session(self.engine) as session:
            d_matches = []
            for i in data:
                d = session.get(db_models.Match, i["match_id"])
                if d:
                    d = self.update_match(d, i)
                else:
                    d = db_models.Match(**i)
                d_matches.append(d)

            session.add_all(d_matches)
            session.commit()

    def exec_collect(self):
        resp = self.get_match()
        if resp.status_code == 200:
            self.save_match(resp.json())
            return True
        else:
            print(f"Error: {resp.status_code}")              
            return False

# %%
collector = CollectorMatch(con)

# %%
result = collector.exec_collect()
result
# %%
