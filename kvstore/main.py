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

        match path.path:
            case "/get":
                self.handle_get(query = path.query)
            case "/set":
                self.handle_set(query = path.query)
            case _:
                self.echo(200, f"Path: {path.path}, params: {path.params}, query: {path.query}")

    def echo(self, status: int, body: str):
        self.send_response(status)
        self.send_header('Content-type', "text/html")
        self.end_headers()
        self.wfile.write(body.encode())

    def handle_get(self, query: str):
        self.send_response(200)
        self.send_header('Content-type', "text/html")
        self.end_headers()
        self.wfile.write(query.encode())

    def handle_set(self, query: str):
        self.send_response(200)
        self.send_header('Content-type', "text/html")
        self.end_headers()
        self.wfile.write(query.encode())


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
