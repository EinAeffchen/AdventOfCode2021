from typing import List, Optional, Union
from pathlib import Path

path = Path(__file__).parent
with open(path / "input4.txt", "r") as f:
    input_data = [line.strip() for line in f.readlines()]


class Field(object):
    def _read_numbers(self, numbers) -> Optional[int]:
        self.bingo_numbers = list()
        for row in numbers:
            self.bingo_numbers.append([int(number) for number in row.split()])

    def _check_vertical(self, drawings, bingo_numbers):
        rotated_bingo_numbers = list(zip(*reversed(bingo_numbers)))
        return self._check_horizontal(drawings, rotated_bingo_numbers)

    def _check_horizontal(
        self, drawings, bingo_numbers: List[List[int]]
    ) -> Optional[int]:
        for row in bingo_numbers:
            if (
                all([ele in drawings for ele in row])
                and frozenset(row) not in self.winning_sets
            ):
                self.winning_sets.add(frozenset(row))
                return row

    def _get_unmarked_sum(self, drawings: List):
        return sum(
            [
                number
                for row in self.bingo_numbers
                for number in row
                if number not in drawings
            ]
        )

    def is_winner(self, drawings) -> Union[int, bool]:
        if self._check_horizontal(drawings, self.bingo_numbers):
            return self._get_unmarked_sum(drawings) * drawings[-1]
        elif self._check_vertical(drawings, self.bingo_numbers):
            return self._get_unmarked_sum(drawings) * drawings[-1]
        else:
            return False

    def __init__(self, numbers: List[str]) -> None:
        self._read_numbers(numbers)
        self.winning_sets = set()


class Bingo:
    def _read_bingo_data(self, input_data: list):
        self.drawings = [int(drawing) for drawing in input_data[0].split(",")]
        bingo_set = list()
        for row in input_data[1:]:
            if len(row) > 1:
                bingo_set.append(row)
            elif bingo_set:
                new_field = Field(bingo_set)
                self.fields.append(new_field)
                bingo_set = list()

    def __init__(self, input_data) -> None:
        self.fields: List[Field] = list()
        self._read_bingo_data(input_data)

    def get_winners(self) -> List[int]:
        winners = list()
        for i in range(len(self.drawings)):
            loosers = list()
            for j, bingo_field in enumerate(self.fields):
                if result := bingo_field.is_winner(self.drawings[: i + 1]):
                    winners.append(result)
                else:
                    loosers.append(j)
            self.fields = [self.fields[looser] for looser in loosers]
        return winners


# part1
b = Bingo(input_data)
winners = b.get_winners()
print(winners[0])
# part2
print(winners[-1])
