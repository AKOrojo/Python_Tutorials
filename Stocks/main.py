import requests
import datetime as df

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "JZJCQNOUV7C4JL9H"
API_KEY_NEWS = "c75f4d4e3ea6448aa163738b6aaae6b3"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
todays_date = df.date.today()
yesterday_date = todays_date - df.timedelta(days=1)
datebefore_yesterday = todays_date - df.timedelta(days=2)

parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": API_KEY
}

response = requests.get(
    url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()

yesterday_close = stock_data["Time Series (60min)"][
    f"{yesterday_date.year}-{yesterday_date.month}-{yesterday_date.day} 20:00:00"]["4. close"]
db_close = stock_data["Time Series (60min)"][f"{datebefore_yesterday.year}-{datebefore_yesterday.month}-{datebefore_yesterday.day} 20:00:00"]["4. close"]

yesterday_close = float(yesterday_close)
db_close = float(db_close)

# TODO 2. - Get the day before yesterday's closing stock price

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(yesterday_close - db_close)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_difference = ((positive_difference/yesterday_close) * 100)
# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_difference > 5:
    print("Get News")

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # Init
    parameters_news = {
        "qInTitle": COMPANY_NAME,
        "apiKey": API_KEY_NEWS
    }

    response_news = requests.get(
        url=NEWS_ENDPOINT, params=parameters_news)

    top_headlines = response_news.json()["articles"]
    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_art = top_headlines[:3]
# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: ????2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: ????5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
