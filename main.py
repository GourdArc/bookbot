def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    print(f"--- Begin report of {book_path} ---")
    
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    chars = get_num_letters(text)
    for char_dict in chars:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- End Report ---")
    
def get_book_text(path):
    #opens the text as a string
    with open(path) as f:
        return f.read()

def get_num_words(text):
    #word count for text
    words = text.split()
    return len(words)

def get_num_letters(text):
    lowered_text = text.lower()
    unique = set()
    unique_count = {}
    #creates a dictionary that contains a letter and the number of times it appears in the text
    for w in lowered_text:
        if w not in unique and w.isalpha():
            unique.add(w)
            unique_count[w] = 1
        elif w in unique and w.isalpha():
            unique_count[w] += 1
    #Convert dictionary to list of dictionaries
    chars = []
    for char, num in unique_count.items():
        char_dict = {"char": char, "num": num}
        chars.append(char_dict)
    
    #sort list by num
    def sort_on(dict):
        return dict["num"]
    
    chars.sort(reverse=True, key=sort_on)
    return chars



if __name__ == "__main__":
    main()