import sys

def main_menu():
    print("....................................................................")
    print("Hello dear user, welcome to our phonebook directory system")
    print("You may now proceed to explore this directory")
    print("....................................................................")
    ch = 0
    while (True):
        ch = menu()
        if ch == 1:
            initial_phonebook()
        elif ch == 2:
            delete_all()
        elif ch == 3:
            search_existing()
        elif ch == 4:
            display_all()
        elif ch == 5:
            break
        else:
            print("Invalid Choice")
    thanks()

def menu():
    print("********************************************************************")
    print("\t\t\tPHONEBOOK DIRECTORY")
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Delete all contacts")
    print("3. Search for a contact")
    print("4. Display all contacts")
    print("5. Exit phonebook")
    choice = int(input("Please enter your choice: "))
    return choice

def initial_phonebook():      

    print("\nEnter contact details in the following order" )
    print("NOTE: * indicates mandatory fields")
    print("....................................................................")
    temp_name=input("Enter name*: ")
    contact_storing("Enter name*: "+temp_name+"\n")
    temp_number=input("Enter number*: ")
    contact_storing("Enter number*: "+temp_number+"\n\n")
    print("Contact succesfully saved")

def contact_storing(temp):
   file = open("./SRC/File/contact.txt","a")
   file.write(temp)
   file.close

def delete_all():
    print("\t\tdeleting Contacts\n")
    contact_deleting()
    print("All contacts deleted")

def contact_deleting():
   file = open("./SRC/File/contact.txt","w")
   file.close
  
def search_existing():
    choice_t=int(input("enter your choice \n 1 for searching by name \n 2 for searching by number\n"))
    if(choice_t==1):
        print("Please enter the name")
        s=input()
        index=search_existing_check("Enter name*: "+s)
        if(index==-1):
            print("Name you are for is not present in phonebook")
        else:
            file = open("./SRC/File/contact.txt")
            # read the content of the file opened
            content = file.readlines()
            print(content[index-1])
            print(content[index])
    elif(choice_t==2):
        print("Please enter the number")
        s=input()
        index=search_existing_check("Enter number*: "+s)
        if(index==-1):
            print("Number you are searching for is not present in phonebook")
        else:
            file = open("./SRC/File/contact.txt")
            # read the content of the file opened
            content = file.readlines()
            print(content[index-2])
            print(content[index-1])
    else:
        print("Invalid choice")

def search_existing_check (string1):
    file1 = open("./SRC/File/contact.txt", "r")
    flag = 0
    index = 0
    for line in file1:  
        index+=1 
        if string1 in line:
            flag=1
            break 
    if flag == 0: 
        return -1 
    else: 
        return index
      

def display_all():
    print("\t\tContact List\n")
    contact_printing()

def contact_printing():
   file = open("./SRC/File/contact.txt","r")
   print(file.read())
   file.close

def thanks():
    print("********************************************************************")
    print("Thank you for using our phonebook directory system.")
    print("Please visit again!")
    print("********************************************************************")
    sys.exit("Goodbye, have a nice day ahead!")

def main():
    main_menu()

if __name__ == "__main__":
    main()
  
