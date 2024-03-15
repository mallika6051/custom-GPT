from flask import Flask, render_template, request
import cx_Oracle

app = Flask(__name__)

# Replace 'your_username', 'your_password', 'localhost:1521', and 'your_service_name' with your actual database credentials
connection = cx_Oracle.connect('system/M@llik@123@localhost:1521/orcl')

# table_name = 'MOBILEPHONES_DETAILS'
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


def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return value


def is_range(query):
    return '-' in query


def get_range_values(query):
    return map(convert_to_float, query.split('-'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    dataset_details = get_dataset_dict()

    user_input = request.form['query'].lower()

    if user_input == 'exit':
        return render_template('result.html', result="Thank You!")

    user_input = user_input.split()

    if is_range(user_input[-1]):
        range_query = user_input[-1]
        start_range, end_range = get_range_values(range_query)

        matching_rows = [
            row for row in dataset_details
            if any(
                isinstance(row[col], (int, float)) and start_range <= row[col] <= end_range
                for col in row if isinstance(row[col], (int, float))
            )
        ]

        if matching_rows:
            return render_template('result.html', result=matching_rows)

    matching_columns = []
    for col in dataset_details[0].keys():
        if any(user_input_item in col.lower() for user_input_item in user_input):
            matching_columns.append(col)

    if matching_columns and len(user_input) > 1:
        col_name = matching_columns[0]
        col_values = user_input[1:]

        matching_rows = []
        for row in dataset_details:
            for val in col_values:
                if isinstance(row[col_name], str) and convert_to_float(row[col_name].lower()) == convert_to_float(
                        val.lower()):
                    matching_rows.append(row)
                elif isinstance(row[col_name], (int, float)) and convert_to_float(row[col_name]) == convert_to_float(
                        val.lower()):
                    matching_rows.append(row)

        if matching_rows:
            return render_template('result.html', result=matching_rows)
        else:
            return render_template('result.html',
                                   result=f"No matching records found for {col_name} values: {', '.join(col_values)}")

    elif matching_columns:
        for col in matching_columns:
            column_values = [columns_with_rows[col] for columns_with_rows in dataset_details]
            return render_template('result.html', result=column_values)

    else:
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
            return render_template('result.html', result=matching_rows)
        elif "column" in user_input or "columns" in user_input:
            return render_template('result.html', result={"Column Names": list(dataset_details[0].keys())})
        else:
            return render_template('result.html', result="No matching records found.")


if __name__ == "__main__":
    app.run(debug=True)
