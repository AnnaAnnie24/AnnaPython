translations = {
    "Hello": "привіт",
    "Thank you": "дякую",
    "Please": "будь ласка",
    "Yes": "так",
    "No": "ні",
    "How are you": "як справи",
    "Water": "води",
    "Book": "книга",
    "Cat": "кішка",
    "Dog": "собака",

}

key_list = translations.keys()
key_list = list(key_list)
print(key_list)

values_list = translations.values()
values_list = list(values_list)
print(values_list)

translations["Goodbye"] = "до побачення"
translations["Friend"] = "друг"
print(translations)
