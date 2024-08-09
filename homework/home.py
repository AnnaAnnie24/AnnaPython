women_names = ["Alexandra", "Brianna", "Charlotte", "Delaney", "Eva", "Fiona", "Grace", "Hailey", "Isabelle",
               "Jennifer", "Karina", "Layla", "Mia", "Nora", "Olivia", "Piper", "Quinn", "Raya", "Sophia",
               "Talia", "Unity", "Vivianne", "Willow", "Xandra", "Yasmin", "Zara"]
for woman_name in women_names:
    number_of_letters = len(woman_name)
    if number_of_letters < 6:
        print(woman_name)

Aaaa = "a"
for woman_name in women_names:
    if woman_name[-1] == Aaaa:
        print("~", woman_name, "~")
