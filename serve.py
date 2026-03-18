import http.server, socketserver, os
os.chdir("/Users/ayakakurogi/Desktop/ehon-test/10page")
with socketserver.TCPServer(("", 8765), http.server.SimpleHTTPRequestHandler) as s:
    print("Serving on http://localhost:8765")
    s.serve_forever()
