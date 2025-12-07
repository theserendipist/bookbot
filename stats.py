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

def sort_on(items):
    return items["num"]

def sort_chars(num_chars):
    sorted = []
    for (k, v) in num_chars.items():
        sorted.append({
            "char": k,
            "num": v
        },)
    sorted.sort(reverse=True, key=sort_on)
    return sorted