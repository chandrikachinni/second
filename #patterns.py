#patterns
#program1

def a(n):
    for i in range(0,n):
        for i in range(0,i+1):
            print("*",end=" ")
        print("\r")
n=5
a(n)

#program 2


def a(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end =" ")
        k=k-2
        for j in range(0,i+1):
                print("*",end=" ")
        print("\r")
n=5
a(n)

#program 3


def triangle(n):
    k=n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
n=5
triangle(n)

#program 4


def a(n):
    num =1
    for i in range(0,n):
        num=1
        for j in range(0,i+1):
            print(num,end =" ")
            num = num+1
        print("\r")
n=5
a(n)

#program 5


def anum(n):
    num =1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end=" ")
            num=num+1
        print("\r")
n=5
anum(n)

#program 6


def alphabet(n):
    num=65
    for i in range(0,n):
        for j in range(0,i+1):
            ch=chr(num)
            print(ch, end=" ")
        num = num+1
        print("\r")
n=5
alphabet(n)


#program 7

def alphabets(n):
    num=65
    for i in range(0,n):
        for j in range(0,i+1):
            ch=chr(num)
            print(ch, end=" ")
            num = num+1
        print("\r")
n=5
alphabets(n)


#program 8

rows =6
for i in range(rows):
    for j in range(i):
        print(i,end=' ')
    print("\r")


#program 9

rows =5
b=0
for i in range(rows,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end=' ')
    print("\r")

#program 10

row=5
num=rows
for i in range(rows,0,-1):
    for j in range(0,i):
        print(num,end=' ')
    print("\r")

#program 11

row =5
for i in range(row,0,-1):
    for j in range(0,i+1):
        print(j,end=' ')
    print("\r")


#program 12

rows =5
i=1
while i<=rows:
    j=1
    while j<=i:
        print((i*2-1),end=" ")
        j=j+1
    i=i+1
    print("")


#program 13

rows=5
for i in range(rows,0,-1):
    num =i
    for j in range(0,i):
        print(num,end=" ")
    print("\r")


# program 14

rows =5
for i in range(1, rows):
    for j in range(i,0,-1):
        print(j,end=' ')
    print("\r")

#program 15

rows=5
for i in range(0,rows+1):
    for j in range(rows-i,0,-1):
        print(j,end=' ')
    print( )

#program 16

rows =6
for i in range(1,rows):
    num=1
    for j in range(rows,0,-1):
        if j>i:
            print(" ",end =' ')
        else:
            print(num,end=' ')
            num+=1
    print(" ")


# program 17

rows=8
for i in range(1,rows+1):
    for j in range(1,i+1):
        square=i*j
        print(i*j,end=' ')
    print( )

#program 18

rows=5
for i in range(rows+1,0,-1):
    for j in range(0,i-1):
        print("*",end=' ')
    print(" ")

#program 19

rows=5
k=2*rows-2
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")

#program 20


rows=5
for i in range(1,rows+1):
    for j in range(1,row+1):
        if j<=1:
            print(i,end=' ')
        else:
            print(j,end=' ')
    print()

        


