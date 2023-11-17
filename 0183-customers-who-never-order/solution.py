import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Get customer IDs not present in orders
    df = customers[
        ~customers.id.isin(orders.customerId)
    ][["name"]]
    df = df.rename(columns={"name": "Customers"})
    return df
