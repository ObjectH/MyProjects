from telebot import*
from bs4 import*
from requests import*

bot = TeleBot('1929785033:AAEwIG2HgfKKXOayS-huMMN4eaomMEumQ7U')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Данные должны храниться в виде словаря: ключ - название города/области/края/республики и т.п.,
    # значение - список из значений количества заболевших, умерших, выздоровевших, процента смертей от общего числа случаев,
    # новых случаев и новых смертей
    stat = dict()
    new_deaths = '0'
    new_cases = '0'
    new_heal = '0'
    new_deaths_world = '0'
    new_cases_world = '0'
    new_heal_world = '0'

    # Получение кода страницы
    url = 'https://ncov.blog/countries/ru/'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Получение кода только таблиц
    body = soup.html.body
    table_russia = body.find_all('tbody')[0]
    table_world = body.find_all('tbody')[1]

    # Обработка данных по России
    # Получение массива, каждый элемент которого - ряд таблицы
    st_russia = table_russia.find_all('tr')
    # Перебираем все строки таблицы
    for x in st_russia:
        try:
            # Получение название города, в любой строке это одна и та же последовательность тегов
            city = x.td.span.strong.u.getText().lower()
            # Получение всех ячеек строки
            div = x.find_all('td')
            for i in range(0, len(div)):
                # Получение новых случаев и новых смертей. Новые случаи - третий тег span во втором столбце,
                # новые смерти - то же самое, но в третьем столбце, новые выздоровления - в четвёртом
                try:
                    if i == 1:
                        new_cases = div[i].find_all('span')[2].getText()
                    elif i == 2:
                        new_deaths = div[i].find_all('span')[2].getText()
                    elif i == 3:
                        new_heal = div[i].find_all('span')[2].getText()
                except:
                    pass
                # Остальные цифры находятся всегда в первом теге span любой ячейки
                div[i] = div[i].span.getText()
            div.append(new_cases)
            div.append(new_deaths)
            div.append(new_heal)
            stat[city] = div
        except:
            continue
    # Обработка данных по миру
    # Получение массива, каждый элемент которого - ряд таблицы
    st_world = table_world.find_all('tr')
    # Перебираем все строки таблицы
    for x in st_world:
        try:
            # Получение название города, в любой строке это одна и та же последовательность тегов
            country = x.td.span.strong.u.getText().lower()
            # Получение всех ячеек строки
            div = x.find_all('td')
            for i in range(0, len(div)):
                # Получение новых случаев и новых смертей. Новые случаи - второй тег span во втором столбце ячейке,
                # а новые смерти - второй тег span в третьем столбце
                try:
                    if i == 1:
                        new_cases_world = div[i].find_all('span')[2].getText()
                    elif i == 2:
                        new_deaths_world = div[i].find_all('span')[2].getText()
                    elif i == 3:
                        new_heal_world = div[i].find_all('span')[2].getText()
                except:
                    pass
                # Остальные цифры находятся всегда в первом теге span любой ячейки
                div[i] = div[i].span.getText()
            div.append(new_cases_world)
            div.append(new_deaths_world)
            div.append(new_heal_world)
            stat[country] = div
        except:
            continue
    print(stat)
    # Если текст сообщения пользователя совпадает с каким-либо ключом словаря,
    # то получаем значение, которое хранится по этому кючу
    for key in stat:
        if message.text.lower() in stat:
            if message.text.lower() == key:
                bot_message = 'Заболели: '+stat[key][1]+'\n'+'Умерли: '+stat[key][2]+'\n'+'Вылечились: '+stat[key][3]+'\n'+'Летальность: '+stat[key][4]+'\n'+'Новые случаи: '+stat[key][5]+'\n'+'Новые смерти: '+stat[key][6]+'\n'+'Новые выздоровления: '+stat[key][7]+'\n'+'Источник:'+url+'\n'+'(А там данные с сайта стопкоронавирус.рф и Университета Джона Хопкинса)'
                bot.send_message(message.from_user.id, bot_message)
                break
            else:
                continue
        # У некоторых стран и регионов может быть несколько названий.
        # Собственно, следующий код обрабатывает получение названий таких мест.
        elif message.text.lower() == 'рф' or message.text.lower() == 'российская федерация':
            bot_message = 'Заболели: '+stat['россия'][1]+'\n'+'Умерли: '+stat['россия'][2]+'\n'+'Вылечились: '+stat['россия'][3]+'\n'+'Летальность: '+stat['россия'][4]+'\n'+'Новые случаи: '+stat['россия'][5]+'\n'+'Новые смерти: '+stat['россия'][6]+'\n'+'Новые выздоровления: '+stat['россия'][7]+'\n'+'Источник:'+url+'\n'+'(А там данные с сайта стопкоронавирус.рф и Университета Джона Хопкинса)'
            bot.send_message(message.from_user.id, bot_message)
            break
        elif message.text.lower() == 'америка' or message.text.lower() == 'сша' or message.text.lower() == 'соединённые штаты америки' or message.text.lower() == 'соединенные штаты америки'or message.text.lower() == 'соединённые штаты':
            bot_message = 'Заболели: '+stat['соединенные штаты'][1]+'\n'+'Умерли: '+stat['соединенные штаты'][2]+'\n'+'Вылечились: '+stat['соединенные штаты'][3]+'\n'+'Летальность: '+stat['соединенные штаты'][4]+'\n'+'Новые случаи: '+stat['соединенные штаты'][5]+'\n'+'Новые смерти: '+stat['соединенные штаты'][6]+'\n'+'Новые выздоровления: '+stat['соединенные штаты'][7]+'\n'+'Источник:'+url+'\n'+'(А там данные с сайта стопкоронавирус.рф и Университета Джона Хопкинса)'
            bot.send_message(message.from_user.id, bot_message)
            break
        elif message.text.lower() == 'кнр' or message.text.lower() == 'китайская народная республика':
            bot_message = 'Заболели: '+stat['китай'][1]+'\n'+'Умерли: '+stat['китай'][2]+'\n'+'Вылечились: '+stat['китай'][3]+'\n'+'Летальность: '+stat['китай'][4]+'\n'+'Новые случаи: '+stat['китай'][5]+'\n'+'Новые смерти: '+stat['китай'][6]+'\n'+'Новые выздоровления: '+stat['китай'][7]+'\n'+'Источник:'+url+'\n'+'(А там данные с сайта стопкоронавирус.рф и Университета Джона Хопкинса)'
            bot.send_message(message.from_user.id, bot_message)
            break
        elif message.text.lower() == 'британия' or message.text.lower() == 'великобритания' or message.text.lower() == 'соединённое королевство':
            bot_message = 'Заболели: '+stat['соединенное королевство'][1]+'\n'+'Умерли: '+stat['соединенное королевство'][2]+'\n'+'Вылечились: '+stat['соединенное королевство'][3]+'\n'+'Летальность: '+stat['соединенное королевство'][4]+'\n'+'Новые случаи: '+stat['соединенное королевство'][5]+'\n'+'Новые смерти: '+stat['соединенное королевство'][6]+'\n'+'Новые выздоровления: '+stat['соединенное королевство'][7]+'\n'+'Источник:'+url+'\n'+'(А там данные с сайта стопкоронавирус.рф и Университета Джона Хопкинса)'
            bot.send_message(message.from_user.id, bot_message)
            break
        elif message.text.lower() == 'якутия' or message.text.lower() == 'республика саха':
            bot_message = 'Заболели: '+stat['республика саха (якутия)'][1]+'\n'+'Умерли: '+stat['республика саха (якутия)'][2]+'\n'+'Вылечились: '+stat['республика саха (якутия)'][3]+'\n'+'Летальность: '+stat['республика саха (якутия)'][4]+'\n'+'Новые случаи: '+stat['республика саха (якутия)'][5]+'\n'+'Новые смерти: '+stat['республика саха (якутия)'][6]+'\n'+'Новые выздоровления: '+stat['республика саха (якутия)'][7]+'\n'+'Источник:'+url+'\n'+'(А там данные с сайта стопкоронавирус.рф и Университета Джона Хопкинса)'
            bot.send_message(message.from_user.id, bot_message)
            break
        elif message.text.lower() == 'северная осетия' or message.text.lower() == 'алания' or message.text.lower() == 'республика северная осетия' or message.text.lower() == 'республика алания':
            bot_message = 'Заболели: '+stat['республика северная осетия — алания'][1]+'\n'+'Умерли: '+stat['республика северная осетия — алания'][2]+'\n'+'Вылечились: '+stat['республика северная осетия — алания'][3]+'\n'+'Летальность: '+stat['республика северная осетия — алания'][4]+'\n'+'Новые случаи: '+stat['республика северная осетия — алания'][5]+'\n'+'Новые смерти: '+stat['республика северная осетия — алания'][6]+'\n'+'Новые выздоровления: '+stat['республика северная осетия — алания'][7]+'\n'+'Источник:'+url+'\n'+'(А там данные с сайта стопкоронавирус.рф и Университета Джона Хопкинса)'
            bot.send_message(message.from_user.id, bot_message)
            break
        elif message.text.lower() == 'северная корея' or message.text.lower() == 'кндр' or message.text.lower() == 'корейская народная демократическая республика':
            bot.send_message(message.from_user.id, 'Северная Корея официально не подтвердила ни одного случая заболевания коронавирусом')
            break
        elif message.text.lower() == 'еврейская ао':
            bot_message = 'Заболели: '+stat['еврейская автономная область'][1]+'\n'+'Умерли: '+stat['еврейская автономная область'][2]+'\n'+'Вылечились: '+stat['еврейская автономная область'][3]+'\n'+'Летальность: '+stat['еврейская автономная область'][4]+'\n'+'Новые случаи: '+stat['еврейская автономная область'][5]+'\n'+'Новые смерти: '+stat['еврейская автономная область'][6]+'\n'+'Новые выздоровления: '+stat['еврейская автономная область'][7]+'\n'+'Источник:'+url+'\n'+'(А там данные с сайта стопкоронавирус.рф и Университета Джона Хопкинса)'
            bot.send_message(message.from_user.id, bot_message)
            break
        elif message.text.lower() == 'ненецкий ао':
            bot_message = 'Заболели: '+stat['ненецкий автономный округ'][1]+'\n'+'Умерли: '+stat['ненецкий автономный округ'][2]+'\n'+'Вылечились: '+stat['ненецкий автономный округ'][3]+'\n'+'Летальность: '+stat['ненецкий автономный округ'][4]+'\n'+'Новые случаи: '+stat['ненецкий автономный округ'][5]+'\n'+'Новые смерти: '+stat['ненецкий автономный округ'][6]+'\n'+'Новые выздоровления: '+stat['ненецкий автономный округ'][7]+'\n'+'Источник:'+url+'\n'+'(А там данные с сайта стопкоронавирус.рф и Университета Джона Хопкинса)'
            bot.send_message(message.from_user.id, bot_message)
            break
        elif message.text.lower() == 'ханты-мансийский ао':
            bot_message = 'Заболели: '+stat['ханты-мансийский автономный округ'][1]+'\n'+'Умерли: '+stat['ханты-мансийский автономный округ'][2]+'\n'+'Вылечились: '+stat['ханты-мансийский автономный округ'][3]+'\n'+'Летальность: '+stat['ханты-мансийский автономный округ'][4]+'\n'+'Новые случаи: '+stat['ханты-мансийский автономный округ'][5]+'\n'+'Новые смерти: '+stat['ханты-мансийский автономный округ'][6]+'\n'+'Новые выздоровления: '+stat['ханты-мансийский автономный округ'][7]+'\n'+'Источник:'+url+'\n'+'(А там данные с сайта стопкоронавирус.рф и Университета Джона Хопкинса)'
            bot.send_message(message.from_user.id, bot_message)
            break
        elif message.text.lower() == 'чукотский ао':
            bot_message = 'Заболели: '+stat['чукотский автономный округ'][1]+'\n'+'Умерли: '+stat['чукотский автономный округ'][2]+'\n'+'Вылечились: '+stat['чукотский автономный округ'][3]+'\n'+'Летальность: '+stat['чукотский автономный округ'][4]+'\n'+'Новые случаи: '+stat['чукотский автономный округ'][5]+'\n'+'Новые смерти: '+stat['чукотский автономный округ'][6]+'\n'+'Новые выздоровления: '+stat['чукотский автономный округ'][7]+'\n'+'Источник:'+url+'\n'+'(А там данные с сайта стопкоронавирус.рф и Университета Джона Хопкинса)'
            bot.send_message(message.from_user.id, bot_message)
            break
        elif message.text == '/help':
            bot.send_message(message.from_user.id, 'Если в названии региона есть слово "республика", то надо его написать. Так же попробуйте написать "е" вместо "ё". Названия регионов со словом "республика" могут быть в форматах "n-ая республика" или "республика n". Можете попробовать поменять формат.')
            break
        else:
            bot.send_message(message.from_user.id, 'Извините, я Вас не понимаю. Если Вы уверены, что правильно написали название страны/региона, напишите /help')
            break

# Запуск бота
bot.polling(none_stop=True)

# Это не используется, но я оставила как запасной вариант на случай, если сайт, откуда я беру информацию,
# переделают, и код выше перестанет работать
data = get("https://covid19.rosminzdrav.ru/wp-json/api/mapdata/").json()
