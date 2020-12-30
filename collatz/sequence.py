from typing import Generator, NamedTuple

from collatz.utils import keep_value


class SequenceOptions(NamedTuple):
    a: int = 3
    b: int = 3
    c: int = 3

    def __repr__(self):
        return f'n * {self.a} + {self.b} if n % {self.c} else n // {self.c}'

    def apply(self, n):
        if n % self.c:
            return n * self.a + self.b
        return n // self.c


@keep_value
def sequence(
    n: int,
    options: SequenceOptions = SequenceOptions()
) -> Generator[int, None, int]:
    result = 1
    yield n
    n = options.apply(n)
    while n != 1:
        yield n
        n = options.apply(n)
        result += 1
    return result
