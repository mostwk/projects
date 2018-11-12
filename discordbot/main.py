import discord
import random
import env

emotes = env.emotes
users = env.users
token = env.token


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
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

        if message.content.startswith(users['antiali']):
            if str(message.author) == 'lappehan#9547':
                await message.channel.send(users['ali'] + " don't talk to me")
            else:
                await message.channel.send("Don't mind me, i am here for fucking with Ali")


client = MyClient()
client.run(token)

