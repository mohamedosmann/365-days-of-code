cargo_list = []

def add_cargo(item):
    cargo_list.append(item)
    print(f"{item} added to cargo ")

def remove_cargo(item):
    cargo_list.remove(item)
    if item in cargo_list:
        print(f"{item} removed from the cargo")
    else:
        print("Item not found ")
def viewcargo(item):
    print(f"\the current cargo list : ")
    for idx, item in enumerate(cargo_list):
        print(f"{idx + 1}.{item}")

while True:
    print("\n1. Add cargo \n2. remove cargo \n3. view cargo \n4. EXIT")
    choice = int(input("Enter choice "))
    if choice == 1:
        item = input("Enter Cargo items to add ")
        add_cargo(item)
    elif choice ==2:
        item = input("enter items to remove ")
        remove_cargo(item)
    elif choice == 3:
        item = input("view cargo ")
        viewcargo(item)
    elif choice == 4:
        print("Exiting")
        break
    else:
        print("Invalid choice ")

