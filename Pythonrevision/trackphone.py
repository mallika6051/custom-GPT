import phonenumbers
from phonenumbers import geocoder
phone_number = phonenumbers.parse("+918069365731")
phone_number1 = phonenumbers.parse("+917294536271")
phone_number2 = phonenumbers.parse("+919159436362")
print(geocoder.description_for_number(phone_number, "en"));

print(geocoder.description_for_number(phone_number2, "en"));
