import requests
response = requests.get("https://restcountries.com/v3.1/all")

data = response.json()

filteredData = list(filter(lambda item: item["name"]["common"][:2].lower() == "br", data))

dataNames = eval(f"list(map(lambda item:item['name']['common'], filteredData))")
print(dataNames)