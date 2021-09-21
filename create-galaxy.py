import requests
import json


class Connector:
    server = "http://127.0.0.1:8000"
    api = "api"

    def __init__(self):
        self.session = requests.session()

    def url_maker(self, *items):
        return "/".join([self.server, *items]) + "/"

    def get_list(self, lc_model: str):
        res = self.session.get(self.url_maker(self.api, lc_model))
        if res.status_code != 200:  # учитывая контекст применения я не стал тут делать, чтобы выкидывало ошибку, а потом ее ловить
            print('exception!')
            print(res.status_code)
            print(res.text)
        return res.json()

    def create(self, lc_model: str, data):
        res = self.session.post(self.url_maker(self.api, lc_model), json=data)
        if res.status_code != 201:
            print('exception!')
            print(res.status_code)
            print(res.text)
        return res.json()

    def delete(self, lc_model: str, pk):
        res = self.session.delete(self.url_maker(self.api, lc_model, pk))
        if res.status_code != 204:
            print('exception!')
            print(res.status_code)
            print(res.text)
        return res

# connector.create('Galaxy', {
#     "name": "galaxy created by script",
#     "size_x": 10,
#     "size_y": 15
# })

def run(connector):
    cmd = input('Действие: ')
    if cmd == 'cg':
        name = input('Название галактики: ')
        x = input('Размер по x: ')
        y = input('Размер по y: ')
        connector.create('Galaxy', {
            "name": name,
            'size_x': x,
            'size_y': y
        })
    if cmd == 'lg':
        for galaxy in connector.get_list('Galaxy'):
            print(f'{galaxy["pk"]}. {galaxy["name"]} ({galaxy["size_x"]}, {galaxy["size_y"]})')

    if cmd == 'dg':
        pk = input('Введите номер галактики для удаления: ')
        print(connector.delete('Galaxy', pk))

    if cmd == 'css':
        name = input('Название звездной системы: ')
        x = input('Расположение по x: ')
        y = input('Расположение по y: ')
        galaxy = input('Галактика: ')

        connector.create('StarSystem', {
            "name": name,
            'position_x': x,
            'position_y': y,
            'galaxy': galaxy
        })
    if cmd == 'lss':
        for star_system in connector.get_list('StarSystem'):
            print(
                f'{star_system["pk"]}. {star_system["name"]} ({star_system["position_x"]}, {star_system["position_y"]}) galaxy: {star_system["galaxy"]}')

    if cmd == 'dss':
        pk = input('Введите номер звездной системы для удаления: ')
        print(connector.delete('StarSystem', pk))

    if cmd == 'cs':
        name = input('Название звезды: ')
        color = input('Цвет: ')
        star_system = input('Звездная система: ')
        diameter = input('Диаметр: ')

        connector.create('Star', {
            "name": name,
            'color': color,
            'star_system': star_system,
            'diameter': diameter
        })
    if cmd == 'ls':
        for star in connector.get_list('Star'):
            print(
                f'{star["pk"]}. {star["name"]} d={star["diameter"]} {star["color"]} star system: {star["star_system"]}')

    if cmd == 'ds':
        pk = input('Введите номер звезды для удаления: ')
        print(connector.delete('Star', pk))

    if cmd == 'cp':
        name = input('Название планеты: ')
        color = input('Цвет: ')
        star_system = input('Звездная система: ')
        diameter = input('Диаметр: ')
        live = input('Обитаемая ли планета? [ПУСТОЕ = нет, Любое значение = да]') != ''

        connector.create('Planet', {
            "name": name,
            'color': color,
            'star_system': star_system,
            'diameter': diameter,
            'live': live
        })
    if cmd == 'lp':
        for planet in connector.get_list('Planet'):
            print(
                f'{planet["pk"]}. {planet["name"]} d={planet["diameter"]} {planet["color"]} is alive: {planet["live"]} star system: {planet["star_system"]}')

    if cmd == 'dp':
        pk = input('Введите номер планеты для удаления: ')
        print(connector.delete('Planet', pk))


def main():
    print('Выберите действие:')

    print('cg создать галактику')
    print('lg список галактик')
    print('dg удалить галактику')
    print()
    print('css создать звездную систему')
    print('lss список звездных систем')
    print('dss удалить звездную систему')
    print()
    print('cs создать звезду')
    print('ls список звезд')
    print('ds удалить звезду')
    print()
    print('cp создать планету')
    print('lp список планет')
    print('dp удалить планету')

    connector = Connector()

    while True:
        run(connector)


if __name__ == '__main__':
    main()
