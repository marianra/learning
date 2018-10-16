# LISTS OF WORDS
cz_list = ["ahoj", "den", "noc", "dobry", "jidlo"]
eng_list = ["hello", "day", "night", "good", "food"]

# AGAIN VAR
again = "yes"

# WHILE LOOP FOR REPEATING
while again == "yes":
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
        else:
            print("!UNSUPPORTED LANGUAGE!")

    # CALLING THE TRANSLATE FUNCTION + ASKING TO REPEAT
    translate(lang_from)
    again = input("DO YOU WANNA TRANSLATE ANYTHING ELSE?")

