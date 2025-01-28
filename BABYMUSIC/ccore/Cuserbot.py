from pyrogram import Client
from ..logging import LOGGER
from BABYMUSIC.utils.database import clonebotdb
assistants = []
assistantids = []

class CUserbot(Client):
    def __init__(self, session_string, assistant_name):
        # Initialize with a specific session string and assistant name
        self.one = Client(
            name=assistant_name,
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(session_string),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        if self.one.session_string:
            await self.one.start()
            try:
                await self.one.join_chat("world_friend_chatting_zone")
                await self.one.join_chat("world_friend_chatting_zone")
            except:
                pass
            assistants.append(self.one)
            try:
                await self.one.send_message(config.LOGGER_ID, f"{self.one.name} Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant {self.one.name} has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")


    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if self.one.session_string:
                await self.one.stop()
        except:
            pass


async def start_all_assistants():
    # Fetch all session names from the database
    sessions = clonebotdb.find({})  # Assuming the sessions are stored in a collection

    for session in sessions:
        session_string = session.get('session_string')  # Assuming 'session_string' field contains session data
        assistant_name = session.get('assistant_name', 'DefaultAssistant')  # Assuming you store assistant names
        
        if session_string:
            # Create and start a Userbot for each session
            userbot = Userbot(session_string, assistant_name)
            await userbot.start()

    LOGGER(__name__).info(f"Started {len(assistants)} assistants successfully.")
