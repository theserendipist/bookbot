def get_num_words(book):
    words = book.split()
    num_words = len(words)

    return num_words

def get_num_chars(book):
    book = book.lower()
    num_chars = {}
    for char in book:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1

    return num_chars