from typing import Union



def localIP() -> Union[str, dict]:
    try:
        from socket import (
            socket,
            AF_INET,
            SOCK_DGRAM
        )
        with socket(AF_INET, SOCK_DGRAM) as googledns:
            googledns.connect(("8.8.8.8", 80))
        IP = googledns.getsockname()[0]
    except Exception as error:
        IP = {'error': error}
    finally:
        return IP