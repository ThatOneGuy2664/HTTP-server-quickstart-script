import sys
import os
import webbrowser
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

def start_http_server(directory=".", port=8000):
    """Starts an HTTP server in the specified directory on the given port."""
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        sys.exit(1)

    os.chdir(directory)  # Change working directory to the specified path
    server_address = ("", port)

    # Define and start the server
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    # Open browser in a separate thread after a slight delay
    threading.Timer(1, lambda: webbrowser.open(f"http://localhost:{port}/")).start()

    print(f"Serving '{directory}' at http://localhost:{port}/ ... (Press Ctrl+C to stop)")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
        httpd.server_close()

if __name__ == "__main__":
    directory = input("Enter the directory to serve (start at C: or your drive name): ").strip() or "."
    
    try:
        port = int(input("Enter port number (default is 8000): ").strip() or 8000)
    except ValueError:
        print("Invalid port number. Using default port 8000.")
        port = 8000

    start_http_server(directory, port)
