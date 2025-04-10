from utils import read_input, clean_text, count_word
# Parent function
def main():
    text, error = read_input()
    if text is None:
        print(error['message'])

    cleaned_text = clean_text(text)

    output = count_word(cleaned_text)

    print(output)
    


# Main function
if __name__ == "__main__":
    main()