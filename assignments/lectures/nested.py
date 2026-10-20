

for i in range(7):
    if i == 2:
        print()
        continue
    for j in range(10):
        print(str((i + 1) * (j + 1)) + "\t", end="")
    print()
