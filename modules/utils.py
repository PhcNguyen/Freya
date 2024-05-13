import socket



def local_ip() -> str:
    IP = ''
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
            server.connect(("8.8.8.8", 80))
            IP = server.getsockname()[0]
    except Exception as e:
        print(f"Không thể lấy địa chỉ IP cục bộ: {e}")
    finally:
        return IP