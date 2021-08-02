import requests, bs4
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 
 
@bot.command()
async def decodeqr(ctx, *, decodeqr):
    url = requests.get("https://zxing.org/w/decode?u=" + decodeqr)
    codigoQR = bs4.BeautifulSoup(url.content, "html.parser")
    decode = codigoQR.find("pre").text
    await ctx.send(decode) 
   
 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run('') #OBTEN UN TOKEN EN: https://discord.com/developers/applications







 

    
