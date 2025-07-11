a = int(input("Enter a number: "))
for x in range(a):
    print(2 * x+1 , end=", " if x < a - 1 else "")