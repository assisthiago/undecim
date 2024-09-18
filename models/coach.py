import random

from modules import names

NATIONALITIES = (["Brazil", "br"], ["Uruguay", "uy"], ["Argentina", "ar"])

RATING_QUALITIES = ("A", "B", "C", "D", "E", "F")

SPECIALITIES = ["Defensive", "Offensive", "Balanced"]

TATICS = [
    (5, 3, 2),
    (5, 4, 1),
    (4, 5, 1),
    (4, 4, 2),
    (4, 3, 3),
    (3, 4, 3),
    (3, 5, 2),
]


class Coach:
    name: str
    nationality: str
    age: int
    tactics: list[tuple[int]]
    rank: str
    speciality: str

    def __init__(self):
        nationality = random.choice(NATIONALITIES)

        self.name = names.full(nationality[1])
        self.nationality = nationality[0]
        self.age = random.randint(16, 40)
        self.tactics = random.choices(TATICS, k=2)
        self.rank = random.choice(RATING_QUALITIES)
        self.speciality = random.choice(SPECIALITIES)

    def __str__(self):
        return f"{self.name} (Rank: {self.rank})"
