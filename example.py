from pathlib import Path
import random


class LosharaCalculator:
    def __init__(self, save_dir: str):
        if not isinstance(save_dir, str):
            raise TypeError("Путь до директории, где все будет сохранено, должен быть строкой!")

        self.save_dir = Path(save_dir)  # оборачивает строку со входа в функцию в путь

        if not self.save_dir.exists():  # Проверяет, есть ли путь
            self.save_dir.mkdir(parents=True, exist_ok=True)  # Если его нет, создает директорию вместе с родительскими

        try:
            user_percentage = int(input(
                "Введите процент лохов, который должен быть в файлах: от 0 до 100: "
            ))  # При вызове класса, просит ввести процент лохов в файлах
        except ValueError:
            print("На вход нужно подать числовое значение, значение по умолчанию - 100, лохами будут все")
            user_percentage = 100

        if user_percentage < 0 or user_percentage > 100:
            raise ValueError("Значение должно быть от 0 до 100!")  # Проверяет процент на выход за пределы

        self.user_percentage = user_percentage

        self.list_friends = ["Диман", "Володя", "Ден", "Архип", "Григс", "Мадер"]

    def poschitat_loshar(self):
        ratio_handsome = []  # создает пустой список красавчиков
        ratio_loshar = []  # создает пустой список лохов
        list_loshkov = random.choices(
            self.list_friends,
            k=round(self.user_percentage / 100 * 6),
        )  # Рандомит список list_frinds в зависимости от процентного соотношения

        for friend in self.list_friends:  # запускает цикл создания файлов.
            friend_file = self.save_dir / f"{friend}.txt"
            with friend_file.open('w', encoding='utf-8') as file:
                if friend in list_loshkov:  # условие, при котором friend попадает в тот или иной список
                    file.write(f'{friend} ЛОХ')
                    ratio_loshar.append(friend)
                else:
                    file.write(f'{friend} Красавчик')
                    ratio_handsome.append(friend)

        print("Список лохов:", *ratio_loshar)
        print("Список красавчиков:", *ratio_handsome)


if __name__ == "__main__":
    # Это хорошая практика, чтобы код ниже запускался только
    # тогда, когда ты вызываешь конкретно этот файл
    save_path = 'F:/0001'
    loshara_calc = LosharaCalculator(save_dir=save_path)
    loshara_calc.poschitat_loshar()
    # Этот подход правильнее, потому что мы можем с разными результатами
    # для одного и того же заданного процента получить разные результаты
    loshara_calc.poschitat_loshar()
    print('Раз')
    loshara_calc.poschitat_loshar()
    print('Два')
    loshara_calc.poschitat_loshar()
    print('Три')
    print('Спасибо за внимание')
