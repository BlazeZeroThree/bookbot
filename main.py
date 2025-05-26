from stats import count_words
from stats import count_letters
from stats import sort_dict
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    # directory = "books/frankenstein.txt"

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    directory = sys.argv[1]
    
    # start printing
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {directory}...")

    print("----------- Word Count ----------")
    num_words = count_words(get_book_text(directory))
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    # print(count_letters(get_book_text(directory)))
    dict_letters = count_letters(get_book_text(directory))
    sorted_letters = sort_dict(dict_letters)
    for i in sorted_letters:
        print(f"{i["ltr"]}: {i["num"]}")

    print("============= END ===============")

main()