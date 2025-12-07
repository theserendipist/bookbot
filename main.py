def main():
    from stats import get_num_words, get_num_chars, sort_chars

    frankenstein = get_book_text("books/frankenstein.txt")
    
    num_words = get_num_words(frankenstein)
    print(f"Found {num_words} total words")

    num_chars = get_num_chars(frankenstein)
    print(num_chars)

    sorted_num_chars = sort_chars(num_chars)
    print(sorted_num_chars)

def get_book_text(path):
    with open(path) as b:
        book = b.read()
    
    return book

main()