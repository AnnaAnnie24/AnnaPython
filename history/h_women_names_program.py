women_names = ["Alexandra", "Brianna", "Charlotte", "Delaney", "Eva", "Fiona", "Grace", "Hailey", "Isabelle",
               "Jennifer", "Karina", "Layla", "Mia", "Nora", "Olivia", "Piper", "Quinn", "Raya", "Sophia",
               "Talia", "Unity", "Vivianne", "Willow", "Xandra", "Yasmin", "Zara"]
print("~Welcome To The Women Name Checker Program~")
name = input("~What Name Would You Like To Check~ ")
if name in women_names:
    print("~Yes, We Have That Name~")
else:
    print("~No, We Don't Have That Name~")
for woman_name in women_names:
    number_of_letters = len(woman_name)
    if number_of_letters < 6:
        print("~", woman_name, "~")
