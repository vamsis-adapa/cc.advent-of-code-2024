

import re
from utils import load_file_lines


MUL_STRING = r"mul\([0-9]+,[0-9]+\)"


def get_all_muls(ln: str) -> list[int]:
    mul_re = re.compile(MUL_STRING)
    muls = mul_re.findall(ln) or []

    exctracted_muls = []
    for mul in muls:
        mul = mul.removeprefix("mul(")
        mul = mul.removesuffix(")")
        mul = mul.split(",")
        exctracted_muls.append(int(mul[0]) * int(mul[1]))
    return exctracted_muls


def get_active_muls(ln: str) -> list[int]:
    lns = ln.split("do()")

    activated_muls = []
    for block in lns:
        activated_muls.extend(get_all_muls(block.split("don't()")[0]))

    return activated_muls


def extract_info_from_data():
    info_sum = 0
    for line in load_file_lines(3, 'input.txt'):
        info_sum += sum(get_all_muls(line))

    return info_sum


def extract_info_from_data_with_disables():
    info_sum = 0
    all_lines = ""
    for line in load_file_lines(3, 'input.txt'):
        all_lines += " " + line

    return sum(get_active_muls(all_lines))


if __name__ == "__main__":
    # print(extract_info_from_data())
    print(extract_info_from_data_with_disables())
