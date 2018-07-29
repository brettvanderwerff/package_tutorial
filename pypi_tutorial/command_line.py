import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--num1', type=int, nargs=1, required=True,
                        help='Enter the value of the first number.')

    parser.add_argument('--num2', type=int, nargs=1, required=True,
                        help='Enter the value of the second number.')
    args = vars(parser.parse_args())

    return args['num1'][0], args['num2'][0]