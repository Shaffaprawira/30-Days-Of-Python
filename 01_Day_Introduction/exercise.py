def euclidean(a,b,c,d):
   return ((c-a)**2 + (d-b)**2)**(0.5)

# print('checking...')
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

ans = euclidean(num1,num2,num3,num4)

print(f'Euclidean distance between ({num1}, {num2}) and ({num3}, {num4}) is {ans}')
