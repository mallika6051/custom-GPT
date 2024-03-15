import cx_Oracle

def run_query(table_name, conditions):
    # Establish a connection to Oracle Database
    connection = cx_Oracle.connect("your_username", "your_password", "your_dsn")

    # Create a cursor
    cursor = connection.cursor()

    # Build the SQL query dynamically
    query = f"SELECT * FROM {table_name}"
    if conditions:
        query += f" WHERE {conditions}"

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    result = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return result

def main():
    # User input for table name and conditions
    user_table = input("Enter table name: ")
    user_conditions = input("Enter conditions (if any): ")

    # Execute the query and print the results
    result = run_query(user_table, user_conditions)

    for row in result:
        print(row)

if __name__ == "__main__":
    main()


