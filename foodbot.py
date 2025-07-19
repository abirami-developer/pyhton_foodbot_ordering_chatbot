import random

menu = {
    "pizza": 12,
    "burger": 8,
    "pasta": 10,
    "fries": 5,
    "coke": 3
}

responses = {
    "greeting": ["Hello! Welcome to FoodBot. How can I assist you?", "Hi there! Ready to order some delicious food?"],
    "menu": [f"We serve: {', '.join(menu.keys())}. What would you like to order?"],
    "order_confirmation": ["Great choice! Your order for {item} is confirmed.","Awesome! {item} has been added to your order."],
    "farewell": ["Thank you for ordering! Enjoy your meal.", "Goodbye! Hope to see you again."]
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greeting"])

    elif "menu" in user_input:
        return random.choice(responses["menu"])

    elif any(item in user_input for item in menu.keys()):
        for item in menu.keys():
            if item in user_input:
                return random.choice(responses["order_confirmation"]).format(item=item)

    elif "bye" in user_input or "thank you" in user_input:
        return random.choice(responses["farewell"])

    else:
        return "I'm sorry, I didn't understand. Would you like to see the menu?"

order_items = []
total_cost = 0

print("FoodBot: Hello! Type 'menu' to see our dishes or type your order directly.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        if order_items:
            print("\nFoodBot: Here's your order summary:")
            for item in order_items:
                print(f"- {item}")
            print(f"Total cost: ${total_cost}")
        print("FoodBot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("FoodBot:", response)

    for item in menu.keys():
        if item in user_input.lower():
            order_items.append(item)
            total_cost += menu[item]
            break
