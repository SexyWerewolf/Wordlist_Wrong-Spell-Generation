# Password Wordlist - Wrong Spell Generation


## Overview

This repository contains a Python script designed to generate **password wordlists** by applying possible misspellings based on user-defined character substitutions. By simulating common typing errors, the program creates variations of a given word, making it useful for **ethical security testing** and password cracking exercises.

The script allows you to define how each character in a word might be mistyped or substituted (e.g., replacing "a" with "s", "q", or "z"). It then generates all possible combinations of those substitutions, resulting in a wordlist that can be used for testing or simulating real-world password guesses.


## Features

- **Customizable misspellings**: You can define possible wrong spellings or mistyped versions for each character in the word.
- **All combinations generated**: Using `itertools.product`, the script generates every possible combination of the misspelled characters.
- **Output to a text file**: The generated wordlist is saved in a `.txt` file, ready for use with password cracking tools.
- **Supports letters, numbers, and special characters**: The script works with any characters, making it versatile for testing passwords with diverse types of input.

## Installation

To run the script, you need **Python 3.x** installed on your machine. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, follow these steps:

1. Clone or download this repository to your local machine:
   ```bash
   git clone https://github.com/SexyWerewolf/Wordlist_Wrong-Spell-Generation.git
2. Navigate to the project folder:
   ```bash
   cd Wordlist_Wrong-Spell-Generation-gen
3. Run the script:
   ```bash
   python3 wrong_spell_gen.py

## Usage

After running the script, you will be prompted to enter the original word and provide possible misspellings for each character in that word. For each character, you will specify a list of potential substitutions (e.g., replacing `p` with `o`, `p`, or `[`).

### Example Input

For the word `palamo`, the program will prompt you to define misspellings for each character. Here's an example of how this would look in the terminal.
```
Enter the original word: palamo
Enter wrong spells for character 'p': ["o", "p", "["]
Enter wrong spells for character 'a': ["a", "s", "d"]
Enter wrong spells for character 'l': ["k", "l", ";"]
Enter wrong spells for character 'm': ["n", "m", ","]
Enter wrong spells for character 'o': ["i", "o", "p"]
```
### Example Output (730 Lines)
```
palami
palamo
pskano
oqksmi
isks,p
```
