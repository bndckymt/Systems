import csv

#dictionary
data = {}

# Function to add a name to the data
def write_data():
    row_index = int(input("Enter the row number where you want to store the name: "))
    name = input("Enter a name: ")
    data[row_index] = name
    print(f"Name '{name}' added to row {row_index}!")

# Function to read a specific row from the data
def read_data():
    row_index = int(input("Enter the row number you want to read: "))
    if row_index in data:
        print(f"Row {row_index}: {data[row_index]}")
    else:
        print("No data found in that row!")

# Function to save the data to an Excel file and close the program
def close_database():
    file_path = input("Enter the file path where you want to save the names.csv file: ")
    with open(file_path + '/names.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Row", "Name"])  # header row
        for row_index, name in sorted(data.items()):
            writer.writerow([row_index, name])
    print("Data saved to " + file_path + "/names.csv! Goodbye!")

# Main 
while True:
    print("Options:")
    print("1. Write data")
    print("2. Read data")
    print("3. Close database")
    choice = input("Enter your choice: ")

    if choice == "1":
        write_data()
    elif choice == "2":
        read_data()
    elif choice == "3":
        close_database()
        break
    else:
        print("Invalid option!")