import string
import re

def read_input():
    print("Would you like to enter text as a 'string' or provide a 'file' path?")
    input_type = input("Enter 1 for string or 2 for file path: ").strip()
    
    text = None
    error = {"message": None}

    # Normalize input to text labels
    match input_type:
        case "1" | "string":
            text = input("Enter the desired string or sentence: ").strip()
        case "2" | "file":
            # TODO: Implement file input later
            error['message'] = "File handling functionality will be implemented in the future."
        case _:
            error['message'] = "Invalid option selected. Please select a valid option (1 or 2)."
    
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