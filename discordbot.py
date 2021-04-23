import discord
from discord.ext import commands
from discord.errors import ClientException
import json
import asyncio
from random import choice

hands = {
    "👊":{"win":"✋","lose":"✌️"},
    "✋":{"win":"✌️","lose":"👊"},
    "✌️":{"win":"👊","lose":"✋"}
}

messages = [
    "俺の勝ち！\nたかがじゃんけん、そう思ってないですか？\nそれやったら明日も俺が勝ちますよ。",
    "俺の勝ち！\n何で負けたか、明日まで考えといてください。\nそしたら何かが見えてくるはずです。",
    "俺の勝ち！\n負けは次につながるチャンスです！\nネバーギブアップ！"
]

bot = commands.Bot(command_prefix="$")
with open("token","r") as f:
    token = json.load(f)["DISCORD_BOT_TOKEN"]

def main():
    bot.run(token)


@bot.event
async def on_ready():
    print("start")


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)


@bot.command()
async def janken(ctx,hand = None):
    if hand == None or not hand in hands.keys():
        await ctx.send("\`\`\`\n You can put \":punch:\",\":raised_hand:\" or \":v:\" \n\`\`\`")
        return
    await ctx.send(hands[hand]["win"])
    await ctx.send(choice(messages))


if __name__ == '__main__':
    main()
    print("finish")
