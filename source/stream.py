
import asyncio
import ip

class StreamSubscriber:
    def update(self, packet: str):
        pass

    def shutdown(self):
        pass

class StreamPublisher:
    def __init__(self):
        self.subscribers = []
        
    def addSubscriber(self, subscriber: StreamSubscriber):
        self.subscribers.append(subscriber)

    def removeSubscriber(self, subscriber: StreamSubscriber):
        self.subscribers.remove(subscriber)

    def sendPacket(self):
        for subscriber in self.subscribers:
            subscriber.update(self.packet)

    def sendShutdown(self):
        for subscriber in self.subscribers:
            subscriber.shutdown()

    async def receiver(self, reader, writer):
        while not reader.at_eof():
            self.packet = (await reader.readline()).decode('utf-8')
            self.sendPacket()

        self.sendShutdown()

    async def start(self, port):
        self.server = await asyncio.start_server(self.receiver, ip.local(), port)
        async with self.server:
            await self.server.serve_forever()
