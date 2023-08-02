from src.job_api import HH, SJ
from src.classes_for_vacancies import Vac_for_HH, JsonVac, VacSJ
from job_json import RAWjson

class WorkWithUser:
    '''Пользовательский интерфейс (почти)'''
    def __init__(self):
        self.site = None
        self.request = None
        self.city = None
        self.quantity = None

    def __str__(self):
        return f"Ваш запрос:" \
               f"\nСайт -{self.site}" \
               f"\nЗапрос - {self.request}" \
               f"\nГород - {self.city}" \
               f"\nКол-во вакансий - {self.quantity}"

    def choice_site(self):
        site_list = ['hh.ru', 'superjob.ru']
        while True:
            try:
                choice_user = int(
                    input(f'1 - {site_list[0]}\n2 - {site_list[1]}\nВыберите платформу: '))
                if choice_user in [1, 2]:
                    self.site = site_list[choice_user - 1]
                    break
                else:
                    raise ValueError
            except ValueError: print("Ошибка ввода")

    def get_request(self):
        self.request = input("\nВведите Ваш запрос: ")

    def city_choice(self):
        city_list = ['Россия', 'Москва', 'Санкт-Петербург']
        while True:
            try:
                choice_user = int(input(f'1 - {city_list[0]}\n2 - {city_list[1]}\n3 - {city_list[2]}\nВыберите регион: '))
                if choice_user in [1, 2, 3]:
                    self.city = city_list[choice_user - 1]
                    break
                else:
                    raise ValueError
            except ValueError: print("Ошибка ввода")


    def number(self):
        if self.site == 'superjob.ru':
            self.quantity = 20
            print(f'Количество вакансий будет - {self.quantity}')
        else:
            while True:
                try:
                    choice_user = int(input("\nДиапазон от 1 до 100\nВведите количество вакансий для вывода в топ: "))
                    if 0 < choice_user < 101:
                        self.quantity = choice_user
                        break
                    else:
                        raise ValueError
                except ValueError: print("Ошибка ввода")

    def api(self, number: int):
        jobs = []
        if self.site == 'hh.ru':
            city = {'Россия': 1, 'Москва': 1, 'Санкт-Петербург': 2}
            info = HH(self.request, self.quantity, city[self.city]).get_info()
            for item in info:
                jobs.append(Vac_for_HH(item).__dict__)
        else:
            city = {'Россия': 1, 'Москва': 4, 'Санкт-Петербург': 14}
            if self.city == 'Россия':
                info = SJ(self.request, c=city[self.city]).get_info()
            else:
                info = SJ(self.request, t=city[self.city]).get_info()
            for item in info:
                jobs.append(VacSJ(item).__dict__)
        if number == 0:
            RAWjson.write_json(jobs)
        else:
            RAWjson.add_json(jobs)

    @staticmethod
    def sort_all():
        """Сортирует полученные вакансии"""

        all_vacancies = RAWjson.read_json()
        total_vacancies = []
        for i in all_vacancies:
            total_vacancies.append(
                JsonVac(i['url'], i['title'], i['city'], i['salary_int'], i['salary'], i['requirements'],
                              i['date']))
        total_vacancies.sort()
        info = []
        for i in total_vacancies:
            info.append(i.__dict__)
        RAWjson.write_json(info)

    def word_finder(self, find_words: str):
        """Выполняет поиск по ключевым словам пользователя"""

        info = RAWjson.read_json()
        list = []
        for i in info:
            try:
                for items in i.values():
                    try:
                        if find_words in items:
                            if i['url'][:14] == 'https://hh.ru/':
                                list.append(i['url'])
                            else:
                                list.append(i['url'])
                    except TypeError:
                        continue
            except AttributeError:
                continue
        if list == []:
            return f'По вашему запросу {find_words} ничего не найдено!'
        else:
            return f'Ваш запрос: {find_words} найден в вакансиях\n{list}'