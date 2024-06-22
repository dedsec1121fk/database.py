import os
import textwrap

DATA_FILE = '/sdcard/database_data.txt'

def add_data():
    data = input("Enter data to add: ")
    with open(DATA_FILE, 'a') as f:
        f.write(data + '\n')
    print("Data added successfully.")

def edit_data():
    if not os.path.exists(DATA_FILE):
        print("No data found to edit.")
        return
    
    with open(DATA_FILE, 'r') as f:
        lines = f.readlines()
    
    if not lines:
        print("The file is empty. Nothing to edit.")
        return
    
    print("Current data (edit as needed):\n")
    current_data = ''.join(lines)
    print(current_data)
    
    new_data = []
    print("Enter your edits (finish with a single line containing 'END'):")
    
    while True:
        line = input()
        if line == 'END':
            break
        new_data.append(line)
    
    with open(DATA_FILE, 'w') as f:
        f.write('\n'.join(new_data) + '\n')
    print("Data edited successfully.")

def search_data():
    search_term = input("Enter search term: ")
    with open(DATA_FILE, 'r') as f:
        matching_lines = [line.strip() for line in f if search_term in line]
    
    if not matching_lines:
        print("No matching data found.")
    else:
        print("Matching data:")
        for line in matching_lines:
            print(line)

def see_database():
    if not os.path.exists(DATA_FILE):
        print("No data found. The database is empty.")
        return
    
    with open(DATA_FILE, 'r') as f:
        data = f.read().strip()
    
    if not data:
        print("The database is empty.")
    else:
        print(data)

def main():
    while True:
        print("\n")
        print("1) Add Data")
        print("2) Edit Data")
        print("3) Search Data")
        print("4) See Database")
        print("5) Exit")
        print("\n")
        
        option = input("Choose an option: ")

        if option == '1':
            add_data()
        elif option == '2':
            edit_data()
        elif option == '3':
            search_data()
        elif option == '4':
            see_database()
        elif option == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()