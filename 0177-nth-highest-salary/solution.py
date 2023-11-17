import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee.salary.unique()
    if N > len(df):
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    return pd.DataFrame({f"getNthHighestSalary({N})": [sorted(df, reverse=True)[N-1]]})
