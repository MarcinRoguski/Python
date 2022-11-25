import time

with open('plw_d.csv', 'r') as file:

    content = file.read().splitlines()
 

data = [(line.split(',')[0], line.split(',')[-1]) for line in content]



start = time.perf_counter()

data = [(val[0], int(val[1])) for val in data[1:]]


max_val = 0

for date, val in data:

    if val > max_val:
        max_val = val
        max_date = date

stop = time.perf_counter()
time = stop - start        
print('Data:', max_date, time)





start = time.perf_counter()

data = [(val[0], int(val[1])) for val in data[1:]]

max_vol = max([val[1] for val in data])

max_date = list(filter(lambda val: val[1] == max_vol, data))[0][0]


stop = time.perf_counter()
time = stop - start 

print(f'Data: {max_date}', time)






