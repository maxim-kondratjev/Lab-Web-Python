# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.
import time


class timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, *args, **kwargs):
        print(time.time()-self.start_time)
