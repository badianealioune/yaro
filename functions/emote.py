from highrise import *
from highrise.models import *
from highrise.webapi import *
from highrise.models_webapi import *

async def emote(self: BaseBot, user: User, message: str) -> None:
    try:
        command, target, emote_id = message.split(" ")
    except:
        await self.highrise.chat("Invalid command format. Please use '/emote <target> <emotename>.")
        return
    user = (await self.webapi.get_users(username=target))
    if user.total == 0:
        await self.highrise.chat("Invalid target.")
        return
    user_id = user.users[0].user_id
    try:
        await self.highrise.send_emote(emote_id, user_id)
    except:
        await self.highrise.chat("Invalid emote.")
        return