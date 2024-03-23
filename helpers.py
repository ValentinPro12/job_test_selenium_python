from typing import Any


def expect_equal(check_name: str, actual_value: Any, expected_value: Any, url: str):
    """Сравнение фактического значения с ожидаемым, проверяем что равны.

    :param check_name: название проверки
    :param actual_value: фактическое значение
    :param expected_value: ожидаемое значение
    """
    error_text = f"{check_name}. Ожидание: '{expected_value}'. Факт: '{actual_value}'. URL: '{url} "
    print(error_text)
    assert actual_value == expected_value, error_text
