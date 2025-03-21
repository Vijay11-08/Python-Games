import pygame
import chess
import chess.engine
import os

# Load Stockfish Engine (Ensure the path is correct)
STOCKFISH_PATH = r"D:\PD CIE-2\GAME\AI Chess\stockfish\stockfish-windows-x86-64-avx2.exe"

if not os.path.exists(STOCKFISH_PATH):
    raise FileNotFoundError(f"Stockfish not found at {STOCKFISH_PATH}")

engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

# Initialize Pygame
pygame.init()

# Window Size & Colors
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (240, 217, 181)
BLACK = (181, 136, 99)
HIGHLIGHT_COLOR = (186, 202, 68)

# Load Chess Pieces
PIECES_PATH = r"D:\PD CIE-2\GAME\AI Chess\pieces"

if not os.path.exists(PIECES_PATH):
    raise FileNotFoundError(f"Pieces folder not found at {PIECES_PATH}")

pieces = {}
piece_names = {'P': 'P', 'N': 'N', 'B': 'B', 'R': 'R', 'Q': 'Q', 'K': 'K'}

# Load piece images
for color in ['w', 'b']:  # White and Black pieces
    for key, name in piece_names.items():
        piece_name = f"{color}{name}"  # Example: wP, bP
        image_path = os.path.join(PIECES_PATH, f"{piece_name}.jpg")
        if os.path.exists(image_path):
            piece_image = pygame.image.load(image_path)
            pieces[piece_name] = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
        else:
            print(f"Warning: Image not found for {piece_name} at {image_path}")

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Chess Battle ♟️")

# Initialize Chess Board
board = chess.Board()

# Game Variables
selected_square = None
valid_moves = []
running = True
player_turn = True  # White (Human) moves first

def draw_board():
    """Draws the chessboard with pieces"""
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            # Highlight Selected Piece & Valid Moves
            if selected_square == (row, col):
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            # Draw Pieces
            square = chess.square(col, 7 - row)
            piece = board.piece_at(square)
            if piece:
                piece_symbol = piece.symbol().upper()
                piece_color = 'w' if piece.color == chess.WHITE else 'b'
                piece_key = f"{piece_color}{piece_symbol}"
                if piece_key in pieces:
                    screen.blit(pieces[piece_key], (col * SQUARE_SIZE, row * SQUARE_SIZE))

def ai_move():
    """AI makes a move using Stockfish"""
    global player_turn
    if not board.is_game_over():
        result = engine.play(board, chess.engine.Limit(depth=3))  # Adjust depth for difficulty
        board.push(result.move)
        player_turn = True

def get_square_under_mouse():
    """Returns the chessboard square coordinates under the mouse"""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col = mouse_x // SQUARE_SIZE
    row = mouse_y // SQUARE_SIZE
    return row, col

def handle_click():
    """Handles player move selection"""
    global selected_square, valid_moves, player_turn
    row, col = get_square_under_mouse()
    square = chess.square(col, 7 - row)

    if selected_square is None:
        # Selecting a piece
        piece = board.piece_at(square)
        if piece and piece.color == chess.WHITE:
            selected_square = (row, col)
            valid_moves = [move for move in board.legal_moves if move.from_square == square]
    else:
        # Making a move
        move = chess.Move(chess.square(selected_square[1], 7 - selected_square[0]), square)
        if move in valid_moves:
            board.push(move)
            player_turn = False
            pygame.time.delay(500)  # Delay before AI moves
            ai_move()
        selected_square = None
        valid_moves = []

def draw_valid_moves():
    """Highlights valid moves"""
    for move in valid_moves:
        target_row = 7 - chess.square_rank(move.to_square)
        target_col = chess.square_file(move.to_square)
        pygame.draw.circle(screen, HIGHLIGHT_COLOR, 
                           (target_col * SQUARE_SIZE + SQUARE_SIZE // 2, target_row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                           10)

def display_game_status():
    """Displays game result if the game is over"""
    if board.is_checkmate():
        winner = "Black (AI)" if board.turn == chess.WHITE else "White (Player)"
        text = f"Checkmate! {winner} wins!"
    elif board.is_stalemate():
        text = "Stalemate! It's a draw."
    elif board.is_insufficient_material():
        text = "Draw! Insufficient material."
    else:
        return

    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 0, 0))
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))

# Main Game Loop
while running:
    screen.fill((0, 0, 0))  # Clear screen
    draw_board()
    draw_valid_moves()
    display_game_status()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            handle_click()

    pygame.display.flip()  # Update screen

engine.quit()
pygame.quit()
