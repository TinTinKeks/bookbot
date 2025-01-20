def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text = text_lower(text)
    num_words = get_num_words(text)
    dictionary = count_letters(text)
    dictionary_list = create_character_lists(dictionary)
    message = "--- Begin report of books/frankenstein.txt ---\n"
    message = message + ((f"{get_num_words(text)} words found in the document\n \n"))
    message = message + (create_message(dictionary_list))
    print(message)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def text_lower(text):
    lowered_string = text.lower()
    return lowered_string

def count_letters(text):
    result_dict = {}
    for letter in text:
        if letter in result_dict:
            result_dict[letter] += 1
        else:
            result_dict[letter] = 1
    return result_dict

def create_character_lists(dictionary):
    list_dictionary = [{}]
    for dic in dictionary:
        if dic.isalpha():
            list_dictionary.append({"character": dic, "count": dictionary[dic]})
    list_dictionary.pop(0)
    return list_dictionary

def create_message(dictionary_list):
    dictionary_list = sorted(dictionary_list, key = lambda x: x["count"], reverse = True)
    result = ""
    for dic in dictionary_list:
        result = result + f"The '{dic["character"]}' character was found '{dic["count"]}' times\n"
    result = result + "--- End report ---"
    return result

main()