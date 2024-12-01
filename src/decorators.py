from functools import wraps


def log(filename=None):
    """Декоратор, который логирует вызов функции, ее успешное выполнение
    или возникновение ошибок."""
    def decorator(func): # func - функция для декорирования
        """Внутренний декоратор, оборачивающий целевую функцию."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            """ Обертка для логирования вызова функции."""
            if filename:
                with open(filename, 'a') as output:
                    def write(message):
                        output.write(message)

            else:
                def write(message):
                    print(message)


            try:
                log_message = f"{func.__name__} started"
                write(log_message)

                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                write(log_message)
                return result

            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                write(log_message)
                raise

        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

# без указания файла
@log()
def another_function(a, b):
    return a * b


my_function(1, 2)
another_function(3, 4)

# с ошибкой
@log(filename="mylog.txt")
def error_function(x, y):
    return x / y


try:
    error_function(1, 0)
except Exception as e:
    print(f"Caught error: {e}")


