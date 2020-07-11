print("Welcome to your daily expense tracker")
print("Enter Login details")

#Accepting login credentials
while True:
    userid=input("enter userid")
    if userid!='diksha':
        continue
    password=input("your password?")
    if password=='patil':
        break

#Accept monthly income
while True:
    try:
        income=int(input("Enter your monthly income"))
    except ValueError:
        print("enter valid income amount")
    else:
        break
#Creating dictionary of expenditure
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
total=expense.values()
totalexp=sum(total)

#accept luxury items
#suggest item to be purchased
def luxury():
    global savings
    print("Welcome to luxury mart")
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
    list1=list(luxury.values())
    list2=list(luxury.keys())
    for i in range(len(luxury)):
        if savings>=list1[i]:
            print("you may buy"+str(list2[i]))
            savings=savings-list1[i]
        else:
            print("you're out of budget to buy luxury item")

savings=income - totalexp        
if savings<0:
    print("you extra spent"+str(abs(savings)))
else:
    print("Congratulations!You managed to save")
    luxury()





