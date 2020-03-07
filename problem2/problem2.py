fibnums = [1,2]
while fibnums[-1] < 4000000:
    fibnums.append(fibnums[-1] + fibnums[-2])
del fibnums[-1]

evenfibnums = [0]
total = 0

for i in fibnums:
    if i % 2 == 0:
        evenfibnums.append(i)

for i in evenfibnums:
    total += i

print(total)
