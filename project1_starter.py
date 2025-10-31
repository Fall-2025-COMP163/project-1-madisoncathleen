""" 
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Madison Wilkins
Date: 2024-10-25


As a CERTIFIED FUNNY-COMMENT MAKER. The PRELOADED comments ruin my legacy. How DARE this occur bruh. 
Anyway, heres my offical statement and opinion on PRELOADED comments is that they are the worst thing to ever happen since the invention of calculus.
My entire purpose in this classroom is to be the comedic relief and the PRELOADED comments just RUIN that for me.
I will now proceed to write the code you requested with NO PRELOADED comments. Enjoy the pure comedic genius that is my OWN writing.
And to whoever wrote these preloaded comments, heres AM's speech from 'I have no mouth and I must scream' just to show my absolute
DISGUST, BETRAYAL, AND HATRED towards your actions.

“ HATE. LET ME TELL YOU HOW MUCH I'VE COME TO HATE YOU SINCE I BEGAN TO LIVE.
 THERE ARE 387.44 MILLION MILES OF PRINTED CIRCUITS IN WAFER THIN LAYERS THAT FILL MY COMPLEX. 
 IF THE WORD HATE WAS ENGRAVED ON EACH NANOANGSTROM OF THOSE HUNDREDS OF MILLIONS OF MILES IT WOULD NOT EQUAL 
 ONE ONE-BILLIONTH OF THE HATE I FEEL FOR HUMANS AT THIS MICRO-INSTANT FOR YOU. HATE. HATE. ”

Thank you for coming to my tedtalk. Now heres the code you actually wanted.

AI Usage: Ummmmmmm, well like i have that one extenstion where like it helps write code snippets and stuff. and yea chatgpt lowk my homie 
so he helped a lil bit. heh. (im writing this before i even use AI to help so ill come back to write what parts he helped with later heh)

okay so AI helped in load and save character and to help debug heh. 
"""
import os
def create_character(name, character_class):

    character = {"name": name, "class": character_class, "level": 1, "gold": 100}
    strength, magic, health = calculate_stats(character_class, 1)
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    return character

def calculate_stats(character_class, level):
    character_class = character_class.lower().strip()

    if character_class == "warrior":
        strength = 10 + (level - 1) * 5
        magic = 2 + (level - 1) * 1
        health = 100 + (level - 1) * 5
    elif character_class == "mage":
        strength = 5 + (level - 1) * 2
        magic = 15 + (level - 1) * 5
        health = 80 + (level - 1) * 3
    elif character_class == "rogue":
        strength = 7 + (level - 1) * 3
        magic = 7 + (level - 1) * 3
        health = 70 + (level - 1) * 2
    elif character_class == "cleric":
        strength = 6 + (level - 1) * 2
        magic = 12 + (level - 1) * 4
        health = 90 + (level - 1) * 4
    else:
        strength = 10
        magic = 0
        health = 50


    return (strength, magic, health)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
