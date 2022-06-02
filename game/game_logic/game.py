'''Oleg Dmitrievich Lasukov'''
import arcade
import math
import random
import time
from abc import ABC, abstractmethod 
from constants import *
from game.actors.big_asteroid import BigAsteroid
from game.actors.ship import Ship
from game.actors.reaper import Reaper
from game.actors.bullet import Bullet
from game.actors.reaper_laser import LaserReaper
from game.actors.fuel import Fuel
PATH = r'F:\Folders\CS210\Asteroids improved\game\assets\textures'

class Game(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background=None
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.background=arcade.load_texture(PATH + r"\15784.jpg")
        self.held_keys = set()
        
        big_asteroid = BigAsteroid()
        self.asteroids = []
        
        self.bullets = []
        self.laser = []
        self.ship = Ship()
        self.game_over = False
        self.fuel = 1000
        self.fuel_gallons = []
        self.center_x = SCREEN_WIDTH/2
        self.center_y = SCREEN_HEIGHT/2
        
        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None
        self.score = 0
        self.reaper = Reaper()
        self.reapers = []
        self.flag = True
        
    def advance_song(self):
        self.current_song_index += 0
        if self.current_song_index >= len(self.music_list):
            self.current_song_index = 0
        print(f"Advancing song to {self.current_song_index}.")
        
    def play_song(self):
        self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(MUSIC_VOLUME)

        time.sleep(0.03)
        
    def switch_song(self):
        self.music.stop(self.current_player)
        self.current_song_index = 2
        self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(MUSIC_VOLUME)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH //2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.ship.draw()

        self.draw_score()
        self.check_lifes()
        for fuel in self.fuel_gallons:
            fuel.draw()
        for reaper in self.reapers:
            reaper.draw()
        for asteroid in self.asteroids:
            asteroid.draw()
        for bullet in self.bullets:
            bullet.draw()
        for laser in self.laser:
            laser.draw()
        if self.ship.alive == False:
            self.game_over == True
            arcade.draw_text("Game Over!\n Press R.", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.RED, 100, width=SCREEN_WIDTH,
                    align="center", anchor_x="center", anchor_y="center")
            arcade.finish_render()

    def update(self, delta_time):
        position = self.music.get_stream_position(self.current_player)
        if position == 0.0:
            self.advance_song()
            self.play_song()
        
        if self.game_over == False:
            self.check_keys()
        
            self.check_collisions()
            self.check_ship_crash()
        
            self.ship.advance()
            self.ship.wrap()
            
            self.reaper.advance()
            self.reaper.wrap()

            if self.score > 100 and self.flag == True:
                self.switch_song()
                self.flag = False
            
            if self.score > 100:
                self.create_reaper()
                
            if random.randint(1, 300) == 150 and len(self.fuel_gallons) < 3:
                fuel = Fuel()
                self.fuel_gallons.append(fuel)
                
            if self.fuel <= 0:
                self.game_over = True
                self.ship.alive = False
                self.game_end()
               
            for asteroid in self.asteroids:
                asteroid.advance()
                asteroid.rotate()
                asteroid.wrap()
            
            for bullet in self.bullets:
                bullet.wrap()
                bullet.advance()
                bullet.life_time += 1
                if bullet.life_time == 60:
                    bullet.alive = False
                    self.bullets.remove(bullet)
                    
            for laser in self.laser:
                laser.wrap()
                laser.advance()
                laser.life_time += 1
                if laser.life_time == 60:
                    laser.alive = False
                    self.laser.remove(laser)
                    
            for reaper in self.reapers:
                reaper.advance()
                reaper.wrap()
                #reaper.turn()
                start_x = reaper.center.x
                start_y = reaper.center.y


                dest_x = self.ship.center.x
                dest_y = self.ship.center.y
                if dest_x < start_x:
                    start_x -= 1
                elif dest_x > start_x:
                    start_x += 1
                if start_y > dest_y:
                    start_y += 1
                else:
                    start_y += 1


                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
                reaper.angle = math.degrees(angle) + 45
                if random.randint(1, 200) == 50:
                    laser = LaserReaper(reaper)
                    laser.fire()
                    self.laser.append(laser)
                    
                    

    def create_reaper(self):           
        if random.randint(1, 300) == 100:
            reaper = Reaper()
            self.reapers.append(reaper)
                    
    def draw_score(self):
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 30
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=20, color=arcade.color.ANDROID_GREEN)
        
            
            
                    
    def game_end(self):
        if self.game_over == True:
            self.current_song_index = 1
            print('Game over')
            self.music.stop(self.current_player)
            self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
            self.current_player = self.music.play(MUSIC_VOLUME)
        #ends game if condition reached

            self.asteroids.clear()
            self.bullets.clear()
            self.reapers.clear()
            self.laser.clear()
            self.fuel_gallons.clear()
            


    def setup(self):
        self.reaper_bullets = arcade.SpriteList()
        self.music_list = [PATH2+r"\sam-hulick-milky-way.mp3", PATH2+r"\sam-hulick-chasing-eva.mp3", PATH2+r"\sam-hulick-evasive-action.mp3"]
        # Array index of what to play
        self.current_song_index = 0
        # Play the song
        self.play_song()
        self.ship.alive = True
        self.game_over = False
        print('alive')
        for i in range(INITIAL_ROCK_COUNT):
            big_asteroid = BigAsteroid()
            self.asteroids.append(big_asteroid)
        self.ship.center.x = SCREEN_WIDTH/2
        self.ship.center.y = SCREEN_HEIGHT/2
        self.ship.velocity.dx = 0
        self.ship.velocity.dy = 0
        self.score = 0
        self.flag = True
        self.fuel = 1000


    def check_keys(self):

        if arcade.key.LEFT in self.held_keys:
            self.ship.left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.right()

        if arcade.key.UP in self.held_keys:
            self.ship.forward()
            self.remove_fuel()

        if arcade.key.DOWN in self.held_keys:
            self.ship.backward()
            self.remove_fuel()
        # Machine gun mode.
        #if arcade.key.SPACE in self.held_keys:
                #bullet = Bullet(self.ship)
                #self.bullets.append(bullet)
                #bullet.fire()
            


    def on_key_press(self, key: int, modifiers: int):

        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                bullet = Bullet(self.ship)
                self.bullets.append(bullet)
                bullet.fire()
                
        if key == arcade.key.R and self.game_over == True:
            self.music.stop(self.current_player)
            self.setup()
           

                

    def on_key_release(self, key: int, modifiers: int):

        if key in self.held_keys:
            self.held_keys.remove(key)
            
    def check_lifes(self):
        score_text = "Fuel: {}".format(self.fuel)
        start_x = 10
        start_y = SCREEN_HEIGHT - 50
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=20, color=arcade.color.ANDROID_GREEN)
    def remove_fuel(self):
        self.fuel = self.fuel - 1
        return (self.fuel)
            
    def check_ship_crash(self):

        for asteroid in self.asteroids:
            too_close = self.ship.radius + asteroid.radius
            if (abs(self.ship.center.x - asteroid.center.x) < too_close and
                abs(self.ship.center.y - asteroid.center.y) < too_close):
                        self.remove_fuel()
                        
        for laser in self.laser:
            too_close = self.ship.radius + laser.radius
            if (abs(self.ship.center.x - laser.center.x) < too_close and
                abs(self.ship.center.y - laser.center.y) < too_close):
                        self.remove_fuel()

        for fuel in self.fuel_gallons:
            too_close = self.ship.radius + fuel.radius
            if (abs(self.ship.center.x - fuel.center.x) < too_close and
                abs(self.ship.center.y - fuel.center.y) < too_close):
                        fuel.alive = False
                        self.fuel += 250
                        self.fuel_gallons.remove(fuel)
                    
        for reaper in self.reapers:
            too_close = self.ship.radius + reaper.radius
            if (abs(self.ship.center.x - reaper.center.x) < too_close and
                abs(self.ship.center.y - reaper.center.y) < too_close):
                        self.ship.alive = False
                        self.game_over = True
                        self.game_end()

    def check_collisions(self):

        for bullet in self.bullets:
            for asteroid in self.asteroids:

                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius

                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                                abs(bullet.center.y - asteroid.center.y) < too_close):
                        bullet.alive = False

                        asteroid.hit(self.asteroids)
                        self.score += asteroid.score()
            
        for bullet in self.bullets:
            for reaper in self.reapers:

                if bullet.alive and reaper.alive:
                    too_close = bullet.radius + reaper.radius

                    if (abs(bullet.center.x - reaper.center.x) < too_close and
                                abs(bullet.center.y - reaper.center.y) < too_close):
                        bullet.alive = False

                        self.score += reaper.hit()
        self.cleanup_zombies()
        
    def cleanup_zombies(self):
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)
        
        for reaper in self.reapers:
            if not reaper.alive:
                self.reapers.remove(reaper)