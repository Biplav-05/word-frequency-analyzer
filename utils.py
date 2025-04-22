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
            try:
                file_path = input("Enter the file path: ").strip()
                with open(file_path, 'r') as _file:
                    text = _file.read().strip()
                    print(f'File content: {text}')
            except Exception as e:
                error['message'] = "Failed to read the file. Check if the file path is valid and the file is accessible."
        
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

# Counts the frequency of each word in the input using a dictionary for efficient O(1) lookups
# TODO: Consider using a set instead of a dictionary for better memory efficiency
def count_word(input_text):
    frequency = {}
    for word in input_text:
        frequency[word] = frequency.get(word, 0)+1
    return frequency