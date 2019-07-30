from collections.abc import Mapping
from typing import _KT, Generator, Iterator, List, Tuple, _T_co, _VT_co


class ParseTableError(Exception):
    """Parse table base error."""


class ParsedTableDict(Mapping):
    def __init__(self, *args, original_line: str, **kwargs):
        self.original_line = original_line
        self._storage = dict(*args, **kwargs)

    def __len__(self) -> int:
        return len(self._storage)

    def __iter__(self) -> Iterator[_T_co]:
        return iter(self._storage)

    def __getitem__(self, k: _KT) -> _VT_co:
        return self._storage[k]


def table2dicts(
    name_line: str, separator_line: str, data_lines: List[str]
) -> Generator[ParsedTableDict, None, None]:
    col_width = tuple(_get_col_width(separator_line))
    names = tuple(map(str.strip, _get_columns(name_line, col_width)))

    for line in data_lines:
        columns = map(str.strip, _get_columns(line, col_width))
        yield ParsedTableDict(zip(names, columns), original_line=line)


def _get_col_width(line: str) -> Iterator[int]:
    line_symbols = set(line)
    separator_set = line_symbols - {" "}
    if len(separator_set) != 1:
        raise ParseTableError
    separator = separator_set.pop()

    return map(lambda s: s.count(separator), line.split())


def _get_columns(line: str, col_width: Tuple[int, ...]) -> Generator[str, None, None]:
    current_pos = 0
    for width in col_width:
        end = current_pos + width
        yield line[current_pos:end]

        current_pos = end + 1
