import io 
import random

class Handsome_Lox_Files: 
    def __init__(self):
        self.ratio_handsome = [] # создает пустой список красавчиков 
        self.ratio_Lox = [] # создает пустой список лохов
        self.Percentage_Lox = int(input("Введите процент лохов, который должен быть в файлах: от 0 до 100 ")) / 100 * 6 # Прри вызове класса, просит ввести процент лохов в файлах
        self.list_frinds = ["Диман", "Володя", "Ден", "Архип", "Григс", "Мадер"]
        self.List_lox = random.choices(self.list_frinds, k=int(self.Percentage_Lox)) # Рандомит список list_frinds в зависимосте от процентного соотношения 
        
        
        for friend in self.list_frinds: # запускает цикл создания файлов.
            with open(f'{friend}.txt', 'w', encoding='utf-8') as file:
                if friend in self.List_lox:             # условия при котором frinds попадает в тот или иной список в зависимости есть ли он в списке лохов или нет 
                    file.write(f'{friend} ЛОХ')
                    self.ratio_Lox.append(friend)
                else:
                    file.write(f'{friend} Красавчик')
                    self.ratio_handsome.append(friend)


        print("Данные красавчики, лохи:", *self.ratio_Lox)   
        print("Данные  лохи, красавчики:", *self.ratio_handsome)
    
    

Handsome_Lox_Files()
print('Спасибо за внимание')