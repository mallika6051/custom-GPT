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

    dataset_dict = []
    for row in cursor.fetchall():
        row_dict = dict(zip(columns, row))
        dataset_dict.append(row_dict)

    return dataset_dict

def main():
    dataset_dict = get_dataset_dict()
    # print(dataset_dict)
    while True:
        user_input = input("Enter your query (or 'exit' to quit): ").lower()
        if user_input == 'exit':
            print("Thank You!")
            break

        user_values = user_input.split()

        # Check if user input matches any column names
        matching_columns = [col for col in dataset_dict[0].keys() if any(user_value in col.lower() for user_value in user_values)]

        if matching_columns:
            # User input matches a column name, print values of that column
            for col in matching_columns:
                column_values = [row_dict[col] for row_dict in dataset_dict]
                print(f"{col.capitalize()} Values:", column_values)
        else:
            # Search for rows where each user value is present in a different column
            matching_rows = []

            for row_dict in dataset_dict:
                if all(any(user_value in str(row_dict[key]).lower() for key in row_dict.keys()) for user_value in user_values):
                    matching_rows.append(row_dict)

            if matching_rows:
                # Print matching rows
                for matching_row in matching_rows:
                    for key, value in matching_row.items():
                        print(f"{key}: {value}")
                    print("---")
            else:
                print("No matching records found.")


if __name__ == "__main__":
    main()
