from PyQtUIkit.widgets import KitForm


class Form(KitForm):
    def __init__(self):
        super().__init__(
            KitForm.ComboField('Тип', ['Пустой файл', 'Описание проекта', 'Отчет'])
        )


def write_file(bm, path: str, form_data: list):
    with open(path, 'w', encoding='utf-8') as f:
        if form_data[0] == 'Описание проекта':
            _readme_pattern(bm, f)
        elif form_data[0] == 'Отчет':
            _report_pattern(bm, f)


def _readme_pattern(bm, file):
    file.write(f"""
[author]: <> (TestGenerator)

# {bm.projects.current.name()}

{bm.projects.current.get_data('description', '')}
""")


def _report_pattern(bm, file):
    file.write(f"""
[author]: <> (TestGenerator)
[page-size]: <> (210 297)

[table-of-content]: <>
[page-break]: <>

# Описание условия задачи

{bm.projects.current.get_data('description', '')}

# Техническое задание

## Входные данные

- ???

## Выходные данные

- ???

## Способ обращения

Способ обращения: при запуске программы из консоли входные данные передаются через стандартный поток ввода.

## Аварийные ситуации

- ???

# Описание внутренних структур данных

```{bm.projects.current.get('language', 'C').lower()}
Some code
```

# Описание алгоритма

???

# Тесты

[tests]: <> (EXPECTED_OUTPUT REAL_OUTPUT STATUS)

# Вывод

???

# Контрольные вопросы

1. Вопрос?

    Ответ

2. Вопрос?

    Ответ
""")
