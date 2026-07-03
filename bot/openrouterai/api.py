import logging
import asyncio
from openai import AsyncOpenAI, APIStatusError
from bot.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MODEL = "meta-llama/llama-3.3-70b-instruct:free"

client = AsyncOpenAI(
    api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

async def generate_challenge() -> str:
    logger.info(f"Calling model: {MODEL}")

    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a fun assistant for a friend group Telegram bot. Be creative and short.",
            },
            {
                "role": "user",
                "content": "Generate one fun daily challenge for a friend group chat. One sentence only.",
            },
        ],
        max_tokens=100,
    )
    return response.choices[0].message.content.strip()

async def main():
    try:
        result = await generate_challenge()
        print(result)

    except APIStatusError as e:
        logger.error(f"API error {e.status_code}: {e.message}")

    except Exception as e:
        logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    asyncio.run(main())