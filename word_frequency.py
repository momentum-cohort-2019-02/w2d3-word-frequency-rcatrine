import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def normalize_text(text):
    """
    Given a text, lowercases it, removes all punctuation, 
    and replaces all whitespace with normal spaces. Multiple whitespace will
    be compressed into a single space.
    """
    text = text.casefold()
    valid_chars = string.ascii_letters + string.whitespace + string.digits

    # Remove all punctuation
    new_text = ""
    for char in text:
        if char in valid_chars:
            new_text += char

    text = new_text
    text = text.replace("\n", " ")
    return text


def print_word_freq(filename):
    """Read in `filename` and print out the frequency of words in that file."""
    with open(filename) as file:
        text = file.read()

    text = normalize_text(text)
    words = []
    for word in text.split(" "):
        if word != '' and word not in STOP_WORDS:
            words.append(word)

# ________________________________________________________________
    ## What now?
    # Get a dictionary of word frequencies and print it out

    # Imports seneca_falls.txt
    import re
    import string
    word_freq = {}
    document_text = open("seneca_falls.txt", "r")
    text_string = document_text.read().lower()
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
     
    
    for word in match_pattern:
        # Reaches into dictionary, counts words
        word_freq[word] = word_freq.get(word,0) + 1
    # breakpoint()  
    word_freq_list = word_freq.keys()
    # breakpoint() 
    for word in word_freq_list:
        print (word, word_freq[word])

# ________________________________________________________________
  


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
