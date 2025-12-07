def main():
    from stats import get_num_words
    
    frankenstein = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(frankenstein)
    print(f"Found {num_words} total words")

def get_book_text(path):
    with open(path) as b:
        book = b.read()
    
    return book

main()