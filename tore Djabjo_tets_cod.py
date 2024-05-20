[1mdiff --git a/Djabjo_tets_cod.py b/Djabjo_tets_cod.py[m
[1mdeleted file mode 100644[m
[1mindex c8868f8..0000000[m
[1m--- a/Djabjo_tets_cod.py[m
[1m+++ /dev/null[m
[36m@@ -1,29 +0,0 @@[m
[31m-import io[m
[31m-import random[m
[31m-[m
[31m-class Handsome_Lox_Files:[m
[31m-    def __init__(self):[m
[31m-        self.ratio_handsome = [][m
[31m-        self.ratio_Lox = [][m
[31m-        self.Percentage_Lox = int(input("Введите процент лохов, который должен быть в файлах: от 0 до 100 ")) / 100 * 6[m
[31m-        self.list_frends = ["Диман", "Володя", "Ден", "Архип", "Григс", "Мадер"][m
[31m-        self.List_lox = random.choices(self.list_frends, k=int(self.Percentage_Lox))[m
[31m-        [m
[31m-        [m
[31m-        for friend in self.list_frends:[m
[31m-            with open(f'C:\\Users\\vovak\\OneDrive\Рабочий стол\\{friend}.txt', 'w', encoding='utf-8') as file:[m
[31m-                if friend in self.List_lox:[m
[31m-                    file.write(f'{friend} ЛОХ')[m
[31m-                    self.ratio_Lox.append(friend)[m
[31m-                else:[m
[31m-                    file.write(f'{friend} Красавчик')[m
[31m-                    self.ratio_handsome.append(friend)[m
[31m-[m
[31m-[m
[31m-        print("Данные красавчики, лохи:", *self.ratio_Lox)[m
[31m-        print("Данные  лохи, красавчики:", *self.ratio_handsome)[m
[31m-    [m
[31m-    [m
[31m-[m
[31m-Handsome_Lox_Files()[m
[31m-print('Спасибо за внимание')[m
