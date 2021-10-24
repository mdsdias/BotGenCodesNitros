import discord
from discord.ext import commands
import random
import requests as rq
import json as j

class DevCommands(commands.Cog, name='Bot nitro gen'):
    '''The nitro gen :D'''
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="nitro")
    async def nitro(self, message):
        limit = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9".split()
        code = ''
        cod1 = random.choice(limit)
        cod2 = random.choice(limit)
        cod3 = random.choice(limit)
        cod4 = random.choice(limit)
        cod5 = random.choice(limit)
        cod6 = random.choice(limit)
        cod7 = random.choice(limit)
        cod8 = random.choice(limit)
        cod9 = random.choice(limit)
        cod10 = random.choice(limit)
        cod11 = random.choice(limit)
        cod12 = random.choice(limit)
        cod13 = random.choice(limit)
        cod14 = random.choice(limit)
        cod15 = random.choice(limit)
        cod16 = random.choice(limit)
        cod17 = random.choice(limit)
        cod18 = random.choice(limit)
        cod19 = random.choice(limit)
        cod20 = random.choice(limit)
        cod21 = random.choice(limit)
        cod22 = random.choice(limit)
        cod23 = random.choice(limit)
        cod24 = random.choice(limit)
        code = cod1+cod2+cod3+cod4+cod5+cod6+cod7+cod8+cod9+cod10+cod11+cod12+cod13+cod14+cod15+cod16+cod17+cod18+cod19+cod20+cod21+cod22+cod23+cod24
        uri = f"http://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        r = rq.get(uri)
        r = j.loads(r.text)
        if r['message'] == "Unknown Gift Code":
            await message.channel.send("Codigo invalido gerado")
        else:
            await message.author.send("discord.gift/"+code)

def setup(bot):
    bot.add_cog(DevCommands(bot))
