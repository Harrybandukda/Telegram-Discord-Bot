from telethon import TelegramClient, events, sync
import config as env
from discord_webhook import DiscordWebhook, DiscordEmbed

client = TelegramClient('DISCORDTELEGRAMBOT', env.API_ID, env.API_HASH)

@client.on(events.NewMessage())
async def printMessage(event):

    try:
        
        if event.peer_id.channel_id == env.FORWARD_ID:
            print("GROUP/CHANNEL NAME")
            await forwardToWebhook(event, env.FORWARD_WB)

        if event.peer_id.channel_id == env.FORWARD2_ID:
            print("GROUP/CHANNEL NAME")
            await forwardToWebhook(event, env.FORWARD2_WB)

        if event.peer_id.channel_id == env.FORWARD3_ID:
            print("GROUP/CHANNEL NAME")
            await forwardToWebhook(event, env.FORWARD3_WB)

        ##################################################################################
        #ADD MORE 
        #if event.peer_id.channel_id == env.FORWARD4_ID:
        #print("GROUP/CHANNEL NAME")
        #await forwardToWebhook(event, env.FORWARD4_WB)            
                         
    except Exception as e:
        print(f'{e} \n {event.message.message}')


async def forwardToWebhook(event, webhookUrl, addExtraContent = True, 
includeDifferentFooter = False, fromeveryone = False):

    hasImage = False
    image_path = ''

    if addExtraContent:
        webhook = DiscordWebhook(url = webhookUrl)
    else:
        #Add @everyone tag to the forward msg, if needed set True
        if fromeveryone:
            webhook = DiscordWebhook(url = webhookUrl, content='@everyone')
        else:
            webhook = DiscordWebhook(url = webhookUrl)

    if event.message.photo:
        image_path = await client.download_media(event.message.photo,
                                                 "img_test.jpg")
        hasImage = True
        print('File saved to', image_path)

    if hasImage:
        with open(image_path, "rb") as f:
            webhook.add_file(file=f.read(), filename='img_test.jpg')

    # create embed object for webhook
    embed = DiscordEmbed(description=event.message.message, inline=False)
    if addExtraContent:
        if not includeDifferentFooter:
            embed.set_footer(text='Extra Footer®') # If you want to have different footer for different channel u can change this. To enable set True
        else:
            embed.set_footer(text='First Footer') # This would be your primary footer.

    # set image
    if hasImage:
        embed.set_image(url='attachment://img_test.jpg')

    # add embed object to webhook
    webhook.add_embed(embed)

    response = webhook.execute()
    print(response)

client.start()
client.run_until_disconnected()