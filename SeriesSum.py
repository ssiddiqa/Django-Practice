def SeriesSum(n):
    sum = (n*(n+1))/2
    return sum


n = int(input("Enter the value of n: "))
sum = SeriesSum(n)
print("Sum of Series: ", sum)
