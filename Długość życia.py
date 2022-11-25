from datetime import datetime

birthdayMarcin = datetime(1975, 5, 22, 0, 0, 0)
birthdayTata = datetime(1951, 12, 6, 0, 0, 0)
death = datetime(1998, 2, 22, 0, 0, 0)
diffMarcin = datetime.today() - birthdayMarcin
diffTata = death - birthdayTata
print('Ja już żyję:', round(diffMarcin.days/365, 2))
print('Tata żył:', round(diffTata.days/365, 2))
