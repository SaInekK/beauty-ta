import re
from typing import Iterable


def check_text_template(text: str, keys: Iterable[str]):
    parentheses_count = check_parentheses_equality(text)
    word_matches = re.findall(r'{([^{}]+)}', text)

    if parentheses_count != len(word_matches):
        raise Exception('В тексте встречаются фигурные '
                        'скобки без значения в них.')

    for word in word_matches:
        if word in keys:
            continue
        raise Exception(f'В переданных ключах не нашлось следующего: {word}')

    return text


def check_parentheses_equality(text) -> int:
    par_matches = re.findall(r'[{|}]', text)
    left_par_matches = len(list(filter(lambda x: x == '{', par_matches)))
    right_par_matches = len(list(filter(lambda x: x == '}', par_matches)))
    if left_par_matches != right_par_matches:
        raise Exception('Текст содержит неравное количество '
                        'левых и правых фигурных скобок.')
    return left_par_matches


def main():
    test_text = '''{name}, ваша запись изменена:
    ⌚ {day_month} в {start_time}
    👩 {master}
    Услуги:
    {services}
    управление записью {record_link}'''

    list_keys = [
        'name',
        'day_month',
        'day_of_week',
        'start_time',
        'end_time',
        'master',
        'services',
    ]
    check_text_template(test_text, list_keys)


if __name__ == '__main__':
    main()
