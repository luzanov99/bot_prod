import aiohttp
import json

async def send_request(user):
    async with aiohttp.ClientSession() as session:
        print(user)
        async with session.post('http://127.0.0.1:8000/users/create_user/', data=user) as response:
            print(response)
            return await response.json()