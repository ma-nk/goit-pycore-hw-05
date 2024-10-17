from typing import Callable
import re
from decimal import Decimal


def generator_numbers(txt: str):
    for number in re.findall(r'\d+\.\d+', txt):
        yield number.strip()


def sum_profit(txt: str, func: Callable):
    sum = 0
    for number in func(txt):
        sum += Decimal(number)
    return sum


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
