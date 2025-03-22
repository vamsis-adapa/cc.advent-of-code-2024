from itertools import permutations

from utils import load_file_lines

POINT = tuple[int, int]

__DIRECTIONS = [0, 1, -1]
DIRECTIONS = set(permutations(__DIRECTIONS, 2)) | set(
    [(i, i) for i in __DIRECTIONS if i]
)

WORD = "XMAS"


class Crossword:
    text_block: list[str]
    word: str

    def __init__(self, text_block, word) -> None:
        self.text_block = text_block
        self.word = word

    def search_direction(
        self, cords: tuple[int, int], direc: tuple[int, int], dist: int
    ):
        st = ""
        try:
            for dev in range(dist):
                index_x = cords[0] + dev * direc[0]
                index_y = cords[1] + dev * direc[1]
                if index_x < 0 or index_y < 0:
                    raise IndexError
                st += self.text_block[index_x][index_y]
        except IndexError:
            # print(cords, dev, direc)
            pass
        if st == WORD:
            print(cords)
            print(self.text_block[cords[0]][cords[1]], direc)
        return st

    def search_all_directions(self, index: tuple[int, int]) -> int:
        is_word = 0
        for direc in DIRECTIONS:
            is_word += (
                1 if self.search_direction(
                    index, direc, len(self.word)) == WORD else 0
            )
        return is_word

    def parse_full_block(self):
        all_words = 0
        for row_id, row in enumerate(self.text_block):
            for col_id, _val in enumerate(row):
                if self.text_block[row_id][col_id] == self.word[0]:
                    all_words += self.search_all_directions((row_id, col_id))

        return all_words


if __name__ == "__main__":
    text_block: list[str] = []
    for line in load_file_lines(4, "wordsearch.txt"):
        # for line in load_file_lines(4, 'mini.txt'):
        text_block.append(line.strip())

    crswrd = Crossword(text_block, WORD)
    print(crswrd.parse_full_block())
    print("------")
    rot = ["".join(i) for i in list(zip(*text_block[::-1]))]
