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

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return value

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
            if any(user_input in col.lower() for user_input in user_input):
                matching_columns.append(col)

        if matching_columns and len(user_input) > 1:
            # User input matches a column name, retrieve rows with specified values
            col_name = matching_columns[0]
            col_values = user_input[1:]

            matching_rows = []
            for row in dataset_details:
                for val in col_values:
                    if isinstance(row[col_name], str) and convert_to_float(row[col_name].lower()) == convert_to_float(val.lower()):
                        matching_rows.append(row)
                    elif isinstance(row[col_name], (int, float)) and convert_to_float(row[col_name]) == convert_to_float(val.lower()):
                        matching_rows.append(row)

            if matching_rows:
                # Print matching rows
                for matching_row in matching_rows:
                    for key, value in matching_row.items():
                        print(f"{key}: {value}")
                    print("---")
            else:
                print(f"No matching records found for {col_name} values: {', '.join(col_values)}")

        elif matching_columns:
            # User input matches a column name, print values of that column
            for col in matching_columns:
                column_values = [columns_with_rows[col] for columns_with_rows in dataset_details]
                print(column_values)

        else:
            # Search for rows where each user value is present in a different column
            matching_rows = []

            for columns_with_rows in dataset_details:
                match = True
                for user_input_item in user_input:
                    if all(user_input_item not in str(columns_with_rows[key]).lower() for key in columns_with_rows.keys()):
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

            elif "column" in user_input or "columns" in user_input:
                # Print column names
                print("Column Names:", dataset_details[0].keys())
            else:
                print("No matching records found.")

if __name__ == "__main__":
    main()
