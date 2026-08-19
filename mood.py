mood = input("How are you? ")
if mood == "good":
 print("Great to hear!")
else:
 print("I hope your day gets better.") 
 mood = input("How are you? ")
if mood == "good":
 print("Great to hear!")
elif mood == "sad":
 print("Sorry to hear that. I am here to chat.")
elif mood == "tired":
 print("Get some rest soon!")
else:
 print("Thanks for sharing.")