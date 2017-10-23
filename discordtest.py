import discord
from discord.ext.commands import Bot
from discord.ext import commands
from html.parser import HTMLParser
import feedparser
import time

d = feedparser.parse('http://rssblog.ameba.jp/tamai-sd/rss20.xml')
previousPost = d.entries[0]
Client = discord.Client()
bot_prefix= "!"
client = commands.Bot(command_prefix=bot_prefix)

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

@client.event
async def on_ready():
	print("Bot Online!")
	print("Name: {}".format(client.user.name))
	print("ID: {}".format(client.user.id))
	
@client.command(pass_context=True)
async def ping(ctx):
	embed = discord.Embed(title="", description="Pong!", color=0x00ff00)
	await client.say(embed=embed)

@client.command(pass_context=True)
async def feed(ctx):
	begin = "https://stat.ameba.jp/user_images"
	end = ".jpg"
	p = d.entries[0].summary
	embed = discord.Embed(title="{}".format(d.feed.title), description="{}\n\nLatest post:".format(d.feed.link), color=0xffff00)
	embed.add_field(name="{}".format(d.entries[0].title), value="{}\n{}".format(strip_tags(d.entries[0].summary),d.entries[0].link), inline=False)
	embed.set_thumbnail(url="{}".format(p[p.find(begin):p.find(end)+4]))
	await client.say(embed=embed)

@client.command(pass_context=True)
async def blogtest(ctx):
	begin = "https://stat.ameba.jp/user_images"
	end = ".jpg"
	p = d.entries[0].summary
	embed = discord.Embed(title="{}".format(d.entries[0].title), description="", color=0x00ff00)
	embed.set_thumbnail(url="{}".format(p[p.find(begin):p.find(end)+4]))
	await client.say(embed=embed)
	
@client.command(pass_context=True)
async def jstest(ctx):
	embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
	await client.say(embed=embed)
	
@client.command(pass_context=True)
async def repeat(ctx):
	for apples in range(0,10):
		embed = discord.Embed(title="Title", description="Desc {}".format(apples), color=0x00ff00)
		await client.say(embed=embed)
		time.sleep(5)
	
client.run("MzcxOTE0ODgxMjI3NTU0ODE2.DM8kQg.-96rQd566TiCJaJa2boLn-XXR-g")