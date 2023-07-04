#print i and i is less than 6.

i=1
while i<6:
    print(i)
    i+=1


#print the message the condition is false.

i =1
while i <6:
    print(i)
    i +=1
else:
    print("i is no longer less then 6")


#print all letters expect f and s

i =0
a='chandrika'
while i<len(a):
    if a[i]=='a' or a[i]=='h':
        i += 1
        continue
    print('current Letter:', a[i])
    i +=1
