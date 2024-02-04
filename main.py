import telebot
import time
from telebot import types


# Токен бота, полученный от BotFather
TOKEN = '6957731964:AAH4Dc28ew6lmBVFmlqiYykfiUfjij2ZolE'
bot = telebot.TeleBot(TOKEN)
user_choices = {}
user_status = {}


# Функция для обработки команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать в наш сервис по заказу производства и покупке одежды!"
                     " Я помогу вам выбрать нужные услуги.")
    time.sleep(1)  # задержка
    send_options(message)

def add_user_choice(user_id, choice):
    if user_id not in user_choices:
        user_choices[user_id] = []
    user_choices[user_id].append(choice)

# Функция для отправки основных кнопок
def send_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Заказ производства", "Покупка одежды", "Сертификат, Декларация и отказное письмо", "Для селлеров"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Заказ производства", "Покупка одежды",
                                                           "Сертификат, Декларация и отказное письмо", "Для селлеров"])
def handle_main_menu(message):
    add_user_choice(message.chat.id, message.text)
    if message.text == "Заказ производства":
        send_manufacturing_options(message)
    elif message.text == "Покупка одежды":
        send_clothing_purchase_options(message)
    elif message.text == "Сертификат, Декларация и отказное письмо":
        send_certification_options(message)
    elif message.text == "Для селлеров":
        send_seller_options(message)

def send_manufacturing_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Под ваш бренд", "Под наш бренд", "Без бренда"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите тип производства:", reply_markup=markup)



def send_brand_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С документами", "Без документов"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант:", reply_markup=markup)

# Под ваш бренд
@bot.message_handler(func=lambda message: message.text == "Под ваш бренд")
def handle_your_brand_options(message):
    add_user_choice(message.chat.id, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С документами", "Без документов"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант для вашего бренда:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["С документами", "Без документов"])
def handle_your_brand_documents_options(message):
    add_user_choice(message.chat.id, message.text)
    if message.text == "С документами":
        send_your_brand_with_documents_options(message)
    else:
        send_your_brand_without_documents_options(message)

def send_your_brand_with_documents_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Ваши лекала", "Наши лекала"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите тип лекал для вашего бренда с документами:", reply_markup=markup)

def send_your_brand_without_documents_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Ваши лекала", "Наши лекала"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите тип лекал для вашего бренда без документов:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Ваши лекала", "Наши лекала"])
def handle_your_brand_lekala_options(message):
    add_user_choice(message.chat.id, message.text)
    if message.text == "Ваши лекала":
        send_your_brand_your_lekala_options(message)
    else:
        send_your_brand_our_lekala_options(message)

def send_your_brand_your_lekala_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["После очистки от НДС и отчетов", "Без очистки от налогов"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант для ваших лекал:", reply_markup=markup)

def send_your_brand_our_lekala_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["После очистки от НДС и отчетов", "Без очистки от налогов"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант для наших лекал:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "После очистки от НДС и отчетов")
def handle_your_brand_after_vat_clearance_options(message):
    add_user_choice(message.chat.id, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С честным знаком", "Без честного знака"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант для налоговой очистки:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Без очистки от налогов")
def handle_your_brand_without_vat_clearance_options(message):
    add_user_choice(message.chat.id, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С честным знаком", "Без честного знака"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант для налоговой очистки:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["С честным знаком", "Без честного знака"])
def handle_your_brand_tax_mark_options(message):
    add_user_choice(message.chat.id, message.text)
    if message.text == "С честным знаком":
        send_your_brand_with_honest_sign_options(message)
    else:
        send_your_brand_without_honest_sign_options(message)

def send_your_brand_with_honest_sign_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С фулфилментом", "Без фулфилмента"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант с честным знаком:", reply_markup=markup)

def send_your_brand_without_honest_sign_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С фулфилментом", "Без фулфилмента"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант без честного знака:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["С фулфилментом", "Без фулфилмента"])
def handle_your_brand_fulfillment_options(message):
    final_choice = f"{message.text} "
    add_user_choice(message.chat.id, final_choice)
    send_final_confirmation(message)  # Теперь передается только один аргумент
    send_terms_and_conditions(message)

# Под наш бренд
@bot.message_handler(func=lambda message: message.text == "Под наш бренд")
def handle_our_brand_options(message):
    add_user_choice(message.chat.id, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С документами", "Без документов"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант для вашего бренда:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["С документами", "Без документов"])
def handle_our_brand_documents_options(message):
    add_user_choice(message.chat.id, message.text)
    if message.text == "С документами":
        send_our_brand_with_documents_options(message)
    else:
        send_our_brand_without_documents_options(message)

def send_our_brand_with_documents_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Ваши лекала", "Наши лекала"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите тип лекал для нашего бренда с документами:", reply_markup=markup)

def send_our_brand_without_documents_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Ваши лекала", "Наши лекала"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите тип лекал для нашего бренда без документов:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Ваши лекала", "Наши лекала"])
def handle_our_brand_lekala_options(message):
    add_user_choice(message.chat.id, message.text)
    if message.text == "Ваши лекала":
        send_our_brand_your_lekala_options(message)
    else:
        send_our_brand_our_lekala_options(message)

