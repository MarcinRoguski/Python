import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

with open('C:\\PythonScripts\\BankChurners.csv', 'r', encoding='UTF-8') as file:

    lines = file.read().splitlines()


def ile_procent(daneDoProcentów):
    resultProcent = round(daneDoProcentów / amount * 100, 2)
    return resultProcent


dataAge = [line.split(',')[0] for line in lines][1:] 
amount = len(dataAge)

print('Ilość elementów:', amount, '\n')

#Obliczenia wieku
print('Struktura wiekowa\n')
dataAge = [line.split(',')[2] for line in lines][1:] #pobieram kolumnę 'wiek'

total = 0
wiek_do_30 = 0
wiek_31_40 = 0
wiek_41_50 = 0
wiek_51_60 = 0
wiek_pow_60 = 0

for item in dataAge:
    total = total + int(item)
    if 20 < int(item) < 31:
        wiek_do_30 = wiek_do_30 + 1
    elif 30 < int(item) < 41:
        wiek_31_40 = wiek_31_40 + 1
    elif 40 < int(item) < 51:
        wiek_41_50 = wiek_41_50 + 1
    elif 50 < int(item) < 61:
        wiek_51_60 = wiek_51_60 + 1
    elif 60 < int(item):
        wiek_pow_60 = wiek_pow_60 + 1

        
avgAge = round(total / len(dataAge))

print(f"Przedział wiekowy do 30 lat      = {wiek_do_30} ({ile_procent(wiek_do_30)} %)")
print(f"Przedział wiekowy 31 - 40 lat    = {wiek_31_40} ({ile_procent(wiek_31_40)} %)")
print(f"Przedział wiekowy 41 - 50 lat    = {wiek_41_50} ({ile_procent(wiek_41_50)} %)")
print(f"Przedział wiekowy 51 - 60 lat    = {wiek_51_60} ({ile_procent(wiek_51_60)} %)")
print(f"Przedział wiekowy powyżej 60 lat = {wiek_pow_60} ({ile_procent(wiek_pow_60)} %)")

avgAge = round(total / len(dataAge))

print('\nMin wiek:', min(dataAge))
print('Max wiek:', max(dataAge))
print('Średni wiek:', avgAge, '\n')

#płeć klientów
print('\nPłeć klientów\n')
dataSex = [line.split(',')[3] for line in lines][1:]#pobieram kolumnę 'płeć'
sexMale = dataSex.count('"M"')
print(f"Mężczyzn w grupie jest: {sexMale} - ({ile_procent(sexMale)} %)")
sexFemale = dataSex.count('"F"')
print(f"Kobiet w grupie jest: {sexFemale} - ({ile_procent(sexFemale)} %)")

#wykształcenie
print('\nWykształcenie\n')
dataEdu = [line.split(',')[5] for line in lines][1:]#pobieram kolumnę 'edukacja'
school = set(dataEdu)
schoolQty = len(school)
a = list(school)
schoolCount = []
for i in range(schoolQty):
    a[i] = dataEdu.count(a[i])
    schoolCount.append(a[i])
print(school)
print(schoolCount)
              

unknown_count = dataEdu.count('"Unknown"')
uneducated_count = dataEdu.count('"Uneducated"')
high_count = dataEdu.count('"High School"')
college_count = dataEdu.count('"College"')
graduate_count = dataEdu.count('"Graduate"')
postgarduate_count = dataEdu.count('"Post-Graduate"')
doctorate_count = dataEdu.count('"Doctorate"')

print("Unknown - ", unknown_count, '(', ile_procent(unknown_count), '%)')
print("Uneducated - ", uneducated_count, '(', ile_procent(uneducated_count), '%)')
print("High School - ", high_count, '(', ile_procent(high_count), '%)')
print("College - ", college_count, '(', ile_procent(college_count), '%)')
print("Graduate - ", graduate_count, '(', ile_procent(graduate_count), '%)')
print("Post-Graduate - ", postgarduate_count, '(', ile_procent(postgarduate_count), '%)')
print("Doctorate - ", doctorate_count, '(', ile_procent(doctorate_count), '%)')



"""
dictEdu = {}
for i in range(amount):
    dictEdu.update({dataEdu[i]: dataEdu.count(dataEdu[i])})
    x = dictEdu.split()
print(dictEdu, )
"""

#



















