import asyncio
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.signaling import BYE, TcpSocketSignaling
from aiortc import MediaStreamTrack, VideoStreamTrack

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

class VideoTransformTrack(VideoStreamTrack):
    async def recv(self):
        frame = await self.track.recv()
        return frame

async def create_pc():
    pc = RTCPeerConnection()
    pc.addTrack(VideoTransformTrack())

    return pc

if __name__ == "__main__":
    signaling = TcpSocketSignaling("127.0.0.1", 9000)
    pc = create_pc()

    # メインイベントループを開始
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run(pc, signaling))
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(pc.close())