def send_our_brand_your_lekala_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["После очистки от НДС и отчетов", "Без очистки от налогов"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант для ваших лекал:", reply_markup=markup)

def send_our_brand_our_lekala_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["После очистки от НДС и отчетов", "Без очистки от налогов"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант для наших лекал:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "После очистки от НДС и отчетов")
def handle_after_vat_clearance_options(message):
    add_user_choice(message.chat.id, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С честным знаком", "Без честного знака"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант для налоговой очистки:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Без очистки налогов")
def handle_without_vat_clearance_options(message):
    add_user_choice(message.chat.id, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С честным знаком", "Без честного знака"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант для налоговой очистки:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["С честным знаком", "Без честного знака"])
def handle_tax_mark_options(message):
    add_user_choice(message.chat.id, message.text)
    if message.text == "С честным знаком":
        send_with_honest_sign_options(message)
    else:
        send_without_honest_sign_options(message)

def send_with_honest_sign_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С фулфилментом", "Без фулфилмента"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант с честным знаком:", reply_markup=markup)

def send_without_honest_sign_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С фулфилментом", "Без фулфилмента"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант без честного знака:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["С фулфилментом", "Без фулфилмента"])
def handle_fulfillment_options(message):
    add_user_choice(message.chat.id, message.text)
    final_choice = f"{message.text} "
    send_final_confirmation(message, final_choice)
    send_terms_and_conditions(message)

    # Без бренда
@bot.message_handler(func=lambda message: message.text == "Без бренда")
def handle_no_brand_options(message):
    add_user_choice(message.chat.id, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Ваши лекала", "Наши лекала"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите тип лекал для производства без бренда:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Ваши лекала", "Наши лекала"])
def handle_no_brand_lekala_options(message):
    add_user_choice(message.chat.id, message.text)
    if message.text == "Ваши лекала":
        send_no_brand_your_lekala_options(message)
    else:
        send_no_brand_our_lekala_options(message)

def send_no_brand_your_lekala_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["После очистки от НДС и отчетов", "Без очистки от налогов"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант для ваших лекал без бренда:", reply_markup=markup)

def send_no_brand_our_lekala_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["После очистки от НДС и отчетов", "Без очистки от налогов"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант для наших лекал без бренда:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["После очистки от НДС и отчетов", "Без очистки от налогов"])
def handle_no_brand_vat_options(message):
    add_user_choice(message.chat.id, message.text)
    if message.text == "После очистки от НДС и отчетов":
        send_no_brand_after_vat_clearance_options(message)
    else:
        send_no_brand_without_tax_clearance_options(message)

def send_no_brand_after_vat_clearance_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С честным знаком", "Без честного знака"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант после очистки от НДС для производства без бренда:", reply_markup=markup)

def send_no_brand_without_tax_clearance_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С честным знаком", "Без честного знака"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант без очистки от налогов для производства без бренда:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["С честным знаком", "Без честного знака"])
def handle_no_brand_tax_mark_options(message):
    add_user_choice(message.chat.id, message.text)
    if message.text == "С честным знаком":
        send_no_brand_with_honest_sign_options(message)
    else:
        send_no_brand_without_honest_sign_options(message)

