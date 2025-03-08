from stats import get_book_text, count_words, character_count

def main():
    book_content = get_book_text("books/frankenstein.txt") 
    words_count = count_words(book_content)
    char_count = character_count(book_content)
    print(f"{words_count} words found in the docume nt")
    print(char_count)

main()
