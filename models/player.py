import random

from models.attributes import RATING_QUALITIES, Attributes
from modules import names

FOOTS = ("L", "R")

POSITIONS = ("GK", "CB", "RB", "LB", "CM", "CDM", "CAM", "ST", "CF", "RW", "LW")

NATIONALITIES = (["Brazil", "br"], ["Uruguay", "uy"], ["Argentina", "ar"])


class Player:
    name: str
    age: int
    height: int
    weight: int
    nationality: str
    position: str
    strong_foot: str
    attributes: dict

    def __init__(self, position: str = None):
        nationality = random.choice(NATIONALITIES)

        self.name = names.full(nationality[1])
        self.age = random.randint(16, 40)
        self.height = random.randint(160, 200)
        self.weight = random.randint(60, 95)
        self.nationality = nationality[0]
        self.position = position if position else random.choice(POSITIONS)
        self.strong_foot = random.choice(FOOTS)
        self.attributes = Attributes(
            position=self.position, rating_points=random.choice(RATING_QUALITIES)
        )

    def __str__(self):
        return (
            f"name: {self.name}\n"
            f"age: {self.age}\n"
            f"height: {self.height} cm\n"
            f"weight: {self.weight} kg\n"
            f"nationality: {self.nationality}\n"
            f"position: {self.position}\n"
            f"strong foot: {self.strong_foot}\n"
            f"attributes:\n{self.attributes}\n"
        )
