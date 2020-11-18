import discord
from discord.ext import commands


class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self, guild):
        try:
            self.bot.load_extension("events.ready")
        except Exception:
            pass

        self.bot.logging(f"Bot:{self.bot.user}")
        self.bot.logger.info(f"D: {self.bot.user.id}")
        self.bot.logging.info(f"Guilds: {len(self.bot.guilds)}")
        self.bot.logger.info(f"Users: {len(self.bot.users)}")
        

def setup(bot):
    try:
        bot.add_cog(Ready(bot))
        bot.logging.info(f"$REENLoaded event $CYANReady!")
    except Exception:
        bot.logger.error(
            f'$REDError while loading event $CYANReady'
        )