import datetime


def param_log_decorator(name_file):
    def log_decorator(old_func):
        def log_func(*args, **kwargs):
            with open(name_file, 'a', encoding='utf-8') as file_log:
                date_log = str(datetime.datetime.today())
                var_ = old_func(*args, **kwargs)
                file_log.write(f'{date_log},Имя функции: {old_func.__name__}, Входные параметры: {" ".join(args)}'
                               f' {" ".join(kwargs)}, Выходное значение: {var_}, \n')
            return var_
        return log_func
    return log_decorator


@param_log_decorator('log.txt')
def minion_game(string_):
    str_ = list(string_)
    cons = ['E', 'U', 'I', 'O', 'A']
    score1 = 0
    score2 = 0
    for i in range(len(string_)):
        if str_[i] in cons:
            score = len(string_) - i
            score1 = score1 + score
        else:
            score = len(string_) - i
            score2 = score2 + score
    if score2 > score1:
        return f'Stuart {score2}'
    elif score1 == score2:
        return f'Draw'
    else:
        return f'Kevin {score1}'


if __name__ == '__main__':
    string = 'NETOLOGY'
    minion_game(string)