def send_no_brand_with_honest_sign_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С фулфилментом", "Без фулфилмента"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант с честным знаком для производства без бренда:", reply_markup=markup)

def send_no_brand_without_honest_sign_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С фулфилментом", "Без фулфилмента"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант без честного знака для производства без бренда:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["С фулфилментом", "Без фулфилмента"])
def handle_no_brand_fulfillment_options(message):
    add_user_choice(message.chat.id, message.text)
    final_choice = f"{message.text} для производства без бренда"
    send_final_confirmation(message, final_choice)
    send_terms_and_conditions(message)

def send_clothing_purchase_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С Документами", "Без Документов"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант покупки одежды:", reply_markup=markup)

# Добавляем обработчики для раздела "Покупка Одежды"
@bot.message_handler(func=lambda message: message.text == "Покупка одежды")
def handle_clothing_purchase_options(message):
    add_user_choice(message.chat.id, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С Документами", "Без Документов"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант покупки одежды:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["С Документами", "Без Документов"])
def handle_clothing_documents_options(message):
    add_user_choice(message.chat.id, message.text)
    if message.text == "С Документами":
        send_clothing_with_documents_options(message)
    elif message.text == "Без Документов":
        send_clothing_without_documents_options(message)

def send_clothing_with_documents_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["После очистки от НДС и отчетов", "Без очистки от налогов"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите тип покупки одежды с документами:", reply_markup=markup)

def send_clothing_without_documents_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Обычный", "Брендированный"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите тип покупки одежды без документов:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Обычный", "Брендированный"])
def handle_clothing_type_options(message):
    add_user_choice(message.chat.id, message.text)
    if message.text == "Обычный":
        send_clothing_with_documents_options(message)
    elif message.text == "Брендированный":
        send_clothing_without_documents_options(message)


@bot.message_handler(func=lambda message: message.text in ["После очистки от НДС и отчетов", "Без очистки от налогов", "Обычный", "Брендированный"])
def handle_clothing_vat_and_brand_options(message):
    add_user_choice(message.chat.id, message.text)
    if message.text in ["После очистки от НДС и отчетов", "Без очистки от налогов"]:
        send_clothing_tax_mark_options(message)
    elif message.text in ["Обычный", "Брендированный"]:
        send_clothing_tax_mark_options(message)
    else:
        final_choice = f"Покупка одежды: {message.text}"
        send_final_confirmation(message)

def send_clothing_tax_mark_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С честным знаком", "Без честного знака"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант покупки одежды:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["С честным знаком", "Без честного знака"])
def handle_clothing_honest_sign_options(message):
    add_user_choice(message.chat.id, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["С фулфилментом", "Без фулфилмента"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите вариант покупки одежды с налоговыми опциями:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["С фулфилментом", "Без фулфилмента"])
def handle_clothing_fulfillment_options(message):
    add_user_choice(message.chat.id, message.text)
    final_choice = f"Покупка одежды: {message.text}"
    send_final_confirmation(message, final_choice)
    send_terms_and_conditions(message)

def send_certification_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Сертификация", "Декларация", "Отказное письмо"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите необходимую опцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Сертификация", "Декларация"])
def handle_certification_and_declaration(message):
    user_id = message.chat.id
    add_user_choice(message.chat.id, message.text)
    send_pdf(message.chat.id, 'certification_info.pdf')
    # После отправки PDF файла вызываем запрос на ввод личных данных
    send_agreement_options(user_id)


