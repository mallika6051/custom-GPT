from flask import Flask, render_template, request

app = Flask(__name__)

# Replace 'your_username', 'your_password', 'localhost:1521', and 'your_service_name' with your actual database credentials
# Assuming you have already imported cx_Oracle and set up the connection in a separate script (as shown in your original code)

# Database connection details
# connection = cx_Oracle.connect('system/M@llik@123@localhost:1521/orcl')
# table_name = 'MOBILEPHONES_DETAILS'

# Mock data for testing (remove this in a real application)
dataset_details = [
    {"ID": 1, "Brand": "Samsung", "Model": "Galaxy S20", "Price": 999.99},
    {"ID": 2, "Brand": "Apple", "Model": "iPhone 12", "Price": 1099.99},
    # Add more rows as needed
]

def is_range(query):
    return '-' in query

def get_range_values(query):
    return map(convert_to_float, query.split('-'))

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return value

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_input = request.form.get('query')

    matching_rows = []

    # Mock data for testing (remove this in a real application)
    for row in dataset_details:
        if user_input.lower() in str(row).lower():
            matching_rows.append(row)

    return render_template('results.html', matching_rows=matching_rows)

if __name__ == '__main__':
    app.run(debug=True)
