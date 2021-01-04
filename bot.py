import discord
import numpy as np
from discord.ext import commands
from boto.s3.connection import S3Connection
token = S3Connection(os.environ['TOKEN'])


client = commands.Bot(command_prefix='pls ')


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def milo(ctx):
    index = np.random.randint(1, 30)
    filename = (f'milo{index}.jpg')
    await ctx.send(file=discord.File(filename))


@client.command()
async def ping(ctx):
    await ctx.send(f'the ping is {client.latency * 1000} milliseconds')


@client.command(aliases=['8ball', 'ask'])
async def _8ball(ctx, *, question):

    responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Reply hazy, try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes – definitely.',
                 'You may rely on it.']
    await ctx.send(random.choice(responses))


@client.command(aliases=['leave', 'die', 'stop', 'quit'])
async def exit(ctx):
    fuckoff = ['no', 'fuck off', 'can\'t let you do that']
    await ctx.send(random.choice(fuckoff))


@client.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount + 1)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
async def manual_override(ctx):
    while True:
        var = input("Message: ")
        await ctx.send(var)

        var2 = input("Continue? (y/n)")
        if var2 == 'n':
            break


client.run(token)
