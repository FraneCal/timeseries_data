import pandas as pd
import numpy as np

# Read data from file
file_path = 'base_data.csv'
df = pd.read_csv(file_path)
df = df.dropna(subset=['TimeStamp'])
cleaned_df = df.dropna()

# ------------------- PREVIOUS DAY INFORMATION ------------------- #
previous_open = df['Open'][0]
previous_day_df = df[df['TimeStamp'].str.startswith('06/May/2024')]
previous_close = previous_day_df['Close'].iloc[-1]

cleaned_df.loc[:, 'Volume'] = cleaned_df['Volume'].str.strip().replace('-', np.nan)
cleaned_df.loc[:, 'Volume'] = cleaned_df['Volume'].str.replace(',', '').astype(float)

previous_day_cumulative_volume = cleaned_df['Volume'].sum()

previous_open_time = cleaned_df['TimeStamp'][0].split(' ')[1]

print(f'Previous day open: {previous_open}\nPrevious day close: {previous_close}\nPrevious day volume: {previous_day_cumulative_volume} \nPrevious day open time: {previous_open_time}')


# ------------------- CURRENT DAY INFORMATION ------------------- #

current_day_df = cleaned_df[cleaned_df['TimeStamp'].str.startswith('07/May/2024')]

today_open = current_day_df['Open'].iloc[0]

today_high = current_day_df['High'].max()
print(today_high)
