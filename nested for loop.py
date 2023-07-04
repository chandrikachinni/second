

names = ['Kelly', 'Jessa', 'Emma']
for name in names:
    count = 0
    while count < 5:
        print(name, end=' ')
        count = count + 1
    print()


rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')