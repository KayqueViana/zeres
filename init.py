import pygame
from dialogs.main import START_DIALOG

# INIT PYGAME
pygame.init()

# MAIN CONFIGURATION
screen = pygame.display.set_mode((850, 720))
clock = pygame.time.Clock()
running = True

# TEXT CONFIGURATION
font = pygame.font.SysFont("Consolas", 26)
txt_color = (0, 255, 0)
secondary_txt_color = (0, 0, 0)
txt_speed = 0.05

# STATE VARIABLES
actual_dialog = START_DIALOG
dialog_index = "initial"
full_text = actual_dialog[dialog_index]["texts"]
actual_text = []
actual_line = 0
timer = 0
char_index = 0
phase = "typing"  # "typing", "options", "waiting"
selected_option = 0

# RESET STATE VARIABLES
def _reset_state_vars():
    global actual_text, actual_line, char_index, timer, selected_option, phase
    
    actual_text = []
    actual_line = 0
    char_index = 0
    phase = "typing"
    timer = 0
    selected_option = 0
    
# PROCCESS MAIN COMMANDS
def _process_comand(event):
    global actual_dialog, selected_option, dialog_index, full_text, phase, running
    
    # Create a list with options indexes
    options = list(actual_dialog[dialog_index]["options"].keys())
    referenced_option = options[selected_option] # Get the first option
    if event.key in [pygame.K_UP, pygame.K_DOWN]:
        step = -1 if event.key == pygame.K_UP else 1
        selected_option = (options.index(referenced_option) + step) % len(options)
        referenced_option = options[selected_option]
    elif event.key == pygame.K_RETURN:
        choice = actual_dialog[dialog_index]["options"][referenced_option]['choice']
        full_text = actual_dialog[choice]["texts"]
        dialog_index = choice
        _reset_state_vars()
    # Skip line to the end or close the game
    elif phase == 'typing' and event.key == pygame.K_SPACE:
        _handle_line_skip()
    # TODO: Maybe this will not be necessary
    elif phase == 'waiting' and event.key == pygame.K_SPACE:
        running = False

def _handle_line_skip():
    global actual_line, full_text, actual_text, char_index
    
    # Complete only the actual typed line 
    if actual_line < len(full_text):
        line = full_text[actual_line]
        
        # Grants that the actual line exists
        if len(actual_text) <= actual_line:
            actual_text.append("")
        
        # Complete the actual line
        actual_text[actual_line] = line  # Copy the line
        char_index = len(line)  # Go to the end of the line
        
        # If already on the end, go to the next line
        if char_index >= len(line):
            actual_line += 1
            char_index = 0

def _handle_typewriting(delta):
    global timer, txt_speed, full_text, actual_line, char_index, actual_text, phase, actual_dialog, dialog_index
    
    timer += delta
    if timer >= txt_speed:
        if actual_line < len(full_text):
            line = full_text[actual_line]

            if char_index < len(line):
                # While have characteres to write continues
                if len(actual_text) <= actual_line:
                    actual_text.append("")  # Add new empty srt if needed
                actual_text[actual_line] = line[:char_index + 1]
                char_index += 1
            else:
                # Go to the next line
                actual_line += 1
                char_index = 0
                
            timer = 0
        else:
            phase = "options" if actual_dialog[dialog_index]["options"] else "waiting"

# MAIN LOOP
while running:
    dt = clock.tick(60) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            _process_comand(event)
            
    # LOGIC FOR TYPEWRITTER LIKE TEXT
    if phase == 'typing': 
        _handle_typewriting(dt)
        
    # SCREEN DRAWN
    screen.fill("black")

    # Desenha texto
    y = 50
    for linha in actual_text:
        surface = font.render(linha, True, txt_color)
        screen.blit(surface, (50, y))
        y += 35
        
    # Desenha opções (se houver)
    if phase == "options":
        y += 20
        for i, opcao in enumerate(actual_dialog[dialog_index]["options"]):
            # Set option color
            option_color = (255, 255, 0) if i == selected_option else (200, 200, 200)
            surface = font.render(opcao, True, option_color)
            screen.blit(surface, (70, y))
            y += 35

    pygame.display.flip()

pygame.quit()
            