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

def search_mobile_by_MANUFACTURER(MANUFACTURER):
    query = f"SELECT * FROM MOBILEPHONES_DETAILS WHERE MANUFACTURER = '{MANUFACTURER}'"
    return execute_query(query)

def search_mobile_by_attributes(MANUFACTURER, MODEL=None, COLOR=None, STORAGE_CAPACITY=None, SCREEN_SIZE=None, BATTERY_CAPACITY=None, OPERATING_SYSTEM=None, RAM=None, PROCESSOR=None, CAMERA_RESOLUTION=None, FRONT_CAMERA_RESOLUTION=None, WEIGHT=None, DIMENSIONS=None, WATER_RESISTANT=None, DUAL_SIM=None, NETWORK_TECHNOLOGY=None, WIFI=None, BLUETOOTH=None, NFC=None, FINGERPRINT_SCANNER=None, FACE_UNLOCK=None, PRICE=None):
    conditions = [f"MANUFACTURER = '{MANUFACTURER}'"]

    if MODEL:
        conditions.append(f"model = '{MODEL}'")
    if COLOR:
        conditions.append(f"color = '{COLOR}'")
    # Add more conditions for other attributes...

    query = f"SELECT * FROM MOBILEPHONES_DETAILS WHERE {' AND '.join(conditions)}"
    return execute_query(query)

# Example usage:
MANUFACTURER_search_result = search_mobile_by_MANUFACTURER('Apple')
print("Mobile phones from Apple:")
print(MANUFACTURER_search_result)

attributes_search_result = search_mobile_by_attributes('Apple', COLOR='white' or 'red', PRICE='<1000')
print("white mobile phones from Apple with a price below 1000:")
print(attributes_search_result)

# Don't forget to close the connection when done
connection.close()
