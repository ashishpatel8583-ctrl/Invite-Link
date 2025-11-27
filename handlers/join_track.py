from pyrogram import Client
from pyrogram.types import ChatMemberUpdated
from database.mongo import tasks

GROUP_A_ID = -5082882000

@app.on_chat_member_updated()
async def join_track(client, update: ChatMemberUpdated):

    invite = update.invite_link
    if not invite:
        return

    link = invite.invite_link

    # Find which user owns this task link
    data = await tasks.find_one({"task_link": link})
    if not data:
        return

    user_id = data["user_id"]
    count = data["count"] + 1

    # Update count
    await tasks.update_one(
        {"user_id": user_id},
        {"$set": {"count": count}}
    )

    # Notify progress
    await client.send_message(
        user_id,
        f"✔ New member joined your link!\nProgress: {count}/2"
    )

    # If completed
    if count == 2:
        main_link = await client.create_chat_invite_link(
            chat_id=GROUP_A_ID,
            member_limit=1
        )

        await tasks.update_one(
            {"user_id": user_id},
            {"$set": {
                "completed": 1,
                "main_link": main_link.invite_link
            }}
        )

        await client.send_message(
            user_id,
            f"🎉 Congratulations! You have completed your task.\n\n"
            f"Here is your MAIN GROUP link:\n{main_link.invite_link}"
        )
