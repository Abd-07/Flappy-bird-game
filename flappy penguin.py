import arcade
import random

from arcade.sprite_list import check_for_collision


SCREEN_WIDTH = 650
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Flappy Penguin"

class Penguin(arcade.AnimatedTimeSprite):
    def __init__(self):
        super().__init__(1)
        self.textures=[]
        self.textures.append(arcade.load_texture("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/flappy bird/penguin1.png"))
        self.textures.append(arcade.load_texture("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/flappy bird/penguin1.png"))
        self.textures.append(arcade.load_texture("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/flappy bird/penguin1.png"))
    def update(self):
        self.center_y += self.change_y
        self.angle += self.change_angle
        self.change_y-=0.4
        if self.center_y<0:
            self.center_y=0
        if self.center_y>SCREEN_HEIGHT:
            self.center_y=SCREEN_HEIGHT
        self.change_angle-=0.4
        if self.angle >= 40:
            self.angle= 40
        if self.angle <= -30:
            self.angle= -30
        

class Collumn_top(arcade.Sprite):
    def update(self):
        self.center_x-=self.change_x
        if self.center_x <=0:
            self.center_x = SCREEN_WIDTH
            self.center_y=random.randint(390,480)

class Collumn_bottom(arcade.Sprite):
    def update(self):
        self.center_x-=self.change_x
        if self.center_x<=0:
            self.center_x = SCREEN_WIDTH
            self.center_y=random.randint(0,70)


# class with the game
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background=arcade.load_texture("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/flappy bird/space.png")
        self.penguin=Penguin()
        self.collumns=arcade.SpriteList()

    # initial values
    def setup(self):
        self.penguin.center_x=100
        self.penguin.center_y=180
        self.penguin.change_x=0
        self.penguin.change_y=2
        self.penguin.change_angle=0

    

        for i in range(5):
            collumn_top=Collumn_top("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/flappy bird/column_top.png",1)
            collumn_top.center_x= 130*i + SCREEN_WIDTH
            collumn_top.change_x=4
            collumn_top.center_y=400
            self.collumns.append(collumn_top)

            collumn_bottom=Collumn_bottom("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/flappy bird/column_bottom.png",1)
            collumn_bottom.center_x= 130*i + SCREEN_WIDTH
            collumn_bottom.change_x=4
            collumn_bottom.center_y=0
            self.collumns.append(collumn_bottom)
            


        self.move=True
        self.score=0

    # rendering
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.penguin.draw()
        arcade.draw_text(f"Score: {self.score}",330,550,arcade.color.BLACK,30)
        self.collumns.draw()

    # logic of the game
    def update(self, delta_time):
        '''self.penguin.update_animation()
        self.penguin.update()
        self.collumns.update()'''
        if self.move == True:
            self.penguin.update_animation()
            self.penguin.update()
            self.collumns.update()
        if self.move == False:
            self.penguin.stop()
            #self.collumns.stop()
        
        if arcade.check_for_collision_with_list(self.penguin,self.collumns):
            self.move=False
            
    # key = pressed
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.move==True:
            self.penguin.change_y=5
            self.penguin.change_angle=5

            

    # key = not pressed
    def on_key_release(self, key, modifiers): 
        pass



window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
