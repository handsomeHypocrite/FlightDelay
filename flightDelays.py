import pandas as pd
import numpy as np


flight_df = pd.read_csv('./flights.csv', low_memory=False)
sample_df = flight_df.iloc[0::100, :]
test_df = flight_df[flight_df.index%100 != 0]

# print(flight_df.head())
print("Dimensions of the data:", flight_df.shape)
print("Dimensions of the sample data:", sample_df.shape)
print("Dimensions of the test data:", test_df.shape)

sample_df.to_csv("sample.csv", sep='\t')
test_df.to_csv("test.csv", sep='\t')