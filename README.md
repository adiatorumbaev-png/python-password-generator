# Python Password Generator

Консольная программа на Python для генерации случайных паролей и PIN-кодов с проверкой надёжности пароля.

## Описание проекта

Многие пользователи придумывают простые и одинаковые пароли для разных сервисов, из-за чего аккаунты легко взломать. Программа решает эту проблему: она генерирует случайные пароли заданной длины, сразу оценивает их надёжность (`weak` / `medium` / `strong`) и умеет подобрать несколько надёжных паролей за один раз.

## Возможности

| Функция | Описание |
|---------|----------|
| `generate_password(length)` | генерация случайного пароля из букв, цифр и символов `!@#$%` |
| `check_strength(password)` | оценка надёжности: длина ≥ 8, цифры, заглавные буквы, спецсимволы |
| `generate_pin(length)` | генерация PIN-кода из цифр |
| `read_length()` | ввод длины пароля с проверкой (от 4 до 32) |
| `generate_many(count, length)` | генерация списка паролей |
| `filter_by_strength(passwords, level)` | отбор паролей нужного уровня надёжности |
| `menu()` | интерактивное меню программы |

## Используемые технологии

- **Python 3.8+** (проверено на Python 3.14) — только стандартная библиотека: `random`, `string`
- **pytest** — автоматические тесты
- **Git** и **GitHub** — контроль версий, ветки, Pull Request
- **Ubuntu 26.04** (VirtualBox) — среда разработки

## Структура проекта

```text
python-password-generator/
├── src/
│   └── main.py          # исходный код программы
├── tests/
│   └── test_main.py     # тесты pytest
├── README.md            # документация проекта
├── requirements.txt     # зависимости
└── .gitignore           # исключения для Git
```

## Требования

1. Python 3.8 или новее.
2. Git (для клонирования репозитория).
3. Модуль `venv` для создания виртуального окружения (в Ubuntu: пакет `python3-venv`).

## Установка

```bash
git clone https://github.com/adiatorumbaev-png/python-password-generator.git
cd python-password-generator
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск

```bash
python3 src/main.py
```

Запуск тестов:

```bash
pytest
```

## Использование

После запуска открывается меню:

```text
1 - password, 2 - PIN, 3 - strong passwords, 0 - exit: 1
Length (4-32): 12
Password: U4$kYhNW@V6c - strong
1 - password, 2 - PIN, 3 - strong passwords, 0 - exit: 2
PIN: 7633
1 - password, 2 - PIN, 3 - strong passwords, 0 - exit: 3
Strong passwords: 7 of 10
  ra#6yD55LXMv
  zPLW8A2Jw!SM
  !Rb8z$Ewrf2H
  bk%5IbGpgi$0
  G7$3sMgk8mpd
  0#aiH$eRc@#D
  ts0Y112fSj#6
1 - password, 2 - PIN, 3 - strong passwords, 0 - exit: 0
```

- **1** — пароль заданной длины с оценкой надёжности;
- **2** — PIN-код из 4 цифр;
- **3** — 10 случайных паролей, из которых выводятся только надёжные;
- **0** — выход.

## Зависимости

Все зависимости перечислены в файле [requirements.txt](requirements.txt).
Сама программа использует **только стандартную библиотеку Python**; внешняя библиотека `pytest` нужна только для запуска тестов.

## Автор

**Орумбаев Адият Жуматаевич**, студент группы П-25-75б, ВК «Astana Polytechnic».
