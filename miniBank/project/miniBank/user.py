import mysql.connector


def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="alireza",
        passwd="alireza",
        database="Bank"
    )
    cursor = conn.cursor()
    return conn, cursor


def check_credentials(username, password):
    conn, cursor = connect()
    try:
        cursor.callproc('bank.CheckCredentials', (username, password))

        result = cursor.stored_results()

        for row in result:
            return row.fetchall()[0]

    except mysql.connector.Error as err:
        print("Error calling stored procedure:", err)

    # Close the cursor and connection
    cursor.close()
    conn.close()


def change_password(user_id, current_password, new_password):
    try:
        conn, cursor = connect()

        # Call the ChangePassword stored procedure
        cursor.callproc("ChangePassword", (user_id, current_password, new_password))

        # Fetch the result message
        for result in cursor.stored_results():
            message = result.fetchone()[0]

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return message

    except mysql.connector.Error as error:
        print("Error:", error)
        return "Error occurred while changing password."


def get_account_credentials(user_id):
    try:
        conn, cursor = connect()
        cursor.callproc("GetAccountCredentials", (user_id,))
        result = cursor.stored_results()
        cursor.close()
        conn.close()
        accounts = []
        for rs in result:
            for row in rs.fetchall():
                accounts.append(row)
        return accounts
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def get_account_info(account_number):
    try:
        conn, cursor = connect()
        cursor.callproc("GetAccountInfoWithOwnerName", (account_number,))
        result = cursor.stored_results()
        for rs in result:
            for row in rs.fetchall():
                print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def transfer_amount(source_account_id, destination_account_id, amount):
    try:
        conn, cursor = connect()
        # Call the stored procedure
        cursor.callproc("TransferAmount", (source_account_id, destination_account_id, amount))

        # Fetch the result of the procedure call
        for result in cursor.stored_results():
            for row in result.fetchall():
                print(row)

        # Commit the changes
        conn.commit()

    except mysql.connector.Error as err:
        # Handle errors
        print("Error:", err)
        # Rollback the transaction in case of an error
        conn.rollback()


# Example usage:
#username = "ali"
#password = "123"
#check_credentials(username, password)

# if name is not None:
#     print("Welcome,", name)
# else:
#     print("Invalid credentials")

# # Example usage:
# user_id = 1
# current_password = "current_password"
# new_password = "new_password"
# result_message = change_password(user_id, current_password, new_password)
# print("Result:", result_message)
