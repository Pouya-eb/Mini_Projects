# Password Generator

## Overview

This project contains a password generator application written in Python. The generator can create three types of passwords:

1. Random Passwords
2. Memorable Passwords
3. Pin Codes

## How It Works

The password generator uses the Python `random` module to generate passwords based on user preferences. The generator is split into three classes, each representing a different type of password generation:

1. `RandomPasswordGenerator` generates a completely random password of a specified length, optional with numbers, and symbols.
2. `MemorablePasswordGenerator` creates a password made up of a set number of randomly chosen words from the NLTK English language corpus. It can optionally separate the words with a separator and use capitalized words.
3. `PinCodeGenerator` creates a numeric password of a specified length.

Each generator class inherits from a base `PasswordGenerator` class. They each override the base class's `generate()` method in order to provide their own unique password generation functionality.

## Directory Structure

```
03-password_generator/
|-- src/
| |-- main.py
|-- README.md
```

## Requirements

- Python 3.7+
- NLTK (Natural Language Toolkit)

To install NLTK, use pip:

```bash
pip install nltk
```

After installing NLTK, you need to download the 'words' corpus uncomment the following in the code:

```python
nltk.download('words')
```

That's all you need to know to get started with this project. Enjoy generating passwords!

## How to Run

Make sure you've installed all the required dependencies. You can then set your PYTHONPATH, navigate to the 'src' directory and run the project using Python:

```bash
export PYTHONPATH="${PYTHONPATH}:/your/path/to/main/directory"
python src/main.py
```

Be sure to replace `/your/path/to/main/directory` with the actual path to the directory containing your project.
