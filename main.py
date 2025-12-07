def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    print(frankenstein)

def get_book_text(path):
    with open(path) as b:
        book = b.read()
    
    return book

main()