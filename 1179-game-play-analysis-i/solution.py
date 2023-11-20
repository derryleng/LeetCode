import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity[["player_id", "event_date"]]
    df.sort_values(by=["player_id", "event_date"], inplace=True)
    df.drop_duplicates("player_id", inplace=True)
    df.columns = ["player_id", "first_login"]
    return df
