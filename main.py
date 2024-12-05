

from contact_manager import add_contact,view_contact,remove_contact,search_contact


while True:
    print("1. add contact")
    print("2. view contact")
    print("3. remove contact")
    print("4. search contact")
    print("0. exit")

    choice = input("enter your choice: ")
    if choice == "1":
        name = input("enter your name: ")
        mobile = int(input("enter your mobile numeber: "))
        email = input("enter your email: ")
        address = input("enter your address:")
        add_contact(name, mobile, email, address)
        print("contact add successfully")

    elif choice == "2":
        view_contact()

    elif choice == "3":
        index = int(input("enter your index:"))
        remove_contact()
        print("contact remove succesfully")
    elif choice == "4":
        query = input("enter your search query:")
        search_contact(query)

    elif choice == "0":
        break


