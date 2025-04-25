import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

bot = telebot.TeleBot("8032873771:AAF8YHOeHOCIVTvjW6_khFGoQB_UsWZtjRM")

# Колода
tarot_cards = [
    {"name": "Шут 🤹‍♂️", "meaning": "Новый путь, неожиданные события, наивность."},
    {"name": "Маг 🧙", "meaning": "Сила воли, инициативность, начало чего-то большого."},
    {"name": "Жрица 🌙", "meaning": "Интуиция, тайны, внутренний голос."},
    {"name": "Императрица 👑", "meaning": "Изобилие, забота, женская энергия."},
    {"name": "Император 🛡️", "meaning": "Контроль, структура, авторитет."},
    {"name": "Влюблённые 💞", "meaning": "Выбор, отношения, союз."},
    {"name": "Колесо Фортуны 🎡", "meaning": "Судьба, перемены, удача."},
    {"name": "Сила 🦁", "meaning": "Мужество, терпение, внутренняя сила."},
    {"name": "Отшельник 🔦", "meaning": "Поиск смысла, уединение, мудрость."},
    {"name": "Смерть ☠️", "meaning": "Конец одного – начало другого, трансформация."},
]

# Главное меню
@bot.message_handler(commands=['start', 'menu'])
def main_menu(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔮 Сделать расклад Таро", callback_data="tarot"))
    markup.add(InlineKeyboardButton("🧹 Очистить", callback_data="clear"))

    sent = bot.send_message(message.chat.id, "Выберите магическое действие:", reply_markup=markup)
    bot.delete_message(message.chat.id, message.message_id)  # Удалим команду
    bot.register_next_step_handler(sent, lambda m: None)  # Просто чтобы не падало

# Коллбек на кнопки
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    try:
        if call.data == "tarot":
            cards = random.sample(tarot_cards, 3)
            positions = ['Прошлое 🕰️', 'Настоящее ⏳', 'Будущее 🌅']

            response = "🔮 *Ваш расклад Таро:*\n\n"
            for i in range(3):
                response += f"{positions[i]} — *{cards[i]['name']}*\n_{cards[i]['meaning']}_\n\n"

            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, response, parse_mode="Markdown")

        elif call.data == "clear":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, "🌬 Магический след рассеян...")

    except Exception as e:
        print(e)

# Запуск
bot.polling()

