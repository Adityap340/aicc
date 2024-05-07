import random

def greet():
    greetings = ["Hi there!", "Hello!", "Hey!"]
    return random.choice(greetings)

def ask_name():
    return input("What's your name? ")

def chat():
    print(greet())
    name = ask_name()
    print("Nice to meet you, " + name + "!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        else:
            response = generate_response(user_input)
            print("Bot:", response)

def generate_response(user_input):
    responses = {
        "hello": "Hello! Welcome to our online store. How can I assist you today?",
        "what products do you offer?": "We offer a wide range of products including electronics, clothing, accessories, home goods, and more!",
        "do you have any sales or promotions?": "Yes, we often have sales and promotions! You can check our website or sign up for our newsletter to stay updated.",
        "can I track my order?": "Of course! Please provide your order number and I'll look up the status for you.",
        "how do I return an item?": "We have a hassle-free return policy. Simply contact our customer service team and they'll assist you with the return process.",
        "what payment methods do you accept?": "We accept various payment methods including credit/debit cards, PayPal, and bank transfers.",
        "do you offer international shipping?": "Yes, we offer international shipping to many countries. You can check the shipping options during checkout.",
        "how long does shipping take?": "Shipping times depend on your location and the shipping method chosen. You can find estimated delivery times during checkout.",
        "is my personal information secure?": "Absolutely! We take customer privacy and security very seriously. Your personal information is encrypted and protected.",
        "what's your refund policy?": "We offer refunds on eligible items within a specified period. Please refer to our refund policy for more details.",
        "do you have a customer loyalty program?": "Yes, we have a loyalty program where you can earn points for every purchase and redeem them for discounts or rewards.",
        "can I speak to a human representative?": "Certainly! If you need further assistance, please contact our customer service team and they'll be happy to help.",
        "bye": "Thank you for visiting our store! Have a great day!",
    }
    response = responses.get(user_input.lower(), "I'm sorry, I didn't understand that.")
    return response

if __name__ == "__main__":
    chat()