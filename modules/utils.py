import socket



def local_ip() -> str:
    IP = ''
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
            server.connect(("8.8.8.8", 80))
            IP = server.getsockname()[0]
    except Exception:
        pass
    finally:
        return IP