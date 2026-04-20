import pandas as pd
import matplotlib as plt
from nba_api.stats.static import teams

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

nba_teams = teams.get_teams()
nt = pd.DataFrame(nba_teams)
