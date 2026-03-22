#!/usr/bin/env python3

# ------------------- PLANTS -----------------------

class Plant:
    # Base Plant

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        return (f"{self.name} grew 1cm")

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"

    def get_category(self) -> str:
        return "regular"


class FloweringPlant(Plant):
    # Plant that can bloom

    def __init__(self,
                 name: str,
                 height: int,
                 color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        self.blooming = True

    def get_info(self) -> str:
        status = "blooming" if self.blooming else "not blooming"
        return (
                f"{self.name}: {self.height}cm, "
                f"{self.color} flowers ({status})"
            )

    def get_category(self) -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):
    # Flowering plant with prize points

    def __init__(self,
                 name: str,
                 height: int,
                 color: str,
                 points: int) -> None:
        super().__init__(name, height, color)
        self.points = points

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.points}"

    def get_category(self) -> str:
        return "prize"


# ------------------- GARDEN ---------------------

class Garden:
    # one garden with plants

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.total_growth: int = 0
        self.plants_added: int = 0

    def add_plant(self, plant: Plant) -> str:
        self.plants.append(plant)
        self.plants_added += 1
        return (f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            print(plant.grow())
            self.total_growth += 1

    def report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print(
            f"\nPlants added: {self.plants_added}, "
            f"Total growth: {self.total_growth}cm"
            )


# --------------- GARDEN MANAGER -----------------

class GardenManager:
    # manages multiple gardens

    garden_count = 0

    class GardenStats:
        # calculates stats

        @staticmethod
        def count_plant_types(plants: list[Plant]) -> tuple[int, int, int]:
            regular = 0
            flowering = 0
            prize = 0
            for plant in plants:
                if plant.get_category() == "regular":
                    regular += 1
                elif plant.get_category() == "flowering":
                    flowering += 1
                elif plant.get_category() == "prize":
                    prize += 1
            return regular, flowering, prize

        @staticmethod
        def validate_height(height: int) -> bool:
            return height >= 0

#  --------------

    def __init__(self) -> None:
        self.gardens: list[Garden] = []

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)
        GardenManager.garden_count += 1

    def get_score(self, garden: Garden) -> int:
        score = 0
        for plant in garden.plants:
            score += plant.height
            score += 10
            if plant.get_category() == "prize":
                score += plant.points
        return score

    @classmethod
    def create_garden_network(cls) -> str:
        return f"Total gardens managed: {cls.garden_count}"


# ------------- GARDEN DEMO --------------

def ft_garden_analytics() -> None:

    print("=== Garden Management System Demo ===\n")

    manager = GardenManager()

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    cactus = Plant("Cactus", 81)

    bob_garden.add_plant(cactus)
    cactus.grow()

    rose.bloom()
    sunflower.bloom()

    print(f"{alice_garden.add_plant(oak)}")
    print(f"{alice_garden.add_plant(rose)}")
    print(f"{alice_garden.add_plant(sunflower)}")

    alice_garden.grow_all()
    alice_garden.report()

    regular, flowering, prize = GardenManager.GardenStats.count_plant_types(
        alice_garden.plants
        )

    print(
        f"Plant types: {regular} regular, "
        f"{flowering} flowering, {prize} prize flowers\n"

    )

    print(
        f"Height validation test: "
        f"{GardenManager.GardenStats.validate_height(10)}"
    )

    alice_score = manager.get_score(alice_garden)
    bob_score = manager.get_score(bob_garden)

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(GardenManager.create_garden_network())


if __name__ == "__main__":
    ft_garden_analytics()
