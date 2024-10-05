import discord

def setup(bot):
    @bot.event
    async def on_ready():
        print("Bot is ready")

    @bot.event
    async def on_member_join(member):
        guild = member.guild
        guild_name = guild.name
        dm_channel = await member.create_dm()
        await dm_channel.send(f"Welcome to {guild_name} {member.display_name}")

    @bot.event
    async def on_raw_reaction_add(payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        guild = bot.get_guild(guild_id)
        member = payload.member
        emoji = payload.emoji.name
        if message_id == 1291067776093655210:
            if emoji == "♂️":
                role = discord.utils.get(guild.roles, name="Male")
            elif emoji == "♀️":
                role = discord.utils.get(guild.roles, name="Female")
            elif emoji == "emoji_20":  # Thanos face emoji
                role = discord.utils.get(guild.roles, name="Gay")

            await member.add_roles(role)

    @bot.event
    async def on_raw_reaction_remove(payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        guild = bot.get_guild(guild_id)
        member = guild.get_member(payload.user_id)
        emoji = payload.emoji.name
        if message_id == 1291067776093655210:
            if emoji == "♂️":
                role = discord.utils.get(guild.roles, name="Male")
            elif emoji == "♀️":
                role = discord.utils.get(guild.roles, name="Female")
            elif emoji == "emoji_20":  # Thanos face emoji
                role = discord.utils.get(guild.roles, name="Gay")

            await member.remove_roles(role)
