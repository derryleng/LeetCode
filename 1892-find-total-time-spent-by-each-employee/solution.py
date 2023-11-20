import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.groupby(["event_day", "emp_id"]).apply(
        lambda x: sum(x["out_time"] - x["in_time"])
    ).reset_index()
    df.columns = ["day", "emp_id", "total_time"]
    return df
