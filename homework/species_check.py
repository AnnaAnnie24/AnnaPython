amphibians = "4 legs"
reptile = "4 legs"
mammals = "4 legs"
animals_pics = {
    "elephant": "https://www.kamranweb.com/photos/wp-content/uploads/2008/12/african-elephant.jpg",
    "giraffe": "https://wallpapercave.com/wp/wp5470314.jpg",
    "cheetah": "https://fullhdwall.com/wp-content/uploads/2016/06/Crying-Baby-Cheetah.jpg",
    "tiger": "https://farm6.staticflickr.com/5210/5221315731_ac9a62585a_b.jpg",
    "zebra": "https://thumbs.dreamstime.com/b/baby-zebra-cape-mountain-watering-hole-southern-african-savanna-82889575.jpg",
    "panda": "https://tse2.mm.bing.net/th?id=OIP.UE6anHxeooIHRonAyGNA_QHaE5&pid=Api&P=0&h=220",
    "bear": "https://www.earthtouchnews.com/media/734894/baby_bear_in_grass_portrait_2014-11-25.jpg",
    "red panda": "https://wallpaperaccess.com/full/658717.jpg",
    "polar bear": "https://cbsnews1.cbsistatic.com/hub/i/2014/03/19/9ec0f31a-051a-40e2-87bb-bb58e8f7c8d3/polarbeartwins1.jpg",
    "eagle": "https://untamedanimals.com/wp-content/uploads/2020/09/Baby-Eagle-Eaglet-FAQ-1.jpg",
    "parrot": "https://www.baltana.com/files/wallpapers-6/Baby-Parrot-Background-Wallpapers-19740.jpg",
    "lion": "https://66.media.tumblr.com/a89c7c0a645dc240f70a83503865a094/tumblr_o26yjzv4571tg93zvo1_1280.jpg",
    "monkey": "https://outforia.com/wp-content/uploads/2021/03/Types_Monkey_1_0321.jpg",
    "gorilla": "https://seancrane.com/blogphotos/gorilla_baby11x.jpg",
    "flamingo": "https://i.huffpost.com/gadgets/slideshows/245499/slide_245499_1394964_free.jpg",
    "alligator": "https://images.freeimages.com/images/large-previews/7da/baby-alligator-1247082.jpg",
    "crocodile": "https://www.goodfreephotos.com/albums/animals/reptiles-and-amphibians/young-baby-crocodile-close-up.jpg",
    "camel": "https://tse3.mm.bing.net/th?id=OIP.yvuiheExwyLcfkuERlh8ygHaFj&pid=Api&P=0&h=220",
    "spider": "https://www.zooborns.com/.a/6a010535647bf3970b016304faac7d970d-800wi",
    "cat": "https://tse1.mm.bing.net/th?id=OIP._phIrl4Q063Ve34x0uF0lgHaE8&pid=Api&P=0&h=220",
    "dog": "https://tse1.mm.bing.net/th?id=OIP.kOq067GmQSbGkNdRx5KckAHaE9&pid=Api&P=0&h=220",
    "turtle": "https://tse3.mm.bing.net/th?id=OIP.qpWzbcnEVD5hkA0KYlcS7wHaE7&pid=Api&P=0&h=220",
    "shark": "https://tse1.mm.bing.net/th?id=OIP.mZMS-dG2Bt7l73-s0fl-7QHaJ4&pid=Api&P=0&h=220",
    "dolphin": "https://images.freeimages.com/images/large-previews/675/baby-dolphin-3-1372849.jpg",
    "fish": "https://i.imgur.com/lkN5t.png",
}
animals = {
    "elephant": 4,
    "giraffe": 4,
    "cheetah": 4,
    "tiger": 4,
    "zebra": 4,
    "panda": 4,
    "bear": 4,
    "red panda": 4,
    "polar bear": 4,
    "eagle": 2,
    "parrot": 2,
    "lion": 4,
    "monkey": 2,
    "gorilla": 2,
    "flamingo": 2,
    "alligator": 4,
    "crocodile": 4,
    "camel": 4,
    "spider": 8,
    "cat": 4,
    "dog": 4,
    "turtle": 4,
    "shark": 0,
    "dolphin": 0,
    "fish": 0,
}

no_legs = 0
answer = input("Welcome To The National State Zoo, What Animal Would You Like To See: ")
if answer in animals:
    legs = animals[answer]
    print("Yes, we have a", answer, "in our zoo")
    if legs == no_legs:
        print(answer, "has no legs")
    else:
        print(answer, "has", legs, "legs")
else:
    print("Sorry, we don't have a", answer, "in our zoo")
