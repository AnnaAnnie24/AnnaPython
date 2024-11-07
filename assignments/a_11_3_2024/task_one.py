kids_books_genres = {
    "Where the Wild Things Are": "Picture Book",
    "Charlotte's Web": "Classic",
    "The Very Hungry Caterpillar": "Picture Book",
    "Harry Potter and the Sorcerer's Stone": "Fantasy",
    "The Cat in the Hat": "Rhyming",
    "Goodnight Moon": "Picture Book",
    "Matilda": "Fantasy",
    "Pete the Cat: I Love My White Shoes": "Picture Book",
    "The Gruffalo": "Picture Book",
    "Winnie-the-Pooh": "Classic"
}
# TODO: for each book write the following text on separate lines:
#       "Book" has a genre ...

for key, value in kids_books_genres.items():
    print(key, '-', value)
for key, value in kids_books_genres.items():
    print(key, 'has a genre', value)
