import pip._vendor.requests as requests, json
def currency_exchange_rate(from_currency,to_currency):
    api_key = "BW8DP6OHTV62MU57"
    from_currency = "USD"
    to_currency = "SGD"
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
    # print (main_url)
    response = requests.get(main_url)
    data = response.json()
    # print (data)
    return data["Realtime Currency Exchange Rate"] ["5. Exchange Rate"]
   
    
print (currency_exchange_rate("USD", "SGD"))
    #data = response.json()
    #print (data.keys())
    #print(json.dumps(data["Realtime Currency Exchange Rate"], indent=4))
    # Python program to get the real-time
    # currency exchange rate

    # Function to get real time currency exchange




