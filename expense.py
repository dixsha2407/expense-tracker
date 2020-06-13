income=int(input())
dict1={}
while input("Enter q to quit,c to continue ") != 'q':
    while True:
        key=input("enter item")
        if not type(key) is str:
            raise TypeError("Enter string value")
        else:
            break
    while True:
        value1=input("enter price ")
        if not type(value1) is int:
            raise TypeError("enter number")
        else:
            break
    dict1.update({key:value1})
print(dict1)
spent= (sum(dict1.values()))
money= income-spent
if money<0:
    print("you extra spent ",abs(money))
else:
    print("you saved ",money)

