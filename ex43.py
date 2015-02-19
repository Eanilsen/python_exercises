# See oop_process.txt

from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # Print out the last scene
        current_scene.enter()

class Death(self):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud... if she were smarter.",
        "Such a loser.",
        "I have a small puppy that is better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print """
                The Gothons of Planet Percal #25 have invaded your ship and
                destroyed your entire crew. You are the last surviving member
                and your last mission is to get the neutron destruct bomb from
                the Weapons Armory when a Gothon jumps out, red scaly skin, dark
                grimy teeth and an evil clown costume flowing around his hate
                filled body. He is blocking the door to the Armory and about to
                pull a weapon to blast you.
        """

        action = raw_input("> ")

        if action == "shoot":
            print "No."
            return 'death'
        elif action == "dodge":
            print "No."
            return 'death'
        elif action == "tell a joke":
            print "Yes."
            return 'laser_weapon_armory'
        else:
            print "Does not compute"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print "Guess the code. 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "Nope"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "Yes."
            return 'the_bridge'
        else:
            print "No."
            return 'death'

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('centras_corridor')
a_game = Engine(a_map)
a_game.play()
