class Filters:
    def __getitem__(self, item):
        """
        Возвращаем метод фильтра при попытке получения через квадратные скобки
        """
        return eval("self." + item, {"self": self})

    @staticmethod
    def black_white(*rgb):
        """
                    "Чёрно-белый"
        Сумму всех каналов делим нацело на 3 канала
        """
        return sum(rgb) // 3, sum(rgb) // 3, sum(rgb) // 3

    @staticmethod
    def negative(r, g, b):
        """
                "Негатив"
        Инвертируем абсолютно все каналы
        """
        return 255 - r, 255 - g, 255 - b

    @staticmethod
    def inversion_red(r, g, b):
        """
        "Инверсия красного канала"
        Инвертируем красный канал
        """
        return 255 - r, g, b

    @staticmethod
    def inversion_green(r, g, b):
        """
        "Инверсия зелёного канала"
        Инвертируем зелёный канал
        """
        return r, 255 - g, b

    @staticmethod
    def inversion_blue(r, g, b):
        """
        "Инверсия синего канала"
        Инвертируем синий канал
        """
        return r, g, 255 - b

    @staticmethod
    def black_gray_white(*rgb):
        """
                                    "Чёрно-серо-белый"
        Находим сумму значений всех каналов и разделяем их на белый, серый и чёрный пиксели
        """
        if sum(rgb) >= 510:
            return 255, 255, 255
        elif sum(rgb) >= 255:
            return 127, 127, 127
        return 0, 0, 0

    @staticmethod
    def retro(r, g, b):
        """
                                    "Ретро"
        Увеличиваем значение красного канала на 50, зелёный уменьшаем на 50, а синий - инвертируем
        """
        return min(r + 50, 255), max(g - 50, 0), 255 - b

    @staticmethod
    def neon_retro(r, g, b):
        """
                                    "Неоновый ретро"
        Уменьшаем значение красного канала на 50, зелёный увеличиваем на 50, а синий - инвертируем
        """
        return max(r - 50, 0), min(g + 50, 255), 255 - b

    @staticmethod
    def sakura(r, g, b):
        """
                            "Сакура"
        Меняем зелёный канал на синий, остальные - не трогаем.
        """
        return r, b, b

    @staticmethod
    def total_black_white(*rgb):
        """
                "Абсолютно чёрно-белый"
        Аналогично "Чёрно-серо-белый", но делим на 2 канала
        """
        if sum(rgb) >= 383:
            return 255, 255, 255
        else:
            return 0, 0, 0

    @staticmethod
    def white_balance(r, g, b):
        """
                            "Баланс белого"
        Находим сумму значений каналов и обнуляем, если их сумма <= 50
        """
        if (r + g + b) <= 50:
            return 0, 0, 0
        return r, g, b

    @staticmethod
    def black_balance(r, g, b):
        """
                                "Баланс чёрного"
        Находим сумму значений каналов и увеличиваем до белого, если их сумма >= 700
        """
        if (r + g + b) >= 700:
            return 255, 255, 255
        return r, g, b
