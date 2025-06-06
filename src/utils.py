from typing import Literal

RESC_DIRECTORY = "src/resources"
OUTPUT_DIRECTORY = 'output'


def load_resc_file(day: int, file: str, mode: Literal['r', 'w'] = "r"):

    path = f"{RESC_DIRECTORY}/day{day}/{file}"
    return open(path, mode)


def load_out_file(day: int, file: str, mode: Literal['r', 'w'] = "r"):

    path = f"{RESC_DIRECTORY}/{OUTPUT_DIRECTORY}/day{day}/{file}"
    return open(path, mode)


def load_file_lines(day, file):
    path = f"{RESC_DIRECTORY}/day{day}/{file}"
    with open(path, encoding="utf-8") as fp:
        for ln in fp:
            yield ln


def print_ln():
    print("-----------------")
