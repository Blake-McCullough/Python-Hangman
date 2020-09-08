import random

#variables for word lists
wordlist1 = [""]
wordlist2 = [""]
wordlist3 = [""]
wordlist4 = [""]
#prints creators name
print('Hangman By Blake McCullough')

#asks for name
name=input("What is your name?")

#capitalizes first letter of word and decapitalize other letters for name
name = name.capitalize()

#says a greetings
print("Hello", name, "Hope you enjoy!")


#ask what subject they want to do
print("What would u like? Mieliestronk's list of over 58,000 english words [Hard] or ?[option 2]")

#gets input for result
result = input("")



#capitalizes first letter of word and decapitalize other letters for result
result = result.capitalize()


#choices subject:
#To add more results copy one of the options and just change what is in the "" and after the words =

#option 1
if result == "Hard":
    print("You picked: Mieliestronk's list of over 58,000 english words ")
    words = wordlist1
    
    
    
#To add more results copy one of the options and just change what is inside the ""

#option 2    
elif result == "":
    print("")
    words = wordlist2
    
#option 3

elif result == "":
    print("")
    words = wordlist3
    
#option 4

elif result == "":
    print("")
    words = wordlist4

#if all fails terminates program

else:
    print("invalid option")
    print("please start ")
    quit()



#word guessing system
def get_guess():
  
  # Set the dashes to the length of the secret word and set the amount of guesses 
  # the user has to 10
  dashes = "-" * len(secret_word)
  guesses_left = 10
  
  
  
  # This will loop as long as BOTH conditions are true:
  # 1. The number of guesses of left is greater than -1
  # 2. The dash string does NOT equal the secret word
  while guesses_left > -1 and not dashes == secret_word:
    
    
    
    # Print the amount of dashes and guesses left
    print(dashes)
    print("guesses left:")
    print (str(guesses_left))
    
    
    
    # Ask the user for input
    guess = input("Guess:")
    
    
    
    # Conditions that will print out a message according to
    # invalid inputs
    if len(guess) != 1:
      print ("Your guess must have exactly one character you fucken retarded tomato!")
      
      
      
    # If the guess is in the secret word then we updtae dashes to replace the
    # corresponding dash with the correct index the guess belongs to in the 
    # secret word
    elif guess in secret_word:
      print ("That letter is in the secret word,you finally did good in your life and now have a purpose")
      dashes = update_dashes(secret_word, dashes, guess)
      
      
      
    # If the guess is wrong then we display a message and subtract
    # the amount of guesses the user has by 1
    else:
      print ("That letter is not in the secret word!")
      guesses_left -= 1
    
    
    
  if guesses_left < 0:
    print ("You lose you. The word was: " + str(secret_word))
  
  
  
  # If the dash string equals the secret word in the end then the
  # user wins
  else:
    print ("Congrats! You Win. The word was: " + str(secret_word))



# This function updates the string of dashes by replacing the dashes
# with words that match up with the hidden word if the user manages to guess
# it correctly
def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess     # Adds guess to string if guess is correctly
      
      
      
    else:
      # Add the dash at index i to result if it doesn't match the guess
      result = result + cur_dash[i]
      
      
      
  return result
    # Words that can be guessed


secret_word = random.choice(words)
get_guess()

print('Thanks', name,'For Playing!')


