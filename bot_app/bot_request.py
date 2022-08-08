import aiohttp
import json
import  os
async def send_request(user):
    async with aiohttp.ClientSession() as session:
        print(user)
        async with session.post('https://keratis.herokuapp.com/users/create_user/', data=user) as response:
            print(response)
            return await response.json()