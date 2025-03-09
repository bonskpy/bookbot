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

def sort_characters(char_count_dict:dict) -> list[dict]:
    """function takes a dictionary and returns a sorted list of dictionaries"""
    char_count_list = []
    
    for key, value in char_count_dict.items():
        char_count_list.append({key:value})

    def value_getter(item: dict):
        return list(item.values())[0]

    char_count_list.sort(key=value_getter, reverse=True)

    return char_count_list
    
