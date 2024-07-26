flowers = {
    "Violet": "https://wallpapercave.com/wp/wp5234037.jpg",
    "Daisy": "https://cdn.britannica.com/36/82536-050-7E968918/Shasta-daisies.jpg",
    "Rose": "https://i.pinimg.com/originals/0c/fe/42/0cfe42b53ae0c76062c74676e8c799c8.jpg",
    "Marigold": "https://dev.mos.cms.futurecdn.net/6btQddey3cCumCij2DP2Ra.jpg",
    "Sunflower": "https://images6.alphacoders.com/415/415232.jpg",
    "Lotus": "https://www.insightstate.com/wp-content/uploads/2024/06/Blue-Lotus-Spiritual-Benefits-5.jpg",
    "Poppy": "https://www.floristwithflowers.com.au/blog/wp-content/uploads/2017/04/poppy-1-1-1024x819.jpg",
    "Waterlily": "https://iwgs.org/wp-content/uploads/Nymphaea-Mahasombut-EXTRA.jpg",
    "Hibiscus": "https://www.publicdomainpictures.net/pictures/230000/velka/beautiful-hibiscus-flower.jpg",
    "Peony": "https://i0.wp.com/www.thebeautyshortlist.com/wp-content/uploads/2011/06/peony-pink1.jpg",
    "Zinnia": "https://www.publicdomainpictures.net/pictures/150000/velka/blooming-zinnias.jpg",
    "Pansy": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Pansy_flower.jpg",
    "Dahlia": "https://www.almanac.com/sites/default/files/image_nodes/dahlia-3598551_1920.jpg",
    "Jasmine": "https://wallpapercave.com/wp/619HSLH.jpg",
    "Petunia": "https://tse1.mm.bing.net/th?id=OIP.-naN63a4ZkczmvPsESdU-QHaFj&pid=Api&P=0&h=220",
    "Tulip": "https://tse2.mm.bing.net/th?id=OIP.nOEjc9BWRr8uCQA4yaYVMAHaEK&pid=Api&P=0&h=220",
    "Hyacinth": "https://www.hollandbulbfarms.com/Shared/Images/Product/Delft-Blue-Hyacinth/84124.jpg",
    "Aster": "https://mygardenflowers.com/wp-content/uploads/2020/09/Aster-novae-angliae.jpg",
    "Daffodil": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Yellow-Daffodil-2009.jpg",
    "Lavender": "https://pacificscents.com.au/wp-content/uploads/2017/08/lavande2.jpg",
    "Magnolia": "https://www.publicdomainpictures.net/pictures/120000/velka/magnolia-tree-flower.jpg",
    "Lilac": "https://cdn.shopify.com/s/files/1/0062/8532/8445/products/Common_Purple_Lilac_3_1024x1024.jpg",
    "Cherry Blossom": "https://tse1.mm.bing.net/th?id=OIP.1v_A1fcBDZ2uvRRDyKgTVwAAAA&pid=Api&P=0&h=220",
    "Primrose": "https://www.applewoodseed.com/wp-content/uploads/2016/12/OSPE-1002-1001x1030.jpg",
    "Dandelion": "https://freebigpictures.com/wp-content/uploads/2009/09/dandelion-flower.jpg",
    "Lily": "https://www.almanac.com/sites/default/files/image_nodes/oriental-lily.jpg",
    "Honey Suckle": "https://2.bp.blogspot.com/-A8QKd97VqYQ/UE40JggeMgI/AAAAAAAAJ9M/glpNDRPXB_o/s1600/honeysuckle.jpg",
    "Orchid": "https://www.gardenmandy.com/wp-content/uploads/2019/09/Vanda-Orchid.jpg",
    "Snow Drop": "https://wallpapercave.com/wp/wp5588634.jpg",
    "Iris": "https://eskipaper.com/images/iris-flower-1.jpg",
    "Bluebell": "https://wallpapercave.com/wp/wp5588634.jpg",
    "Narcissus": "https://www.petalrepublic.com/wp-content/uploads/2020/10/Popular-Types-of-Narcissus-Flower.jpg",
    "Carnation": "https://cdn.britannica.com/38/189538-050-6EC8A082/carnation-flowers.jpg",
}
number_of_flowers = len(flowers)
print(number_of_flowers)
an_empty_dict = {}
# A dict is a dictionary, and it has elements
# Is it possible for dict to have 5 elements? yes
# Is it possible for dict to have 0 elements? yes
# Create an empty dict called harry_potter
# Add an element to this dict with key "name" and an appropriate value
# Add an element to this dict with key "pet" and an appropriate value
# Add an element to this dict with key "number of parents alive" and an appropriate value
# Find out the number of elements in the dict and print this number out
#
harry_potter = {}
harry_potter["name"] = "Harry Potter"
harry_potter["pet"] = "Hedwig"
harry_potter["number of parents alive"] = 0
harry_potter = len(harry_potter)
print(harry_potter)

# work with flowers 💐
# TODO:
#  print out all the flowers

print(flowers)

flower_name = input("Pick A Flower To See: ")
if flower_name in flowers:
    link = flowers[flower_name]
    print("Flower is present")
    print(link)
else:
    "Sorry, try again"

#  Homework
# https://docs.google.com/document/d/13C80aYLsLb6QqFRwRLaRFTodmRMkRfe1Mxui_RLvyn4/edit
