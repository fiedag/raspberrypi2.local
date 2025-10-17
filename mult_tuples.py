import argparse

def parse_pair(string):
    try:
        x, y = string.split(',')
        return (float(x), float(y))
    except ValueError:
        raise argparse.ArgumentTypeError(f"Pairs must be x,y format")

parser = argparse.ArgumentParser()
parser.add_argument('--points', type=parse_pair, action='append',
                    help='Add a point as x,y (can be used multiple times)')

args = parser.parse_args(['--points', '1,2', '--points', '3,4', '--points', '5,6'])
print(args.points)  # [(1.0, 2.0), (3.0, 4.0), (5.0, 6.0)]

for water, fert in args.points:
    print(f"water for {water} seconds and fertiliser for {fert} seconds")

    