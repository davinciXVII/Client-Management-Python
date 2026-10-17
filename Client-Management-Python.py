clients = []

def create_client():
    name = input("Enter your name: ") 
    age = input("Enter your age: ")
    address = input("Enter your address: ")
    return [name, age, address]

def find(name):
    found = False
    for i in clients:
        if i[0].lower() == name.lower():  
            read(i)
            print()
            found = True
    if not found:
        print("Client not found.")

def read(client):
    name = client[0]
    age = client[1]
    address = client[2]
    print(f"Client name: {name}\nClient age: {age}\nClient address: {address}")

def menu():
    while True:  
        print("What do you want to do:")
        print("1. Create a Card")
        print("2. Show all Cards")
        print("3. Find a client by name")
        print("4. Exit")  
        
        answer = input("Your choice: ")
        print("-" * 40)
        
        if answer == "1":
            card = create_client()
            clients.append(card)
            print("Card created successfully!")
            print("=" * 40)
        elif answer == "2":
            if not clients:
                print("No cards found.")
            for i in clients:
                read(i)
                print()
            print("=" * 40)
        elif answer == "3":
            name = input("Enter client's name: ")
            find(name)
            print("=" * 40)
        elif answer == "4":
            print("Goodbye!")
            break  
        else:
            print("ERROR: Command not found.")
            print("=" * 40)


if __name__ == "__main__":
    menu()
