def count_words(document):
    num_words = 0
    array_split = document.split()
    num_words = len(array_split)
    return num_words

def count_letters(document):
    # dictionary to output
    dict_count = {}

    # normalizing document
    lowercase_doc = document.lower() 
    for letter in lowercase_doc:
        if letter in dict_count:
            dict_count[letter] += 1
        if letter not in dict_count:
            dict_count[letter] = 1

    return dict_count

def sort_dict(dict):
    sorted_dict = []
    for i in dict:
        if i.isalpha(): # results should only be for alphanum characters
            entry = {"ltr": i, "num": dict[i]}
            sorted_dict.append(entry)

    def sort_key(sorted_dict):
        return sorted_dict["num"]

    sorted_dict.sort(reverse=True, key=sort_key)

    return sorted_dict