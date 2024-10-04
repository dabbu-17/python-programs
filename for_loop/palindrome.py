start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
    if str(num) == str(num)[::-1]:
        print(num , end=" ")
