
# 🧠 Word Frequency Analyzer

## 📜 Overview

A simple Python project that reads user input (either as a direct string or from a file), removes punctuation, and calculates the frequency of each word. The project uses regular expressions and efficient dictionary operations for performance.

## 📂 Project Structure

```
.
├── main.py            # Main script for running the program
├── utils.py           # Utility functions for input, cleaning text, and word counting
└── README.md          # Project documentation (this file)
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/Biplav-05/word-frequency-counter.git
```

### 2. Navigate to the project directory

```bash
cd word-frequency-counter
```

No external dependencies are required. The project uses only Python's built-in libraries.

## 🛠️ Usage

Run the program:

```bash
python main.py
```

You'll be prompted to choose the type of input:

- **string**: Directly input the text into the console.
- **file**: This feature is a placeholder and can be implemented later.

### Example

```
Would you like to enter text as a 'string' or provide a 'file' path ? string
Enter the desired strings or sentence. Hello, world! Python is great. Python, Python!
{'hello': 1, 'world': 1, 'python': 3, 'is': 1, 'great': 1}
```

## 🔍 Functions

### `read_input()`
Prompts the user to enter either a string or file path. Returns the input text and error message if applicable.

### `remove_punctuation(text)`
Removes all punctuation from the given text using regular expressions.  
**Time Complexity**: O(n), where n is the length of the text.

### `count_word(input_text)`
Counts word frequency from a list of words using a dictionary.  
**Time Complexity**: O(n), where n is the number of words.

## 📊 Time Complexity Summary

| Function           | Time Complexity |
|--------------------|-----------------|
| remove_punctuation | O(n)            |
| count_word         | O(n)            |

## 🤝 Contributions

Contributions are welcome!

1. Fork the repository
2. Create a new branch  
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and commit  
   ```bash
   git commit -am 'Add new feature'
   ```
4. Push to your branch  
   ```bash
   git push origin feature/your-feature
   ```
5. Create a pull request

---

Feel free to open issues for suggestions or bugs!
