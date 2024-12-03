#Print out a greeting message for the user, welcoming them to your first chatbot
greeting = "Hi there! I'm Echo Chatbot, created by Emmelia Gardner."
print(greeting)

#Now that you’ve welcomed the user, explain what they can expect to happen: the chatbot will repeat what they say
details = "My purpose is to repeat what you say back to you - like a parrot. I'll stop when you tell me to 'end chat'."
tip = "Fun tip: Give me the name of an animal and see how I respond."
print(details)
print(tip)

animal_dict = {
  "pig" : "oink",
  "chicken" : "bawk bawk",
  "cow" : "mooooo",
  "horse" : "neigh",
  "dog" : "woof woof",
  "cat" : "meow"
}

#Prompt your user to enter something for the program to repeat
while True:
  stuff_to_echo = input("What would you like me to repeat?")
  if stuff_to_echo.casefold() == "end chat":
    break
  elif stuff_to_echo in animal_dict.keys():
    user_message = "You said: " + stuff_to_echo + ". A " + stuff_to_echo + " says " + animal_dict[stuff_to_echo] + "!"
    print(user_message)
  else: 
    #Print out "You said: " followed by the user input you collected
    user_message = "You said: " + stuff_to_echo
    print(user_message)