from pathlib import Path
import pip._vendor.requests as requests, json
def currency_exchange_rate():
    api_key = "BC94UTRLKLJQB8ZA"
    from_currency = "USD"
    to_currency = "SGD"
    base_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={base_url}"
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
    # print (main_url)
    response = requests.get(main_url)
    data = response.json()
    # print (data)
    return data["Realtime Currency Exchange Rate"] ["5. Exchange Rate"]
   
    

    #data = response.json()
    #print (data.keys())
    #print(json.dumps(data["Realtime Currency Exchange Rate"], indent=4))
    # Python program to get the real-time
    # currency exchange rate

    # Function to get real time currency exchange




