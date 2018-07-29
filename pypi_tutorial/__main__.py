from pypi_tutorial import command_line
from pypi_tutorial import my_prog # why odes this not work


def main():
    num1, num2 = command_line.parse_args()
    my_prog.compare_num(num1, num2)

main()