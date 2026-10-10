def chatbot():

    print("=" * 45)
    print("        WELCOME TO SIMPLE CHATBOT")
    print("=" * 45)
    print("Bot: Hello! I am your chatbot.")
    print("Bot: You can ask me simple questions.")
    print("Bot: Type 'bye' to exit the chatbot.\n")

    while True:

        user_input = input("You: ").lower().strip()

        # Greeting
        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi! Nice to meet you.")

        # How are you
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
            print("Bot: How are you doing?")

        # User's response
        elif user_input == "i am fine" or user_input == "i am good":
            print("Bot: That's great to hear!")

        # Name
        elif user_input == "what is your name":
            print("Bot: My name is SimpleBot.")

        elif user_input == "who are you":
            print("Bot: I am a simple rule-based chatbot.")

        # Help
        elif user_input == "help":
            print("Bot: I can respond to simple questions.")
            print("Bot: Try asking:")
            print("     - hello")
            print("     - how are you")
            print("     - what is your name")
            print("     - what can you do")
            print("     - what is python")
            print("     - thank you")
            print("     - bye")

        # About chatbot
        elif user_input == "what can you do":
            print("Bot: I can have a simple conversation with you.")
            print("Bot: My responses are based on predefined rules.")

        # Python
        elif user_input == "what is python":
            print("Bot: Python is a popular programming language.")
            print("It is easy to learn and widely used in many fields.")

        # Programming
        elif user_input == "what is programming":
            print("Bot: Programming is the process of writing instructions")
            print("that a computer can understand and execute.")

        # Internship
        elif user_input == "what is internship":
            print("Bot: An internship provides practical work experience.")
            print("It helps students learn skills in a real-world environment.")

        # Thanks
        elif user_input == "thank you" or user_input == "thanks":
            print("Bot: You're welcome!")

        # Good morning
        elif user_input == "good morning":
            print("Bot: Good morning! Have a great day.")

        # Good night
        elif user_input == "good night":
            print("Bot: Good night! Sleep well.")

        # Joke
        elif user_input == "tell me a joke":
            print("Bot: Why do programmers prefer dark mode?")
            print("Bot: Because light attracts bugs!")

        # Time-related question
        elif user_input == "what is your favorite language":
            print("Bot: I like Python because it is simple and powerful.")

        # Bye
        elif user_input == "bye" or user_input == "goodbye":
            print("Bot: Goodbye!")
            print("Bot: It was nice talking to you.")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I don't understand that.")
            print("Bot: Type 'help' to see what I can understand.")

        print()


# Start the chatbot
chatbot()