# # F = (9/5)*C + 32
# places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]


# converted_temps = list(map(lambda place: (place[0], (9/5)*place[1] + 32), places))
# print(converted_temps)

def fibonacci(i):
    if i == 0:
        return 0
    elif i  == 1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)
for x in range(10):
    print(fibonacci(x))