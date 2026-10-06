import pandas as pd
def combine_two_tables(person, address):
    return pd.merge(person, address,
                    how='left', on='personId')\
        [['firstName', 'lastName', 'city', 'state']]