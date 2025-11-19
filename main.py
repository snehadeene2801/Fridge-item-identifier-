 def _init_(self, name, expiration_date, quantity):
        self.name = name
        self.expiration_date = expiration_date
        self.quantity = quantity

class Fridge:
    def _init_(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"{item_name} removed from fridge.")
                return
        print(f"{item_name} not found in fridge.")

    def check_expiration(self):
        for item in self.items:
            print(f"{item.name}: {item.expiration_date}")

    def check_quantity(self, item_name):
        for item in self.items:
            if item.name == item_name:
                print(f"{item_name}: {item.quantity}")
                return
        print(f"{item_name} not found in fridge.")

def main():
    fridge = Fridge()

    while True:
        print("\n1. Add item to fridge")
        print("2. Remove item from fridge")
        print("3. Check expiration dates")
        print("4. Check quantity of item")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            expiration_date = input("Enter expiration date: ")
            quantity = input("Enter quantity: ")
            item = FridgeItem(name, expiration_date, quantity)
            fridge.add_item(item)
        elif choice == "2":
            item_name = input("Enter item name: ")
            fridge.remove_item(item_name)
        elif choice == "3":
            fridge.check_expiration()
        elif choice == "4":
            item_name = input("Enter item name: ")
            fridge.check_quantity(item_name)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()