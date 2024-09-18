import random

import randomname

from models.coach import Coach
from models.player import POSITIONS, Player


class Team:
    name: str
    players: list[Player]
    coach: Coach
    tactic: tuple[int]
    budget: int
    overall: int

    def __init__(self):
        self.name = (
            f"Clube {' '.join(randomname.get_name(noun=['sports']).split('-')).title()}"
        )
        self.players = self.__create_players()
        self.coach = Coach()
        self.tactic = random.choice(self.coach.tactics)
        self.budget = random.randint(1000000, 10000000)
        self.overall = self.__calculate_overall()

    def __create_players(self):
        players = []

        for position in POSITIONS:
            for _ in range(2):
                players.append(Player(position=position))

        return players

    def __calculate_overall(self):
        total_overall = sum(player.attributes.overall for player in self.players)
        return total_overall // len(self.players)

    def __str__(self):
        players = []
        for player in sorted(
            self.players,
            key=lambda p: (
                POSITIONS.index(p.position)
                if p.position in POSITIONS
                else len(POSITIONS)
            ),
        ):
            players.append(
                f"\n  {player.position} - {player.name} ({player.attributes.overall})"
            )

        return (
            f"Team: {self.name} (Overall {self.overall})\n"
            f"Coach: {self.coach}\n"
            f"Tactic: {'-'.join([str(x) for x in self.tactic])}\n"
            f"Players (Total {len(self.players)}): {''.join(players)}\n"
        )
