import asyncio
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.signaling import BYE, TcpSocketSignaling
from aiortc import VideoStreamTrack

class VideoTransformTrack(VideoStreamTrack):
    async def recv(self):
        frame = await self.track.recv()
        return frame

async def run(pc, signaling):
    # シグナリングチャネルの接続
    await signaling.connect()

    # シグナリングチャネルでのメッセージ交換
    while True:
        obj = await signaling.receive()
        if isinstance(obj, RTCSessionDescription):
            await pc.setRemoteDescription(obj)
            if obj.type == "offer":
                await pc.setLocalDescription(await pc.createAnswer())
                await signaling.send(pc.localDescription)
        elif obj is BYE:
            print("Exiting")
            break

async def main():
    signaling = TcpSocketSignaling("127.0.0.1", 9000)
    pc = RTCPeerConnection()
    pc.addTrack(VideoTransformTrack())

    try:
        await run(pc, signaling)
    finally:
        await pc.close()

if __name__ == "__main__":
    asyncio.run(main())
