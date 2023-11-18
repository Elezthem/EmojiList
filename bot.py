from discord import Embed

@bot.command()
async def list_emojis(ctx):
    """
    `.list_emojis` Показывает эмодзи на данном сервере.
    """
    # Получаем список всех эмодзи на сервере
    emojis = ctx.guild.emojis

    # Создаем встроенное сообщение (embed)
    embed = Embed(color=0x2b2d31)  # Можете изменить цвет под свой стиль

    if emojis:
        emoji_names = ', '.join(str(emoji) for emoji in emojis)
        embed.description = f'Эмодзи на этом сервере: {emoji_names}'
    else:
        embed.description = 'На этом сервере нет собственных смайлов.'

    # Отправляем встроенное сообщение
    await ctx.send(embed=embed)
