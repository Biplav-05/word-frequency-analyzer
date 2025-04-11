# 🧠 Word Frequency Counter

## 📜 Overview

A simple Python project that reads a text input, removes punctuation, and calculates the frequency of each word. It uses regular expressions for efficient text cleaning.

---

## 📂 Project Structure

```
.
├── main.py            # Main script for running the program
├── README.md          # Project documentation (this file)
└── utils.py           # Utility functions for text processing (e.g., remove punctuation)
```

---

## ⚙️ Setup

Clone the repository:

```bash
git clone https://github.com/Biplav-05/word-frequency-counter.git
```

Navigate to the project directory:

```bash
cd word-frequency-counter
```

No external dependencies are required; the project uses only Python's built-in libraries.

---

## 🛠️ Usage

### Function: `remove_punctuation`

This function removes all punctuation from a given text using regular expressions.

```python
from utils import remove_punctuation

# Sample text
text = "Hello, world! Let's test: regex."
cleaned_text = remove_punctuation(text)

print(cleaned_text)
# Output: "Hello world Lets test regex"
```

### Function: `word_frequency`

This function counts the frequency of each word in the cleaned text.

```python
from utils import word_frequency

# Sample text
text = "Hello, world! Python is great. Python, Python!"
cleaned_text = remove_punctuation(text)
frequency = word_frequency(cleaned_text)

print(frequency)
# Output: {'hello': 1, 'world': 1, 'python': 3, 'is': 1, 'great': 1}
```

---

## 📊 Time Complexity

- `remove_punctuation`: O(n), where _n_ is the length of the input text.
- `word_frequency`: O(n), where _n_ is the length of the cleaned text.

---

## 🤝 Contributions

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Make your changes and commit:

   ```bash
   git commit -am "Add new feature"
   ```

4. Push to your branch:

   ```bash
   git push origin feature/your-feature
   ```

5. Create a pull request with a description of your changes.