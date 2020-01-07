'''
- Use a for loop to compute the 10th triangular number.
- The nth triangular number is defined as 1+2+3+...+n.
- You can also compute the nth triangular number as n*(n+1)/2
'''

n = 10
triangular = 0
for i in range(n + 1):
    triangular += i

print(triangular)
print(n * (n + 1) / 2)
