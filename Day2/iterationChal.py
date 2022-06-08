entries = []

for x in range(2000, 3200):
    if x % 5 != 0:
        if x % 7 == 0:
          entries.append(x)
        
print(entries)