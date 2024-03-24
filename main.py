def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    chars = count_chars(text)
    char_sorted_list = letters_for_report(chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words was found in this report\n")
    
    for item in char_sorted_list:
        if not  item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(txt):
    return len(txt.split())

def count_chars(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def letters_for_report(charcter_dict):
    list_dicts = []
    for char in charcter_dict:
        list_dicts.append({"char": char, "count": charcter_dict[char]}) 
    list_dicts.sort(reverse=True, key=sort_on)    
    return list_dicts

def sort_on(dict):
    return dict["count"]

main()