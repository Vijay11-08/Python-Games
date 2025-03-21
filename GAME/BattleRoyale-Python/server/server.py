import socket
import threading

# Server Configuration
HOST = "0.0.0.0"  # Accept connections from all IPs
PORT = 5555
players = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Server started on {HOST}:{PORT}")

def handle_client(conn, player_id):
    print(f"Player {player_id} connected.")
    conn.send(f"Welcome Player {player_id}".encode())

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break

            print(f"Received from Player {player_id}: {data}")

            # Broadcast to all other players
            for pid, p_conn in players.items():
                if pid != player_id:
                    p_conn.send(f"{player_id}:{data}".encode())

        except:
            break

    print(f"Player {player_id} disconnected")
    del players[player_id]
    conn.close()

# Accept connections
player_count = 0
while True:
    conn, addr = server.accept()
    players[player_count] = conn
    thread = threading.Thread(target=handle_client, args=(conn, player_count))
    thread.start()
    player_count += 1
