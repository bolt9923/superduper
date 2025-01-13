HELP_1 = """<b><u>ADMIN COMMANDS :</b></u>

Just add <b>ᴄ</b> in the starting of the commands to use them for channel.


/pause : Pause the current playing stream.

/resume : Resume the paused stream.

/skip : Skip the current playing stream and start streaming the next track in queue.

/end ᴏʀ /stop : Clears the queue and end the current playing stream.

/player : Get a interactive player panel.

/queue : Shows the queued tracks list.
"""

HELP_2 = """
<b><u>AUTH USERS :</b></u>

Auth users can use admin rights in the bot without admin rights in the chat.

/auth [username/user_id] : Add a user to auth list of the bot.
/unauth [username/user_id] : Remove a auth users from the auth users list.
/authusers : Shows the list of auth users of the group.
"""

HELP_3 = """
<u><b>BROADCAST FEATURES</b></u> [only for sudors] :

/broadcast [message or reply to a message] : broadcast a message to served chats of the bot.

<u>Broadcasting modes:</u>
<b>-pin</b> : Pins your broadcasted messages in served chats.
<b>-pinloud</b> : Pins your broadcasted message in served chats and send notification to the members.
<b>-user</b> : Broadcasts the message to the users who have started your bot.
<b>-assistant</b> : Broadcast your message from the assistant account of the bot.
<b>-nobot</b> : Forces the bot to not broadcast the message.

<b>Example:</b> <code>/broadcast -user -assistant -pin testing broadcast</code>
"""


HELP_4 = """<u><b>CHAT BLACKLIST FEATURES :</b></u> [only for sudors]

Restrict shit chats to use our precious bot.

/blacklistchat [chat ID] : Blacklist a chat from using the bot.
/whitelistchat [chat ID] : Whitelist the blacklisted chat.
/blacklistedchat : Shows the list of blacklisted chats.
"""


HELP_5 = """
<u><b>BLOCK USERS:</b></u> [only for sudors]

Starts ignoring the blacklisted user, so that he can't use bot commands.

/block [username or reply to a user] : Block the user from our bot.
/unblock [username or reply to a user] : Unblocks the blocked user.
/blockedusers : Shows the list of blocked users.
"""

HELP_6 = """
<u><b>CHANNEL PLAY COMMANDS :</b></u>

You can stream audio/video in channel.

/cplay : Starts streaming the requested audio track on channel's videochat.
/cvplay : Starts streaming the requested video track on channel's videochat.
/cplayforce or /cvplayforce : Stops the ongoing stream and starts streaming the requested track.

/channelplay [chat username or ID] or [disable] : Connect channel to a group and starts streaming tracks by the help of commands sent in group.
"""

HELP_7 = """
<u><b>GLOBAL BAN FEATURES</b></u> [only for sudors] :

/gban [username or reply to a user] : Globally bans the chutiya from all the served chats and blacklists him from using the bot.
/ungban [username or reply to a user] : Globally unbans the globally banned user.
/gbannedusers : Shows the list of globally banned users.
"""

HELP_8 = """
<b><u>LOOP STREAM :</b></u>

<b>Starts streaming the ongoing stream in loop</b>

/loop [enable/disable] : Enables/Disables loop for the ongoing stream
/loop [1, 2, 3, ...] : Enables the loop for the given value.
"""


HELP_9 = """
<u><b>MAINTENANCE MODE</b></u> [only for sudors] :

/logs : Get logs of the bot.

/logger [enable/disable] : Bot will start logging the activities happen on bot.

/maintenance [enable/disable] : Enable or disable the maintenance mode of your bot.
"""

HELP_10 = """
<b><u>PING & STATS :</b></u>

/start : Starts the music bot.
/help : Get help menu with explanation of commands.

/ping : Shows the ping and system stats of the bot.

/stats : Shows the overall stats of the bot.
"""

HELP_11 = """
<u><b>PLAY COMMAND :</b></u>

<b>v :</b> Stands for video play.
<b>force :</b> Stands for force play.

/play or /vplay : Starts streaming the requested track on videochat.

/playforce or /vplayforce : Stops the ongoing stream and starts streaming the requested track.
"""

HELP_12 = """
<b><u>SHUFFLE QUEUE :</b></u>

/shuffle : Shuffles the queue.
/queue : Shows the shuffled queue.
"""

HELP_13 = """
<b><u>SEEK STREAM :</b></u>

/seek [duration in seconds] : Seek the stream to the given duration.
/seekback [duration in seconds] : Backward seek the stream to the given duration.
"""

