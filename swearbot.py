import time
import sys
import discord
from discord_webhook import DiscordWebhook, DiscordEmbed

shitlist = ["shit", "fuck", "bitch", "lesss gooooooo"]

piplist = ["@Inspector Esperie", "@blazemob", "@TK-0456",]

randomshit = random.randint(shitlist)

randompip = random.randint(piplist

    while True:
            webhook = DiscordWebhook(
                url='https://discord.com/api/webhooks/833812343917772840/T86mdx3uhg-3-VFwNAGxXUdwXmHLVqFz2N4S_U3Fwifa8SUlkXT6tcJ3YJ_kSqdl51xd',
                content=randompip+" is "+randomshit
            response = webhook.execute()
