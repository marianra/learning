# LISTS OF WORDS
cz_list = ["ahoj", "den", "noc", "dobry", "jidlo"]
eng_list = ["hello", "day", "night", "good", "food"]

# START
print("!!!TRANSLATING ONLY FROM CZ TO ENG!!!")
lang_from = input("FROM: ")
word = input("THE WORD: ")


# TRANSLATE FUNCTION
def translate(l_from):
    if l_from == "cz":
        index = cz_list.index(word)
        print("IN ENGLISH: " + eng_list[index])
    elif l_from == "eng":
        index = eng_list.index(word)
        print("IN CZECH: " + cz_list[index])


translate(lang_from)
