from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime, date, time
import datetime

if __name__ == '__main__':



    get_employees()
    calculate_salary()


    print(datetime.datetime.today())
    print(datetime.datetime.now())

