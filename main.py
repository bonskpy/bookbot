import sys
from stats import get_book_text, count_words, character_count 
from stats import sort_characters

BOOK_PATH = "books/frankenstein.txt"

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    BOOK_PATH = sys.argv[1]

    book_content = get_book_text(BOOK_PATH) 
    words_count = count_words(book_content)
    char_count = character_count(book_content)
    sorted_characters = sort_characters(char_count)
    
    
    print("\n\n============ BOOKBOT ============")
    print(f"Analyzing book found at {BOOK_PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        for key, value in item.items():
            if key.isalpha():
                print(f"{key}: {value}")
    print("============= END ===============\n\n")

main()