HELP_14 = """
<b><u>SONG DOWNLOAD :</b></u>

/song [song name/yt url] : Download any track from YouTube in mp3 or mp4 formats.
"""

HELP_15 = """
<b><u>SPEED COMMAND :</b></u>

You can control the playback speed of the ongoing stream. [Admins only]

/speed or /playback : For adjusting the audio playback speed in group.
/cspeed or /cplayback : For adjusting the audio playback speed in channel.
"""


# New Clone Bot
CLONE_HELP = """
<b><u>CLONE COMMAND :</b></u>

Give Bot Token After /clone Command From @Botfather.
"""

HELP_16 = """
<b><u>GPT ai COMMAND :</b></u>
/ask : Queries the ai model to get a response to your questions.
"""

HELP_17 = """
<b><u>STICKER COMMAND :</b></u>

/packkang : Creates a pack of stickers from a other pack.
/stickerid : Get the stickers id of a sticker.
"""

HELP_18 = """
<b><u>TAG COMMAND : </b></u>

/gmtag : Good morning 
Tag stop : /gmstop

/gntag : Good night tag stop ⇴ /gnstop

/tagall : Random message tag stop ⇴ /tagoff /tagstop

/hitag : Random hindi message tag stop ⇴/histop

/shayari : Random shayari tag stop ⇴ /shstop

/utag : Any written text tag stop ⇴ /cancel 

/vctag : Voice chat invite tag stop ⇴ /vcstop
"""


HELP_19 = """
<b><u>INFO COMMAND :</b></u>

/id : Get the current group ID. If used by replying to a message, gets that user's ID.
/info : Get information about a user.
/github <username> : Get information about a GitHub user.
"""

HELP_20 = """
<b><u>GROUP COMMAND :</b></u>

These are the available group management commands:

/pin : Pins a message in the group.
/pinned : Displays the pinned message in the group.
/unpin : Unpins the currently pinned message.
/staff : Displays the list of staff members.
/bots : Displays the list of bots in the group.
/settitle : Sets the title of the group.
/setdiscription : Sets the description of the group.
/setphoto : Sets the group photo.
/removephoto : Removes the group photo.
/zombies : Removes deleted members from the group.
/imposter on/off : Turns on or off the watcher for your group, which notifies about users who change their name or username.
"""

HELP_21 = """
<b><u>EXTRA COMMAND :</b></u>

/math : Solves mathematical problems and equations.
/blackpink : Generates a blackpink-style logo.
/carbon : Generates a carbon code image from a code snippet.
/speedtest : Measures the internet speed.
/reverse : Reverses a given text.
/webss : Takes a screenshot of a website.
/paste : Uploads a text snippet to the cloud and provides a link.
/tgm : Uploads a photo (under 5MB) to the cloud and provides a link.
/tr : Translates text.
/google : Searches for information on Google.
/stack : Searches for programming-related information on Stack Overflow.
"""

HELP_22 = """
<b><u>IMAGE COMMAND :</b></u>

/draw : Generates a drawing based on a given prompt.
/image : Searches for an image based on a given keyword.
/upscale : Reply to an image to upscale it and improve its quality.
"""

HELP_23 = """
<b><u>ACTION COMMAND :</b></u>

Available commands for Bans & Mute:

❍ /kickme: Kicks the user who issued the command.

Admins only:
❍ /ban <userhandle>: Bans a user. (via handle, or reply)
❍ /sban <userhandle>: Silently bans a user. Deletes command, Replied message and doesn't reply. (via handle, or reply)
❍ /tban <userhandle> x(m/h/d): Bans a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
❍ /unban <userhandle>: Unbans a user. (via handle, or reply)
❍ /kick <userhandle>: Kicks a user out of the group, (via handle, or reply)
❍ /mute <userhandle>: Silences a user. Can also be used as a reply, muting the replied to user.
❍ /tmute <userhandle> x(m/h/d): Mutes a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
❍ /unmute <userhandle>: Unmutes a user. Can also be used as a reply, unmuting the replied to user.
__
Special Commands Support All Example - Yumi ban Yumi mute Yumi promote ..... etc
"""

HELP_24 = """

<b><u>SEARCH COMMAND :</b></u>

• /google <query> : Search the google for the given query.
• /anime <query>  : Search myanimelist for the given query.
• /stack <query>  : Search stackoverflow for the given query.
• /image (/imgs) <query> : Get the images regarding to your query

Example:
/google pyrogram: return top 5 reuslts.
"""
