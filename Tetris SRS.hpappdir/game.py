from sys import platform
from data import Data

if platform == "HP Prime":
    from hpprime import *
    from graphic import *
    from urandom import randint # HP Prime

else:
    from random import randint # PC
    def rect(*args):
        pass
    def fillrect(*args):
        pass
    def clear_screen(*args):
        pass
    def keyboard(*args):
        pass


class PieceObserver():
    def PieceInserted(self):
        pass
    def GameOver(self):
        pass


class Piece():

    CYAN = 0x00FFFF
    BLUE = 0x0000FF
    ORANGE = 0xFF8000
    YELLOW = 0xFFFF00
    GREEN = 0x00FF00
    PURPLE = 0x8000FF
    RED = 0xFF0000
    GRAY = 0x404040
    WHITE = 0xFFFFFF

    # Piece I
    I = (
        (
            (None, None, None, None),
            (CYAN, CYAN, CYAN, CYAN),
            (None, None, None, None),
            (None, None, None, None)
        ),
        (
            (None, None, CYAN, None),
            (None, None, CYAN, None),
            (None, None, CYAN, None),
            (None, None, CYAN, None)
        ),
        (
            (None, None, None, None),
            (None, None, None, None),
            (CYAN, CYAN, CYAN, CYAN),
            (None, None, None, None)
        ),
        (
            (None, CYAN, None, None),
            (None, CYAN, None, None),
            (None, CYAN, None, None),
            (None, CYAN, None, None)
        )
    )

    # Piece J
    J = (
        (
            (BLUE, None, None),
            (BLUE, BLUE, BLUE),
            (None, None, None)
        ),
        (
            (None, BLUE, BLUE),
            (None, BLUE, None),
            (None, BLUE, None)
        ),
        (
            (None, None, None),
            (BLUE, BLUE, BLUE),
            (None, None, BLUE)
        ),
        (
            (None, BLUE, None),
            (None, BLUE, None),
            (BLUE, BLUE, None)
        )
    )

    # Piece L
    L = (
        (
            (None, None, ORANGE),
            (ORANGE, ORANGE, ORANGE),
            (None, None, None)
        ),
        (
            (None, ORANGE, None),
            (None, ORANGE, None),
            (None, ORANGE, ORANGE)
        ),
        (
            (None, None, None),
            (ORANGE, ORANGE, ORANGE),
            (ORANGE, None, None)
        ),
        (
            (ORANGE, ORANGE, None),
            (None, ORANGE, None),
            (None, ORANGE, None)
        )
    )

    # Piece O
    O = (
        (
            (None, YELLOW, YELLOW, None),
            (None, YELLOW, YELLOW, None),
            (None, None, None, None)
        ),
    )

    # Piece S
    S = (
        (
            (None, GREEN, GREEN),
            (GREEN, GREEN, None),
            (None, None, None)
        ),
        (
            (None, GREEN, None),
            (None, GREEN, GREEN),
            (None, None, GREEN)
        ),
        (
            (None, None, None),
            (None, GREEN, GREEN),
            (GREEN, GREEN, None)
        ),
        (
            (GREEN, None, None),
            (GREEN, GREEN, None),
            (None, GREEN, None)
        )
    )

    # Piece T
    T = (
        (
            (None, PURPLE, None),
            (PURPLE, PURPLE, PURPLE),
            (None, None, None)
        ),
        (
            (None, PURPLE, None),
            (None, PURPLE, PURPLE),
            (None, PURPLE, None)
        ),
        (
            (None, None, None),
            (PURPLE, PURPLE, PURPLE),
            (None, PURPLE, None)
        ),
        (
            (None, PURPLE, None),
            (PURPLE, PURPLE, None),
            (None, PURPLE, None)
        )
    )

    # Piece Z
    Z = (
        (
            (RED, RED, None),
            (None, RED, RED),
            (None, None, None)
        ),
        (
            (None, None, RED),
            (None, RED, RED),
            (None, RED, None)
        ),
        (
            (None, None, None),
            (RED, RED, None),
            (None, RED, RED)
        ),
        (
            (None, RED, None),
            (RED, RED, None),
            (RED, None, None)
        )
    )

    # Piece Error
    ERROR = (
        (
            (None, RED, RED, None),
            (None, RED, RED, None),
            (None, None, None, None)
        ),
    )

    # See https://harddrop.com/wiki/SRS#Wall_Kicks
    WALL_KICKS = {
        "JLSTZ": {
            (0, 1): [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  # 0 -> R
            (1, 0): [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],      # R -> 0
            (1, 2): [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],      # R -> 2
            (2, 1): [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],  # 2 -> R
            (2, 3): [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],     # 2 -> L
            (3, 2): [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],   # L -> 2
            (3, 0): [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],   # L -> 0
            (0, 3): [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],     # 0 -> L
        },
        "I": {
            (0, 1): [(0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2)],  # 0 -> R
            (1, 0): [(0, 0), (2, 0), (-1, 0), (2, 1), (-1, -2)],  # R -> 0
            (1, 2): [(0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1)],  # R -> 2
            (2, 1): [(0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1)],  # 2 -> R
            (2, 3): [(0, 0), (2, 0), (-1, 0), (2, 1), (-1, -2)],  # 2 -> L
            (3, 2): [(0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2)],  # L -> 2
            (3, 0): [(0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1)],  # L -> 0
            (0, 3): [(0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1)],  # 0 -> L
        }
    }

    def __init__(self, observer, board, time, piece):
        #super().__init__(board.origin_x, board.origin_y)
        self.observer = observer
        self.board = board
        self.time = time
        self.current_piece = piece
        self.pos_grid_i = int(board.cols) // 2 - 2 + int(board.cols) % 2
        self.pos_grid_j = board.rows_visible
        self.rotation = 0

        self.shape = getattr(self, piece, self.ERROR) # Return the piece, return ERROR piece if bad input

        self.piece = self.shape[self.rotation]
    
        if self.check_colisions(self.pos_grid_i, self.pos_grid_j) == False: # If piece spawn in another piece
            self.observer.GameOver()
        
    
    def to_grid_pos(self, i, j, pos_grid_i = None, pos_grid_j = None):
        return ((pos_grid_i if pos_grid_i != None else self.pos_grid_i) + j, (pos_grid_j if pos_grid_j != None else self.pos_grid_j) - i)

    def rotate(self, input):
        new_rotation = (self.rotation + input + len(self.shape)) % len(self.shape)
        piece_type = "I" if self.current_piece == "I" else "JLSTZ"
        kicks = self.WALL_KICKS[piece_type].get((self.rotation, new_rotation), [(0, 0)]) # If no kick found, do not kick (180 kick not implemented)
        
        for kick in kicks:
            if self.check_colisions(self.pos_grid_i + kick[0], self.pos_grid_j + kick[1], new_rotation - self.rotation):
                self.rotation = new_rotation
                self.pos_grid_i += kick[0]
                self.pos_grid_j += kick[1]
                self.piece = self.shape[self.rotation]
                return  # Exit the method after successful rotation
        
    
    def draw(self):
        # Draw the ghost piece
        self.draw_piece(self.pos_grid_i, self.pos_grid_j - self.drop_distance(), Piece.GRAY)

        # Draw the piece
        self.draw_piece()

    def draw_piece(self, pos_grid_i = None, pos_grid_j = None, color = None):
        if pos_grid_i is None:
            pos_grid_i = self.pos_grid_i
        
        if pos_grid_j is None:
            pos_grid_j = self.pos_grid_j
        
        for i in range(len(self.piece)):
            for j in range(len(self.piece[0])):
                if self.piece[i][j] != None:
                    if color is None:
                        self.board.draw_block(self.to_grid_pos(i,j, pos_grid_i, pos_grid_j), self.piece[i][j])
                    else:
                        self.board.draw_block(self.to_grid_pos(i,j, pos_grid_i, pos_grid_j), color)

    def update_pos(self, keys):
        
        # Gravity and lock delay

        # If piece not lay on the bottom or another piece
        if self.check_colisions(self.pos_grid_i, self.pos_grid_j - 1):
            self.time.gravity.resume()

            self.time.lock_delay.pause()

            if self.time.gravity():
                self.pos_grid_j -= min(self.time.gravity.value, self.drop_distance())
                #print(self.time.gravity.value)
        
        else:
            self.time.gravity.pause()
            self.time.gravity.rst()

            self.time.lock_delay.resume()

            if self.time.lock_delay():
                self.insert_piece()

        #if self.time.gravity.value != 0:
            #print(self.time.gravity.value)

        # Collisions to the left and right
        if keys.dx != 0:
            self.pos_grid_i += max(-self.left_wall_distance(), min(keys.dx, self.right_wall_distance()))
            #print(self.left_wall_distance(), self.right_wall_distance())

        # Collisions if rotating
        if keys.rotate != 0:
            self.rotate(keys.rotate)

        # Do hard drop
        if keys.hard_drop:
            self.pos_grid_j -= self.drop_distance()
            self.insert_piece()

        #elif keys.soft_drop and self.check_colisions(self.pos_grid_i, self.pos_grid_j - 1):
        #    self.pos_grid_j -= 1

    def drop_distance(self):
        distance = 0
        while (self.check_colisions(self.pos_grid_i, self.pos_grid_j - (distance + 1))):
            distance += 1
        return distance

    def left_wall_distance(self):
        distance = 0
        while (self.check_colisions(self.pos_grid_i - (distance + 1), self.pos_grid_j)):
            distance += 1
        return distance

    def right_wall_distance(self):
        distance = 0
        while (self.check_colisions(self.pos_grid_i + (distance + 1), self.pos_grid_j)):
            distance += 1
        return distance
    
    def insert_piece(self):
        for i in range(len(self.piece)):
            for j in range(len(self.piece[0])):
                if self.piece[i][j] is not None:
                    grid_i, grid_j = self.to_grid_pos(i,j)
                    self.board.grid[grid_i][grid_j] = self.piece[i][j]
        
        self.observer.PieceInserted()

    def check_colisions(self, pos_i, pos_j, rotation = 0):
        # Calcul de la nouvelle pièce
        piece = self.shape[(self.rotation + rotation + len(self.shape)) % len(self.shape)]

        # Collisions
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                grid_i, grid_j = self.to_grid_pos(i, j, pos_i, pos_j)
                if piece[i][j] != None:
                    if grid_i < 0 or grid_i >= self.board.cols or grid_j < 0 or grid_j >= self.board.rows:
                        return False
                    if self.board.grid[grid_i][grid_j] != None:
                        return False

        return True

    @staticmethod
    def draw_static(x, y, size, piece, color = None, rotation = 0):
        if piece is None:
            return
        shape = getattr(Piece, piece, Piece.ERROR) # Return the piece, return ERROR piece if bad input
        piece = shape[rotation]

        if color is not None:
            color = getattr(Piece, color, Piece.WHITE) # Return the color, return WHITE piece if bad input
        
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                #print(piece[i][j])
                if piece[i][j] is not None:
                    if color is None:
                        fillrect(1, x + size * j, y + size * i, size, size, piece[i][j], piece[i][j])
    
                    else:
                        fillrect(1, x + size * j, y + size * i, size, size, color, color)
        #print("STOP\n\n")


class Board():

    def __init__(self, cols, rows):
        screen_width = 320
        screen_height = 240
        self.cols = max(int(cols), 4)
        self.rows_visible = max(int(rows), 4)
        self.rows = rows * 2
        self.grid = [[None for _ in range(self.rows)] for _ in range(self.cols)] # Create an empty grid
        self.board_color = 0x808080
        self.size = 10
        self.origin_x = int((screen_width - self.cols * self.size - 1) // 2)
        self.origin_y = int((screen_height - self.rows_visible * self.size - 1) // 2)

    @property
    def board_height(self):
        return self.size * min(self.rows, self.rows_visible)
    
    def draw_block(self, pos, block):
        fillrect(1, self.origin_x + 1 + pos[0] * self.size, self.origin_y  + 1 + self.board_height - (pos[1] + 1) * self.size, self.size, self.size, block, block)

    def draw(self):
        rect(1, self.origin_x, self.origin_y, self.size*self.cols + 2, self.size*self.rows_visible + 2, self.board_color)
        for i in range(self.cols):
            for j in range(self.rows_visible + 1):
                if self.grid[i][j] != None:
                    self.draw_block((i, j), self.grid[i][j])
    
    def update_grid(self):
        for j in range(self.rows):
            Remove = True
            while(Remove):
                for i in range(self.cols):
                    if self.grid[i][j] is None:
                        Remove = False
                        break
                if Remove:
                    self.remove_row(j)

    def remove_row(self,n):
        temp_len = self.rows - n
        temp_grid = [[None for _ in range(temp_len)] for _ in range(self.cols)]
        for j in range(temp_len - 1):
            for i in range(self.cols):
                temp_grid[i][n - j - 1] = self.grid[i][self.rows - 1 - j]
        for j in range(temp_len):
            for i in range(self.cols):
                self.grid[i][self.rows - 1 - j] = temp_grid[i][n - j]


class Keys():

    def __init__(self, time):
        self.time = time
        self.old_keyboard_input = keyboard()
        
        self.k_left = 7 # Left key
        self.k_right = 8 # Right key
        self.k_soft_drop = 12 # Down key
        self.k_hard_drop = 2 # Up key
        self.k_rotate_clockwise = 30 # Enter key
        self.k_rotate_counter_clockwise = 24 # LN Key
        self.k_rotate_180 = 25 # LOG Key= 7 # Left key
        self.k_right = 8 # Right key
        self.k_soft_drop = 12 # Down key
        self.k_hard_drop = 2 # Up key
        self.k_rotate_clockwise = 30 # Enter key
        self.k_rotate_counter_clockwise = 24 # LN Key
        self.k_rotate_180 = 25 # LOG Key
        self.k_hold = 29 # , key

        self.k_hold = 29 # , key

    def just_pressed(self, key):
        if self.old_keyboard_input & (1 << key) == False and self.keyboard_input & (1 << key) != False:
            return True
        else:
            return False

    def is_pressed(self, key):
        if self.keyboard_input & (1 << key) != False:
            return True
        else:
            return False

    def get(self):
        # TODO: Add Handling options for the input, line 627 for timer and explanation
        self.dx = 0
        self.hard_drop = False
        self.soft_drop = False
        self.hold = False
        self.rotate = 0
        
        self.keyboard_input = keyboard()

        # Horizontal movement
        if self.just_pressed(self.k_right):
            self.dx = 1

        if self.just_pressed(self.k_left):
            self.dx = -1


        # Hard drop
        if self.just_pressed(self.k_hard_drop):
            self.hard_drop = True

        # Soft Drop
        if self.just_pressed(self.k_soft_drop):
            self.soft_drop = True


        #Rotation
        if self.just_pressed(self.k_rotate_counter_clockwise):
            # Rotate counter-clockwise
            self.rotate -= 1

        if self.just_pressed(self.k_rotate_clockwise):
            # Rotate clockwise
            self.rotate += 1
        
        if self.just_pressed(self.k_rotate_180):
            #rotate to 180
            self.rotate = 2
        
        if self.just_pressed(self.k_hold): # , key
            self.hold = True
        


        self.old_keyboard_input = self.keyboard_input


class PieceBag():
    def __init__(self, max_next_preview, board):
        self.max_next_preview = max_next_preview

        self.reset_bag()

        self.next_pieces = []

        self.next_pieces = [self.get_piece_from_bag() for _ in range(max_next_preview)]
        #Equivalent:
        #for i in range(max_next_preview):
        #    self.next_pieces.append(self.get_piece_from_bag())

        self.board = board

        self.origin_x = self.board.origin_x + self.board.cols * self.board.size + 1
        self.origin_y = board.origin_y
        

    def reset_bag(self):
        self.bag = ["I", "J", "L", "O", "S", "T", "Z"]

    def get_piece_from_bag(self):
        if len(self.bag) == 0:
            self.reset_bag()
        return self.bag.pop(randint(0, len(self.bag) - 1))

    def get_piece(self):
        piece = self.next_pieces.pop(0)
        self.next_pieces.append(self.get_piece_from_bag())
        return piece
    
    def draw(self):
        rect(1, self.origin_x, self.origin_y, 6 * self.board.size, (2 * self.max_next_preview + 6) * self.board.size, self.board.board_color)

        for i, piece in enumerate(self. next_pieces):

            if piece == "I":
                offset_x = 0
                offset_y = - self.board.size // 2
            elif piece == "O":
                offset_x = 0
                offset_y = 0
            else:
                offset_x = self.board.size // 2
                offset_y = 0
            
            offset_between = i * 3 * self.board.size
            Piece.draw_static(self.origin_x + self.board.size + offset_x, self.origin_y + self.board.size + offset_y + offset_between, self.board.size, piece)


class Hold():
    def __init__(self, board):
        self.board = board
        self.origin_x = self.board.origin_x - 6 * self.board.size + 1
        self.origin_y = self.board.origin_y
        self.hold_piece = None
        self.can_hold = True

    # Return the piece after using hold
    def process(self, current_piece):
        if self.hold_piece is None:
            self.hold_piece = current_piece
            return None # No piece in Hold, None means take a piece in the bag
        else:
            temp = self.hold_piece
            self.hold_piece = current_piece
            return temp
        
    def draw(self):
        if self.hold_piece == "I":
            offset_x = 0
            offset_y = - self.board.size // 2
        elif self.hold_piece == "O":
            offset_x = 0
            offset_y = 0
        else:
            offset_x = self.board.size // 2
            offset_y = 0

        rect(1, self.origin_x, self.origin_y, 6 * self.board.size, 4 * self.board.size, self.board.board_color) 

        if self.can_hold == True:
            color = None # Normal color of the piece
        else:
            color = "GRAY"

        Piece.draw_static(self.origin_x + self.board.size + offset_x, self.origin_y + self.board.size + offset_y, self.board.size, self.hold_piece, color)

    
class Time():

    def __init__(self, data):
        self.data = data
        time = self.get_time()
        self.time_things = []

        self.gravity = self.TimeThing(self.data("gravity"), time, False, True)
        self.time_things.append(self.gravity)

        self.lock_delay = self.TimeThing(1, time, False, False)
        self.time_things.append(self.lock_delay)

        # Handling Timer, base config from tetr.io

        # Automatic Repeat Rate: 
        # The speed at which tetrominoes move when holding down movement keys
        self.arr = self.TimeThing(self.data("ARR"), time, False, True)
        self.time_things.append(self.arr)

        # Delayed Auto Shift:
        # The time between the initial keypress and the start of its automatic repeat movement.
        self.das = self.TimeThing(self.data("DAS"), time, False, False)
        self.time_things.append(self.das)

        # DAS Cut Delay: 
        # If not 0, any ongoing DAS movement will pause for a set amount of time after dropping/rotating a piece, measured in frames.
        self.dcd = self.TimeThing(self.data("DCD"), time, False, True)
        self.time_things.append(self.dcd)

        # Soft Drop Factor: 
        # The factor with which soft drops change the gravity speed.
        self.sdf = self.data("SDF")
    

    def update(self):
        time = self.get_time()

        for time_thing in self.time_things:
            time_thing.update(time)
    
    def pause(self):
        for time_thing in self.time_things:
            time_thing.pause()
    
    def resume(self):
        for time_thing in self.time_things:
            time_thing.resume()

    def rst(self):
        for time_thing in self.time_things:
            time_thing.rst()

    # The only method I found for getting time on the calculator
    def get_time(self):
        return int(eval("ticks")) / 1000
    

    class TimeThing():
        def __init__(self, countdown, current_time, running = True, reset = True):
            self.value = 0
            self.countdown = countdown
            self.running = running
            self.reset = reset
            self.elapsed_time = 0
            self.old_time = current_time

        def update(self, current_time):

            if self.running:
                if self.value != 0:
                    if self.reset:
                        self.rst(self.elapsed_time)
                    else:
                        self.pause()

                self.elapsed_time += max(current_time - self.old_time, 0)

                if self.elapsed_time >= self.countdown:
                    self.value = int(self.elapsed_time // self.countdown)
                    self.elapsed_time = self.elapsed_time - self.value
            
            self.old_time = current_time
        
        
        def pause(self):
            self.running = False

        def resume(self):
            self.running = True

        def rst(self, elapsed_time = 0):
            self.elapsed_time = elapsed_time
            self.value = 0

        def __call__(self):
            return False if self.value == 0 else True


class Game(PieceObserver):
    def __init__(self):
        self.gameover = False
        self.pieceinserted = False
        self.data = Data()
        self.time = Time(self.data)
        self.keys = Keys(self.time)
        self.board = Board(10, 20)
        self.piecebag = PieceBag(5, self.board)
        self.piece = Piece(self, self.board, self.time, self.piecebag.get_piece())
        self.hold = Hold(self.board)
    
    def PieceInserted(self):
        self.pieceinserted = True

    def GameOver(self):
        self.gameover = True

    def ProcessGameOver(self):
        if self.gameover:
            self.gameover = False
            del self.keys, self.piecebag, self.board, self.piece, self.hold, self.time
            self.__init__()
        
    def ProcessPieceInserted(self):
        if self.pieceinserted:
            self.pieceinserted = False
            self.hold.can_hold = True
            self.time.__init__(self.data)
            self.piece.__init__(self, self.board, self.time, self.piecebag.get_piece())
            self.board.update_grid()

    def ProcessEvent(self):
        self.ProcessPieceInserted()
        self.ProcessGameOver()
    
    def ProcessInput(self):
        self.keys.get()

        # TODO: Redo hold in a better way, should be in Hold class ?
        if self.keys.hold and self.hold.can_hold:

            self.hold.can_hold = False

            piece = self.hold.process(self.piece.current_piece)

            del self.piece

            if piece is None: 
                self.piece = Piece(self, self.board, self.time, self.piecebag.get_piece())
            else:
                self.piece = Piece(self, self.board, self.time, piece)

        self.piece.update_pos(self.keys)

    def Draw(self):
        self.board.draw()
        self.piece.draw()
        self.hold.draw()
        self.piecebag.draw()

    def run(self):
        try:
            while(1):
                self.time.update()
                self.ProcessEvent()
                self.ProcessInput()
                #TODO: Not always wipes buffer layer, should be more optimised
                dimgrob(1,320,240,0) # Black screen to layer G1
                self.Draw()
                blit(0,0,0,1) # copy layer G1 to layer G0

        # This prevents an error message on the calculator when On/Off is pressed for exiting the game.
        # Exits the game now
        except KeyboardInterrupt:
            self.data.save()
            return 0


g=Game()
g.run()
