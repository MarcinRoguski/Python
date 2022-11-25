#Wydrukuj te itemy z indeksem mWIG40
stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]
print(list(filter(lambda item: item['indeks'] == 'mWIG40', stocks)))


#usuń "-" z listy

items = ['P-1', 'R-2', 'D-4', 'F-6']
print(list(map(lambda item: item.replace('-',''), items)))
