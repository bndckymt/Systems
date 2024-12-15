import sqlite3

# Connect to a database
conn = sqlite3.connect('MSMdatabase.db')

# Create a cursor object
cursor = conn.cursor()

while True:
    item = int(input("How many items do you want to delete? "))
    if item == 1:
        user_id_to_delete = int(input("Enter the number of the item you want to delete: "))
        cursor.execute("DELETE FROM product WHERE number = ?", (user_id_to_delete,))
        conn.commit()
    elif item > 1:
        start = int(input("Enter the number where you want to start deleting: "))
        end = int(input("Enter the last number of the items you want to delete: "))
        if start <= end:
            for delete in range(start, end + 1):  # Adjust loop to include 'end' value
                cursor.execute("DELETE FROM product WHERE number = ?", (delete,))
            conn.commit()
        else:
            print("Start number must be less than or equal to the end number.")
    else:
        print("Invalid input. Please enter a valid number of items to delete.")
        break  # This ensures the loop stops for invalid input

    continue_prompt = input("Do you want to delete more items? (yes/no): ").strip().lower()
    if continue_prompt != 'yes':
        break


# Commit the changes
conn.commit()
conn.close()
