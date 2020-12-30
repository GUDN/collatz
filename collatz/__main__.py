import argparse

import numpy as np
import matplotlib.pyplot as plt

from collatz.sequence import SequenceOptions, sequence
from collatz.utils import Natural

parser = argparse.ArgumentParser(
    description='A Collatz hypothesis tester and visualizer'
)
parser.add_argument(
    '-s', '--start', help='a start number (inclusive)',
    type=Natural, default=1
)
parser.add_argument(
    '-e', '--end', help='a end number (inclusive)',
    type=Natural, default=10
)
parser.add_argument(
    '-a', help='a A sequence option',
    type=int, default=3
)
parser.add_argument(
    '-b', help='a B sequence option',
    type=int, default=3
)
parser.add_argument(
    '-c', help='a C sequence option',
    type=int, default=3
)
parser.add_argument(
    '--max', help='a max step counts',
    type=int, default=200000
)


def main():
    args = parser.parse_args()
    options = SequenceOptions(a=args.a, b=args.b, c=args.c, max_=args.max)
    ns = np.arange(args.start, args.end + 1)
    values = np.zeros(len(ns), dtype=np.uint64)
    for i, n in enumerate(ns):
        seq = sequence(n, options)
        try:
            list(seq)
        except ValueError:
            values[i] = 0
        else:
            values[i] = seq.value
    colors = np.clip(np.random.random((len(ns), 3)), 0, 0.9)
    plt.scatter(ns, values, c=colors)
    plt.title(f'A Collatz steps count ({options})')
    plt.xlim(left=-1)
    plt.ylim(bottom=-1)
    plt.xlabel('Start number')
    plt.ylabel('Steps count')
    plt.show()


if __name__ == '__main__':
    main()
