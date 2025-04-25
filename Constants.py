class DateUtils:
    MONTHS = {
        '01': 'Январь',
        '02': 'Февраль',
        '03': 'Март',
        '04': 'Апрель',
        '05': 'Май',
        '06': 'Июнь',
        '07': 'Июль',
        '08': 'Август',
        '09': 'Сентябрь',
        '10': 'Октябрь',
        '11': 'Ноябрь',
        '12': 'Декабрь'
    }

    @staticmethod
    def get_month_name(month_number):
        """
        Возвращает название месяца по его номеру
        :param month_number: номер месяца (строка в формате '01', '02' и т.д.)
        :return: название месяца
        """
        return DateUtils.MONTHS.get(month_number, 'Неизвестный месяц')

class Colors:
    GOOGLE_COLORS = {
        "Blue": '#4285F4',
        "Red": '#DB4437',
        "Yellow": '#F4B400',
        "Green": '#0F9D58',
        "Purple": '#AB47BC',
        "Cyan": '#00BCD4',
        "Orange": '#FF9800',
        "Brown": '#795548',
        "Blue Grey": '#607D8B',
        "Pink": '#E91E63'
    }
