import mysql.connector
from datetime import datetime
def connect_database():
    return mysql.connector.connect(
        host='localhost', user='root', passwd='Abhay@321', database='railways')

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_future_date(date_string):
    try:
        input_date = datetime.strptime(date_string, "%Y-%m-%d")
        # Check if the date is in the future
        return input_date > datetime.now()
    except ValueError:
        return False

def print_border():
    print("=" * 76)

def checking():
    mycon = connect_database()
    cursor = mycon.cursor()

    print_border()
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    cursor.execute("SELECT * FROM user_account WHERE user_name=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    mycon.close()
    return result is not None

def checking_1():
    mycon = connect_database()
    cursor = mycon.cursor()

    print_border()
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    cursor.execute('SELECT user_name FROM user_account WHERE user_name=%s', (username,))

    existing_user = cursor.fetchone()

    if existing_user:
        print("This username already exists.")
        mycon.close()
        return False

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    phone_number = input("Enter your phone number: ")
    gender = input("Enter your gender (M/F/N): ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    if not is_valid_date(dob):
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        mycon.close()
        return False
    age = input("Enter your age: ")

    try:
        cursor.execute(
            "INSERT INTO user_account (user_name, password, first_name, last_name, phone_number, gender, dob, age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (username, password, first_name, last_name, phone_number, gender, dob, age))
        mycon.commit()
        print("User registered successfully.")
        mycon.close()
        return True

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mycon.close()
        return False

def checking_2():
    mycon = connect_database()
    cursor = mycon.cursor()

    print_border()
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    cursor.execute("SELECT user_name FROM user_account WHERE user_name=%s AND password=%s", (username, password))
    data = cursor.fetchone()

    if data:
        try:
            cursor.execute("DELETE FROM user_account WHERE user_name=%s AND password=%s", (username, password))
            mycon.commit()
            print("Account deleted successfully.")
            mycon.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mycon.close()
            return False
    else:
        print("Your username or password is incorrect.")
        mycon.close()
        return False

def ticket_booking():
    mycon = connect_database()
    cursor = mycon.cursor()

    print_border()
    while True:
        name = input('Enter your name: ')
        if not name.isalpha():
            break
        else:
            print("The name is not valid. Please enter a valid name")

    while True:
        phone = input('Enter your 10-digit phone number: ')
        if len(phone) == 10 and phone.isdigit():
            break
        print("Invalid phone number. Please enter a valid 10-digit number.")

    age = input('Enter your age: ')
    gender = input('Enter your gender (M/F/N): ')

    from_destination = input('Enter your starting point: ')
    to_destination = input('Enter your destination: ')

    # Validate travel date format (YYYY-MM-DD) and ensure it's a future date
    while True:
        travel_date = input('Enter the traveling date (YYYY-MM-DD): ')
        if is_valid_date(travel_date):
            if is_future_date(travel_date):
                break
            else:
                print("The date must be a future date. Please enter a valid future date.")
        else:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    try:
        cursor.execute(
            "INSERT INTO tickets (name, phone, age, gender, from_destination, to_destination, travel_date) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (name, phone, age, gender, from_destination, to_destination, travel_date))
        mycon.commit()
        print('Ticket booked successfully!')

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        mycon.close()

def ticket_checking():
    mycon = connect_database()
    cursor = mycon.cursor()

    print_border()
    phone = input('Enter your phone number: ')

    # Validate phone number format
    if len(phone) != 10 or not phone.isdigit():
        print("Invalid phone number format. Please enter a valid 10-digit phone number.")
        mycon.close()
        return

    try:
        cursor.execute("SELECT * FROM tickets WHERE phone=%s", (phone,))
        data = cursor.fetchall()

        if data:
            print("\nYour tickets:")
            print("=" * 60)
            print(f"{'ID':<10}{'Name':<20}{'From':<15}{'To':<15}{'Date':<15}")
            print("=" * 60)
            for row in data:
                print(f"{row[0]:<10}{row[1]:<20}{row[4]:<15}{row[5]:<15}{row[6]:<15}")
            print("=" * 60)
        else:
            print(f"No tickets found for the phone number {phone}.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        mycon.close()

def ticket_cancelling():
    mycon = connect_database()
    cursor = mycon.cursor()
    phone = input('Enter your phone number: ')

    print_border()
    try:
        cursor.execute("DELETE FROM tickets WHERE phone=%s", (phone,))
        mycon.commit()
        print('Ticket cancelled successfully.')

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        mycon.close()

def menu():
    while True:
        print_border()
        print('################### WELCOME TO RAILWAY RESERVATION SYSTEM ##################')
        print('1. SIGN IN')
        print('2. SIGN UP')
        print('3. DELETE ACCOUNT')
        print('4. EXIT')
        print_border()
        choice = input('Enter your choice: ')

        if choice == '1':
            if checking():
                print('Welcome!')
                main_menu()
            else:
                print('Incorrect username or password.')

        elif choice == '2':
            if checking_1():
                print('Account created successfully. Please sign in.')

        elif choice == '3':
            if checking_2():
                print('Account deleted successfully.')

        elif choice == '4':
            print('Thank you for using the Railway Reservation System. Goodbye!')
            break

        else:
            print('Invalid choice. Please try again.')

def main_menu():
    while True:
        print_border()
        print('1. TICKET BOOKING')
        print('2. TICKET CHECKING')
        print('3. TICKET CANCELLING')
        print('4. LOG OUT')
        print_border()
        choice = input('Enter your choice: ')

        if choice == '1':
            ticket_booking()
        elif choice == '2':
            ticket_checking()
        elif choice == '3':
            ticket_cancelling()
        elif choice == '4':
            print('Logging out...')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    menu()
