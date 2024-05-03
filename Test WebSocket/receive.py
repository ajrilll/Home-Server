import asyncio
import websockets

async def echo(websocket, path):
    print(f"Server started at {websocket.remote_address[0]}:{websocket.remote_address[1]}")

    async for message in websocket:
        print(f"Received from {websocket.remote_address[0]}:{websocket.remote_address[1]}: {message}")
        await websocket.send(message)

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
