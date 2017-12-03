# FlightDelay

Pulling delay time of flight from data.
Flight_Delay.csv
The aggregate rolling average within 7 days.
Moving_Average_Delay.csv

Data obtained from: https://www.kaggle.com/usdot/flight-delays/data


Note:
1. Delay time was taken straight from data, because arrival and scheduled_arrival information has only time but not date. And some delay can get up to 36 hours. Making it very difficult to determine exact delay time from other information. Moving average is taken from departure time.

2. The rolling average is taken on the mean of the delay time of each day. This is a cleaner solution, but days with abnormal air traffic may have an under-proportional impact on the result of the rolling average.

3. Only 57263 of the data is used, due to flight cancellation, diversion and resampling( data too large.)
