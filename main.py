def main():
    import sys
    from stats import get_num_words, get_num_chars, sort_chars

    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    
    num_words = get_num_words(book)
    num_chars = get_num_chars(book)

    sorted_num_chars = sort_chars(num_chars)
    
    print_report(book_path, num_words, sorted_num_chars)

def get_book_text(path):
    with open(path) as b:
        book = b.read()
    
    return book

def print_report(book_path, num_words, sorted_num_chars):
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for item in sorted_num_chars:
        if item["char"].isalpha():
            char = item["char"]
            count = item["num"]
            print(f"{char}: {count}")

    print("============= END ===============")

main()