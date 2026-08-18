print("Hi! I am ChatBot. What is your name?")
name = input("You: ")
print("Nice to meet you, " + name + "! Type bye to leave.")
def get_reply(message):
 while True:
      message = input(name + ": ")

      if message in "bye":
         print ("ChatBot: Goodbye, " + name + "!")
         break
      elif message == "hello":
         print("ChatBot: Hello there!")
      elif message == "how are you":
         print("ChatBot: I am just code, but I feel great!")
      elif "joke" in message:
         print("ChatBot: Why did the programmer quit? They lost their domain!")
      elif "help" in message:
         print("ChatBot: You can ask me about the time, jokes, or food.")
      elif "study" in message:
         print("chatBot: how can i help in ours studies")   
 else:
  print("ChatBot: I am not sure how to answer that yet.")