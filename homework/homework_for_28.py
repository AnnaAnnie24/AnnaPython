trees = {
    "Birch": "https://justfunfacts.com/wp-content/uploads/2016/10/birch-trees-2.jpg",
    "Elm": "https://cdn.shopify.com/s/files/1/0059/8835/2052/products/American_Elm_Tree_5_FGT_1024x1024.jpg",
    "Chesnut": "https://images.freeimages.com/images/large-previews/c19/blooming-chestnut-tree-1338029.jpg",
    "Pine": "https://www.thetreecenter.com/wp-content/uploads/eastern-white-pine-2.jpg",
    "Spruce": "https://www.familyhandyman.com/wp-content/uploads/2021/04/blue-spruce-GettyImages-1147811728.jpg",
    "Willow": "https://wallpapercave.com/wp/x8T3mis.jpg",
    "Palm": "https://www.thetreecenter.com/wp-content/uploads/palm-trees-beach.jpg",
    "Maple": "https://www.savatree.com/wp-content/uploads/2019/05/shutterstock_178723310-1024x683.jpg",
    "Cedar": "https://www.treeguideuk.co.uk/wp-content/uploads/2021/07/cedar-atlas-1-scaled.jpg",
    "Oak": "https://pixfeeds.com/images/topic/5555/1200-5555-oak-trees-photo2.jpg",
}

trees_name = input("Pick A Tree To See: ")
if trees_name in trees:
    link = trees[trees_name]
    print("Tree is present")
    print(link)
else:
    "Sorry, try again"

number_of_trees = len(trees)
print(number_of_trees)
