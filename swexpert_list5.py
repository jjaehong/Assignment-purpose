
num = int(input())

result = []
for i in range(1, num + 1):
    if num % i == 0:
        result.append(i)

print(result)

# lst = [i for i in range(1,num+1) if num % i ==0]
# print(lst)