import discord
from discord.ext import commands
import random

def setup(bot, default_categories):
    @bot.command()
    async def ping(ctx):
        await ctx.send('Pong!')

    @bot.command()
    async def flip(ctx):
        await ctx.send(random.choice(["heads", "tails"]))

    @bot.command()
    async def rps(ctx, hand):
        hands = ["👊", "🤚", "✂️"]
        bot_hand = random.choice(hands)
        if hand == bot_hand:
            await ctx.send(f"{bot_hand}\n\n{hand}{bot_hand}\n\nIt's a tie!")
        elif (hand == "👊" and bot_hand == "✂️") or (hand == "🤚" and bot_hand == "👊") or (hand == "✂️" and bot_hand == "🤚"):
            await ctx.send(f"{bot_hand}\n\n{hand}{bot_hand}\n\nYou win!")
        else:
            await ctx.send(f"{bot_hand}\n\n{hand}{bot_hand}\n\nYou lose!")

    @bot.command()
    async def roll(ctx):
        await ctx.send(random.randint(1, 6))

    @bot.command(aliases=["about"])
    async def help(ctx):
        myEmbed = discord.Embed(title="Help", description="List of commands", color=discord.Color.gold())
        myEmbed.add_field(name="!ping", value="Returns 'Pong!'")
        myEmbed.add_field(name="!flip", value="Flips a coin and returns 'heads' or 'tails'", inline=False)
        myEmbed.add_field(name="!rps <hand>", value="Play rock-paper-scissors with the bot")
        myEmbed.add_field(name="!roll", value="Rolls a dice and returns a number between 1 and 6", inline=False)
        myEmbed.add_field(name="!edit servername <name>", value="Changes the server name", inline=False)
        myEmbed.add_field(name="!setdefaultvoice <category>", value="Sets the default voice category", inline=False)
        myEmbed.add_field(name="!setdefaulttext <category>", value="Sets the default text category", inline=False)
        myEmbed.add_field(name="!edit createtextchannel <name>", value="Creates a text channel in the default text category", inline=False)
        myEmbed.add_field(name="!edit createvoicechannel <name>", value="Creates a voice channel in the default voice category", inline=False)
        myEmbed.add_field(name="!edit createrole <name>", value="Creates a role with the specified name", inline=False)
        myEmbed.add_field(name="!kick <member> [reason]", value="Kicks the specified member from the server", inline=False)
        myEmbed.add_field(name="!query <question>", value="Queries the Gemini API with your question and returns a response", inline=False)
        myEmbed.add_field(name="!pm", value="Sends a private message to you asking how the bot can help", inline=False)
        await ctx.send(embed=myEmbed)

    @bot.group()
    async def edit(ctx):
        pass

    @edit.command()
    async def servername(ctx, *name):
        name = "".join(i + " " for i in name)
        oldname = ctx.guild.name
        await ctx.guild.edit(name=name)
        await ctx.send(f"Server name changed from {oldname} to {name}")

    @bot.command()
    async def setdefaultvoice(ctx, *, category: discord.CategoryChannel):
        """Sets the default voice category."""
        default_categories['voice'] = category.name
        await ctx.send(f'Default voice category set to {category.name}')

    @bot.command()
    async def setdefaulttext(ctx, *, category: discord.CategoryChannel):
        """Sets the default text category."""
        default_categories['text'] = category.name
        await ctx.send(f'Default text category set to {category.name}')

    @edit.command()
    async def createtextchannel(ctx, *name):
        category_name = default_categories.get('text')
        name = "".join(i + " " for i in name)[:-1]
        category = discord.utils.get(ctx.guild.categories, name=category_name)
        await ctx.guild.create_text_channel(name, category=category)
        await ctx.send(f"Text channel {name} created in category {category.name if category else 'None'}")

    @edit.command()
    async def createvoicechannel(ctx, *name):
        category_name = default_categories['voice']
        name = "".join(i + " " for i in name)[:-1]
        category = discord.utils.get(ctx.guild.categories, name=category_name)
        await ctx.guild.create_voice_channel(name, category=category)
        await ctx.send(f"Voice channel {name} created in category {category_name}")

    @edit.command()
    async def createrole(ctx, *name):
        name = "".join(i + " " for i in name)[:-1]
        await ctx.guild.create_role(name=name)
        await ctx.send(f"Role {name} created")

    @bot.command()
    async def kick(ctx, member: discord.Member, *, reason=None):
        
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked")
    
    @bot.command()
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} has been banned")
    
 
    @bot.command()
    async def unban(ctx, *, user_name):
        banned_users = ctx.guild.bans()
        

        async for ban_entry in banned_users:
            
            user = ban_entry.user
            await ctx.send(user.mention)
            if user.mention == user_name:
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

