# Morse code
Мой первый самостоятельный проект. Сделал я его, когда изучал функции Python.
Программа умеет кодировать английский текст и цифры в код Morse и декодировать код Morse  в английские буквы и цифры обратно.
## Используемые ресурсы
Википедия -  Азбука Морзе 
## Структура проекта
Данные представлены в виде двух списков. Первый – список буквы и цифры, второй – соответствующий по индексам код Морзе букв и цифр.
Использую три функции, цикл while, простую логику проверки данных if/elif/else.
## Графическое отображение
![](https://github.com/Aleshichev/code_morse/blob/main/1.png)

## Процесс программы
1.	Програма просит подтвердить начало процесса (цикл будет выполняться до того момента пока пользователь не ответит “No”).
2.	Пользователь должен также ответить, хочет он кодировать или расшифровать данные. Затем ввести данные. После ввода функция **def del_gap()**  удаляет лишние пробелы из  текста.
3.	В зависимости от выбора пользователя выполняется кодировка функцией  **def morze_encode()**,  или дешефровка – функцией **def morze_decode()** введённых данных. Каждая функция выводит соответствующий результат. Цикл повторяется.


