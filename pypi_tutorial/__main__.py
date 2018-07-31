from pypi_tutorial.command_line import parse_args
from pypi_tutorial.my_prog import compare_num


def main():
    num1, num2 = parse_args()
    compare_num(num1, num2)

if __name__ == '__main__':
    main()