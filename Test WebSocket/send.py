import asyncio
import websockets

async def send_message():
    async with websockets.connect('ws://localhost:8765') as websocket:
        message = input("Masukkan pesan yang akan dikirim: ")
        await websocket.send(message)
        print(f"Sent: {message}")

asyncio.get_event_loop().run_until_complete(send_message())
