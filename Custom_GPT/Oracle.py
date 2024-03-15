import cx_Oracle

# Replace 'your_username', 'your_password', 'your_host:your_port/your_service' with your actual database credentials
connection = cx_Oracle.connect('system/M@llik@123@localhost:1521/orcl')

# Create a cursor
cursor = connection.cursor()

try:
    # Execute a sample SQL query
    cursor.execute("SELECT * FROM MOBILEPHONES_DETAILS")

    # Fetch and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()



import cx_Oracle

# Replace 'your_username', 'your_password', 'localhost:1521', and 'your_service_name' with your actual database credentials
connection = cx_Oracle.connect('system/M@llik@123@localhost:1521/orcl')

table_name = 'ORDER_DETAILS'


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

        user_input_tokens = user_input.split()

        # Check if user input exactly matches any column names
        matching_columns = [col for col in dataset_details[0].keys() if user_input in col.lower()]

        if matching_columns:
            # User input exactly matches a column name, print values of that column
            for col in matching_columns:
                column_values = [columns_with_rows[col] for columns_with_rows in dataset_details]
                print(f"{col.capitalize()} Values:", column_values)

        else:
            # Search for rows where each user value is present in a different column
            matching_rows = []

            for columns_with_rows in dataset_details:
                match = True
                for user_input in user_input_tokens:
                    if user_input.isdigit():
                        # Handle numeric values
                        if not any(float(user_input) == columns_with_rows[key] for key in columns_with_rows.keys()):
                            match = False
                            break
                    else:
                        # Handle non-numeric values
                        if not any(user_input in str(columns_with_rows[key]).lower() for key in columns_with_rows.keys()):
                            match = False
                            break

                if match:
                    matching_rows.append(columns_with_rows)

            if matching_rows:
                # Print matching rows
                for matching_row in matching_rows:
                    for key, value in matching_row.items():
                        print(f"{key}: {value}")
                    print("---")

            elif "column" in user_input_tokens or "columns" in user_input_tokens:
                # Print column names
                print("Column Names:", dataset_details[0].keys())

            else:
                print("No matching records found.")


if __name__ == "__main__":
    main()




