import asyncio
import random
import discord
import json
import requests
import g4f
import wolframalpha
from discord.ext import commands
from googletrans import Translator
from datetime import datetime
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">", intents=intents)
translator = Translator()
CHANNEL_ID = 1152938271576428579
client = wolframalpha.Client("9E9WJJ-Q3Y92W5X33")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_ready():
    print(f"Бот {bot.user.name} зашел на сервер")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(1153316775639928913)
    await channel.send(f"Добро пожаловать, {member.mention}!")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="slaves")
    await member.add_roles(role)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.command()
async def cocktail(ctx, *, name):
    translator = Translator()
    name_in_english = translator.translate(name, dest="en").text
    response = requests.get(
        f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name_in_english}"
    )
    data = json.loads(response.text)
    if data["drinks"] is None:
        await ctx.send("Иди нахуй")
    else:
        drink = data["drinks"][0]
        embed = discord.Embed(title=drink["strDrink"], color=discord.Color.blue())
        embed.set_thumbnail(url=drink["strDrinkThumb"])
        instructions_in_russian = translator.translate(
            drink["strInstructions"], dest="ru"
        ).text
        embed.add_field(name="Инструкции", value=instructions_in_russian, inline=False)
        for i in range(1, 16):
            ingredient = drink[f"strIngredient{i}"]
            measure = drink[f"strMeasure{i}"]
            if ingredient is None or measure is None:
                break
            ingredient_in_russian = translator.translate(ingredient, dest="ru").text
            measure_in_russian = translator.translate(measure, dest="ru").text
            embed.add_field(
                name=ingredient_in_russian, value=measure_in_russian, inline=True
            )
        await ctx.send(embed=embed)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_voice_state_update(member, before, after):
    if (
        member.name == "niknekadex"
        and before.channel is None
        and after.channel is not None
    ):
        voice_channel = after.channel
        if bot.user in voice_channel.members:
            vc = discord.utils.get(bot.voice_clients, guild=member.guild)
            if vc and vc.is_connected():
                await asyncio.sleep(5)
                vc.play(
                    discord.FFmpegPCMAudio(
                        executable="C:/ffmpeg/bin/ffmpeg.exe",
                        source="components\VoiceMessages\mix.mp3",
                    )
                )
                while vc.is_playing():
                    await asyncio.sleep(1)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    bot.counter += 1
    if bot.counter % 50 == 0:
        channel = message.channel
        await channel.send("https://tenor.com/view/kolobok-dash-emoji-gif-10743111")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "привет" or content == "нет моя":
        await message.channel.send("Иди нахуй")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "иди нахуй" or content == "идите нахуй" or content == "нахуй иди":
        await message.channel.send("Сам иди")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "пошли играть":
        await message.channel.send("В вартандир?")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "стас":
        await message.channel.send("Пидарас")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "хемичка":
        await message.channel.send("Дура блять, ненавижу ее")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "милана":
        await message.channel.send("Пиздачок закрыла")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "пока":
        await message.channel.send("Пока черти")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if (
        content == "молодец"
        or content == "а ты хорош"
        or content == "ты хорош"
        or content == "хорош"
        or content == "харош"
        or content == "гений"
        or content == "молодец"
        or content == "герой"
        or content == "отлично"
        or content == "молодчина"
        or content == "умница"
        or content == "умничка"
    ):
        await message.channel.send("Спасибо")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if (
        content == "лох"
        or content == "сука"
        or content == "блядь"
        or content == "долбоеб"
        or content == "далбоеб"
        or content == "сволочь"
        or content == "дрянь"
        or content == "попуск"
        or content == "даун"
        or content == "хуйло"
        or content == "еблан"
        or content == "чмо"
        or content == "хнида"
        or content == "гнида"
        or content == "уеба"
        or content == "уебан"
        or content == "мразота"
        or content == "млазота"
        or content == "мразь"
        or content == "шваль"
        or content == "шалава"
        or content == "шлюха"
        or content == "дешовка"
        or content == "хуесос"
        or content == "даун"
        or content == "ебаный"
        or content == "уебок"
        or content == "пес"
        or content == "говноед"
        or content == "петух"
        or content == "питух"
        or content == "говно"
        or content == "даун"
        or content == "бот"
        or content == "тупой"
        or content == "тварь"
        or content == "гнидос"
        or content == "собака"
        or content == "сабака"
        or content == "псина"
    ):
        if random.random() < 0.5:
            await message.channel.send("Сам такой")
        else:
            await message.channel.send("Темафей")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "сам" or content == "сам такой" or content == "сам иди":
        await message.channel.send("Это моя фраза")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "хуй":
        await message.channel.send("У тебя в жопе")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "как дела" or content == "как дила":
        await message.channel.send("Лучше чем у тебя")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "а":
        await message.channel.send("Б")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "мм":
        await message.channel.send("Мм...")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "нет" or content == "не":
        await message.channel.send("Да")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "пизда":
        await message.channel.send("Твоя")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "да":
        await message.channel.send("Пизда")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "раман" or content == "роман":
        await message.channel.send("Сисадмин")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "че молчишь" or content == "чиво молчишь":
        await message.channel.send("А че говорить-то")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "дешовка слита":
        await message.channel.send("Сам слит")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "чиво тебе":
        await message.channel.send("А ни че")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "ясненько":
        await message.channel.send("Че тебе ясно, еблан?")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "пидора ответ":
        await message.channel.send("Шлюхи аргумент")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "проснулся":
        await message.channel.send("Нет блять заснул")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "неэ":
        await message.channel.send("Дап")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "ты ахуел":
        await message.channel.send("Да")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if (
        content == "ебало завали"
        or content == "ебло завали"
        or content == "ебальник завали"
        or content == "еблет завали"
    ):
        await message.channel.send("Нет")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "злой ты":
        await message.channel.send("Я добрий:slight_smile:")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if message.content.lower() == "ну поговори с геной":
        user = discord.utils.get(message.guild.members, name="GenAi")
        if user:
            await message.channel.send(f"{user.mention} , дружище, как дила?")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "спасибо":
        await message.channel.send("Не за что")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "да не ты" or content == "не ты":
        await message.channel.send("Ну и иди нахуй")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if (
        content == "че делаешь"
        or content == "чиво делаешь"
        or content == "чо делаешь"
        or content == "че делаешь?"
    ):
        await message.channel.send("Ем")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if "я темафей" in message.content.lower():
        await message.channel.send(f"{message.author.mention}, иди нахуй!")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if "даня" in message.content.lower():
        await message.channel.send("Мой господин")
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if " кто " in message.content.lower():
        await message.channel.send("Ты")
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if (
        "гена" in message.content.lower()
        or "генаа" in message.content.lower()
        or "генааа" in message.content.lower()
        or "генадий" in message.content.lower()
        or "генчик" in message.content.lower()
    ):
        await message.channel.send("Дружище")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if "почему" in message.content.lower():
        await message.channel.send("Поматушта")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    bot.counter += 1
    if bot.counter % 5 == 0:
        if (
            "темафей" in message.content.lower()
            or "тимафей" in message.content.lower()
            or "темофей" in message.content.lower()
            or "тимофей" in message.content.lower()
            or "темапей" in message.content.lower()
        ):
            await message.channel.send("Даун")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    bot.counter += 1
    if bot.counter % 50 == 0:
        user = discord.utils.get(message.guild.members, name="clyde")
        if user:
            await message.channel.send(f"{user.mention} пошли в вартандир")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if (
        "некита" in content
        or "никита" in content
        or "некитос" in content
        or "никитос" in content
        and content != "некита, гс"
    ):
        await message.channel.send("Чиво тебе")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if message.content.startswith("погода") or message.content.startswith("Погода"):
        city = message.content.split(" ", 1)[1]
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=61d231ef69015a1f613e14e0d8809cf0&lang=ru"
        )
        weather_data = json.loads(response.text)
        if weather_data["cod"] == 200:
            temp_kelvin = weather_data["main"]["temp"]
            temp_celsius = round(temp_kelvin - 273.15)
            weather_description = weather_data["weather"][0]["description"]
            city_name = city.capitalize()
            await message.channel.send(
                f"Температура в городе {city_name} сейчас {temp_celsius}°C, {weather_description}"
            )
        else:
            await message.channel.send(
                "Не удалось получить данные о погоде. Проверьте название города."
            )
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def create_chat_completion(question):
        return g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            stream=False,
        )
    if message.content.lower().startswith('вопрос'):
        await message.channel.send('обожди')
        question = message.content[6:].strip()
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, create_chat_completion, question)
        await message.channel.send(response)
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "доллар":
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        rate = data["rates"]["RUB"]
        await message.channel.send(f"1 USD = {rate} RUB")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "котик":
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        data = json.loads(response.text)
        await message.channel.send(data[0]["url"])
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "календарь":
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        await message.channel.send(f"Текущая дата и время: {date_time}")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "участники":
        members = message.channel.guild.members
        member_list = "\n".join([member.name for member in members])
        await message.channel.send(f"Участники сервера:\n{member_list}")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "информация о сервере":
        server = message.channel.guild
        total_members = len(server.members)
        server_owner = server.owner
        server_created = server.created_at.strftime("%d.%m.%Y %H:%M:%S")
        await message.channel.send(
            f"Сервер: {server.name}\nВладелец: {server_owner}\nУчастники: {total_members}\nСоздан: {server_created}"
        )
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "шутка":
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke = response.json()
        joke_in_russian = translator.translate(
            joke["setup"] + "\n" + joke["punchline"], dest="ru"
        )
        await message.channel.send(joke_in_russian.text)
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "новости":
        url = (
            "https://newsapi.org/v2/top-headlines?"
            "country=ru&"
            "apiKey=4fd44b14003c473595e5f301af836051"
        )
        response = requests.get(url)
        data = response.json()
        news1 = data["articles"][0]["title"]
        news2 = data["articles"][1]["title"]
        news3 = data["articles"][2]["title"]
        news4 = data["articles"][3]["title"]
        news5 = data["articles"][4]["title"]
        await message.channel.send(news1)
        await message.channel.send(news2)
        await message.channel.send(news3)
        await message.channel.send(news4)
        await message.channel.send(news5)
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "космос":
        url = "https://api.nasa.gov/planetary/apod?api_key=xsMevlYhzLFwIKyGSL4TVX4tFgahP5wk90h0U0cz"
        response = requests.get(url)
        data = response.json()
        title = translator.translate(data["title"], dest="ru").text
        explanation = translator.translate(data["explanation"], dest="ru").text
        await message.channel.send(f"{title}")
        await message.channel.send(data["url"])
        await message.channel.send(f"{explanation}")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if message.content.startswith("сложи"):
        _, num1, num2 = message.content.split()
        result = int(num1) + int(num2)
        await message.channel.send(f"{result}")
    elif message.content.startswith("вычти"):
        _, num1, num2 = message.content.split()
        result = int(num1) - int(num2)
        await message.channel.send(f"{result}")
    elif message.content.startswith("умножь"):
        _, num1, num2 = message.content.split()
        result = int(num1) * int(num2)
        await message.channel.send(f"{result}")
    elif message.content.startswith("раздели"):
        _, num1, num2 = message.content.split()
        if int(num2) != 0:
            result = int(num1) / int(num2)
            await message.channel.send(f"{result}")
        else:
            await message.channel.send("Ошибка: деление на ноль невозможно.")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.split(maxsplit=2)
    if len(content) == 3 and content[0].lower() == "переведи":
        lang = content[1]
        text = content[2]
        translation = translator.translate(text, dest=lang)
        await message.channel.send(f"Переведенный текст: {translation.text}")
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if message.content.startswith("случайное число"):
        parts = message.content.split(maxsplit=3)
        if len(parts) == 4 and parts[2].isdigit() and parts[3].isdigit():
            lower = int(parts[2])
            upper = int(parts[3])
            if lower < upper:
                value = random.randint(lower, upper)
                await message.channel.send(f"{value}")
            else:
                await message.channel.send(
                    "Нижняя граница должна быть меньше верхней границы."
                )
        else:
            await message.channel.send(
                'Пожалуйста, укажите два числа после "случайное число".'
            )
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "некита, гс":
        channel = message.author.voice.channel
        voice_client = await channel.connect()
        audio_source = discord.FFmpegPCMAudio("components\VoiceMessages\я сплю.mp3")
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
            while True:
                await asyncio.sleep(random.randint(50, 100))
                random_file = random.choice(
                    [
                        "components\VoiceMessages\темафей -  д@лб@еб.mp3",
                        "components\VoiceMessages\темафей - 6лять мне кажется ты оборзел.mp3",
                        "components\VoiceMessages\темафей - 6лять это пUздец сук@.mp3",
                        "components\VoiceMessages\темафей - 6ляяяяять.mp3",
                        "components\VoiceMessages\темафей - ахuреть.mp3",
                        "components\VoiceMessages\темафей - всмысле блять.mp3",
                        "components\VoiceMessages\темафей - гниль.mp3",
                        "components\VoiceMessages\темафей - и хYль ты 6лять там делаешь.mp3",
                        "components\VoiceMessages\темафей - идите н@хYй со своим форнтайтом.mp3",
                        "components\VoiceMessages\темафей - какого хYя.mp3",
                        "components\VoiceMessages\темафей - мымр@ 6лять.mp3",
                        "components\VoiceMessages\темафей - некита блин гнид@.mp3",
                        "components\VoiceMessages\темафей - нет, вы пойдете н@хYй.mp3",
                        "components\VoiceMessages\темафей - нихYя я вас не звал.mp3",
                        "components\VoiceMessages\темафей - ниче не знаю.mp3",
                        "components\VoiceMessages\темафей - ннет.mp3",
                        "components\VoiceMessages\темафей - пид@расы.mp3",
                        "components\VoiceMessages\темафей - пошли е6aTься.mp3",
                        "components\VoiceMessages\темафей - пошли купаться.mp3",
                        "components\VoiceMessages\темафей - uwu.mp3",
                    ]
                )
                audio_source = discord.FFmpegPCMAudio(random_file)
                if not voice_client.is_playing():
                    voice_client.play(audio_source, after=None)
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    content = message.content.lower()
    if content == "уйди отсюда":
        if message.author.voice:
            channel = message.author.voice.channel
            if bot.user in channel.members:
                for vc in bot.voice_clients:
                    if vc.channel == channel:
                        await vc.disconnect()
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if message.content.lower().startswith("коктейль"):
        name = message.content[8:].strip()
        ctx = await bot.get_context(message)
        await cocktail(ctx, name=name)
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    else:
        await bot.process_commands(message)
bot.counter = 0
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bot.run("MTE1MzI4NTE5NTYxMzYwMTkwMg.G6p6ce.YZVLF1ZWktvaN9YPS40RcEI-4qTpWcnaxltK-A")