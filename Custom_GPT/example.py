# import cx_Oracle
#
# # Replace 'your_username', 'your_password', 'localhost:1521', and 'your_service_name' with your actual database credentials
# connection = cx_Oracle.connect('system/M@llik@123@localhost:1521/orcl')
#
# table_name = 'MOBILEPHONES_DETAILS'
#
# def execute_query(query):
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         result = cursor.fetchall()
#     return result
#
# def get_dataset_dict():
#     query = f"SELECT * FROM {table_name} "
#     cursor = connection.cursor()
#     cursor.execute(query)
#     columns = []
#     for col in cursor.description:
#         columns.append(col[0])
#
#     dataset_details = []
#     for row in cursor.fetchall():
#         columns_with_rows = dict(zip(columns, row))
#         dataset_details.append(columns_with_rows)
#
#     return dataset_details
#
# def main():
#     dataset_details = get_dataset_dict()
#     while True:
#         user_input = input("Enter your query (or 'exit' to quit): ").lower()
#         if user_input == 'exit':
#             print("Thank You!")
#             break
#
#         user_input = user_input.split()
#
#         # Check if user input matches any column names
#         matching_columns = []
#         for col in dataset_details[0].keys():
#             for token in user_input:
#                 if token in col.lower():
#                     matching_columns.append(col)
#                     # break
#
#         if matching_columns:
#             # User input matches a column name, print values of that column
#             for col in matching_columns:
#                 column_values = []
#                 for row in dataset_details:
#                     column_values.append(row[col])
#                 print(f"{col.capitalize()} Values:", column_values)
#         else:
#             # Search for rows where each user value is present in a different column
#             matching_rows = []
#
#             for row in dataset_details:
#                 match = True
#                 for token in user_input:
#                     if not any(token in str(row[key]).lower() for key in row.keys()):
#                         match = False
#                         break
#                 if match:
#                     matching_rows.append(row)
#
#             if matching_rows:
#                 # Print matching rows
#                 for matching_row in matching_rows:
#                     for key, value in matching_row.items():
#                         print(f"{key}: {value}")
#                     print("---")
#
#             elif "column" in user_input or "columns" in user_input:
#                 # Print column names
#                 print("Column Names:", dataset_details[0].keys())
#
#             else:
#                 print("No matching records found.")
#
# if __name__ == "__main__":
#     main()


import cx_Oracle

# Replace 'your_username', 'your_password', 'localhost:1521', and 'your_service_name' with your actual database credentials
connection = cx_Oracle.connect('system/M@llik@123@localhost:1521/orcl')

table_name = 'MOBILEPHONES_DETAILS'

def execute_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

def get_dataset_dict():
    query = f"SELECT * FROM {table_name} "
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]

    dataset_details = []
    for row in cursor.fetchall():
        columns_with_rows = dict(zip(columns, row))
        dataset_details.append(columns_with_rows)

    return dataset_details

def main():
    dataset_details = get_dataset_dict()
    while True:
        user_input = input("Enter your query (or 'exit' to quit): ").lower()
        if user_input == 'exit':
            print("Thank You!")
            break

        user_input = user_input.split()

        # Check if user input matches any column names
        matching_columns = []
        for col in dataset_details[0].keys():
            for token in user_input:
                if token in col.lower():
                    matching_columns.append(col)

        if matching_columns:
            # User input matches a column name, print values of that column
            for col in matching_columns:
                column_values = []
                for row in dataset_details:
                    column_values.append(row[col])
                print(f"{col.capitalize()} Values:", column_values)
        else:
            # Search for rows where each user value is present in a different column
            matching_rows = []

            for row in dataset_details:
                match = True
                for token in user_input:
                    if token.startswith('<') and token[1:].isdigit():
                        col_name = token[1:]
                        if row[col_name] >= float(row[col_name]):
                            match = False
                            break
                    elif token.startswith('>') and token[1:].isdigit():
                        col_name = token[1:]
                        if row[col_name] <= float(row[col_name]):
                            match = False
                            break
                    elif 'to' in token:
                        range_values = token.split('to')
                        if len(range_values) == 2 and range_values[0].isdigit() and range_values[1].isdigit():
                            col_name = range_values[0]
                            value1, value2 = float(range_values[0]), float(range_values[1])
                            if not (value1 <= row[col_name] <= value2):
                                match = False
                                break
                    elif not any(token in str(row[key]).lower() for key in row.keys()):
                        match = False
                        break

                if match:
                    matching_rows.append(row)

            if matching_rows:
                # Print matching rows
                for matching_row in matching_rows:
                    for key, value in matching_row.items():
                        print(f"{key}: {value}")
                    print("---")

            elif "column" in user_input or "columns" in user_input:
                # Print column names
                print("Column Names:", dataset_details[0].keys())

            else:
                print("No matching records found.")

if __name__ == "__main__":
    main()
