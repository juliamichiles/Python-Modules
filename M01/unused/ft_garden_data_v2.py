class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print("{}: {}cm, {} days old".format(rose.name, rose.height, rose.age))
    print("{}: {}cm, {} days old".format(sunflower.name, sunflower.height, sunflower.age))
    print("{}: {}cm, {} days old".format(cactus.name, cactus.height, cactus.age))


if __name__ == "__main__":
    ft_garden_data()
