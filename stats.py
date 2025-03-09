def get_book_text(path:str):
    with open(path) as f:
        file_content = f.read()
    return file_content 

def count_words(text:str):
    spearated_words = text.split()
    return len(spearated_words)

def character_count(text:str):
    text_lowercase = text.lower()
    characters_included = list(set(text_lowercase))
    character_counter = {}

    for character in text_lowercase:
        if character in characters_included:
            if character in character_counter:
                 character_counter[character] += 1
            else:
                character_counter[character] = 1
        else:
            print("something funky is going on here")
    return character_counter

def sort_characters(character_dictionary:dict) -> list[dict]:

    def extract_value(key_value_pair: tuple):
        return key_value_pair[1]
 
    items_char_dict = character_dictionary.items()

    sorted_char_dict = sorted(items_char_dict, key=extract_value, reverse=True)
    print(sorted_char_dict)


    
