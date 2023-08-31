from flywheels.request import HttpRequest, read_body


class Flywheels:
    """Flywheels application."""

    async def __call__(self, scope, receive, send):
        assert scope["type"] == "http"

        body = await read_body(receive)

        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"content-type", b"text/plain"],
                ],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": b"Hello, world!",
            }
        )


app = Flywheels()
