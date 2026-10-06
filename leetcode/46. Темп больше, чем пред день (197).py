import pandas as pd

weather = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "recordDate": [
        "2015-01-01",
        "2015-01-02",
        "2015-01-03",
        "2015-01-04"
    ],
    "temperature": [10, 25, 20, 30]
})
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    #отсортировать по дате
    weather.sort_values("recordDate", inplace=True)
    #вектор дат сдвинутый на строку вниз
    weather_date_shift = weather["recordDate"].shift(1)
    #вектор температур сдвинутый на строку вниз
    weather_temp_shift = weather['temperature'].shift(1)
    mask = (
        (weather["recordDate"] - weather_date_shift == pd.Timedelta(days=1))
        &
        (weather["temperature"] > weather_temp_shift)
    )

    return weather.loc[mask, ["id"]]
