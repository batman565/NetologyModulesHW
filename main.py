from datetime import datetime
from numpy import sin
from people import get_employees
from salary import calculate_salary


if __name__ == "__main__":
    get_employees()
    calculate_salary()
    print(datetime.now())
    print(sin(60))