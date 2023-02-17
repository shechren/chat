import socket
import traceback
import asyncio
from mygame_server_ui import UI

class Connection(UI):
    def __init__(self):
        super().__init__()

    def start(self):
        try:
            self.view_append("안녕")
            asyncio.run(self.server())
        except Exception as e:
            err = traceback.format_exc()
            print(e, err)

    async def server(self):
        print("서버")
        server = await asyncio.start_server(self.handler, "localhost", 5050)
        async with server:
            print(socket.gethostbyname(socket.gethostname()))
            await server.serve_forever()


    async def handler(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        data = await reader.read(1024)
        msg = data.decode("utf-8")
        self.view_append(msg)
        if self.button_send:
            my_msg = self.line.text()
            writer.write(my_msg.encode("utf-8"))
            await writer.drain()

