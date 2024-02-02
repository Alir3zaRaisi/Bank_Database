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

# sql_account_info_procedure = """
#     CREATE PROCEDURE GetAccountInfo(IN p_account_number INT)
#         BEGIN
#             SELECT a.account_number, a.balance, a.status, c.firstname, c.lastname
#             FROM accounts a
#             INNER JOIN customers c ON a.userID = c.userID
#             WHERE userID = p_userID;
#         END
# """
#
# cursor.execute(sql_account_info_procedure)


# sql_account_name_function = """
#     CREATE FUNCTION GetOwnerNameForAccount(p_account_number INT)
#     RETURNS VARCHAR(255)
#     READS SQL DATA
#     BEGIN
#         DECLARE owner_name VARCHAR(255);
#         SELECT CONCAT(c.firstname, ' ', c.lastname) INTO owner_name
#         FROM accounts a
#         INNER JOIN customers c ON a.userID = c.userID
#         WHERE a.account_number = p_account_number;
#         RETURN owner_name;
#     END
# """
#
# cursor.execute(sql_account_name_function)

# cursor.execute("""
#     ALTER TABLE accounts
#     ADD COLUMN creation_date DATE;
# """)

# cursor.execute("""
#     CREATE TABLE transactions(
#     transaction_number INT AUTO_INCREMENT PRIMARY KEY,
#     source_number INT,
#     destination_number INT,
#     amount INT check ( amount > 0 ),
#     date DATE,
#     FOREIGN KEY (source_number) REFERENCES accounts (account_number) ON DELETE SET NULL,
#     FOREIGN KEY (destination_number) REFERENCES accounts(account_number) ON DELETE set null
#     )
# """)
#
# cursor.execute("""
#     CREATE TABLE Loans(
#     loan_number INT AUTO_INCREMENT PRIMARY KEY,
#     account_number INT,
#     amount INT check ( amount > 0 ),
#     payment_amount INT check ( payment_amount > 0 ),
#     FOREIGN KEY (account_number) REFERENCES accounts(account_number) ON DELETE SET NULL
#     )
# """)
#
# cursor.execute("""
#     CREATE TABLE loan_payment(
#     loan_number INT,
#     payment_date DATE,
#     FOREIGN KEY (loan_number) REFERENCES loans(loan_number)
#     )
# """)


# sql_transaction_procedure = """
# CREATE PROCEDURE TransferAmount(
#     IN p_source_account_id INT,
#     IN p_destination_account_id INT,
#     IN p_amount INT
# )
# BEGIN
#     DECLARE source_balance INT;
#
#     -- Start transaction
#     START TRANSACTION;
#
#     -- Get balance of the source account
#     SELECT balance INTO source_balance
#     FROM accounts
#     WHERE account_number = p_source_account_id;
#
#     -- Check if the source account has sufficient balance
#     IF source_balance >= p_amount THEN
#         -- Subtract the amount from the source account
#         UPDATE accounts
#         SET balance = balance - p_amount
#         WHERE account_number = p_source_account_id;
#
#         -- Add the amount to the destination account
#         UPDATE accounts
#         SET balance = balance + p_amount
#         WHERE account_number = p_destination_account_id;
#
#         -- Commit the transaction
#         COMMIT;
#
#         SELECT 'Transaction Successful' AS result;
#     ELSE
#         -- Rollback the transaction
#         ROLLBACK;
#
#         SELECT 'Insufficient Balance' AS result;
#     END IF;
# END
# """
#
# cursor.execute(sql_transaction_procedure)

db.commit()

cursor.close()
db.close()

