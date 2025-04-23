def get_word_count(book):
    book_words = book.split()
    return book_words

def get_char_count(book):
    book_chars = list(book.lower())
    char_count = {}

    for char in book_chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(dict):
    return dict["count"]

def sort_dictionary(dictionary):
    sorted_dictionary = [{'char': char, 'count': count} for char, count in dictionary.items()]
    sorted_dictionary.sort(reverse=True, key=sort_on)
    return sorted_dictionary
