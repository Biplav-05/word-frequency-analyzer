import string


def read_input():
    input_type = input("Would you like to enter text as a 'string' or provide a 'file' path ?").strip().lower()
    text = None
    error ={"message": "Invalid Option selected."}
    if input_type == "file":
        # text= "Input type is of file."
        a =1
    elif input_type ==  "string":
        text = input("Enter the desired strings or sentese.")

    return text, error