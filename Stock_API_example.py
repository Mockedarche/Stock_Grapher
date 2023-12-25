"""
Very simple example to grap data from stocks that is very nicely provided from polygon for free

"""


from polygon import RESTClient

client = RESTClient(api_key="PLACE YOUR POLYGON KEY HERE")

ticker = "AAPL"

with open("Apple.txt", 'w+') as file:
    # List Aggregates (Bars)
    aggs = []
    for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000):
        aggs.append(a)

    # Writing each aggregate to the file with a new line separator
    for agg in aggs:
        print(agg, file=file)


"""

# Get Last Trade
trade = client.get_last_trade(ticker=ticker)
print(trade)

# List Trades
trades = client.list_trades(ticker=ticker, timestamp="2022-01-04")
for trade in trades:
    print(trade)

# Get Last Quote
quote = client.get_last_quote(ticker=ticker)
print(quote)

# List Quotes
quotes = client.list_quotes(ticker=ticker, timestamp="2022-01-04")
for quote in quotes:
    print(quote)

"""