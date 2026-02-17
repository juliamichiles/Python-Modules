class Plant:
    name: str
    height: str
    age: str

def ft_garden_data():
    rose = Plant()
    sunflower = Plant()
    cactus = Plant()
    rose.name = "Rose:"
    rose.height = "25cm,"
    rose.age = "30 days old"
    sunflower.name = "Sunflower:"
    sunflower.height = "80cm,"
    sunflower.age = "45 days old"
    cactus.name = "Cactus:"
    cactus.height = "15cm,"
    cactus.age = "120 days old"
    print(rose.name, rose.height, rose.age) 
    print(sunflower.name, sunflower.height, sunflower.age) 
    print(cactus.name, cactus.height, cactus.age)  
if __name__ == "__main__":
    ft_garden_data()
