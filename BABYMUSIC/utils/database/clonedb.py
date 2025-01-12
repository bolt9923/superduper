from BABYMUSIC.core.mongo import mongodb, pymongodb
from typing import Dict, List, Union

cloneownerdb = mongodb.cloneownerdb
clonebotdb = pymongodb.clonebotdb
clonebotnamedb = mongodb.clonebotnamedb
users_collection = mongodb.users

async def save_user(user_id: int):
    await users_collection.insert_one({
        "user_id": user_id,
        "points": 0,
        "referrals": 0
    })

# Update user's points
async def update_user_points(user_id: int, new_points: int):
    await users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"points": new_points}}
    )
# Get user data
async def get_user_data(user_id: int) -> Union[Dict, None]:
    return await users_collection.find_one({"user_id": user_id})

# Update referrer points and referrals
async def update_referrer(referrer_id: int):
    await users_collection.update_one(
        {"user_id": referrer_id},
        {"$inc": {"points": 20, "referrals": 1}}
    )

# clone bot owner
async def save_clonebot_owner(bot_id, user_id):
    await cloneownerdb.insert_one({"bot_id": bot_id, "user_id": user_id})


async def get_clonebot_owner(bot_id):
    result = await cloneownerdb.find_one({"bot_id": bot_id})
    if result:
        return result.get("user_id")
    else:
        return False


async def save_clonebot_username(bot_id, user_name):
    await clonebotnamedb.insert_one({"bot_id": bot_id, "user_name": user_name})


async def get_clonebot_username(bot_id):
    result = await clonebotnamedb.find_one({"bot_id": bot_id})
    if result:
        return result.get("user_name")
    else:
        return False
