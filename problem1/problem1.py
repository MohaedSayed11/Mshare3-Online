total = 0

for i in nums:
    if i % 5 == 0 or i % 3 == 0:
        total = total + i
print(total)
