import sys
import time
import year_2015
import year_2024


if __name__ == '__main__':
    year = sys.argv[1]
    day = sys.argv[2]
    test = False
    if len(sys.argv) >= 4:
        test = sys.argv[3] == 't'
    print(f'Solving year {year}, day {day}{["", " with test input"][test]}...')
    data = 'year_{}/input/day{:02d}{}.txt'.format(year, int(day), ["", "_test"][test])

    start = time.time()
    try:
        for i, ans in enumerate(eval('year_{}.day{:02d}.solve("{}")'.format(year, int(day), data))):
            print(f'\tAnswer to part {i+1}: {ans}')
    except FileNotFoundError:
        print(f'\t[ERROR] Required input file not found: {data}')
    end = time.time()
    print('Finished in {:.2f} ms'.format((end-start)*1000))