@bot.message_handler(func=lambda message: message.text == "Отказное письмо")
def handle_rejection_letter(message):
    user_id = message.chat.id
    # Добавление выбора пользователя
    add_user_choice(message.chat.id, message.text)

    # Отправка текстового сообщения с информацией
    info_text = (
        "Что такое отказное письмо на продукцию?\n"
        "Это официальное уведомление от органов, занимающихся сертификацией, о "
        "том, что конкретный товар не нуждается в сертификации или "
        "декларировании. Этот документ подтверждает, что оценка безопасности "
        "данной продукции не может быть осуществлена в рамках установленных "
        "технических регламентов и стандартов ГОСТ. "
        "Это гарантия для производителя или поставщика, что их товар соответствует "
        "спецификации и внешним требованиям, несмотря на отсутствие "
        "обязательной сертификации.\n"
        "Для каких товаров нужно отказное письмо? Существует общий перечень товаров, для которых обязательно требуется "
        "прохождение процедуры декларирования или сертификации (примеру в "
        "России- Постановление Правительства РФ от 23.12.2021 N 2425). А для "
        "товаров, НЕ ПОДЛЕЖАЩИХ обязательному подтверждению соответствия, "
        "применяется механизм отказного письма.\n"
        "Это официальное уведомление о том, что данная продукция выходит за "
        "рамки стандартных категорий и областей регулирования. Это могут быть "
        "уникальные и нетипичные товары, например, продукция, без аналогов на "
        "рынке, или товары с высокоспецифичными характеристиками и тд.\n"
        "На какие товары оформляется отказное письмо список? Общие правило: продукция не должна подключатся к электричеству и "
        "должна не попадать под действие Технические регламенты Таможенного Союза.\n"
        "Пример продукции, на которую можно оформить отказное письмо: "
        "Ювелирные украшения. Бижутерия. Сувенирная продукция. Маски для сна. "
        "Массажеры для лица и тела. Накладные ресницы. Сантехника. Аксессуары "
        "для телефона. Палатки туристические. Картины. Канцелярские товары, "
        "включая бумагу."
    )
    bot.send_message(message.chat.id, "Вы выбрали: Отказное письмо. Вот информация по этой теме:")
    bot.send_message(message.chat.id, info_text)

    # После отправки текстового сообщения вызываем запрос на ввод личных данных
    send_agreement_options(user_id)


def send_pdf(chat_id, file_name):
    with open(file_name, 'rb') as pdf:
        bot.send_document(chat_id, pdf)


def send_certification_type_options(message, cert_type):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["На товар", "На производство"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, f"Выберите тип {cert_type}:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["На товар", "На производство"])
def handle_certification_product_or_production_options(message):
    add_user_choice(message.chat.id, message.text)
    final_choice = f"{message.text}"
    send_final_confirmation(message, final_choice)

def send_seller_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Фотостудия", "Инфографика", "Кросс-докинг", "Другие вопросы"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите услугу для селлеров:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Фотостудия", "Инфографика", "Кросс-докинг"])
def handle_service_options(message):
    user_id = message.chat.id
    # Добавление выбора пользователя
    add_user_choice(message.chat.id, message.text)

    # Отправка текстового сообщения с информацией
    info_text = (
        "В настоящее время все производственные процессы (заказ производства, "
        "покупка одежды, услуги фотостудии, оформление инфографики, карточки, "
        "услуги фулфилмента, кросс-докинг, сертификация, бизнеса, отчеты и т.д.) "
        "можно оформить дистанционно, о чем мы может позаботиться и сделать за вас. "
        "Для наиболее обзорного предоставления информации ниже заполните "
        "заявку и мы обязательно свяжемся с Вами."
    )
    bot.send_message(message.chat.id, "Вы выбрали: {}. Вот информация по этой услуге:".format(message.text))
    bot.send_message(message.chat.id, info_text)

    # Вызов функции для подтверждения выбора
    send_agreement_options(user_id)



# Изменение обработчика для "Другие вопросы"
@bot.message_handler(func=lambda message: message.text == "Другие вопросы")
def handle_seller_options(message):
    add_user_choice(message.chat.id, message.text)
    send_pdf(message.chat.id, 'other_questions.pdf')
    # После отправки PDF файла вызываем запрос на ввод личных данных
    request_contact_info(message)

def send_agreement_options(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Согласен", "Не согласен"]
    markup.add(*buttons)
    bot.send_message(user_id, "Вы согласны работать с нами на этих условиях?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Согласен", "Не согласен"])
def handle_user_decision(message):
    chat_id = message.chat.id
    if message.text == "Согласен":
        request_contact_info(message)
    elif message.text == "Не согласен":
        handle_disagreement(message)
        # Не отправляем данные в админку и очищаем данные пользователя
        clear_user_data(chat_id)

