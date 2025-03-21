def get_num_words(blob_of_text):
    blob_of_text = blob_of_text.split()
    num_words = len(blob_of_text)
    return num_words

def count_characters(input_string):
    character_dictionary = {}
    for char in input_string.lower():
        if char in character_dictionary: 
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    return character_dictionary

def dict_to_sorted_list_of_dicts(dict_to_sort):
    list_of_dicts = []
    for key in dict_to_sort:
        tmp_dict = {}
        tmp_dict["character"] = key
        tmp_dict["count"] = dict_to_sort[key]
        list_of_dicts.append(tmp_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts


def sort_on(dict):
    return dict["count"]


