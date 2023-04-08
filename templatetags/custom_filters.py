from django import template
 
register = template.Library() 
# если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются :(

@register.filter(name='multiply') # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg): # первый аргумент здесь — это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т.е. примерно следующее будет в шаблоне value|multiply:arg
    return str(value) * arg # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон

@register.filter(name='filter_message')
def filter_message(message: str):
    variants = ['мудаков', 'твари', 'козлы', 'лошара', 'ублюдок', 'дичь'] # непристойные выражения
    ln = len(variants)
    filtred_message = ''
    string = ''
    string2 = ''
    pattern = ' ' # чем заменять непристойные выражения
    for i in message:
        string += i
        string2 = string.lower()
        
        flag = 0
        for j in variants:
            if not string2 in j:
                flag += 1
            if string2 == j:
                filtred_message += pattern
                flag -= 1
                string = ''
                
        if flag == ln:
            filtred_message += string
            string = ''
            
    if string2 != '' and string2 not in variants:
        filtred_message += string
    elif string2 != '':
        filtred_message += pattern
        
    return filtred_message