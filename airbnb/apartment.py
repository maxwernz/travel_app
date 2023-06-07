import pandas as pd



class AirBnbApartment:

    def __init__(self, df: pd.DataFrame):
        self._df = df
        self._price_df = pd.DataFrame(self._df['price'].to_dict()).transpose()
        print(self._price_df)



