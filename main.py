from utils import read_input, remove_punctuation, count_word
# Parent function
def main():
    # Read user input and if error occur output the error to console.
    text, error = read_input()
    if text is None:
        print(error['message'])

    # After reading the text from input, this function clean the text like exclude special character and retrun list of string.
    cleaned_text = remove_punctuation(text)

    # # After getting cleaned file, this function count the word occurance or frequency and output the word with frequency in dictionary.
    output = count_word(cleaned_text.lower().split())

    print(output)
    


# Main function
if __name__ == "__main__":
    # Entrypoint for the program.
    main()