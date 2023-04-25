import pygame, pymunk, sys

def create_body(space, body_pos):
   body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC) # parameters (mass: float, inertia: float, body_type: _BodyType)
   body.position = body_pos
   shape = pymunk.Circle(body, 30)
   space.add(body, shape)
   return shape

def draw_body(objects):
   for object in objects:
      pygame.draw.circle(screen,(0,0,0), object.body.position, 30)

def create_static_obj(space, vertices):
   body = pymunk.Body(body_type = pymunk.Body.STATIC)
   body.position = (0, 0)
   w,h = 2, 2
   #vs = [(-w/2,-h/2), (w/2, h/2), (w/2, -h/2)]
   #vertices = [(200,300), (500,450), (200, 400)]
   shape = pymunk.Poly(body, vertices)
   space.add(body, shape)
   return {"shape": shape, "w": w, "h": h, "vs": vertices}

def draw_static_body(static_objects):
   for object in static_objects:
     pygame.draw.polygon(screen, (0,0,0), object["vs"], object["w"])

pygame.init()
screen = pygame.display.set_mode((800, 800)) # Display Surface
clock = pygame.time.Clock() # Game Clock
space = pymunk.Space()
space.gravity = (0,500)
dt = 0
object_body = []
#object_body.append(create_body(space))
static_object = []
static_object.append(create_static_obj(space,[(200,300), (450,460), (200, 400)]))
static_object.append(create_static_obj(space,[(660,500), (300,650), (650, 600)]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #pygame.QUIT -> User clicked X to close the windows 
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
           object_body.append(create_body(space, event.pos))
    screen.fill("cyan")
    draw_body(object_body)
    draw_static_body(static_object)
    space.step(1/50)
    pygame.display.flip()
    clock.tick(120) # FPS limited to 120
	# dt is delta time in seconds since last frame, used for framerate-independent physics
    dt = clock.tick(60)/1000
