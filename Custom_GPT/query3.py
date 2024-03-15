# import cx_Oracle
#
# # Replace 'your_username', 'your_password', 'localhost:1521', and 'your_service_name' with your actual database credentials
# connection = cx_Oracle.connect('system/M@llik@123@localhost:1521/orcl')
#
# def execute_query(query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         result = cursor.fetchall()
#         return result
#     finally:
#         cursor.close()
#
# def table_details():
#     query="SELECT * FROM MOBILEPHONES_DETAILS"
#     return execute_query(query)
# def get_manufacturer_details():
#     query = "SELECT DISTINCT MANUFACTURER FROM MOBILEPHONES_DETAILS"
#     return execute_query(query)
# def get_details_for_manufacturer(manufacturer):
#     query = f"SELECT * FROM MOBILEPHONES_DETAILS WHERE MANUFACTURER = '{manufacturer}'"
#     return execute_query(query)
# def count_manufacturers():
#     query = "SELECT COUNT(DISTINCT MANUFACTURER) FROM MOBILEPHONES_DETAILS"
#     return execute_query(query)
# def get_models_details():
#     query="SELECT DISTINCT MODEL FROM MOBILEPHONES_DETAILS"
#     return (execute_query(query))
# def get_details_for_model(model):
#     query = f"SELECT * FROM MOBILEPHONES_DETAILS WHERE MODEL = '{model}'"
#     return execute_query(query)
# # def get_details_for_query(manufacturer,model,color,storage_capacity,screen_size,battery_capacity,operating_system,ram,processor,camera_resolution,front_camera_resolution,weight,dimensions,water_resistant,dual_sim,network_technology,wifi,bluetooth,nfc,fingerprint_scanner,face_unlock,price):
# #     query = f"SELECT * FROM MOBILEPHONES_DETAILS WHERE MANUFACTURER = '{manufacturer}' AND MODEL = '{model}' AND COLOR = '{color}' AND STORAGE_CAPACITY = {storage_capacity} AND SCREEN_SIZE = {screen_size} AND BATTERY_CAPACITY = {battery_capacity} " \
# #             f"AND OPERATING_SYSTEM = {operating_system} AND RAM = {ram} AND PROCESSOR = {processor} AND CAMERA_RESOLUTION = {camera_resolution} AND FRONT_CAMERA_RESOLUTION = {front_camera_resolution} AND WEIGHT = {weight} AND DIMENSIONS = {dimensions}" \
# #             f"AND WATER_RESISTANT = {water_resistant} AND DUAL_SIM = {dual_sim} AND NETWORK_TECHNOLOGY = {network_technology} AND WIFI = {wifi} AND BLUETOOTH = {bluetooth} AND NFC = {nfc} AND FINERPRINT_SCANNER = {fingerprint_scanner} AND FACE_UNLOCK = {face_unlock} AND PRICE = {price}"
# #     return execute_query(query)
# while True:
#     user_input = input("Enter your query (or 'exit' to quit): ")
#     if user_input.lower() == 'exit':
#         print("Thank You !")
#         break
#
#     keywords = user_input.lower()
#     if ("count" in keywords or "number" in keywords or 'howmany' in keywords or 'how many' in keywords) and any(keyword in keywords for keyword in ["manufacturer", "brand", "types", "list","brands","type","lists"]):
#         manufacturer_count = count_manufacturers()
#         print("Number of manufacturers:")
#         print(manufacturer_count[0][0])
#     elif "mobilephoene" in keywords or "mobilephone" in keywords:
#         Table_details = table_details()
#         print(table_details())
#     elif "apple" in keywords:
#         MANUFACTURER_search_result =get_details_for_manufacturer('Apple')
#         print("Mobile phones from Apple :")
#         print(MANUFACTURER_search_result)
#     elif "samsung" in keywords:
#         MANUFACTURER_search_result =get_details_for_manufacturer('Samsung')
#         print("Mobile phones from Samsung :")
#         print(MANUFACTURER_search_result)
#     elif "google" in keywords:
#         MANUFACTURER_search_result =get_details_for_manufacturer('Google')
#         print("Mobile phones from Google :")
#         print(MANUFACTURER_search_result)
#     elif "xiaomi" in keywords:
#         MANUFACTURER_search_result =get_details_for_manufacturer('Xiaomi')
#         print("Mobile phones from Xiaomi :")
#         print(MANUFACTURER_search_result)
#     elif "huawei" in keywords:
#         MANUFACTURER_search_result =get_details_for_manufacturer('Huawei')
#         print("Mobile phones from Huawei :")
#         print(MANUFACTURER_search_result)
#     elif any(keyword in keywords for keyword in ["manufacturer", "brands","brand" ,"types","type", "lists","list"]):
#         manufacturer_details = get_manufacturer_details()
#         print("Manufacturer details:")
#         print(manufacturer_details)
#     elif "pixel 5" in keywords or "pixel5" in keywords:
#         MODEL_search_details = get_details_for_model("Pixel 5")
#         print("Models from Pixel 5:")
#         print(MODEL_search_details)
#     elif "mi11" in keywords or "mi 11" in keywords:
#         MODEL_search_details = get_details_for_model("Mi 11")
#         print("Models from Mi 11:")
#         print(MODEL_search_details)
#     elif "p40 pro" in keywords or "p40pro" in keywords:
#         MODEL_search_details = get_details_for_model("P40 Pro")
#         print("Models from P40 Pro:")
#         print(MODEL_search_details)
#     elif "galaxys21" in keywords or "galaxy s21" in keywords:
#         MODEL_search_details = get_details_for_model("Galaxy S21")
#         print("Models from Galaxy S21:")
#         print(MODEL_search_details)
#     elif "iphone12" in keywords or "i phone12" in keywords:
#         MODEL_search_details = get_details_for_model("iPhone 12")
#         print("Models from iPhone 12:")
#         print(MODEL_search_details)
#     elif "model" in keywords or "models" in keywords:
#         models_details = get_models_details()
#         print("Models details:")
#         print(models_details)
#     else:
#         print("Invalid query. Please enter a valid query or 'exit' to quit.")








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













