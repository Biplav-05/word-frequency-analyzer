import string

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

# This function is used to clean the user inputed text and remove the punctuation.
# TODO need to be refactor below logic because its time complexity will be O(n*m) 
# where n is the number of characters in the string and m is the average length of the words.
def clean_text(text):
    cleaned_text = ""
    for char in text:
        if char not in string.punctuation:
            cleaned_text +=char
    return cleaned_text.lower().split()

# This function is used to count the word occurance using dict for O(1) lookup
def count_word(input_text):
    frequency = {}
    for item in input_text:
        frequency[item] = frequency.get(item, 0)+1
    return frequency