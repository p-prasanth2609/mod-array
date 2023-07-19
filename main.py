a = list(map(int,input().split()))
b=int(input())
number = 0
for digit in a:
    number = number * 10 + digit
c=number%b
print(c)
