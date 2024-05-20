import io
import random

class Handsome_Lox_Files:
    def __init__(self):
        self.ratio_handsome = []
        self.ratio_Lox = []
        self.Percentage_Lox = int(input("Введите процент лохов, который должен быть в файлах: от 0 до 100 ")) / 100 * 6
        self.list_frends = ["Диман", "Володя", "Ден", "Архип", "Григс", "Мадер"]
        self.List_lox = random.choices(self.list_frends, k=int(self.Percentage_Lox))
        
        
        for friend in self.list_frends:
            with open(f'C:\\Users\\vovak\\OneDrive\Рабочий стол\\{friend}.txt', 'w', encoding='utf-8') as file:
                if friend in self.List_lox:
                    file.write(f'{friend} ЛОХ')
                    self.ratio_Lox.append(friend)
                else:
                    file.write(f'{friend} Красавчик')
                    self.ratio_handsome.append(friend)


        print("Данные красавчики, лохи:", *self.ratio_Lox)
        print("Данные  лохи, красавчики:", *self.ratio_handsome)
    
    

Handsome_Lox_Files()
print('Спасибо за внимание')
