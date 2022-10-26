# for i in range(10,22): print(i,end=" ")

# for i in range(15,32,2): print(i,end=" ")

# for i in range(99,9,-1): print(i, end=" ")

# for i in range(10,100,1): print(i,end=" ")

# for i in range(-99,-9,1): print(100-i,end=" ")

# zad 1

# n=int(input())
# for i in range(n):
#   print(i**3+3,end="")


# pre 2 

# petle for liczb trzycyfrowych podzielonych przez 13
# for i in range(100,1000);
#     if i% 13 == 0:
#           print(i)
# petle for liczb dwucyfrowych parzystych 
# for i in range (10,99,2): print(i, end = " ")
# petle for poteg cyfr: 0, 1, 4, 9, 16, .. 81
#  for i in range (10):
#       print(i*i, end=" ")

# zad 3 

# n = int(input())
# for i in range(11, n+1):

# zad 4
# suma = 0 
# for i in range (10,100):
#     suma=suma + i #0+10+11+12+13+....+99
# print(suma)

# suma liczb trzycyfrowych parzystych 

# zad 5

# n = int(input())
# suma = n * (n+1)//2

# for i in range(n-1):
#     k = int(input())
#     suma = suma - k

# print(suma)

# zad 6

n = int(input())
a,b = 0,1

for i in range(n):
    a , b = b , a + b
    print(a,end="")


