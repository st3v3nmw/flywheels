async def read_body(receive):
    """
    Read and return the entire body from an incoming ASGI message.
    """
    body = b""
    more_body = True

    while more_body:
        message = await receive()
        body += message.get("body", b"")
        more_body = message.get("more_body", False)

    return body


class HttpRequest:
    def __init__(self) -> None:
        self.http_version = ""
        self.method = method
        self.headers = {}
        self.url = ""
        self.query_params = {}
        self.body = None
