 #Expense tracker project


expenselist=[] #list all expense in the form of dictionary
print("WELCOME TO  EXPENSE TRACKER :SAVE MONEY 💸")

while True:
    print("=====MENU💗====")
    print("1. ADD EXPENSE")
    print("2.VIEW ALL EXPENSES")
    print("3. VIEW TOTAL EXPENSES")
    print("4.EXIT⛳")


    choice= int(input("please enter your choice :"))
#ADD EXPENSE 💰
    if (choice ==1):
        data= input("The date on which the expenses were incurred.📅")
        category= input("Expense category📊(e.g.,food🍔,shopping🛍️,travel✈️)")
        description= input(" Give more details📄:")
        amount=float(input("enter the amount💸"))

        expense={
            "data📅":data,
            "category🗂️":category,
            "description📝":description,
            "amount💸":amount
        }

        expenselist.append(expense)  
        print("\n DONE :👍. Expenses is added sucessfully✅😊")


# 2. VIEW ALL EXPENSES👀📊
  
    elif(choice == 2):
        if(len(expenselist)==0):
            print("No EXPENSES ADDED❌💰")
        else:
            print("==== HERE YOUR EXPENSE====")
            count= 1   
            for eachexpense in expenselist:
                print(f"expense number {count} -> {eachexpense["data📅"]} ,{eachexpense["category🗂️"]},{eachexpense["description📝"]},{eachexpense["amount💸"]} ")
                count=count+1

# 3. VIEW TOTAL SPENDING 📊💰

    elif(choice==3):
        total=0
        for eachspending in expenselist:
            total=total+eachexpense["amount💸"]
        print("\n TOTAL EXPENSE =",total)

#4. EXIT 🚪 
    elif(choice==4):
        print("THANK YOU FOR USING THIS SYSTEM 😊🙏")
        break
    else:
        print("INVAID CHOICE")
    





