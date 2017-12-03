# Bokai Chen
# Calculating moving average delay for flight data

import pandas as pd
import numpy as np

# Resampling data from flights.csv, due to size too large.

# flight_df = pd.read_csv('./flights.csv', low_memory=False)
# sample_df = flight_df.iloc[0::100, :]
# test_df = flight_df[flight_df.index%100 != 0]
#
# # print(flight_df.head())
# print("Dimensions of the data:", flight_df.shape)
# print("Dimensions of the sample data:", sample_df.shape)
# print("Dimensions of the test data:", test_df.shape)

# sample_df.to_csv("sample.csv")
# test_df.to_csv("test.csv")




sample_df = pd.read_csv("./sample.csv")

# Taking useful data into the context of the question
sample_df['DEPARTURE_DATE'] = pd.to_datetime(sample_df[['YEAR', 'MONTH', 'DAY']])
question_df = sample_df[["DEPARTURE_DATE", "SCHEDULED_DEPARTURE", "DEPARTURE_TIME", "TAIL_NUMBER", "SCHEDULED_ARRIVAL", "ARRIVAL_TIME", "ARRIVAL_DELAY"]]


# Dropping flight cancellations and Diverted flights
question_df['ARRIVAL_TIME'].replace('', np.nan, inplace = True)
question_df = question_df.dropna(subset=['ARRIVAL_TIME'])



flightDelay_df = question_df[["DEPARTURE_DATE", "TAIL_NUMBER", "SCHEDULED_ARRIVAL", "ARRIVAL_TIME", "ARRIVAL_DELAY"]]


print(flightDelay_df.head())
flightDelay_df.to_csv("Flight_Delay.csv")

delay_df = question_df[["DEPARTURE_DATE", "ARRIVAL_DELAY"]]
delay_df.set_index("DEPARTURE_DATE", inplace = True)



# Resample data on daily basis. The mean delay of flight is taken per day. Some data will be weighted unevenly.
delay_df = delay_df.resample('D').mean()


#Moving average is taken
delay_df["ROLLING_AVERAGE_DELAY"] = delay_df.rolling(center=False, window=7).mean()
delay_df.rename(columns={"ARRIVAL_DELAY": "DAILY_DELAY_AVERAGE"}, inplace=True)
delay_df.to_csv("Moving_Average_Delay.csv")


print(question_df.shape)
print(delay_df)
