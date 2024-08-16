monkey_song = """
Bob the monkey liked to dance and he was a good dancer.
Although he falls on banana peels, he could never stop prancing.
One day Bob was on the dance floor, eating a banana.
They caught him and he got in trouble for eating a banana.
Bob the monkey was very sad, he wanted another banana.
The other monkey saw that he was sad and gave him a banana.
Bob the monkey leaped with joy and munched secretly.
Bob hugged the another monkey and thanked him for his kindness.
"""
b = "b"
B = "B"
counter = 0
for symbol in monkey_song:
    if symbol == b or symbol == B:
        counter += 1

print(counter)














