import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="alireza",
    passwd="alireza",
    database="bank"
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

#

# sql_create_procedure = """
# CREATE PROCEDURE `CheckCredentials`(IN p_username VARCHAR(255), IN p_password VARCHAR(255), OUT p_full_name VARCHAR(255), OUT p_user_id INT)
#     BEGIN
#     DECLARE v_user_name VARCHAR(255);
#     DECLARE v_user_id INT;
#
#     -- Retrieve the concatenated first name and last name and the user ID if the provided username and password match
#     SELECT CONCAT(firstname, ' ', lastname), userID INTO v_user_name, v_user_id
#     FROM customers
#     WHERE username = p_username AND password = p_password;
#
#     -- If a record with the provided username and password exists, set the output parameters, otherwise set them to NULL
#     IF v_user_name IS NOT NULL THEN
#         SET p_full_name = v_user_name;
#         SET p_user_id = v_user_id;
#     ELSE
#         SET p_full_name = NULL;
#         SET p_user_id = NULL;
#     END IF;
#     END
#
#     """
#
# # Execute the SQL query to create the function
# cursor.execute(sql_create_procedure)


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

# sql_function_loan_points = """
#     CREATE FUNCTION calculate_loan_points(p_account_number INT)
#     RETURNS INT
#     BEGIN
#         DECLARE total_income INT;
#         DECLARE total_expense INT;
#         DECLARE two_months_ago DATE;
#
#         -- Get the date two months ago
#         SET two_months_ago = DATE_SUB(CURDATE(), INTERVAL 2 MONTH);
#
#         -- Calculate total income for the past two months
#         SELECT COALESCE(SUM(amount), 0) INTO total_expense
#         FROM transactions
#         WHERE source_number = p_account_number
#         AND transaction_date >= two_months_ago;
#
#         -- Calculate total expense for the past two months
#         SELECT COALESCE(SUM(amount), 0) INTO total_income
#         FROM transactions
#         WHERE destination_number = p_account_number
#         AND transaction_date >= two_months_ago;
#
#         -- Return net value (income - expense)
#         RETURN total_income - total_expense;
#     END;
# """


# sql_last_n_transactions_account_procedure = """
#     CREATE PROCEDURE GetLastNTransactionsForAccount(
#         IN p_account_number INT,
#         IN p_n INT
#     )
#     BEGIN
#         SELECT transaction_number, source_number, destination_number, amount, date
#         FROM transactions
#         WHERE source_number = p_account_number OR destination_number = p_account_number
#         ORDER BY date DESC
#         LIMIT p_n;
# END
# """
# cursor.execute(sql_last_n_transactions_account_procedure)

# cursor.execute("select CheckCredentials(%s,%s)", ("ali", "123"))
# result = cursor.fetchone()[0]
# print(result)


# statements = [
#     "set @p_full_name = '0';",
#     "set @p_user_id = 0;",
#     "call bank.CheckCredentials('ali', '123', @p_full_name, @p_user_id);",
#     "select @p_full_name, @p_user_id;"
# ]
#
# for statement in statements:
#     cursor.execute(statement)


# Call the stored procedure
cursor.callproc('bank.CheckCredentials', ('ali', '234'))

result = cursor.stored_results()

for row in result:
    name, userid = row.fetchall()[0]

print(name)
# db.commit()

cursor.close()
db.close()
