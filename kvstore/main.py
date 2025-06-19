from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import logging

logger = logging.getLogger(__name__)

class KVHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kvstore = KVStore()

    def do_GET(self):
        path = urlparse(self.path)
        output = f"Path: {path.path}, params: {path.params}, query: {path.query}"

        match path.path:
            case "/get":
                self.respond(200, output)
            case "/set":
                self.respond(200, output)
            case _:
                self.respond(200, "wat")

    def respond(self, status: int, body: str):
        self.send_response(status)
        self.send_header('Content-type', "text/html")
        self.end_headers()
        self.wfile.write(body.encode())


class KVStore:
    _db = None

    def __init__(self, db_path: str = "/tmp/random"):
        if KVStore._db is None:
           KVStore._db = db_path

    def get(self, key: str) -> str:
        """Retrieves value stored for the key.

        Args:
            key (str): key whose value we want to retrieve.

        Returns:
            str: value stored in the key, or "" if there is nothing stored
        """
        return ""

    def set(self, key: str, value: str) -> None:
        """Sets the value for the key to the value specified.

        Args:
            key (str): key whose value we want to set
            value (str): value we want to store the key

        Returns:
            None
        """
        pass

if __name__ == "__main__":
    port = 4000
    print(f"Serving now on {port}...")
    server = HTTPServer(("localhost", port), KVHandler)
    server.serve_forever()
