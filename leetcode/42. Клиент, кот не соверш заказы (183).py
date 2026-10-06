import pandas as pd
Customers = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['J', 'H', 'S', 'M']})
Orders = pd.DataFrame({'id': [1, 2], 'customerId': [3, 1]})
def find_customers(customers, orders):
    merged = pd.merge(left=customers, right=orders,
                      how='left',
                      left_on='id',
                      right_on='customerId',
                      suffixes=('', '_order'))
    mask = merged['id_order'].isna()
    return merged[mask][['name']].rename(columns={'name': 'Customers'})
print(find_customers(Customers, Orders))