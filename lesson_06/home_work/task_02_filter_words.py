
def filter_words(*words):
    if len(words) == 0:
        return

    initial_word_list = list(words)
    print(f"initial_word_list is {initial_word_list}")
    filtered_list = [x for x in initial_word_list if len(x)>5]

    return filtered_list


result = filter_words("Miriam","Rachel","Sara")
print(f"the words that have more than 5 chars are : {result}")