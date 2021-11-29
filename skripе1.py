from random import randint
 
N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)
 
 
for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
 
print(a)
#def bSort(array):
#  length = len(array)
#  for i in range(length):
#    for j in range(0, length-i-1):
#        if array[j] > array[j+1]:
 #     temp = array[j]
  #          array[j] = array[j+1]
   #   array[j+1] = temp