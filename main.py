from stats import *

def get_book_text(path_to_file):
      
    with open(path_to_file) as f:
        file_contents = f.read()

    return str(file_contents)



def main():
    path_to_book = "books/frankenstein.txt"
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(path_to_book))} total words")
    print("--------- Character Count -------")
    for list_element in dict_to_sorted_list_of_dicts(count_characters(get_book_text(path_to_book))):
        if list_element["character"].isalpha():
            print(f"{list_element["character"]}: {list_element["count"]}")

    print("============= END ===============")




main()