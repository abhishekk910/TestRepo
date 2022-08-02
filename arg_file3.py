import argparse
parser = argparse.ArgumentParser()
parser.add_argument('x', type=int)
parser.add_argument('y', type=int)
args = parser.parse_args()
product = args.x * args.y
print('Product:', product)

# python3 arg_file3.py 10 15