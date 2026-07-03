from aiogram.types import Message
from aiogram import F, Router
import random
import json

router = Router()

def load_replies() -> dict:
    try:
        with open("bot/backend/links.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: The file 'links.json' was not found.")
        return {}
    except OSError as e:
        print(f"Error: OS error: {e}")
        return {}

# TikTok Links reply
@router.message(F.text.contains("tiktok.com"))
async def reply_tiktok(message: Message) -> None:
    replies = load_replies()
    await message.reply(random.choice(replies["tiktok_replies"]))


# YouTube Links reply
@router.message(F.text.contains("youtube.com/shorts"))
async def reply_youtube(message: Message) -> None:
    replies = load_replies()
    await message.reply(random.choice(replies["youtube_replies"]))


# Instagram Reels Links reply
@router.message(F.text.contains("instagram.com/reel/"))
async def reply_instagram(message: Message) -> None:
    replies = load_replies()
    await message.reply(random.choice(replies["insta_replies"]))
