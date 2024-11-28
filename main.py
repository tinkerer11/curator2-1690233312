import telebot
from random import choice

bot = telebot.TeleBot('7582784090:AAGUWEsR4f8JJzTOk6-8UzsH7G7SFj4JM-k')

# Список идей для постов
post_ideas = [
    "Расскажи свою историю успеха или трудностей.",
    "Поделись любимыми инструментами для работы.",
    "Опиши свой типичный день.",
    "Составь список полезных советов для подписчиков.",
    "Сними бэкстейдж процесса создания контента."
]

# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я помогу тебе вести блог. Вот список доступных команд:\n\n"
                                      "/idea - получить идею для поста\n"
                                      "/schedule - совет по планированию контента\n"
                                      "/promotion - советы по продвижению\n"
                                      "/help - список всех команд")

# Команда /idea
@bot.message_handler(commands=['idea'])
def post_idea(message):
    idea = choice(post_ideas)
    bot.send_message(message.chat.id, f"Вот идея для твоего поста: {idea}")

# Команда /schedule
@bot.message_handler(commands=['schedule'])
def schedule_tips(message):
    bot.send_message(message.chat.id, "Совет по планированию: \n\n"
                                      "1. Установи цель — чего ты хочешь добиться с помощью контента.\n"
                                      "2. Создай контент-план — выдели дни для разных типов постов (например, понедельник — мотивация, пятница — советы).\n"
                                      "3. Используй инструменты для планирования: Trello, Notion или Google Календарь.")

# Команда /promotion
@bot.message_handler(commands=['promotion'])
def promotion_tips(message):
    bot.send_message(message.chat.id, "Советы по продвижению:\n\n"
                                      "1. Будь активен: отвечай на комментарии и взаимодействуй с подписчиками.\n"
                                      "2. Используй тренды и популярные хэштеги.\n"
                                      "3. Коллаборации с другими блогерами могут значительно расширить аудиторию.")

# Команда /help
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Список доступных команд:\n"
                                      "/idea - получить идею для поста\n"
                                      "/schedule - совет по планированию контента\n"
                                      "/promotion - советы по продвижению\n"
                                      "/help - список всех команд")

# Обработчик текстовых сообщений (на случай, если пользователь пишет что-то вручную)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, "Я тебя не понял. Напиши /help, чтобы узнать, что я умею!")

# Запуск бота
bot.polling(none_stop=True)