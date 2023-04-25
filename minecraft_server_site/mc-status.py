from mcstatus import JavaServer


server = JavaServer.lookup("192.168.1.5:15306")

status = server.status()
print(f"The server has {status.players.online} player(s) online and replied in {status.latency} ms")

latency = server.ping()
print(f"The server replied in {latency} ms")
