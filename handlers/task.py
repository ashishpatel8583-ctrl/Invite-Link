from pyrogram import Client, filters
from database.mongo import tasks
import time

GROUP_B_ID = -5032773808  # Task Group
GROUP_A_ID = -5082882000  # Main Group

@app.on_message(filters.command("task") & filters.private)
async def task(client, message):
    user_id = message.from_user.id

    # Check if already completed
    data = await tasks.find_one({"user_id": user_id})
    if data and data.get("completed") == 1:
        return await message.reply("You already completed the task and received main link.")

    # Generate 10-member invite
    invite = await client.create_chat_invite_link(
        chat_id=GROUP_B_ID,
        member_limit=2,
        name=f"task-{user_id}-{int(time.time())}"
    )

    await tasks.update_one(
        {"user_id": user_id},
        {"$set": {
            "user_id": user_id,
            "task_link": invite.invite_link,
            "count": 0,
            "completed": 0
        }},
        upsert=True
    )

    await message.reply(
        f"Here is your task link (Add 2 members):\n\n{invite.invite_link}")
