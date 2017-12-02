import pandas as pd
import numpy as np
import datetime
import math


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


# def calc_delay(actual, expected):
#     """Because Python datetime sucks really bad"""
#
#     expected_h = math.floor(expected/100)
#     expected_m = expected % 100
#     actual_h = math.floor(actual/100)
#     actual_m = actual % 100
#     e_m = expected_h * 60 + expected_m
#     a_m = actual_h * 60 + actual_m
#     delay = a_m - e_m
#     if delay > 12 * 60:
#         delay -= 24*60
#     elif delay < -12 * 60:
#         delay += 24 * 60
#     return delay_list




sample_df = pd.read_csv("./sample.csv")
print(sample_df.shape)


sample_df['DEPARTURE_DATE'] = pd.to_datetime(sample_df[['YEAR', 'MONTH', 'DAY']])
question_df = sample_df[["DEPARTURE_DATE", "SCHEDULED_DEPARTURE", "DEPARTURE_TIME", "TAIL_NUMBER", "SCHEDULED_ARRIVAL", "ARRIVAL_TIME", "ARRIVAL_DELAY"]]
print(question_df.shape)


question_df['ARRIVAL_TIME'].replace('', np.nan, inplace=True)
question_df.dropna(subset=['ARRIVAL_TIME'], inplace=True)


# question_df['DELAY'] = question_df.apply(lambda row: question_df(row["ARRIVAL_TIME"], row["SCHEDULED_ARRIVAL"]), axis = 1)
rquestion_df = question_df[["DEPARTURE_DATE", "ARRIVAL_DELAY"]]

rquestion_df.set_index("DEPARTURE_DATE", inplace = True)

rquestion_df = rquestion_df.resample('D').mean()
rquestion_df["ROLLING_DELAY"] = pd.rolling_mean(rquestion_df["ARRIVAL_DELAY"], 7)
rquestion_df.to_csv("Moving_Average_Delay.csv")


print(question_df.shape)
print(rquestion_df.head(1000))
