import discum
from time import sleep

bot = discum.Client(token='OTY2ODQxMTk0NjA2ODg2OTEz.YmXW0g.0o4wP0TIs8DI3_p2aW1NCKeAJ64', log=False)

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members


members = get_members('958682005204258897', '963782576496050267')
memberslist = []

for memberID in members:
    if (memberID != "966841194606886913"):
        memberslist.append(memberID)

f = open("users.txt", "a")
for element in memberslist:
    f.write(element + "\n")
f.close()

# @bot.gateway.command
# def helloworld(resp):
#     if resp.event.ready_supplemental: #ready_supplemental is sent after ready
#         user = bot.gateway.session.user
#         print("Logged in as {}#{}".format(user['username'], user['discriminator']))
#         for memberID in memberslist:
#             print(memberID)
#             newDM = bot.createDM([memberID]).json()["id"]
#             bot.sendMessage(newDM, "This will the ads message")
#     if resp.event.message:
#         m = resp.parsed.auto()
#         guildID = m['guild_id'] if 'guild_id' in m else None #because DMs are technically channels too
#         channelID = m['channel_id']
#         username = m['author']['username']
#         discriminator = m['author']['discriminator']
#         content = m['content']
#         if content == "Hello guys":
#             print("Running ads")
#
#
#         print("> guild {} channel {} | {}#{}: {}".format(guildID, channelID, username, discriminator, content))
#
# bot.gateway.run(auto_reconnect=True)

import discord

text = """
Hello, this is PolyLolis ads message
Hello we are the PolyLolis a new project on the polygon blockchain which is committed to providing value to our community in a variety of different 
🍭 Giveaways 🍭
🍭 Staking 🍭
🍭 Mutations 🍭
🍭 Downloadable Game 🍭
🍭 A comic book which will portray the nfts origin story and give all revenue to holders 🍭

 Discord is not even a week old so join early to secure a easy WL spot 
https://discord.gg/3ZJUwNeY9A
"""

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        print("Logged in using the thing")
        for memberID in memberslist:
            sleep(20)
            try:
                user = await client.fetch_user(memberID)
                sleep(1)
                await user.send(text)
            except Exception as e:
                print(e)
        #DMChannel = await self.create_dm("966841194606886913")
        #await DMChannel.send("Hello")

    async def on_message(self, message):

        try:
            print("Guild ID: " + str(message.guild.id) + ", Channel ID: " + str(message.channel.id) + ", Message Content: " + str(message.content))
        except Exception as e:
            print(e)
client = MyClient()
client.run('OTY2ODQxMTk0NjA2ODg2OTEz.YmXW0g.0o4wP0TIs8DI3_p2aW1NCKeAJ64')
