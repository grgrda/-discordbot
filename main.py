import discord
from discord.ext import commands
import os
import asyncio
import keep_alive

bot = commands.Bot(command_prefix="x.")
bot.remove_command("help")

@bot.event
async def on_ready():
  print('起動しました')

color = 0x621fb5

@bot.command()
async def help(ctx):
  em=discord.Embed(
    description="好きなように書いてください",color=color
  )
  await ctx.send(embed=em)

@bot.command()
async def kick(ctx, user: discord.Member):
  if ctx.author.guild_permissions.administrator:
    await user.kick()
    await ctx.send(f"{user}をサーバーからkickしました")

@bot.command()
async def ban(ctx, user: discord.Member):
  if ctx.author.guild_permissions.administrator:
    await user.ban()
    await ctx.send(f"{user}をサーバーからbanしました")

@bot.command()
async def clear(ctx,arg : int):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=arg)
        embed=discord.Embed(title="", description="メッセージの削除できました！", color=color)
        await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1)
    else:
        embed=discord.Embed(title="", description="このコマンドは管理者専用ですよ！", color=color)
        await ctx.channel.send(embed=embed)
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=2)

keep_alive.keep_alive()
bot.run(os.getenv("token"))