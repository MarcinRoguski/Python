import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open ("stocks.json", "w", encoding="UTF-8") as file:
    json.dump(stocks, file, ensure_ascii=False, indent=4)
