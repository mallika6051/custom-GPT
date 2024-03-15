import cx_Oracle

# Replace 'your_username', 'your_password', 'localhost:1521', and 'your_service_name' with your actual database credentials
connection = cx_Oracle.connect('system/M@llik@123@localhost:1521/orcl')

def execute_query(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    finally:
        cursor.close()

def search_value_in_any_column(value):
    query = f"SELECT * FROM MOBILEPHONES_DETAILS WHERE " \
            f"MANUFACTURER LIKE '%{value}%' OR " \
            f"MODEL LIKE '%{value}%' OR " \
            f"COLOR LIKE '%{value}%' OR " \
            f"STORAGE_CAPACITY LIKE '%{value}%' OR " \
            f"SCREEN_SIZE LIKE '%{value}%' OR " \
            f"BATTERY_CAPACITY LIKE '%{value}%' OR " \
            f"OPERATING_SYSTEM LIKE '%{value}%' OR " \
            f"RAM LIKE '%{value}%' OR " \
            f"PROCESSOR LIKE '%{value}%' OR " \
            f"CAMERA_RESOLUTION LIKE '%{value}%' OR " \
            f"FRONT_CAMERA_RESOLUTION LIKE '%{value}%' OR " \
            f"WEIGHT LIKE '%{value}%' OR " \
            f"DIMENSIONS LIKE '%{value}%' OR " \
            f"WATER_RESISTANT LIKE '%{value}%' OR " \
            f"DUAL_SIM LIKE '%{value}%' OR " \
            f"NETWORK_TECHNOLOGY LIKE '%{value}%' OR " \
            f"WIFI LIKE '%{value}%' OR " \
            f"BLUETOOTH LIKE '%{value}%' OR " \
            f"NFC LIKE '%{value}%' OR " \
            f"FINGERPRINT_SCANNER LIKE '%{value}%' OR " \
            f"FACE_UNLOCK LIKE '%{value}%' OR " \
            f"PRICE LIKE '%{value}%'"

    return execute_query(query)

while True:
    user_input = input("Enter a value to search in any column (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Thank You!")
        break

    result = search_value_in_any_column(user_input)
    print("Search results for the provided value:")
    print(result)

# def main():
#     dataset_dict = get_dataset_dict()
#
#     while True:
#         user_input = input("Enter your query (or 'exit' to quit): ").lower()
#         if user_input == 'exit':
#             print("Thank You!")
#             break
#
#         a = user_input.lower()
#
#         if "columns" in user_input:
#             # Print column names
#             columns = dataset_dict[0].keys() if dataset_dict else []
#             print("Column Names:", columns)
#         else:
#             # Search for user input in dataset
#             found = False
#             for row_dict in dataset_dict:
#                 for key, value in row_dict.items():
#                     if user_input in key.lower() or user_input in str(value).lower():
#                         print(f"{key}: {value}")
#                         found = True
#
#             if not found:
#                 print("No matching records found.")

# def main():
#     dataset_dict = get_dataset_dict()
#
#     while True:
#         user_input = input("Enter your query (or 'exit' to quit): ").lower()
#         if user_input == 'exit':
#             print("Thank You!")
#             break
#
#         if "columns" in user_input:
#             # Print column names
#             columns = dataset_dict[0].keys() if dataset_dict else []
#             print("Column Names:", columns)
#         else:
#             # Check if user input matches any column names
#             matching_columns = [col for col in dataset_dict[0].keys() if user_input in col.lower()]
#
#             if matching_columns:
#                 # User input matches a column name, print values of that column
#                 for col in matching_columns:
#                     column_values = [row_dict[col] for row_dict in dataset_dict]
#                     print(f"{col.capitalize()} Values:", column_values)
#             else:
#                 # Search for user input in dataset values
#                 found = False
#                 printed_rows = set()
#
#                 for row_dict in dataset_dict:
#                     if any(user_input in str(value).lower() for value in row_dict.values()) and id(row_dict) not in printed_rows:
#                         for key, value in row_dict.items():
#                             print(f"{key}: {value}")
#                         printed_rows.add(id(row_dict))
#                         found = True
#
#                 if not found:
#                     print("No matching records found.")
# def main():
#     dataset_dict = get_dataset_dict()
#
#     while True:
#         user_input = input("Enter your query (or 'exit' to quit): ").lower()
#         if user_input == 'exit':
#             print("Thank You!")
#             break
#
#         if "columns" in user_input:
#             # Print column names
#             columns = dataset_dict[0].keys() if dataset_dict else []
#             print("Column Names:", columns)
#         else:
#             user_values = user_input.split()
#
#             # Check if user input matches any column names
#             matching_columns = [col for col in dataset_dict[0].keys() if user_input in col.lower()]
#
#             if matching_columns:
#                 # User input matches a column name, print values of that column
#                 for col in matching_columns:
#                     column_values = [row_dict[col] for row_dict in dataset_dict]
#                     print(f"{col.capitalize()} Values:", column_values)
#             else:
#                 # Search for rows where all user values are present
#                 matching_rows = []
#
#                 for row_dict in dataset_dict:
#                     if all(user_value in str(row_dict[key]).lower() for key, user_value in zip(row_dict.keys(), user_values)):
#                         matching_rows.append(row_dict)
#
#                 if matching_rows:
#                     # Print matching rows
#                     for matching_row in matching_rows:
#                         for key, value in matching_row.items():
#                             print(f"{key}: {value}")
#                         print("---")
#                 else:
#                     print("No matching records found.")
# def main():
#     dataset_dict = get_dataset_dict()
#
#     while True:
#         user_input = input("Enter your query (or 'exit' to quit): ").lower()
#         if user_input == 'exit':
#             print("Thank You!")
#             break
#         user_values = user_input.split()
#
#         # Search for rows where all user values are present in any column
#         matching_rows = []
#
#         for row_dict in dataset_dict:
#             if all(any(user_value in str(value).lower() for value in row_dict.values()) for user_value in user_values):
#                 matching_rows.append(row_dict)
#
#         if matching_rows:
#             # Print matching rows
#             for matching_row in matching_rows:
#                 for key, value in matching_row.items():
#                     print(f"{key}: {value}")
#                 print("---")
#         else:
#             print("No matching records found.")

