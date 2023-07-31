from src.job_api import HH


class WorkWithUser:
    '''Пользовательский интерфейс (почти)'''
    def __init__(self):
        self.request = None
        self.city = None
        self.quantity = None

    def __str__(self):
        return f"Ваш запрос:" \
               f"\nСайт - Headhunters" \
               f"\nЗапрос - {self.request}" \
               f"\nГород - {self.city}" \
               f"\nКоличество вакансий - {self.quantity}"

    def get_request(self):
        self.request = input("\nВведите Ваш запрос по поиску вакансий: ")

