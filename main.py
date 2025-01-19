def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    num_unique_letters = get_num_letters(text)
    print(f" {num_unique_letters} is the count for each character in the text")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    lowered_text = text.lower()
    unique = set()
    unique_count = {}
    for w in lowered_text:
        if w not in unique:
            unique.add(w)
            unique_count[w] = 1
        elif w in unique:
            unique_count[w] += 1
    return unique_count



if __name__ == "__main__":
    main()