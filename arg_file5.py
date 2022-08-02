import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--values', type=int, nargs=3)
args = parser.parse_args()
sum = sum(args.values)
print('Sum:', sum)

# python arg_file5.py --values 1 2 3