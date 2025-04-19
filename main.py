from db.crud import db
import asyncio

asyncio.run(db.remove_subscription("123132", "sdfsdf"))