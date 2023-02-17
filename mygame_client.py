import sys
import traceback

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget

import asyncio
from mygame_client_ui import UI

class Connection(UI):
    def __init__(self):
        super().__init__()
        self.host = "localhost"
        import os
        self.port = int(os.environ.get('PORT', 5050))

    def start(self):
        asyncio.run(self.client())

    async def client(self):
        print("클라이언트 시작")
        try:
            self.view.append("클라이언트를 시작합니다.")
            reader: asyncio.StreamReader
            writer: asyncio.StreamWriter
            reader, writer = await asyncio.open_connection(self.host, self.port)
            while True:
                if self.button_send:
                    my_msg = self.line.text()
                    writer.write(my_msg.encode("utf-8"))
                    await writer.drain()
                data = await reader.read(1024)
                msg = data.decode("utf-8")
                self.view.append(msg)
        except Exception as e:
            print("에러")
            err = traceback.format_exc()
            print(e, err)
            self.view.append(f"{e, err}")