import interactions

class PingPong(interactions.Extension):
    @interactions.slash_command("ping", description="Ping pong!")
    async def ping(self, ctx: interactions.SlashContext):
        """A command to ping pong"""
        await ctx.send("Pong3!")
