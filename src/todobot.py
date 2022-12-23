import telebot
import random

token = "5134644031:AAH8vmMoIIz7Lr6lH8e_2BP9z-XsnLJOB6o"

bot = telebot.TeleBot(token)

HELP = """
/help - вывести список доступных команд.
/add - добавить задачу в список (название задачи запршивать у пользователя).
/show - напечатать все добавленные задачи.
/random - добавить случайную задачу на дату Сегодня."""

RANDOM_TASK = ["Записаться на курс в Нетологию", "Написать письмо", "Покормить кота", "Помыть машину"]
tasks = {}


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        #     Даты нет в словаре, создаем запись с ключом вdate
        tasks[date] = []
        tasks[date].append(task)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASK)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[]" + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

    # print(date, task)
