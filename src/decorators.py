from functools import wraps


def log(filename=None):
    def decorator(func):  # func - функция для декорирования
        @wraps(func)
        def wrapper(*args, **kwargs):
            output = open(filename, 'a') if filename else None  # открываем файл для записи логов

            log_message = f"{func.__name__} started"
            if output:
                output.write(log_message)
            else:
                print(log_message)

            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if output:
                    output.write(log_message)
                else:
                    print(log_message, end='')
                return result

            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if output:
                    output.write(log_message)
                else:
                    print(log_message, end='')
                raise

            finally:
                if output:
                    output.close()

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


