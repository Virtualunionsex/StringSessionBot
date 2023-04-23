import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "16246834").strip()
API_HASH = os.getenv("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5940961389:AAGD32HWrBCAEHF-qfzcXyoG_Wdd6P7fbGA").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://dqvpoxxi:4McOyOwZaE3bQI5FSoydXS81pt9gzsIx@rosie.db.elephantsql.com/dqvpoxxi").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "https://t.me/nakama_asl")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
