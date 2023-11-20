import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df1 = employee.merge(department, left_on="departmentId", right_on="id", suffixes=("_employee", "_department"))
    df2 = df1.groupby("departmentId").apply(
        lambda x: x[x["salary"] == x["salary"].max()]
    )
    df3 = df2[["name_department", "name_employee", "salary"]]
    df3.columns = ["Department", "Employee", "Salary"]
    return df3
