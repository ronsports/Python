import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# Change working directory to the directory where this script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Veebileht on avatud aadressil: http://localhost:{PORT}")
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer suletud.")
