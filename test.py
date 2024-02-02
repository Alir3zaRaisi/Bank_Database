import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="alireza",
    passwd="alireza",
    database="Bank"
)

cursor = db.cursor()

# cursor.execute("""CREATE TABLE customers(
#     userID INT AUTO_INCREMENT PRIMARY KEY,
#     firstname VARCHAR(255) NOT NULL,
#     lastname VARCHAR(255) NOT NULL,
#     username VARCHAR(255) UNIQUE,
#     password VARCHAR(255) NOT NULL
# );
# )""")


# cursor.execute("""
#     CREATE TABLE accounts (
#         account_number INT PRIMARY KEY,
#         userID INT,
#         balance INT CHECK (balance > 0),
#         status ENUM('active', 'inactive'),
#         FOREIGN KEY (userID) REFERENCES customers(userID) ON DELETE CASCADE
#     );
# """)


# sql_create_function = """
#     CREATE FUNCTION CheckCredentials(p_username VARCHAR(255), p_password VARCHAR(255))
#     RETURNS VARCHAR(255)
#     DETERMINISTIC
#     BEGIN
#         DECLARE v_user_name VARCHAR(255);
#
#         -- Retrieve the concatenated first name and last name if the provided username and password match
#         SELECT CONCAT(firstname, ' ', lastname) INTO v_user_name
#         FROM customers
#         WHERE username = p_username AND password = p_password;
#
#         -- If a record with the provided username and password exists, return the concatenated name, otherwise return NULL
#         IF v_user_name IS NOT NULL THEN
#             RETURN v_user_name;
#         ELSE
#             RETURN NULL;
#         END IF;
#     END
#     """
#
# # Execute the SQL query to create the function
# cursor.execute(sql_create_function)


# sql_create_procedure = """
#
#         CREATE PROCEDURE ChangePassword(
#             IN p_userID INT,
#             IN p_password VARCHAR(255),
#             IN p_new_password VARCHAR(255)
#         )
#         BEGIN
#             DECLARE v_count INT;
#
#             -- Check if the provided userID and password match a record in the customers table
#             SELECT COUNT(*) INTO v_count
#             FROM customers
#             WHERE userID = p_userID AND password = p_password;
#
#             -- If a match is found, update the password with the new password
#             IF v_count > 0 THEN
#                 UPDATE customers
#                 SET password = p_new_password
#                 WHERE userID = p_userID;
#
#                 SELECT 'Password changed successfully.' AS message;
#             ELSE
#                 SELECT 'Invalid credentials.' AS message;
#             END IF;
#         END
#         """
#
# # Execute the SQL query to create the procedure
# cursor.execute(sql_create_procedure)
#
# print("Procedure created successfully.")


# sql_account_credentials_procedure = """
#     CREATE PROCEDURE GetAccountCredentials(IN p_userID INT)
#         BEGIN
#             SELECT account_number, balance, status
#             FROM accounts
#             WHERE userID = p_userID;
#         END
# """
# cursor.execute(sql_account_credentials_procedure)

sql_account_info_procedure = """
    CREATE PROCEDURE GetAccountInfo(IN p_account_number INT)
        BEGIN
            SELECT a.account_number, a.balance, a.status, c.first_name, c.last_name
            FROM accounts a
            INNER JOIN customers c ON a.userID = c.userID
            WHERE userID = p_userID;
        END
"""

cursor.execute(sql_account_info_procedure)

db.commit()

cursor.close()
db.close()

