import pgzrun
import random
font_option = (255,255,255)
width = 800
height = 600
centre_x = width / 2
centre_y = height / 2
centre = (centre_x , centre_y)
final_level = 6
start_speed = 20
ITEMS = ["rugby","ball"]
game_over = False
game_complete = False
items = []
animations = []
current_level =1

def draw():
    global items , current_level , game_over , game_complete
    screen.clear()
    screen.blit("backround" , (0,0))
    if game_over:
        display_message("Game 0ver!" , "Try again!")
    elif game_complete:
        display_message("You Won!" , "Well done!")
    else:
        for item in items:
           item.draw()

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
     items_to_create = ["cricket"]
     for i in range(0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
     return items_to_create

def create_items(items_to_create):
     new_items = []
     for option in items_to_create:
         item = Actor(option)
         new_items.append(item)
     return new_items

def layout_items(items_to_layout):
     number_of_gaps = len(items_to_layout) + 1
     gap_size = width / number_of_gaps
     random.shuffle(items_to_layout)
     for index,item in enumerate(items_to_layout):
       new_x_pos = (index + 1) * gap_size
       item.x = new_x_pos
    
def animate_items(items_to_animate):
     global animations
     for item in items_to_animate:
         duration = start_speed - current_level
         item.anchor = ("center","bottom")
         animation = animate(item,duration = duration, on_finished = handle_game_over , y = height)
         animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global items , current_level
    for item in items:
        if item.collidepoint(pos):
            if "cricket" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global current_level , items , animations , game_complete
    stop_animations(animations)
    if current_level == final_level:
        game_complete = True
    else:
        current_level += 1
        items = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text , subheading_text):
    screen.draw.text(heading_text , fontsize = 60 , center = centre , color = "black")
    screen.draw.text(subheading_text , fontsize = 30 , center = (centre_x , centre_y + 30) , color = "black")
pgzrun.go()




