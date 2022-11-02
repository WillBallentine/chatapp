#discordchatbot

import discord
import random
import os
#from dotenv import load_dotenv
from neuralintents import GenericAssistant
import ssl
from googlesearch import search


chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

print('Bot Running...')

client = discord.Client()

#load_dotenv()
#TOKEN = os.getenv('TOKEN')
TOKEN = ('insert token here')




@client.event
async def on_message(message):
	#
	coin = ['heads', 'tails']


	if message.author == client.user:
		return
	if message.content.startswith('/pretendwill'):
		response = chatbot.request(message.content[7:])
		await message.channel.send(response)

	if message.content.startswith('/help'):
		await message.channel.send("I am just chatting for now but more coming soon! Real me is building out my features!")

	if message.content.startswith('/commands'):
		await message.channel.send("/pretendwill - chat with me \n /help - see my feature set \n /commands - get a list of active commands to use \n /chris - who is Chris? \n /jason - who is Jason? \n /flip - Flip a coin \n /math - Follow prompts for math")

	if message.content.startswith('/chris'):
		await message.channel.send(file=discord.File('chris.png'))

	if message.content.startswith('/jason'):
		await message.channel.send(file=discord.File('jason.png'))

	if message.content.startswith('/flip'):
		await message.channel.send(random.choice(coin))

	if message.content.startswith('/math'):
	    def check(m):
	        return len(m.content) >= 1

	    await message.channel.send("Number 1: ")
	    number_1 = await client.wait_for("message", check=check)
	    await message.channel.send("Operator: ")
	    operator = await client.wait_for("message", check=check)
	    await message.channel.send("number 2: ")
	    number_2 = await client.wait_for("message", check=check)
	    try:
	        number_1 = float(number_1.content)
	        operator = operator.content
	        number_2 = float(number_2.content)
	    except:
	        await message.channel.send("invalid input")
	        return
	    output = None
	    if operator == "+":
	        output = number_1 + number_2
	    elif operator == "-":
	        output = number_1 - number_2
	    elif operator == "/":
	        output = number_1 / number_2
	    elif operator == "*":
	        output = number_1 * number_2
	    else:
	        await message.channel.send("invalid input")
	        return
	    await message.channel.send("Answer: " + str(output))

	if message.content.startswith('/google'):
		async def check(m):
			return len(m.content) >1
		await message.channel.send("What would you like to look up?: ")
		google_search = await client.wait_for("message", check=check)
		google_search2 = str(google_search)
		google_answer = []
		for j in search(google_search2, num_results=1, lang="en"):
			google_answer.append(j)

		final = str(google_answer)
		

		await message.channel.send(final)

client.run(TOKEN)
