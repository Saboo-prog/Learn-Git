# Input:  [10, 5, 20, 20, 8, 15]
# Output: 15


arr = [10, 5, 20, 70, 8, 15]
a = float('-inf')
b = float('-inf')

for i in range(len(arr)):
    if(arr[i] > a):
        b= a
        a = arr[i]
    elif(arr[i] > b) and arr[i] != a :
        b = arr[i]


print(a)
print(b)

