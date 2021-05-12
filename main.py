import discord

client = discord.Client()
keywords = ["hi", "hello"]

@client.event
async def on_message(message):
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            for j in range(100000):
                await message.channel.send(",s")
                await message.channel.send(",f 2")

client.run('ODI3Mzk5Mzg1MDI0ODIzMzc2.YGaduQ.cDqDWLkvPDT7-VC3C9dUPVK7AV4')