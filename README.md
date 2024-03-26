Установка проекта.
1. Скопировать ссылку из git или получть архив.
2. Открыть в pycharm, перейти в настройки -> настройки проекта выбрать пункт python interpreter -> add interpreter -> add local interpreter
   выбрать virtualenv environment, если версий python  несколько выбрать версию 3.10 или выше, нажать ОК.

Альтернативный способ установки 
1. Установить python3 с сайта https://www.python.org/ или sudo apt install python3
2. Установить компоненты Python: 
sudo apt install python3.10-venv 
sudo apt install python-pip 
3. Установить виртуальное окружение в корневой директории проекта командой python3 -m venv venv

5. source .venv/bin/activate

6. Установка зависемостей pip install -r requarements.txt



Установка Google Chrome
1.Установить Google Chrome: 
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i --force-depends google-chrome-stable_current_amd64.deb

Запуск тестов
Запуск всех тестов осуществляется командой pytest или pytest -s -v 
Запуск тестов из конкретного модуля pytest <./test_модуль_с_тестами.py>
Запуск конкретной тестовой функции pytest -k <test_тестовая_функция> (пока не доступно)
Запуск тестов с генерацией Allure отчета pytest --alluredir=<директория_для_генерации_allure_файлов> (пока не доступно)





