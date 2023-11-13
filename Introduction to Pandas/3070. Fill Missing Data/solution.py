# DataFrame products
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | quantity    | int    |
# | price       | int    |
# +-------------+--------+

# Write a solution to fill in the missing value as 0 in the quantity column.

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    return products.fillna(value={"quantity": 0})

