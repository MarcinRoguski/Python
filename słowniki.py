"""
#myDict = dict(zip(['one', 'two', 'three'], [1,2,3]))
myDict = dict(one = 1, two = 2, three = 3)


print(list(myDict.keys()))
print(list(myDict.values()))

del myDict['two']
print(myDict)
"""

with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()
 
data = [(line.split(',')[0], line.split(',')[5]) for line in content]

max_vol = max(float(data[1:][i][1]) for i in range(len(data) - 1))
print(max_vol)

"""
result = {
    data[1][0]: [data[1:][i][0] for i in range(len(data) - 1)],
    data[1][1]: [float(data[1:][i][1]) for i in range(len(data) - 1)],
}
print(result)

"""
