from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import logging

logger = logging.getLogger(__name__)

class KVHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path)

        self.send_response(200)
        self.send_header('Content-type', "text/html")
        self.end_headers()
        output = f"Path: {path.path}, params: {path.params}, query: {path.query}"
        self.wfile.write(output.encode())

class KVStore:
    def __init__(self, db_path: str):
        self.db = db_path

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
    print("Serving now on 8000...")
    server = HTTPServer(("localhost", 4000), KVHandler)
    server.serve_forever()
