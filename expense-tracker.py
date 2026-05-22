import json

class Expense():
    def __init__(self,amount,category,description,serial_number):
        self.amount = amount
        self.category = category
        self.description = description
        self.serial_number = serial_number
    
expenses = []
def save_expense():

    data = []
    for expense in expenses:
        expense_data = {
            "amount" :expense.amount,
            "category" :expense.category,
            "description" :expense.description,
            "serial_number" :expense.serial_number
        }

        data.append(expense_data)

    with open("expense.json","w") as file:
        json.dump(data,file)

def load_expense():
    try:

        with open("expense.json","r")as file:
            data = json.load(file)
            for item in data:
                expense = Expense(
                    item["amount"],
                    item["category"],
                    item["description"],
                    item["serial_number"]
                )

                expenses.append(expense)
    except:
        pass


def add_expense():
    amount = float(input("Enter amount:"))
    category = input("Enter Category:")
    description = input("Enter description:")
    serial_number = int(input("Enter Serial Number:"))

    expense = Expense(amount,category,description,serial_number)

    expenses.append(expense)

    save_expense()

    print("Item successfully been added!!")

def view_expense():
    if len(expenses) == 0:
        print("Nothing in the Cart!!")
        return
    else:
        for expense in expenses:

            print(f"Amount :${expense.amount}")
            print(f"Category :{expense.category}")
            print(f"Description :{expense.description}")
            print(f"Serial Number :{expense.serial_number}")

def delete_expense():
    delete_serialno = int(input("Enter a serial number to be deleted:"))
    found = 1
    for expense in expenses:

        if expense.serial_number == delete_serialno:
            expenses.remove(expense)
            found = 0
            print(f"Amount :{expense.amount}")
            print(f"Category :{expense.category}")
            print(f"Description :{expense.description}")
            print(f"Serial Number :{expense.serial_number}")

            save_expense()

            print("Expense deleted successfully!!")
            break

    if found == 1:
        print("Unavialable..")

def total_expense():
    total = 0
    for expense in expenses:
        total+= expense.amount

    print(f"The total expense amount is-:,${total}")            
# e1 = Expense(500,"Shirt","Maariage")
# e2 = Expense(600,"Pant","Marriage")
# e3 = Expense(700,"Shoes","Marriage")

# expenses.append(e1)
# expenses.append(e2)
# expenses.append(e3)

load_expense()

while True:
    print("\nMENU-:")
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Delete Expense")
    print("4.Total Expense")
    print("5.Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        total_expense()
    elif choice == "5":
        print("Program Ended..")        
        break
    else:
        print("Invalid Choice!!")