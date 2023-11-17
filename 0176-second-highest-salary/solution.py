import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.salary.unique()
    if len(df) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    return pd.DataFrame({"SecondHighestSalary": [sorted(df, reverse=True)[1]]})
