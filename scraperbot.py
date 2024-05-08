import discord
import os
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.all()
client = commands.Bot(command_prefix = 's!', intents=intents)

@client.event
async def on_ready():
	print("scraper is initiated")
	await client.change_presence(status = discord.Status.online,activity = discord.Game("scraper"))

client.remove_command('help')
 
@client.command()
async def scrape(ctx, url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	img_tags = soup.find_all('img')

	for img in img_tags:
		try:
			img_url = img['src']
			filename = os.path.basename(img_url)
			if not "logo" in filename and not "Logo" in filename and not "icon" in filename and not "Icon" in filename and not "svg" in filename:
				await ctx.send(file=discord.File(filename))
				print(f"sent {filename}")
		except Exception as e:
			print(f"Error sending image: {e}")
   
client.run("token")
