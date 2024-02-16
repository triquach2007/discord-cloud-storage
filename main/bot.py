from data_uploading.data_process import *
from data_downloading.data_processing import *
from data_storage.data_storaging import *
from constant import DOWNLOAD_PATH
import typing
import logging
import discord
import io
import os

class Upload_Bot(discord.Client):
    async def on_ready(self):
        logging.info("Start sending data")

        channel = self.get_channel(1207612400971419688)
        for file_number, file in enumerate(load_up_files()):
            logging.info(f"File #{file_number}")
            channel.send(os.path.basename(file))

            messages_id = []
            for splitted_file_number, splitted_file in enumerate(split_up_file(file)):
                logging.info(f"Sub-file #{splitted_file_number}")
                message = await channel.send(file=discord.File(io.BytesIO(splitted_file), f"{os.path.basename(file)}_{splitted_file_number:04d}"))
                messages_id.append(message.id)
            

            delete_file_in_upload_buffer(os.path.basename(file))
            new_file_entry(os.path.basename(file), messages_id)

            logging.info(f"Completed sending file #{file_number}")

        logging.info("Completed sending data")
        await self.close()


class Download_Bot(discord.Client):
    def __init__(self, file_name:str, *, intents: discord.Intents, **options: typing.Any) -> None:
        super().__init__(intents=intents, **options)
        self.download_file_name = file_name

    async def on_ready(self):
        logging.info("Start downloading file")
        delete_file_in_download_buffer()

        channel = self.get_channel(1207612400971419688)
        for msg_number, msg_id in enumerate(load_entry(self.download_file_name)["message_ids"]):
            logging.info(f"Downloading sub-file #{msg_number}")
            msg = await channel.fetch_message(msg_id)
            await msg.attachments[0].save(f"./main/download_buffer/{msg.attachments[0].filename}")


        save_file_name = self.download_file_name
        i = 1
        while os.path.exists(os.path.join(DOWNLOAD_PATH, save_file_name)):
            save_file_name = f"{os.path.splitext(self.download_file_name)[0]} ({i}){os.path.splitext(self.download_file_name)[1]}"
            i+=1
            
        with open(os.path.join(DOWNLOAD_PATH, save_file_name), "wb") as f:
            f.write(join_data())
        
        delete_file_in_download_buffer()
        await self.close()