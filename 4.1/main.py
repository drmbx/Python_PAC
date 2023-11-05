import numpy as np
import sys


def main():
    real_file = sys.argv[1]
    synth_file = sys.argv[2]
    p = float(sys.argv[3])

    real_data = np.loadtxt(real_file)
    synth_data = np.loadtxt(synth_file)

    indices = np.arange(len(real_data))
    np.random.shuffle(indices)

    mixed_data = np.where(indices < int(p * len(indices)), real_data, synth_data)
    print(mixed_data)


main()
