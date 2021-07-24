from telebot import*
from bs4 import*
from requests import*

bot = TeleBot('1929785033:AAEwIG2HgfKKXOayS-huMMN4eaomMEumQ7U')
i = 1
# Данные должны храниться в виде словаря: ключ - название города/области/края/республики и т.п.,
# значение - список из значений количества заболевших, умерших, выздоровевших, процента смертей от общего числа случаев,
# новых случаев и новых смертей
stat = dict()
stat_item = dict()
new_deaths = '0'
new_cases = '0'

# Получение кода страницы
url = 'https://ncov.blog/countries/ru/'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Получение кода только таблицы
body = soup.html.body
div = body.find_all('div', {'class': 'container-fluid'})[0]
table = div.table.tbody

# Получение массива, каждый элемент которого - ряд таблицы
st = table.find_all('tr')
# Перебираем все строки таблицы
for x in st:
    try:
        # Получение название города, в любой строке это одна и та же последовательность тегов
        city = x.td.span.strong.u.getText().lower()
        # Получение всех ячеек строки
        div = x.find_all('td')
        for i in range(0, len(div)):
            # Получение новых случаев и новых смертей. Новые случаи - второй тег span во втором столбце ячейке,
            # а новые смерти - второй тег span в третьем столбце
            try:
                if i == 1:
                    new_cases = div[i].find_all('span')[2].getText()
                elif i == 2:
                    new_deaths = div[i].find_all('span')[2].getText()
            except:
                pass
            # Остальные цифры находятся всегда в первом теге span любой ячейки
            div[i] = div[i].span.getText()
        div.append(new_cases)
        div.append(new_deaths)
        stat[city] = div
        new_deaths = '0'
        new_cases = '0'
    except:
        continue

print(stat)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global i
    for key in stat:
        if message.text.lower() == key:
            bot_message = 'Заболели: '+stat[key][1]+'\n'+'Умерли: '+stat[key][2]+'\n'+'Вылечились: '+stat[key][3]+'\n'+'Летальность: '+stat[key][4]+'\n'+'Новые случаи: '+stat[key][5]+'\n'+'Новые смерти: '+stat[key][6]+'\n'+'Источник:'+url+'\n'+'(Как я проверила, совпадает со статистикой Яндекса)'
            bot.send_message(message.from_user.id, bot_message)
            break
        else:
            if i == len(stat):
                bot.send_message(message.from_user.id, 'Извините, я Вас не понимаю')
            else:
                continue
        i += 1


# Запуск бота
bot.polling(none_stop=True)

# Это не используется, но я оставила как запасной вариант на случай, если сайт, откуда я беру информацию,
# переделают, и код выше перестанет работать
data = get("https://covid19.rosminzdrav.ru/wp-json/api/mapdata/").json()
