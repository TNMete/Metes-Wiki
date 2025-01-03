# Code 1

# # 10 Wörter Gemüse und Obst
# ger_eng = {
#     "Apfel": "apple",
#     "Banane": "banana",
#     "Erdbeere": "strawberry",
#     "Gurke": "cucumber",
#     "Ananas": "pineapple",
#     "Zitrone": "lemon",
#     "Orange": "orange",
#     "Kirsche": "cherry",
#     "Tomate": "tomato",
#     "Aubergine": "eggplant",
# }
# my_input = input("Welches Wort soll übersetzt werden? ").strip().capitalize()

# if my_input in ger_eng:
#     trans_input = ger_eng[my_input]
#     print(f"Die Übersetzung von {my_input} lautet: {trans_input}")
# else:
#     print(f"Das Wort {my_input} befindet sich nicht im Wörterbuch")


# CODE 2


# dictionary = {
#     "Apfel": "apple",
#     "Hund": "dog",
#     "Katze": "cat",
#     "Baum": "tree",
#     "Auto": "car",
#     "Haus": "house",
#     "Tisch": "table",
#     "Stuhl": "chair",
#     "Fenster": "window",
#     "Buch": "book",
# }


# def extend_dictionary():
#     print(
#         "Erweiterung des Wörterbuchs. Geben Sie 'exit' ein, um die Erweiterung zu beenden."
#     )
#     while True:
#         german_word = input("Geben Sie ein deutsches Wort ein: ").strip()
#         if german_word.lower() == "exit":
#             break
#         english_translation = input(
#             f"Geben Sie die englische Übersetzung für '{german_word}' ein: "
#         ).strip()
#         dictionary[german_word] = english_translation
#         print(
#             f"'{german_word}' wurde mit der Übersetzung '{english_translation}' hinzugefügt."
#          )


# user_input = input("Welches deutsche Wort möchten Sie übersetzen? ").strip()
# if user_input.capitalize() in dictionary:
#     print(
#         f"Die englische Übersetzung von '{user_input}' ist '{dictionary[user_input.capitalize()]}'."
#     )
# else:
#     print(f"Das Wort '{user_input}' ist nicht im Wörterbuch enthalten.")
#     extend = input("Möchten Sie das Wörterbuch erweitern? (ja/nein): ").strip().lower()
#     if extend == "ja":
#         extend_dictionary()


# Hiermit werden neue Wörter zum Wörterbuch hinzugefügt:

# my_dict = {"apfel": "Apple", "wörterbuch": "dictionary"}
# my_userinput = input("Gib ein deutsches Wort ein: ")
# if my_userinput in my_dict:
#     print(f"Die Übersetzung zu {my_userinput} ist {my_dict[my_userinput]}")
# else:
#     actual_translation = input(
#         "Das Wort gibt es noch nicht, gib die engl. Übersetzung ein: "
#     )
#     my_dict[my_userinput] = actual_translation
#     print(f"Die Übersetzung zu {my_userinput} ist {my_dict[my_userinput]}")


def translate(german_word):
    my_dict = {"apfel": "Apple", "Wörterbuch": "dictionary"}

    if german_word in my_dict:
        print(f"Die Übersetzung zu {german_word} ist {my_dict[german_word]}")
    else:
        actual_translation = input(
            "Das Wort gibt es noch nicht, gib die engl. Übersetzung ein: "
        )
        my_dict[german_word] = actual_translation
        print(f"Die Übersetzung zu {german_word} ist {my_dict[german_word]}")


my_userinput = input("Gib ein deutsches Wort ein: ")
if my_userinput == "exit":
    print("I am not going to translate anything")
else:
    translate(my_userinput)
