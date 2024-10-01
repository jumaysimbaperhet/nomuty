from telethon import TelegramClient, events
import asyncio
from pystyle import Write, Colors, Center, Colorate

api_id = '25812027'
api_hash = 'c240a94b40c3af9ce927a0fe30730ccb'
bot_username = '@scorpion_network_bot'

def print_logo():
    logo = f"""                      
                    ,--.          ____   
                  ,--.'|        ,'  , `. 
              ,--,:  : |     ,-+-,.' _ | 
           ,`--.'`|  ' :  ,-+-. ;   , || 
           |   :  :  | | ,--.'|'   |  ;| 
           :   |   \ | :|   |  ,', |  ': 
           |   : '  '; ||   | /  | |  || 
           '   ' ;.    ;'   | :  | :  |, 
           |   | | \   |;   . |  ; |--'  
           '   : |  ; .'|   : |  | ,     
           |   | '`--'  |   : '  |/      
           '   : |      ;   | |`-'       
           ;   |.'      |   ;/           
           '---'        '---'            
                              
█████████████████████████████████████████████████

"""
    Write.Print(logo, Colors.white_to_green , interval=0.005)

async def search():
    print_logo()

    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()

    loop = asyncio.get_event_loop()
    bot_message = await loop.run_in_executor(None, lambda: input("[NM] Введите запрос -!> "))

    await client.send_message(bot_username, bot_message)
    search_message = await client.send_message(bot_username, '⏳ Идет поиск, ожидайте...')

    @client.on(events.NewMessage(chats=bot_username))
    async def handler(event):
        message = event.message

        if '⏳ Идет поиск, ожидайте...' in message.text:
            Write.Print("[INFO] Идет поиск...\n", Colors.white_to_green, interval=0.000005)
            return

        Write.Print(f"[NM] RESULT -!> \n: {message.text}", Colors.white_to_green, interval=0.000005)

        if message.media and message.media.document:
            document = message.media.document
            if document.mime_type == 'text/html':
                file_path = await client.download_media(message, file='searchbyscorpion.html')
                Write.Print(f"\nHTML файл скачан: {file_path}", Colors.white_to_green, interval=0.000005)
            else:
                Write.Print("\nПрикрепленный файл не является HTML.", Colors.white_to_green, interval=0.000005)
        else:
            Write.Print(f"[NM] RESULT - !> \n{message.text}", Colors.white_to_green, interval=0.000005)

        await client.delete_messages(bot_username, search_message.id)
        await client.disconnect()

    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(search())
    input()
