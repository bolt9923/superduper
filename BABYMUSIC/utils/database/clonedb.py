from BABYMUSIC.core.mongo import mongodb, pymongodb
from typing import Dict, List, Union

cloneownerdb = mongodb.cloneownerdb
clonebotdb = pymongodb.clonebotdb
clonebotnamedb = mongodb.clonebotnamedb
users_collection = mongodb.users
referrals_collection = mongodb.referrals  # New collection for storing referral data

# Save user data
async def save_user(user_id: int):
    await users_collection.insert_one({
        "user_id": user_id,
        "points": 0,
        "referrals": 0,
        "referrer": None  # Initially, there's no referrer
    })

# Update user's points
async def update_user_points(user_id: int, new_points: int):
    await users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"points": new_points}}
    )

# Update user data (like referrer)
async def update_user_data(user_id: int, update_data: Dict):
    await users_collection.update_one(
        {"user_id": user_id},
        {"$set": update_data}
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

# Save referral data (new function)
async def save_referral(user_id: int, referrer_id: int):
    # Ensure the referral is only saved once
    existing_referral = await referrals_collection.find_one({"user_id": user_id})
    if existing_referral:
        return False  # Referral already used
    else:
        # Save referral information
        await referrals_collection.insert_one({
            "user_id": user_id,
            "referrer_id": referrer_id
        })
        
        # Update the user's referrer field in the users collection
        await users_collection.update_one(
            {"user_id": user_id},
            {"$set": {"referrer": referrer_id}}
        )
        return True  # Referral saved successfully

# Check if a user has already used a referral (new function)
async def has_used_referral(user_id: int) -> bool:
    user_data = await get_user_data(user_id)
    if user_data and user_data.get("referrer"):
        return True  # Referral has been used
    return False  # No referrer set, meaning no referral used

# Save clone bot owner
async def save_clonebot_owner(bot_id, user_id):
    await cloneownerdb.insert_one({"bot_id": bot_id, "user_id": user_id})

# Get clone bot owner
async def get_clonebot_owner(bot_id):
    result = await cloneownerdb.find_one({"bot_id": bot_id})
    if result:
        return result.get("user_id")
    else:
        return False

# Save clone bot username
async def save_clonebot_username(bot_id, user_name):
    await clonebotnamedb.insert_one({"bot_id": bot_id, "user_name": user_name})

# Get clone bot username
async def get_clonebot_username(bot_id):
    result = await clonebotnamedb.find_one({"bot_id": bot_id})
    if result:
        return result.get("user_name")
    else:
        return False
