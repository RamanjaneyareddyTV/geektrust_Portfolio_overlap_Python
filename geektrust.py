import sys
from core.utils import (
    create_portfolio,
    compare,
    add_stock,
    split_command,
    process_result,
    CURRENT_PORTFOLIO,
    CALCULATE_OVERLAP
)


def getinput(input_file_name=None):
    """
    Reads inputs from commandline argument or
    optionally, from an input file (for testing).

    Args:
        input_file_name (str, optional): Optionally reads input file
        (used only for testing). Defaults to None.
    """
    if not (input_file_name):
        input_file_name = sys.argv[-1]

    with open(input_file_name, "r") as input_file:
        for _line in input_file.readlines():
            if _line.startswith(CURRENT_PORTFOLIO):
                fund_names = _line.replace(
                    CURRENT_PORTFOLIO, "").strip().split()
                current_portfolio = create_portfolio(fund_names)

            elif _line.startswith(CALCULATE_OVERLAP):
                fund_name = _line.strip().split()[-1]
                result = compare(fund_name, current_portfolio)
                process_result(result)

            else:
                fund_name, stock_name = split_command(_line)
                add_stock(fund_name, stock_name)


if __name__ == "__main__":
    getinput()
