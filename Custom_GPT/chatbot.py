from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
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

def get_mobile_details(MANUFACTURER):
    query = f"SELECT * FROM MOBILEPHONES_DETAILS WHERE MANUFACTURER = '{MANUFACTURER}'"
    result = execute_query(query)
    return result

# Create a chatbot
chatbot = ChatBot('MobilePhoneBot')
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train("chatterbot.corpus.english")

# Define a function to handle mobile phone details queries
def handle_mobile_phone_query(MANUFACTURER):
    details = get_mobile_details(MANUFACTURER)
    if details:
        response = f"Here are the details for {MANUFACTURER} phones:\n"
        for row in details:
            response += str(row) + "\n"
    else:
        response = f"Sorry, I couldn't find details for {MANUFACTURER} phones."
    return response

# Example interaction with the chatbot
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Get the chatbot's response
    bot_response = chatbot.get_response(user_input)

    # If the response indicates a mobile phone details query, handle it
    if "mobile phone details" in bot_response.text.lower():
        manufacturer = user_input.split("about")[-1].strip()
        mobile_details_response = handle_mobile_phone_query(manufacturer)
        print("MobilePhoneBot:", mobile_details_response)
    else:
        print("MobilePhoneBot:", bot_response)
