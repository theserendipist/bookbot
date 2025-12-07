def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(frankenstein)
    print(f"Found {num_words} total words")

def get_book_text(path):
    with open(path) as b:
        book = b.read()
    
    return book

def get_num_words(book):
    words = book.split()
    num_words = len(words)

    return num_words

main()