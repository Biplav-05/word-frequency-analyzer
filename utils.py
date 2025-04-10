import string

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

def clean_text(text):
    cleaned_text = ""
    for char in text:
        if char not in string.punctuation:
            cleaned_text +=char
    return cleaned_text.lower().split()


def count_word(input_text):
    frequency = {}
    for item in input_text:
        frequency[item] = frequency.get(item, 0)+1
    return frequency