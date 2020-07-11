print("Welcome to your daily expense tracker")
print("Enter Login details")
while True:
    userid=input("enter userid")
    if userid!='diksha':
        continue
    password=input("your password?")
    if password=='patil':
        break

income=int(input("Enter your monthly income"))
expense={}
while True:  
    item=input("enter item purchased")
    while True:
        try:
            price=int(input("enter price "))
        except ValueError:
            print("invalid input")
        else:
            break
    expense.update({item:price})
    response=input("enter q to quit,any key to continue")
    if response=='q'or response=='Q':
        break
print(expense)
totalexp=sum(expense.values)
savings=income-totalexp

def luxury():
    print("you saved"+str(savings))
    print("Enter your luxury list")
    luxury={}
    while True:  
        lxitem=input("enter luxury item ")
        while True:
            try:
                lxprice=int(input("enter item price "))
            except ValueError:
                print("invalid input")
            else:
                break
        luxury.update({lxitem:lxprice})
        res=input("enter q to quit,any key to continue")
        if res=='q'or res=='Q':
            break
    
        



if savings<0:
    print("you extra spent"+str(abs(savings)))
else:
    luxury()




