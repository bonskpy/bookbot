def get_book_text(path:str):
    with open(path) as f:
        file_content = f.read()
    return file_content 

def count_words(text:str):
    spearated_words = text.split()
    return len(spearated_words)

def main():
    book_content = get_book_text("books/frankenstein.txt") 
    words_count = count_words(book_content)
    print(f"{words_count} words found in the document")

main()
