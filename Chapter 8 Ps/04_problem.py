# wap by recusion sum of n natural number
def sum (n):
    if(n==1):
        return 1
    return(sum(n-1)+n)
print(sum(3))
