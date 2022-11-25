with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

close = []
Dict = {}

for idx, line in enumerate(content):
    if idx > 0:
        #close.append(str(line.split(',')[0]))
        #close.append(float(line.split(',')[-2]))
        Dict["Data"] = str(line.split(',')[0])
        Dict["Zamkniecie"] = float(line.split(',')[-2])

"""
Dict = {}
for i, item in range(1,len(close)):
    if i % 2 ==0:
        Dict["Data"] = item[i]
    else:
        Dict["Zmkniecie"] = item[i]
"""

print(Dict)
