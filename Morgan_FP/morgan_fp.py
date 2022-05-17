import sys


from fingerprint_finder.read_db_2 import *
from fingerprint_finder.read_fingerprint import *
from fingerprint_finder.morgan_fp_finder import *


def main():
    parser = Read_db_2(sys.argv[1])
    dfs = parser.get_df()
    count = 0
    for x in dfs:
        fp_sample = Read_fingerprint(sys.argv[2])
        pattern = fp_sample.get_smile()
        finder = Finder(pattern, x, count)
        count += 1


if __name__ == '__main__':
    main()