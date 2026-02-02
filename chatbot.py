print("🤖 ChatBot Started (type 'exit' to stop)")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! Nice to meet you ")

    elif user == "how are you":
        print("Bot: I'm doing great! What about you?")

    elif user == "what is your name":
        print("Bot: I am your friendly chatbot ")

    elif user == "who created you":
        print("Bot: I was created using Python programming.")

    elif user == "what is python":
        print("Bot: Python is a programming language used for web, AI, automation and more.")

    elif user == "thank you":
        print("Bot: You're welcome! ")

    elif user == "bye":
        print("Bot: Bye bye! Have a good day ")

    elif user == "exit":
        print("Bot: See you soon! ")
        break

    else:
        print("Bot: Sorry, I didn’t get that. Try saying 'hi' or 'what is python'.")
