import mysql.connector


def connect():
    conn = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    cursor = conn.cursor()
    return conn, cursor


def check_credentials(username, password):
    # Connect to your MySQL database
    conn, cursor = connect()

    # Execute the SQL query that calls the CheckCredentials function
    cursor.callproc("CheckCredentials", (username, password))
    result = cursor.fetchone()[0]

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return result


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


def call_stored_procedure(user_id):
    try:
        conn, cursor = connect()
        cursor.callproc("GetAccountCredentials", (user_id,))
        result = cursor.stored_results()
        for rs in result:
            for row in rs.fetchall():
                print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# Example usage:
username = "example_username"
password = "example_password"
name = check_credentials(username, password)

if name is not None:
    print("Welcome,", name)
else:
    print("Invalid credentials")

# Example usage:
user_id = 1
current_password = "current_password"
new_password = "new_password"
result_message = change_password(user_id, current_password, new_password)
print("Result:", result_message)
