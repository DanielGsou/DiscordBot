import discord
from key import token


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = token.get("TOKEN")

@client.event
async def on_ready():
    print(f"{client.user} está online!")



@client.event
async def on_message(message):

    conteudo = message.content
    l_conteudo = conteudo.lower()


    if message.author == client.user:
        return
    

    if l_conteudo.startswith("tierlist"): # COMO COLOCAMOS LOWERCASE ENTÃO TEM QUE SER TUDO EM MINUSCULO < 
        await message.channel.send(f"Toma a tierlist aqui filho da puta https://u.gg/lol/tier-list")
    
    if l_conteudo.startswith("test"):
        await message.channel.send(f"")

client.run(TOKEN)