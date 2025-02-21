'''
https://adventofcode.com/2024/day/2
'''
import math
from utils import load_resc_file, print_ln

REPORTS = "reports.txt"
SAMPLE_REPORTS = "sample_reports.txt"

MAX_STEP = 3


def validate_report(report: list[int]) -> bool:
    dir = 0
    for i, val in enumerate(report[1:]):
        diff = val - report[i]
        if not diff or abs(diff) > 3:
            return False
        curr_dir = diff/abs(diff)
        dir = dir or diff/abs(diff)
        if dir != curr_dir:
            return False
    return True


def validate_reports() -> int:
    # reports = "sample_reports2.txt"
    with load_resc_file(2, REPORTS) as fp:
        counter = 0

        while True:
            ln = fp.readline()
            if not ln:
                break
            if validate_report_v4([int(i)
                                   for i in ln.split(" ")]):
                counter += 1
    return counter


def validate_report_v4(reports: list[int]) -> bool:
    graph = AccessabilityGraph(reports, num_dampers=3)
    graph.generate_accessability_graph()
    if graph.validate_graph():
        return True
    graph = graph.reverse_graph()
    graph.generate_accessability_graph()
    if graph.validate_graph():
        return True
    return False


def validate_report_v2(report: list[int], damper: int = 1) -> bool:
    print('straw')
    print(report)
    if validate_increasing(report, damper):
        print('wh')
        return True
    if damper > 0 and validate_increasing(report[1:], damper-1):
        print('hm')
        return True
    if validate_increasing([i for i in reversed(report)], damper):
        print('s')
        return True
    if damper > 0 and validate_increasing([i for i in reversed(report[:-1])], damper-1):
        print('ch')
        return True
    print(report)
    return False


class AccessabilityGraph():
    '''Construct a graph that tracks if index `i` in `report` can be reached using `k` number of dampers'''
    num_dampers: int
    report: list[int]
    _graph: list[list[int]]

    def __init__(self, report: list[int], num_dampers: int):
        '''Construcn'''
        self.num_dampers = num_dampers
        self.report = report

        self._graph = [[0 for _i in range(len(report))]
                       for _j in range(num_dampers + 1)]
        for damper in range(num_dampers+1):
            self._graph[damper][damper] = 1

    def reverse_graph(self):
        return AccessabilityGraph([_i for _i in reversed(self.report)], self.num_dampers)

    def validate_graph(self):
        for dampers_used in range(self.num_dampers+1):
            if self._graph[self.num_dampers - dampers_used][len(self.report)-1 - dampers_used]:
                return True
        return False

    def generate_accessability_graph(self):
        for report_index, _ in enumerate(self.report):
            for dampers_used in range(self.num_dampers + 1):
                if self.get_accessablity(report_index, dampers_used):
                    self.mark_next_values(report_index, dampers_used)
        self._print_graph()

    def get_accessablity(self, report_index, dampers_used) -> int:
        return self._graph[dampers_used][report_index]

    def mark_next_values(self, report_index, dampers_used):
        for dampers_to_use in range(dampers_used, self.num_dampers+1):
            next_report_index = report_index + 1 + dampers_to_use - dampers_used
            next_report_val = self.report[next_report_index] if next_report_index < len(
                self.report) else math.inf
            if self.determin_elig(next_report_val, self.report[report_index]):
                self._graph[dampers_to_use][next_report_index] = 1

    def determin_elig(self, new_val, old_val):
        if new_val <= old_val:
            return False
        if new_val - old_val > MAX_STEP:
            return False
        return True

    def _print_graph(self):
        print_ln()
        for li in self._graph:
            print(li)
        print_ln()


def validate_report_v3(report: list[int], dampers: int = 1) -> bool:
    # status : 1 : visitable, 0: not visitable

    _report_graph = [[0 for _i in range(len(report))]
                     for _j in range(dampers + 1)]
    for damper in range(dampers+1):
        _report_graph[damper][damper] = 1

    for report_index, _ in enumerate(report):
        for damper in range(dampers + 1):
            if _report_graph[damper][report_index] == 0:
                continue
            for dampers_used in range(damper, dampers + 1):
                next_item = (report_index + dampers_used -
                             damper + 1, dampers_used)
                _report_val = report[next_item[0]
                                     ] if next_item[0] < len(report) else math.inf
                report_diff = _report_val - report[report_index]
                if report_diff > MAX_STEP or report_diff <= 0:
                    continue
                print('aha')
                _report_graph[next_item[1]][next_item[0]] = 1


def validate_increasing(report: list[int], damper: int) -> bool:
    i = 0
    j = 1
    print(report)
    while j < len(report):
        if report[i] >= report[j] or report[j]-report[i] > MAX_STEP:
            damper -= 1
            if damper < 0:
                return False
        else:
            i = j
        j = j+1

    return True


if __name__ == "__main__":
    print(validate_reports())
