
import sys
sys.path.append("../source")
import asyncio
import stream
import datetime

class LogStreamSubscriber(stream.StreamSubscriber):
    def update(self, packet: str):
        print(packet)

class FileStreamSubscriber(stream.StreamSubscriber):
    def __init__(self, file: str):
        self.output = open(file, "w+")
        
    def update(self, packet: str):
        self.output.write(packet)

        
jsonStream = stream.StreamPublisher()
subscriber = {
    "log": LogStreamSubscriber(),
    "csv": FileStreamSubscriber(file = f"output/{datetime.datetime.now():%Y-%m-%d_%H:%M:%S}")
}

jsonStream.addSubscriber(subscriber["log"])
jsonStream.addSubscriber(subscriber["csv"])

try:
    asyncio.run(jsonStream.start(port = 11772))
except KeyboardInterrupt:
    sys.exit(0)
