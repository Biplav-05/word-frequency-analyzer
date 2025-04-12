from utils import read_input, remove_punctuation, count_word

def main():
    """Main entry point of the program."""

    # Step 1: Read input from user
    text, error = read_input()
    if text is None:
        print("Error:", error['message'])
        return  # Exit early on error

    # Step 2: Clean the input text (remove punctuation/special characters)
    cleaned_text = remove_punctuation(text)

    # Step 3: Count word occurrences
    word_list = cleaned_text.lower().split()
    word_frequencies = count_word(word_list)

    # Step 4: Display the output
    print("Word Frequencies:", word_frequencies)


if __name__ == "__main__":
    main()