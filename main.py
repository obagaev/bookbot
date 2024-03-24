def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    print(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(txt):
    return len(txt.split())

main()