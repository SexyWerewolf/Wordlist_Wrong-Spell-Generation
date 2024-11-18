import itertools

def generate_misspellings(word):
    misspellings = []
    char_to_misspells = {}

    for c in word:
        if c not in char_to_misspells:
            input_string = input(f"Enter wrong spells for character '{c}': ")
            try:
                char_to_misspells[c] = eval(input_string)
                if not isinstance(char_to_misspells[c], list):
                    print("Error: The input must be a list. Please try again.")
                    return []
            except Exception as e:
                print(f"Error: {e}. The input must be a valid list.")
                return []

    spell_lists = [char_to_misspells[c] for c in word]
    
    for permutation in itertools.product(*spell_lists):
        new_word = ''.join(permutation)
        misspellings.append(new_word)
    
    return list(set(misspellings))

def save_to_file(misspellings, filename="misspellings.txt"):
    with open(filename, "w") as file:
        for misspelled_word in misspellings:
            file.write(misspelled_word + "\n")
    print(f"Misspellings have been saved to {filename}")

print("Enter the original word:")
word = input()

misspellings = generate_misspellings(word)

if misspellings:
    save_to_file(misspellings)

    print("\nAll possible misspellings:")
    for m in misspellings:
        print(m)
