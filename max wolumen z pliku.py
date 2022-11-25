

with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

 
data = [(line.split(',')[0], line.split(',')[4]) for line in content]



result = {
    data[0][0]: [data[1:][i][0] for i in range(len(data) - 1)],
    data[0][1]: [float(data[1:][i][1]) for i in range(len(data) - 1)],
}
print(result)




""" Wydrukowanie max vol
volumes = [line.split(',')[-1] for line in content][1:]
volumes = [int(volume) for volume in volumes]
max_volume = max(volumes)
print('Max Vol:', max_volume)
"""



