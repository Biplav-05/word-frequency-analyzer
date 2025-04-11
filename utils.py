import string
import re

# This function reads the user input and return the text accoriding to it
def read_input():
    input_type = input("Would you like to enter text as a 'string' or provide a 'file' path ?").strip().lower()
    text = None
    error ={"message": "Invalid Option selected."}
    if input_type == "file":
        # TODO
        pass
    
    elif input_type ==  "string":
        text = input("Enter the desired strings or sentese.").strip()

    return text, error

# O (n) lookup implemented
def remove_punctuation(text):
   # Step 1: Create a regex pattern that includes all punctuation characters
    # `string.punctuation` contains all the common punctuation marks (e.g., !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~)
    # `re.escape` ensures that special characters in the punctuation set are safely handled in regex
    # Example: escaping `.` to `\.` and `[` to `\[`
    pattern = f"[{re.escape(string.punctuation)}]"

    # Step 2: Use re.sub() to replace all occurrences of punctuation characters with an empty string
    # The regex pattern will match any character from the punctuation set and remove it
    # `re.sub()` operates in O(n) time, where n is the length of the text
    # This is efficient for processing large strings
    return re.sub(pattern, '', text)

# This function is used to count the word occurance using dict for O(1) lookup
def count_word(input_text):
    frequency = {}
    for item in input_text:
        frequency[item] = frequency.get(item, 0)+1
    return frequency