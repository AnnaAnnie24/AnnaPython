text = input("Please enter any text: ")
# 1 Way
# text = text.replace(" ", "")
# 2 Way
text = text.strip()
# .upper(), .lower()
amount_of_symbols = len(text)
print(amount_of_symbols)
text = text.upper()
print(text)
