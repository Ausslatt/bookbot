
def main():
    file_path = "books/frankenstein.txt"
    print("Begin report of books/frankenstein.txt")

    # print_text(get_text(file_path))
    count_words(get_text(file_path))
    count_characters(get_text(file_path))

def get_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content
    
def print_text(text):
    print(text)

def count_words(text):
    words = text.split()
    word_count = len(words)
    print(f"{word_count} words are in the text.")

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for k,v in char_count.items():
        print(f"{k} occurs {v} times in the text.")

if __name__ == "__main__":
    main()