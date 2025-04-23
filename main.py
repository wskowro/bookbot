from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = './books/frankenstein.txt'
    book = get_book_text(filepath)
    word_count = len(get_word_count(book))
    char_count = get_char_count(book)
    sorted_char_count = sort_dictionary(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_char_count:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['count']}")
    print("============= END ===============")

main()
