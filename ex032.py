# mode 1
from datetime import date
date = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
count = date % 4 == 0 and date % 100 != 0 or date % 400 == 0
if date == 0:
    atual_year = date.yeartoday().year
    if atual_year % 4 == 0 and atual_year % 100 != 0 or atual_year % 400 == 0:
        print('O ano {} é Bissexto.'.format(date.year))
    else:
        print('O ano {} não é Bissexto.'.format(date.year))
else:
    if count == True:
        print('O ano {} é Bissexto.'.format(date))
    else:
        print('O ano {} não é Bissexto.'.format(date))

# mode 2
from datetime import date
date = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
count = date % 4 == 0 and date % 100 != 0 or date % 400 == 0
if date == 0:
    date = date.yeartoday().year
if date % 4 == 0 and date % 100 != 0 or date % 400 == 0:
    print('O ano {} é Bissexto.'.format(date))
else:
    print('O ano {} não é Bissexto.'.format(date))