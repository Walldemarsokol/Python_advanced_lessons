num = int(input("enter year: "))

if num <1582:
    res = "Not answer"

elif num%4 !=0 or num % 100 == 0 and num % 400 !=0:
    res = "Not Visokosniy"
else:
    res = "Visokosniy"

print(res)