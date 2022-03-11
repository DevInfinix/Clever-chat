import aiohttp 
import requests
import json

class AsyncClient():
    async def get_response(message: str, user = None, gender: str = "Male", chatbot_name: str = "ABLETON", developer_name: str = "`INFINIX#7276`", company: str = "`ABLETON INC`", email: str = "admin@abletonbot.me", job: str = "Chatbot", age: str = "3", birthday: str = "October 5", birthplace: str = "Mumbai, India", birthyear: str = "2022", religion: str = "ABLE", favouriteactor: str = "Tom Hanks", favouriteactress: str = "Julia Roberts", favouriteartist: str = "Leonardo da Vinci", favouriteauthor: str = "Ernest Hemingway", favouriteband: str = "Beatles", favouritebook: str = "The Odyssey"):
        async with aiohttp.ClientSession() as session:
            request = await session.get(f"https://yourmommmaosamaobama.hisroyal123.repl.co/?message={message}&user={user}&gender={gender}&name={chatbot_name}&developer_name={developer_name}%company={company}&email={email}%job={job}&age={age}&birthday={birthday}&birthplace={birthplace}&birthyear={birthyear}&religion={religion}&favouriteactor={favouriteactor}&favouriteactress={favouriteactress}&favouriteartist={favouriteartist}&favouriteauthor={favouriteauthor}&favouriteband={favouriteband}&favouritebook={favouritebook}")
            fetch = await request.json()
            response = fetch["message"]
            await session.close()
            return response

class Client():
    def get_response(message: str, user = None, gender: str = "Male", chatbot_name: str = "ABLETON", developer_name: str = "`INFINIX#7276`", company: str = "`ABLETON INC`", email: str = "admin@abletonbot.me", job: str = "Chatbot", age: str = "3", birthday: str = "October 5", birthplace: str = "Mumbai, India", birthyear: str = "2022", religion: str = "ABLE", favouriteactor: str = "Tom Hanks", favouriteactress: str = "Julia Roberts", favouriteartist: str = "Leonardo da Vinci", favouriteauthor: str = "Ernest Hemingway", favouriteband: str = "Beatles", favouritebook: str = "The Odyssey"):
        request = requests.get(f"https://yourmommmaosamaobama.hisroyal123.repl.co/?message={message}&user={user}&gender={gender}&name={chatbot_name}&developer_name={developer_name}%company={company}&email={email}%job={job}&age={age}&birthday={birthday}&birthplace={birthplace}&birthyear={birthyear}&religion={religion}&favouriteactor={favouriteactor}&favouriteactress={favouriteactress}&favouriteartist={favouriteartist}&favouriteauthor={favouriteauthor}&favouriteband={favouriteband}&favouritebook={favouritebook}")
        fetch = request.json()
        response = fetch["message"]
        return response
