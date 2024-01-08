import telebot # pip install pyTelegramBotAPI
from info.material_help import *
from info.student_union import *
from info.scholarship import *
from start import keep_alive

from telebot import types

token = '6745756211:AAFzxf7bBKsgQlFARmceZ2QC3VyQJT5sR_w'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Поселение')
    btn2 = types.KeyboardButton('Мат. помощь')
    btn3 = types.KeyboardButton('Стипендии')
    btn4 = types.KeyboardButton('Профсоюз')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    #file = open('./images/start.png', 'rb')
    #bot.send_photo(message.chat.id, photo=file, reply_markup=markup)
    text = 'Теперь выбери в меню необходимую категорию👇🏻'
    try:
        bot.send_message(message.chat.id, text=text, parse_mode='Markdown', reply_markup=markup)
    except:
        pass


@bot.message_handler(content_types=['text'])
def main(message):
    try:
        if message.text == 'Мат. помощь':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Бюджет')
            btn2 = types.KeyboardButton('Контракт')
            btn_back = types.KeyboardButton('Назад')
            file = open('./images/start_matirial_help.png', 'rb')
            markup.row(btn1, btn2, btn_back)
            bot.send_photo(message.chat.id, photo=file, reply_markup=markup)


        if message.text.lower() == 'бюджет':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Профбюро института')
            btn2 = types.KeyboardButton('Профком (ГУК-309)')
            btn_back = types.KeyboardButton('Назад')
            markup.add(btn1, btn2, btn_back)
            bot.send_message(message.chat.id, text="Выбери куда хочешь подать на матпомощь", reply_markup=markup)

        if message.text == "Профбюро института":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_back = types.KeyboardButton('Назад')
            for i in range(len(questions_PB_budget)):
                markup.add(questions_PB_budget[i])
            markup.add(btn_back)
            bot.send_message(message.chat.id, text="Выберете вопрос", reply_markup=markup, parse_mode='HTML')

        if message.text in questions_PB_budget:
            answerIndex = questions_PB_budget.index(message.text)
            if 'ответ картинкой' in answers_PB_budget[answerIndex]:
                ans = answers_PB_budget[answerIndex]
                file = open('./images/' + str(ans[16:]) + '.png', 'rb')
                bot.send_photo(message.chat.id, photo=file)
            else:
                bot.send_message(message.chat.id, text=str(answers_PB_budget[answerIndex]))

        if message.text == 'Как подать заявление в профбюро интситута?':
            file = open('./images/material_help_img.png', 'rb')
            bot.send_photo(message.chat.id, photo=file)



        if message.text == "Профком (ГУК-309)":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_back = types.KeyboardButton('Назад')
            for i in range(len(questions_POS_budget)):
                markup.add(questions_POS_budget[i])
            markup.add(btn_back)
            bot.send_message(message.chat.id, text="Выберете вопрос", reply_markup=markup)

        if message.text in questions_POS_budget:
            answerIndex = questions_POS_budget.index(message.text)
            if 'ответ картинкой' in answers_POS_budget[answerIndex]:
                ans = answers_POS_budget[answerIndex]
                file = open('./images/' + str(ans[16:]) + '.png', 'rb')
                bot.send_photo(message.chat.id, photo=file)
            else:
                bot.send_message(message.chat.id, text=str(answers_POS_budget[answerIndex]), parse_mode='Markdown', disable_web_page_preview=True)

        if message.text.lower() == 'контракт':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_back = types.KeyboardButton('Назад')
            for i in range(len(questions_POS_contract)):
                markup.add(questions_POS_contract[i])
            markup.add(btn_back)
            bot.send_message(message.chat.id,
                             text="Выберете вопрос",
                             reply_markup=markup)

        if message.text in questions_POS_contract:
            answerIndex = questions_POS_contract.index(message.text)
            if 'ответ картинкой' in answers_POS_contract[answerIndex]:
                ans = answers_POS_contract[answerIndex]
                file = open('./images/' + str(ans[16:]) + '.png', 'rb')
                bot.send_photo(message.chat.id, photo=file)
            else:
                bot.send_message(message.chat.id, text=str(answers_POS_contract[answerIndex]))






        if message.text == "Стипендии":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for _ in questions_scolarship:
                btn = types.KeyboardButton(_)
                markup.add(btn)
            btn2 = types.KeyboardButton('Государственная социальная стипендия')
            btn_back = types.KeyboardButton('Назад')
            markup.add(btn2)
            markup.add(btn_back)

            bot.send_message(message.chat.id, text='Выберете раздел', reply_markup=markup)

        if message.text == "Государственная социальная стипендия":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Категории студентов, которые могут получать социальную стипендию')
            btn2 = types.KeyboardButton('Условия назначения')
            btn3 = types.KeyboardButton('Размер социальной стипендии')
            btn4 = types.KeyboardButton('Повышенная социальная стипендия')
            btn5 = types.KeyboardButton('Как оформить государственную социальную помощь?')
            btn_back = types.KeyboardButton('Назад')
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn4)
            markup.add(btn5)
            markup.add(btn_back)
            bot.send_message(message.chat.id, text="Выбери категорию", reply_markup=markup)


        if message.text == 'Повышенная социальная стипендия':
            text = 'Назначается только студентам 1-2 курсов, имеющим оценки успеваемости «отлично», «хорошо», «хорошо» и «отлично».\n' \
                   '\n' \
                   'В случае, если повышенный размер выплаты не был назначен автоматически, следует обратиться в ГУК-403.'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)

        if message.text == "Повышенная государственная академическая стипендия":
            text = 'Назначается за достижения в учебной, научно-исследовательской деятельности, ' \
                   'общественной, культурно-творческой и спортивной деятельности.\n' \
                   '\n' \
                   'Подробнее о получении каждой стипендии можно узнать на [сайте](https://urfu.ru/ru/students/study/scholarships/).'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)

        if message.text in questions_scolarship:
            answerIndex = questions_scolarship.index(message.text)
            if 'ответ картинкой' in answers_scolarship[answerIndex]:
                ans = answers_scolarship[answerIndex]
                file = open('./images/' + str(ans[16:]) + '.png', 'rb')
                bot.send_photo(message.chat.id, photo=file)
            else:
                bot.send_message(message.chat.id, parse_mode='Markdown', text=str(answers_scolarship[answerIndex]))
        if message.text == "Как оформить государственную социальную помощь?":
            text = 'Студенты, имеющие основание для получения государственной социальной помощи, ' \
                   'могут оформить заявление в отделах социальной защиты по месту жительства или в МФЦ и получить соответствующую справку.\n' \
                   '\n' \
                   'Для оформления потребуется ряд документов:\n' \
                   '— справка о доходах за 3 последних календарных месяца, предшествующих месяцу подачи заявления;\n' \
                   '— справка с места жительства;\n' \
                   '— справка об обучении;\n' \
                   '— реквизиты банковской карты;\n' \
                   '— СНИЛС;\n' \
                   '— копия паспорта.\n' \
                   '\n' \
                   'С собранными документами студенту необходимо обратиться в МФЦ и оформить запрос. ' \
                   'В случае одобрения справку о получении государственной социальной помощи необходимо отнести в ГУК-403 до 10 числа месяца.\n' \
                   'Срок действия справки – 1 календарный год.'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)

        if message.text == "Категории студентов, которые могут получать социальную стипендию":
            file = open('./images/social_scolarship.png', 'rb')
            bot.send_photo(message.chat.id, photo=file)


        if message.text == "Условия назначения":
            text = '— стипендия назначается независимо от наличия государственной академической стипендии;\n' \
                    '\n' \
                   '— назначается со дня предоставления в ГУК-403 подтверждающего документа;\n' \
                   '\n' \
                   '— в случае, если документ, подтверждающий основание, является бессрочным, ' \
                   'социальная стипендия назначается до окончания обучения;\n' \
                   '\n' \
                   '— студентам, получившим государственную социальную помощь, социальная стипендия назначается ' \
                   'со дня предоставления соответствующей справки на один год со дня назначения государственной социальной помощи.'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)

        if message.text == 'Размер социальной стипендии':
            text = '2985,8 руб. – базовый размер социальной стипендии.\n'\
            '6585 руб. – повышенная государственная социальная стипендия.\n'\
            '*без учета районного коэффициента.\n'\
            '\n'\
            'Повышенная государственная социальная стипендия назначается студентам 1 и 2 курса, '\
            'имеющим оценки успеваемости «отлично», «хорошо», «хорошо» и «отлично».'
            bot.send_message(message.chat.id, text=text)






        if message.text == "Поселение":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('поселение')
            btn2 = types.KeyboardButton('переселение')
            btn3 = types.KeyboardButton('контактная информация')
            btn4 = types.KeyboardButton('памятка поселения')
            btn5 = types.KeyboardButton('правила проживания в общежитии')
            btn6 = types.KeyboardButton('компенсация за ремонт в комнате')
            btn7 = types.KeyboardButton('стоимость общежития')
            btn8 = types.KeyboardButton('оплата общежития')
            btn9 = types.KeyboardButton('порядок восстановления пропуска')
            btn10 = types.KeyboardButton('возврат обеспечительного платежа')
            btn_back = types.KeyboardButton('назад')
            markup.add(btn1);
            markup.add(btn2)
            markup.add(btn3);
            markup.add(btn4)
            markup.add(btn5);
            markup.add(btn6)
            markup.add(btn7);
            markup.add(btn8)
            markup.add(btn9);
            markup.add(btn10)
            markup.add(btn_back)
            bot.send_message(message.chat.id, text='Выберете раздел', reply_markup=markup, disable_web_page_preview=True)

        if message.text == 'поселение':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Для граждан РФ и ближнего зарубежья')
            btn2 = types.KeyboardButton('Граждане ближнего зарубежья, обучающиеся по квоте МОН и граждане дальнего зарубежья')
            btn3 = types.KeyboardButton('Семейные обучающиеся')
            btn_back = types.KeyboardButton('Назад')
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn_back)
            bot.send_message(message.chat.id, text='Выберете раздел', reply_markup=markup, disable_web_page_preview=True)

    #    if message.text == '':
        if message.text == 'памятка поселения':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Граждане РФ')
            btn2 = types.KeyboardButton('Граждане ближнего зарубежья по квоте МОН и дальнего зарубежья')
            btn_back = types.KeyboardButton('Назад')
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn_back)
            bot.send_message(message.chat.id, text='Выберете раздел', reply_markup=markup, disable_web_page_preview=True)

        if message.text == 'Граждане РФ':
            file1 = open('./images/accommodation_in_hostel_for_Russian_citizens_1.png', 'rb')
            file2 = open('./images/accommodation_in_hostel_for_Russian_citizens_2.png', 'rb')
            bot.send_photo(message.chat.id, photo=file1)
            bot.send_photo(message.chat.id, photo=file2)

        if message.text == 'правила проживания в общежитии':
            text = 'С правилами внутреннего распорядка можете ознакомиться ' \
                   'пройдя по [ссылке](https://vk.com/doc265355641_567722400?hash=7363b012c60df98fd4&dl=5e6fb6ca3b1cf0404c).'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)


        if message.text == 'компенсация за ремонт в комнате':
            text = 'Ознакомиться с информацией о компенсации денежных средств ' \
                   'за ремонт можно перейдя по [ссылке](https://vk.com/ossg.urfu?w=wall-191626771_2122).'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)

        if message.text == 'стоимость общежития':
            text = 'С информацией о размере платы за проживание в студенческих ' \
                   'общежитиях УрФУ можно ознакомиться по [ссылке](https://vk.com/doc172382045_672537884).'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)

        if message.text == 'оплата общежития':
            text = 'Информацию о начислениях и задолженностях можно найти в личном кабинете студента:\n' \
                   'Документы и финансы > Финансовые сервисы > Информация о задолженности за пользование жилым помещением и коммунальные услуги\n\n' \
                   'ИЛИ\n\n' \
                   'Документы и финансы > Платежи и задолженности' \
                   'Совершить оплату можно несколькими способами: \n' \
                   '1.	Через [«Платежи УрФУ»](https://pay.urfu.ru/) \n' \
                   '2.	В отделениях: Синара банка и Сбер банка \n' \
                   '3.	В приложении вашего банка, используя код оплаты (указан на ордере).'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)

        if message.text == 'порядок восстановления пропуска':
            text = '[Порядок восстановления пропуска](https://vk.com/doc265355641_567722308?hash=bd86e768f8eb7d8e61&dl=5d60e09592619f1f8b)'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)

        if message.text == 'возврат обеспечительного платежа':
            text = 'Документы, необходимые для возврата обеспечительного платежа:\n' \
                   '\n' \
                   '1. Копия или оригинал договора обеспечительного платежа;\n' \
                   '2. Банковские реквизиты;\n' \
                   '3. Заявление, подписанное по адресу: ул. Коминтерна, 11 (паспортный отдел) или ул. С. Ковалевской, 5, каб. Т123а;\n' \
                   '4. Для иностранных студентов – копию паспорта.\n' \
                   '\n' \
                   '📌 Заявление на возврат обеспечительного платежа необходимо отдать в бухгалтерию по адресу: ' \
                   'ул. Ленина, 51, каб. 108 или ул. Мира, 19, каб. М-230.\n' \
                   '\n' \
                   '📌 Обращаем ваше внимание, что заявление будет подписано только при наличии справки, ' \
                   'полученной в администрации общежития о сдаче имущества. Справка выдаётся тем, кто уже выселился из общежития.\n' \
                   '\n' \
                   '📌 Также обеспечительный платёж учитывается обособленно и не является платой за услугу. ' \
                   'Чек на сумму обеспечительного платежа не формируется\\*\n' \
                   '\n' \
                   '\\* В случаях, когда из обеспечительного платежа удерживается сумма в счет ' \
                   'возмещения нанесенного вреда имуществу или возмещения задолженности за проживание ' \
                   'в общежитии, на сумму удержания формируется чек и выдается плательщику.\n' \
                   '\n' \
                   'Сумма обеспечительного платежа, оставшаяся после удержания в счет возмещения ' \
                   'нанесенного вреда имуществу или возмещения задолженности за проживание в общежитии, подлежит возврату плательщику.\n' \
                   '\n' \
                   '[Бланк заявления](https://vk.com/s/v1/doc/CxIxgXtKXUnw7uLL8Smpz4DwqDbz27JL_824etq_6-1j2VWsZ0o)'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)


        if message.text == 'Граждане ближнего зарубежья по квоте МОН и дальнего зарубежья':
            text = 'Необходимую информацию вы можете найти в [группе Вконтакте](https://vk.com/adaptationurfu).'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)


        if message.text == 'Для граждан РФ и ближнего зарубежья':
            text = 'Абитуриентам: при формировании заявления на поступление поставить галочку о необходимости получения общежития. ' \
                   'Дальнейшую информацию ждите от жилищно-бытовой комиссии вашего института ' \
                   'или в соответствующей группе Вконтакте. По всем вопросам можете обращаться к ответственному ' \
                   'за поселение сотруднику или заместителю жилищно-бытовой комиссии института. \n' \
                   '\n' \
                   'Студентам: по вопросам поселения старших курсов необходимо обратиться в жилищную комиссию вашего института.\n' \
                   '\n' \
                   '[Контакты ответственных за поселение](https://urfu.ru/ru/students/social/campus/contacts/)'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)


        if message.text == 'Граждане ближнего зарубежья, обучающиеся по квоте МОН и граждане дальнего зарубежья':
            text = 'Абитуриентам: при формировании заявления на поступление поставить галочку о необходимости получения общежития. ' \
                   'Дальнейшую информацию ждите информацию от центра адаптации иностранных обучающихся ' \
                   'в соответствующей группе Вконтакте. По всем вопросам можете обращаться в Центр адаптации иностранных обучающихся.\n' \
                   '\n' \
                   'Студентам: по вопросам поселения старших курсов необходимо обратиться в Центр адаптации иностранных обучающихся.\n' \
                   '\n' \
                   'Citizens of neighboring countries studying under the quota of the Ministry of Education and Science and citizens of Far Abroad countries"\n' \
                   '' \
                   'For applicants: you must check the box indicating the need to receive dormitories. Wait for further information from your institute’s housing and communal services commission in the corresponding Vcontact group. For any questions, please contact the Center for Adaptation of Foreign Students.' \
                   'Students: regarding accommodation of senior students, please contact the Center for Adaptation of Foreign Students.\n' \
                   '\n' \
                    '根据教育、科学及文化部配额就读的近国公民和远国公民\n' \
                    '申请者： 您必须在需要宿舍住宿的方框内打勾。\n' \
                    '您所在学院的住房-生活委员会将在 VK上的相应群组中提供更多信息。 如果您有任何疑问，请联系外国学生适应中心。\n' \
                    '学生：关于住宿问题，高年级学生请联系外国学生适应中心。\n' \
                   '\n' \
                   "مواطنو الدول المجاورة الذين يدرسون بموجب حصة وزارة التعليم والعلوم ومواطني الدول البعيدة"\
            'للمتقدمين: يجب'\
            'وضع'\
            'علامة'\
            'في'\
            'المربع'\
            'الذي'\
            'يشير'\
            'إلى'\
            'ضرورة'\
            'الاستلام'\
            'المهاجع'\
            '.انتظر'\
            'المزيد'\
            'من'\
            'المعلومات'\
            'من'\
            'لجنة'\
            'الإسكان'\
            'في'\
            'معهدك'\
            'في'\
            'مجموعة'\
            'في'\
            'كي'\
            '(vk)'\
            'المقابلة'\
            '.'\
            'لأية'\
            'أسئلة'\
            '،'\
            'يرجى'\
            'الاتصال'\
            'بمركز'\
            'تكيف'\
            'الطلاب'\
            'الأجانب'\
            '.'\
            'الطلاب'\
                ':' \
            'فيما'\
            'يتعلق'\
            'بسكن'\
            'الطلاب'\
            'الكبار'\
            '،'\
            'يرجى'\
            'الاتصال'\
            'بمركز'\
            'تكيف'\
            'الطلاب'\
            'الأجانب'\
            '.\n' \
            '\n' \
            '[Контакты Центра адаптации иностранных обучающихся](https://vk.com/adaptationurfu)'\

            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)


        if message.text == 'Семейные обучающиеся':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Граждане РФ и граждане ближнего зарубежья')
            btn2 = types.KeyboardButton('Граждане дальнего зарубежья')
            btn_back = types.KeyboardButton('Назад');
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn_back)
            bot.send_message(message.chat.id, text='Выберете раздел', reply_markup=markup, disable_web_page_preview=True)

        if message.text == 'Граждане РФ и граждане ближнего зарубежья':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            text = 'Семейные студенты, *имеющие гражданство РФ* могут получить место в общежитии в том случае, если хотя бы один член семьи является обучающимся УрФУ.\n' \
                   'Семейные студенты, *имеющие гражданство ближнего* зарубежья могут получить место в общежитии только в том случае, если все члены семьи  являются студентами УрФУ.\n' \
                   'Пакет документов должен в себя включать:\n' \
                   '— Заявление на поселение;\n' \
                   '— Сканы паспорта всех членов семьи (всех заполненных страниц);\n' \
                   '— Сканы справок об обучении/с места работы всех членов семья;\n' \
                   '— Скан свидетельства о рождении ребенка (при наличии);\n' \
                   '— Скан свидетельства о заключении брака;\n' \
                   '— Фото 3\\*4 всех членов семьи;\n' \
                   '— Документы подтверждающие социально-льготный статус (при наличии);\n' \
                   '— Скан медицинской страховки всех членов семьи (для иностранных обучающихся);\n' \
                   '— Скан миграционной карты всех членов семьи (для иностранных обучающихся);\n' \
                   '— Документы на поселение семейных студентов необходимо направить на почту familystudents@yandex.ru.\n' \
                   '\n' \
                   '[Группа Вконтакте](https://vk.com/familyurfu).'
            bot.send_message(message.chat.id, text=text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)


        if message.text == 'Граждане дальнего зарубежья':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            text = 'Для получения информации, необходимо обратиться ' \
                   'в [Центр адаптации иностранных обучающихся](https://vk.com/adaptationurfu), кабинет И-110.'
            bot.send_message(message.chat.id, text=text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

        if message.text == 'переселение':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            text = 'Для переселения, необходимо взять заявление в жилищной комиссии своего института и заполнить его. ' \
                   'В случае, если происходит обмен мест между несколькими проживающими, ' \
                   'то необходимы заявления от всех проживающих, участвующих в обмене.  ' \
                   'На каждом заявлении на переселение должна быть резолюция начальника УЭИКиТ ' \
                   '(ул. Коминтерна, 11 пн-пт с 9:00 до 16:00, перерыв с 12:00 до 13:00) ' \
                   'и всех студентов, проживающих в комнатах, которые участвуют обмене.\n' \
                   '\n' \
                   '[Контакты ответственных за поселение](https://urfu.ru/ru/students/social/campus/contacts/).'
            bot.send_message(message.chat.id, text=text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

        if message.text == 'контактная информация':
            text = '*Жилищно-бытовое направление Союза студентов:*\n' \
                   'ИЕНиМ - [Спиридонова Наталья](https://vk.com/osquije), [группа](https://vk.com/poselenie\\_ien\\_urfu)\n' \
                   'ИНМТ - [Малкова Евгения](https://vk.com/jeshhhh), [группа](https://vk.com/poselinmt)\n' \
                   'УГИ - [Ипулаева Элина](https://vk.com/elinameoww), [группа](https://vk.com/urgi_hostel)\n' \
                   'УралЭНИН - [Скульбида Дарья](https://vk.com/daaririii), [группа](https://vk.com/uralei)\n' \
                   'ХТИ - [Перова Юлия](https://vk.com/yulya_prv), [группа](https://vk.com/hti_urfu)\n' \
                   'ФТИ - [Дербенёва Ксения](https://vk.com/xenon532), [группа](https://vk.com/profburo_fti)\n' \
                   'ИРИТ-РТФ - [Ковтонюк Полина](https://vk.com/kovtpolly), [группа](https://vk.com/irit_rtf)\n' \
                   'ИФКСиМП - [Окорокова Полина](https://vk.com/lina_ppppp), [группа](https://vk.com/poselenifksimp)\n' \
                   'ИнЭУ - [Лескова Анна](https://vk.com/m0ndoro), [группа](https://vk.com/poselenie_ineu)\n' \
                   'УПИШ - [Семенова Екатерина](https://vk.com/sssemenka), [группа](https://vk.com/upish_urfu)\n' \
                   '\n' \
                   'Проектный офис «Платное Жильё» - Зверев Михаил Вячеславович (+7 (999) 559-61-12, mail@studentrealty.ru)\n' \
                   '\n' \
                   '*Другие подразделения университета*\n' \
                   '\n' \
                   '*Объединенный совет студенческого городка:*\n' \
                   'Председатель ОССГ - [Наугольных Валерия](https://vk.com/lerahas_264)\n' \
                   'Студенческий корпус №1 - [Ботина Анастасия](https://vk.com/idanastasia_botina)\n' \
                   'Студенческий корпус №2 - [Вишнякова Анастасия](https://vk.com/id422991339)\n' \
                   'Студенческий корпус №3 - [Базуева Екатерина](https://vk.com/kowbaska_iz_koteyki)\n' \
                   'Студенческий корпус №4 - [Чибирова Анна](https://vk.com/annachibo)\n' \
                   'Студенческий корпус №5 - [Зюбенко Артем](https://vk.com/zyubenkin)\n' \
                   'Студенческий корпус №6 - [Харрасов Даниил](https://vk.com/ennoootttt)\n' \
                   'Студенческий корпус №7 - [Коновалов Степан](https://vk.com/konovalovst1)\n' \
                   'Студенческий корпус №8 - [Шамарин Александр](https://vk.com/alex.wrestler)\n' \
                   'Студенческий корпус №9 - [Насибов Фариз](https://vk.com/ntfriz)\n' \
                   'Студенческий корпус №10 - [Одышева Александра](https://vk.com/odik004)\n' \
                   'Студенческий корпус №11 - [Булатов Иван](https://vk.com/id149102317)\n' \
                   'Студенческий корпус №12 - [Сарымамед Рамзан](https://vk.com/adeptque)\n' \
                   'Студенческий корпус №13 - [Наговицына Ульяна](https://vk.com/ulyana_nagovitsyna)\n' \
                   'Студенческий корпус №14 - [Сергеев Антон](https://vk.com/nedostoevski)\n ' \
                   '\n' \
                   '*Общежития УрФУ:* \n' \
                   '[Студенческий корпус №1](https://vk.com/urfuone)\n' \
                   '[Студенческий корпус №2](https://vk.com/urfu_ssk_2)\n' \
                   '[Студенческий корпус №3](https://vk.com/urfu_3sk)\n' \
                   '[Студенческий корпус №4](https://vk.com/sk4_urfu)\n' \
                   '[Студенческий корпус №5](https://vk.com/sk5_urfu)\n' \
                   '[Студенческий корпус №6](https://vk.com/hostel_urfu_6)\n' \
                   '[Студенческий корпус №7](https://vk.com/7sstudkorpus)\n' \
                   '[Студенческий корпус №8](https://vk.com/8sk_urfu)\n' \
                   '[Студенческий корпус №9](https://vk.com/urfu9sk)\n' \
                   '[Студенческий корпус №10](https://vk.com/cck10)\n' \
                   '[Студенческий корпус №11](https://vk.com/urfu11)\n' \
                   '[Студенческий корпус №12](https://vk.com/sk12_urfu)\n' \
                   '[Студенческий корпус №13](https://vk.com/urfu_13sk)\n' \
                   '[Студенческий корпус №14](https://vk.com/ssk14)\n' \
                   '[Кампус Новокольцовский](https://vk.com/urfu_nk)\n' \
                   '\n' \
                   '*Заместители директоров институтов, ответственные за поселение:*\n' \
                   'ИЕНиМ - Фалько Наталья Васильевна (+7 (343) 389-95-96, n.v.falko@urfu.ru); Неугодникова Елизавета Алексеевна (+7 (343) 389-95-96, e.a.neugodnikova@urfu.ru)\n' \
                   'ИнЭУ - Горбунова Галина Анатольевна (+7 (912) 208-14-26, Galina.Gorbunova@urfu.ru)\n' \
                   'ИНМТ - Еланцев Алексей Владимирович (+7 (912) 635 52 97, a.v.elantcev@urfu.ru)\n' \
                   'ИРИТ-РтФ - Курочкина Марина Сергеевна (+7 (343) 375-48-99, m.s.kurochkina@urfu.ru)\n' \
                   'ИСА - Андреева Мария Андреевна (+7 (343) 374-59-82, +7 (343) 375-44-70, m.a.kochneva@urfu.ru)\n' \
                   'ИТОО - Тюкалова Наталья Валерьевна (+7 (343) 375-47-54, n.v.tille@urfu.ru)\n' \
                   'ИФКСиМП - Панова Наталья Анатольевна (+7 (900) 045-98-94, n.a.panova@urfu.ru)\n' \
                   'ИНФО - Данилова Анна Андреевна (+7 (343) 375-45-34, a.a.danilova@urfu.ru)\n' \
                   'УГИ - Гречухина Татьяна Ивановна (+7 (343) 389-97-82, grechuhinati@yandex.ru)\n' \
                   'УПИШ - Балясов Александр Анатольевич (+7 (343) 375-93-76, a.a.balyasov@urfu.ru)\n' \
                   'УралЭНИН - Вдовина Ольга Игоревна (+7 (343) 375-46-29, o.i.vdovina@urfu.ru)\n' \
                   'ФТИ - Наугольных Валерия Егоровна (+7 (982) 625-65-34, V.e.naugolnykh@urfu.ru)\n' \
                   'ХТИ - Шатунова Дарья Викторовна (+7 (343) 375-93-78, d.v.shatunova@urfu.ru)\n' \
                   '\n' \
                   '*Другие подразделения университета:*\n' \
                   'УРСП - Наугольных Валерия Егоровна (+7 (982) 625-65-34, V.e.naugolnykh@urfu.ru), Спиридонова Ирина (i.s.spiridonova@urfu.ru +7 (343) 375-97-18)\n' \
                   'Медико-санитарная часть УрФУ (регистратура) - +7 (343) 375-94-77\n' \
                   '[Центр адаптации иностранных обучющихся](https://vk.com/adaptationurfu) ' \
                   '- Буянов Никита Александрович (+7 (343) 375-41-93, n.a.buyanov@urfu.ru), кабинет И-110\n' \
                   'Центр инклюзивного образования - Рудакова Наталья Дмитриевна (+7 (343) 375-94-30, n.d.petriakova@urfu.ru)'

            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)





        if message.text == "Профсоюз":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Что такое профсоюз')
            btn2 = types.KeyboardButton('Союз студентов УрФУ и его плюшки')
            btn3 = types.KeyboardButton('Бонусные программы Profcards и СКС Бонус')
            btn4 = types.KeyboardButton('Как вступить в профсоюз')
            btn_back = types.KeyboardButton('Назад')
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn4)
            markup.add(btn_back)
            bot.send_message(message.chat.id, text='Выберете раздел', reply_markup=markup, disable_web_page_preview=True)

        if message.text == 'Что такое профсоюз':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            text = f'📌 На сложном: профсоюз – добровольное общественное объединение граждан, ' \
                   f'связанных общими производственными, профессиональными интересами по роду их деятельности, ' \
                   f'создаваемое в целях представительства и защиты их социально-трудовых прав и интересов.\n' \
                   f'\n' \
                   f'📌 На простом: профсоюз – самый распространенный способ извлечь максимум выгоды, скидок, ' \
                   f'«плюшек» из своего студенчества. Для этого достаточно быть членом профсоюза ' \
                   f'и быть знакомым со всеми преимуществами членства в нем, чтобы грамотно их использовать. \n' \
                   f'\n' \
                   f'📌 Профсоюз (Союз студентов) обеспечит досуг и будет способствовать вашему всестороннему развитию. ' \
                   f'Самое главное: на протяжении всего студенчества профсоюз будет неизменно защищать ваши права и интересы, ' \
                   f'помогать в реализации планов. Если произошла ситуация, нарушающая ваши права, ' \
                   f'или у вас есть идея для развития университета – обращайтесь в Союз студентов. \n' \
                   f'\n' \
                   f'📌 Быть членом профсоюза ' \
                   f'= иметь профсоюзный билет (профсоюзник)  ' \
                   f'= получать максимум «плюшек» (использование скидок, акций, предложений) ' \
                   f'+ (опционально) посещать (или даже организовывать) мероприятия института или университета ' \
                   f'+ иметь возможность развиваться самому и развивать университет ' \
                   f'+ знать, куда обратиться за помощью при необходимости или в случае нарушения прав ' \
                   f'= находиться в комфортной и безопасной среде. '
            bot.send_message(message.chat.id, text=text, reply_markup=markup)

        if message.text == "Союз студентов УрФУ и его плюшки":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            text = f'🤩 *Союз студентов УрФУ* – первичная профсоюзная организация студентов Уральского федерального университета, ' \
                   f'одна из самых крупных профсоюзных организаций в стране.  ' \
                   f'Команда реализует множество проектов различной направленности, ' \
                   f'подробнее о них и об их пользе членам профсоюза рассказываем ниже. \n' \
                   f'\n' \
                   f'📌 Год Союза студентов это: ответить на тысячи вопросов, ' \
                   f'помочь сотням студентов в решении различных проблем, ' \
                   f'реализовать множество инициатив студентов, организовать восемь окружных форумов, ' \
                   f'20-ть комплексных мероприятий, более ста спортивных мероприятий, ' \
                   f'вовлечь более 2 000 участников в образовательные проекты, ' \
                   f'подарить крутой новый мерч 500-ста лидерам рейтинга внеучебной ' \
                   f'деятельности – и здесь лишь малая часть результатов работы команды за 2022 / 2023 учебный год. '

            for _ in questions_Student_union_opportunities:
                btn = types.KeyboardButton(_)
                markup.add(btn)
            btn_back = types.KeyboardButton('Назад')
            markup.add(btn_back)
            bot.send_message(message.chat.id, text=text, reply_markup=markup, parse_mode='Markdown')

        if message.text in questions_Student_union_opportunities:
            index = questions_Student_union_opportunities.index(message.text)
            text = answers_Student_union_opportunities[index]
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)

        if message.text == "Бонусные программы Profcards и СКС Бонус":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('СКС Бонус')
            btn2 = types.KeyboardButton('Программа Profcard')
            btn_back = types.KeyboardButton('Назад')
            markup.row(btn1, btn2, btn_back)
            bot.send_message(message.chat.id, text="Выберете категорию", reply_markup=markup)
        if message.text == "СКС Бонус":
            text = 'С РЖД Бонус скидка 25% предоставляется на верхние и нижние места купе. ' \
                   'Максимальная скидка достигается при покупке билета за 45 суток ' \
                   'и может быть ниже стоимости места в плацкарте. Подробнее в приложении СКС РФ. \n' \
                   '*Чтобы познакомиться с программой СКС Бонус, необходимо:* \n' \
                   '*1. Состоять в профсоюзе* \n' \
                   '*2. Скачать приложение СКС РФ* \n' \
                   '*3. Зарегистрироваться в системе*'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown')
        if message.text == "Программа Profcard":
            text = 'Чтобы познакомиться с программой Profcards, необходимо:\n' \
                   '1. Состоять в профсоюзе\n' \
                   '2. Зарегистрироваться на сайте https://profcards.ru/'
            bot.send_message(message.chat.id, text=text, disable_web_page_preview=True)

        if message.text == "Как вступить в профсоюз":
            text = 'Чтобы получить профсоюзный билет = вступить в профсоюз ' \
                   '= стать частью Союза студентов УрФУ = получать максимум скидок, ' \
                   'пользы, преимуществ, комфорта и безопасности от студенчества, ' \
                   'нужно выполнить ряд простых действий: \n' \
                   '\n' \
                   '1. Обратиться в профбюро института к заместителю председателя ' \
                   'по организационно-массовой работе\n' \
                   '2. Заполнить заявление на вступление в профсоюз \n' \
                   '3. Оплатить членский взнос: 55 рублей для студентов бакалавриата и специалитета, 82 рубля для студентов магистратуры \n' \
                   '4. Получить номер электронного профсоюзника \n' \
                   '\n' \
                   '*Добро пожаловать в профсоюз :)*'
            bot.send_message(message.chat.id, text=text, parse_mode='Markdown', disable_web_page_preview=True)





        if message.text.lower() == 'назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Поселение')
            btn2 = types.KeyboardButton('Мат. помощь')
            btn3 = types.KeyboardButton('Стипендии')
            btn4 = types.KeyboardButton('Профсоюз')
            markup.row(btn1, btn2)
            markup.row(btn3, btn4)
            bot.send_message(message.chat.id, text="Вы вернулись назад", reply_markup=markup)
    except:
        pass


keep_alive()
bot.infinity_polling(timeout=10, long_polling_timeout = 5)