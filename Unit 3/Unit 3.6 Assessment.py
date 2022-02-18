# Name: Fady Elsayed
# Date: Nov 4th 2021
# File Name: Unit 3.6 Assessment.py
# Description: A program that asks the user to enter some English text,
# then converts the text to Pig-Latin.
# Test cases: "this course is amazing", "hello", "and", "image", "rain",
# "i love to eat chicken".

# Program: Creates translate to pig latin function.
def translate_to_pig(sentence):
    """Translates text from english to pig latin.

    assumptions:
        sentence includes no puncuation, words are seperated by one space,
        all letters are lower case, only words are entered.
    
    Args:
        sentence(list): A english sentence with only letters.

    Return:
        new_sentence(list): A pig latin sentence formed by english text.
    """

# Process: Sets values.
    new_sentence = []
    letters = ""

# Process: Spits the sentence into words by seperating the list by spaces.
    words = sentence.split()

# Process: If the word starts with a vowel then adds the pig latin word.
    for i in words:
        if i.startswith("a"):
            new_sentence.append(i + "hay")
            
        elif i.startswith("e"):
            new_sentence.append(i + "hay")
            
        elif i.startswith("i"):
            new_sentence.append(i + "hay")
            
        elif i.startswith("o"):
            new_sentence.append(i + "hay")
            
        elif i.startswith("u"):
            new_sentence.append(i + "hay")
            
# Process: If the word doesnt start with a vowel then reformats the text.              
        else:
            for lett in i:
                if i.startswith(lett):
                    first = lett
                    
                else:
                    letters += lett
                    pig_lat = letters + first + "ay"

# Process: adds word to list and resets values.                
            new_sentence.append(pig_lat)
            letters = ""
            reword = ""
            first = ""
            
# Output: Returns list. 
    return new_sentence            



# Program: Creates main program.
def main():
    """ Creates main function to get input and print pig latin translation.

    """
    # Output: prints instructions.
    print("Hello, welcome! This program is a english to Pig-Latin \
translator. \nTo translate text from english to Pig-latin please enter a text \
below with: \n\nNO punctuation \nNO upper cases \nONLY use letters \nONLY \
use 1 space to seperate words\n")
    
    # Input: Asks user for input.
    sentence =  input("Enter a text: ")
    print("\nPig-Latin:", *translate_to_pig(sentence))



# Main program:
main()
