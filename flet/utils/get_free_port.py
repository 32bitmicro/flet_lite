


def free_port():
    import socketserver

    with socketserver.TCPServer(("localhost", 0), None) as s:
        free_port = s.server_address[1]
        return int(free_port)