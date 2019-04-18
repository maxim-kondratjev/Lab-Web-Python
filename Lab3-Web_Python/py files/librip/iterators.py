# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.counter = -1
        self.items = []
        if not kwargs.get("ignore_case"):
            if items:
                for x in items:
                    if x not in self.items:
                        self.items.append(x)
        else:
            if items:
                items = map(str.lower, items)
                for x in items:
                    if x not in self.items:
                        self.items.append(x)
        self.size = len(self.items)

    def __next__(self):
        if self.counter + 1 < self.size:
            self.counter += 1
        else:
            raise StopIteration()
        return self.items[self.counter]

    def __iter__(self):
        return self