def request_contact_info(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Введите ваше имя, номер телефона и город. Мы обязательно свяжемся с Вами")
    bot.register_next_step_handler(message, process_contact_info)

def process_contact_info(message):
    chat_id = message.chat.id
    contact_info = message.text  # Пользователь ввел эту информацию

    # Собираем информацию о выборах пользователя и его контактные данные
    user_data = "Выборы пользователя:\n{}\nКонтактная информация:\n{}".format(
        '\n'.join(user_choices.get(chat_id, [])), contact_info)
    # Отправляем данные администратору
    admin_id = '5013185502'
    bot.send_message(admin_id, user_data)

    # Сообщаем пользователю, что его информация была отправлена
    bot.send_message(chat_id, "Ваши данные отправлены. В ближайшее время с вами свяжутся наши менеджеры.")

    # Очищаем данные пользователя
    clear_user_data(chat_id)



def send_final_confirmation(message, final_choice=None):
    user_id = message.chat.id
    if final_choice:
        user_choices[user_id].append(final_choice)
    last_choice = user_choices.get(user_id, [])[-1]
    choices_text = "\n".join(user_choices.get(user_id, []))
    bot.send_message(user_id, f"Вы выбрали:\n{choices_text}")

    if last_choice in ["Фотостудия", "Инфографика", "Кросс-докинг", "Другие вопросы",
                       "Сертификация", "Декларация", "Отказное письмо"]:
        request_contact_info(message)  # Запрашиваем дополнительную информацию
    else:
        send_agreement_options(user_id)


def send_terms_and_conditions(message):
    terms_text = (
        "Общие условия:\n"
        "- предварительное согласование условий взаимодействия;\n"
        "- поиск и выбор товара, согласование количества, цены, сроков, транспортировки и иных условий покупки товара;\n"
        "- начало исполнения заказа после предоплаты 80% цены товара;\n"
        "- проведение процедуры ОТК с использованием фулфилмента г. Бишкек, фото видео отчет;\n"
        "- 100% оплата заказа после отбраковки и направление товара по указанному адресу в том числе сразу на склады маркетплейсов.\n"
        "В целях исполнения всеми сторонами своих обязательств денежные средства находятся на счету у нас, после полной оплаты и прохождения товара проверки ОТК с использованием фулфилмента, денежные средства и товар предоставляются сторонам.\n"
        "*Поиск, перевозка товара, маркировка и иные необходимые действия осуществляются за счет покупателя по договоренности.\n"
        "Основные условия:\n"
        "- договор поставки заключаете с российским ИП на УСН, который после уплаты косвенных налогов (ввозной НДС), подачи декларации в ФНС и статформы в ФТС, товаросопроводительную документацию (счет-фактура, декларация, накладные, справки и т.д.) направляет на электронную почту или по ЭДО, КИЗы честного знака по ЭДО."
    )
    bot.send_message(message.chat.id, terms_text)

def handle_disagreement(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Поддержка", "Главное меню", "Завершить"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите следующий шаг:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Поддержка")
def handle_support(message):
    support_message = "Вы можете связаться с нами по WhatsApp по номеру: +996706935720.\nТакже вы можете написать в нашу администрацию: https://t.me/+996706935720"
    bot.send_message(message.chat.id, support_message)

@bot.message_handler(func=lambda message: message.text == "Главное меню")
def handle_main_menu_return(message):
    send_options(message)

@bot.message_handler(func=lambda message: message.text == "Завершить")
def handle_exit(message):
    goodbye_message = "Спасибо, что поинтересовались нашими услугами. Мы всегда рады помочь вам. Ждем вас снова!"
    bot.send_message(message.chat.id, goodbye_message)


def process_additional_info(message):
    chat_id = message.chat.id
    contact_info = message.text
    user_data = "Выборы пользователя:\n{}\nКонтактная информация:\n{}".format(
        '\n'.join(user_choices.get(chat_id, [])), contact_info)

    # Отправляем данные администратору
    admin_id = '6425572782'
    bot.send_message(admin_id, user_data)

    # Сообщаем пользователю, что его информация была отправлена
    bot.send_message(chat_id, "Ваши данные отправлены. В ближайшее время с вами свяжутся наши менеджеры.")

def clear_user_data(user_id):
    if user_id in user_choices:
        del user_choices[user_id]
    if user_id in user_status:
        del user_status[user_id]

# Запуск бота
bot.polling(none_stop=True)
