import os

import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.repolink = "https://github.com/ShamsAnsari/ImageBot"
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        description = f'[:robot: Invite me!]({os.environ.get("INVITE")})\n[:information_source: Github Repo]({self.repolink})'
        e = discord.Embed(color=discord.Color.purple(), title="Help Menu", description=description)
        e.add_field(name="*grab", value="• Type \"\*grab\" followed by a couple words to search for an image."
                                        + "\n• Can also type \\*grab <n> followed by a couple words to search for the nth image."
                                        + "\n• For example \"\*grab <5> apple pie\"",
                    inline=False)
        e.add_field(name="*help", value="Type \"*help\" for the help menu", inline=False)
        e.set_image(url="https://media.giphy.com/media/Lt5eOpMHfyHveYg8Bu/giphy.gif")
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Misc(bot))
