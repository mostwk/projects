import discord
import random
from discordbot import env
from discordbot import mytoken
import time

emotes = env.emotes
users = env.users
token = mytoken.token

cs_party = {
            'Fe4P3b#4998': users['almat'],
            'damirqa#2367': users['damir'],
            'tolyanidze#1860': users['tolya'],
            'Timore#9341': users['timore'],
            'mostwk#5270': users['mostwk']
            }


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        my_guild = client.get_guild(184004764424601600)
        print(f'Message from {message.author}: {message.content}')

        if message.author == client.user:
            return

        if message.content.lower() == 'fuck ali':
            await message.channel.send('Fuck Ali!!!' + emotes['almatW'])

        if ':AYAYA:' in message.content:
            if ':OMEGALUL:' not in message.content:
                await message.channel.send(emotes['AYAYA'])
            else:
                await message.delete()
                await message.channel.send(emotes['AYAYA'] + emotes['pepeGun'] + emotes['aliW'])

        if ':gachiGASM:' in message.content:
            await message.channel.send(emotes['gachiGASM'])

        if str(message.author) == 'lappehan#9547':
            if random.randint(0, 100) <= 2:
                await message.channel.send(users['ali'] + ' SHUT THE FUCK UP')
                await message.channel.send(emotes['almatW'] + emotes['pepeGun'] + emotes['aliW'])

            if 'youtu' in message.content:
                message.delete()
                await message.channel.send(
                    users['ali'] + " don't post your videos here bitsch" + emotes['monkaGun']
                )

        if message.content.startswith(users['antiali']):
            if str(message.author) == 'lappehan#9547':
                await message.channel.send(users['ali'] + " don't talk to me")
            else:
                await message.channel.send("Don't mind me, i am here for fucking with Ali")

        if message.content == "cs?":
            if str(message.author) == 'lappehan#9547':
                await message.channel.send(
                    users['ali'] + "you think they want to play with you? I don't." + emotes['pepeLaugh']
                )
            else:
                result = ''
                for user in my_guild.members:
                    if str(user) in cs_party and str(user.status) == 'online':
                        result += cs_party[str(user)] + ' '
                await message.channel.send(result + ' cs?')

        if message.content.lower() == "almat?":
            await message.channel.send('Almat is ...')
            time.sleep(1)
            if str(my_guild.get_member(184005290746839040).status) == 'online':
                await message.channel.send('Almat is online' + emotes['FeelsGoodMan'])
            else:
                await message.channel.send('Oh no...')
                time.sleep(1)
                await message.channel.send(emotes['PepeHands'] + '🕯' + emotes['almatW'] + '🕯')

        if message.content == "commands":
            await message.channel.send('cs? / fuck ali / almat? / ali wow /')

        if message.content.lower() == 'ali wow':
            await message.channel.send(users['ali'])
            await message.channel.send(
                '🇼' + emotes['OMEGALUL'] + '🇼' + ' 🇮 🇳 2⃣0⃣1⃣8⃣' + emotes['OMEGALUL']
            )


client = MyClient()
client.run(token)

