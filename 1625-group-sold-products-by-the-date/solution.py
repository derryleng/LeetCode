import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.drop_duplicates()
    size = df.groupby("sell_date").size().reset_index(name="num_sold")
    prod = df.groupby("sell_date")["product"].apply(lambda x: ",".join(sorted(x))).reset_index(name="products")
    return pd.merge(size, prod, on="sell_date")
