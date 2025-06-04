import pgzrun
import random
TITLE = "Flappy Ball"
WIDTH = 800
HEIGHT = 600
def random_color():
  return (
  random.randint(0,255),
  random.randint(0,255),
  random.randint(0,255))

GRAVITY = 2000.0
class Ball:
    def __init__(self,start_x,start_y,color,radius):
        self.x = start_x
        self.y = start_y
        self.vx = 200
        self.vy = 0
        self.radius = radius
        self.color = color

    def draw(self):
       pos = (self.x,self.y)
       screen.draw.filled_circle(pos,self.radius,self.color)


    def update(self,dt):
      uy = self.vy
      self.vy += GRAVITY * dt
      self.y += (uy + self.vy) * 0.5 * dt

      if self.y > HEIGHT - self.radius:
         self.y = HEIGHT - self.radius
         self.vy = -self.vy * 0.9
      self.x += self.vx * dt
      if self.x > WIDTH - self.radius or self.x < self.radius:
         self.vx = -self.vx
    
    def kick(self,b):
       self.vy = b
       
ball1 = Ball(100,-200,random_color(),60)
ball2 = Ball(400,-200,random_color(),45)
ball3 = Ball(700,-200,random_color(),50)

def draw():
  screen.clear()
  ball1.draw()
  ball2.draw()
  ball3.draw()

def update(dt):
   ball1.update(dt)
   ball2.update(dt)
   ball3.update(dt)

def on_key_down(key):
       if key == keys.SPACE:
          ball1.kick(-500)
          ball2.kick(-350)
          ball3.kick(-410)


pgzrun.go()
