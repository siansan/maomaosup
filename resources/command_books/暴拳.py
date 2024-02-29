"""A collection of all commands that Shadower can use to interact with the game. 	"""

from src.common import config, settings, utils
import time
import math
from src.routine.components import Command
from src.common.vkeys import press, key_down, key_up,up_jump_press
from src.modules import runearrow
from src.modules import global_var
from random import random
# List of key mappings
class Key:
    # Movement
    key1='0'
    key2='1'
    key3='2'
    key4='3'
    key5='4'
    key6='5'
    key7='6'
    key8='7'
    key9='8'
    key10='9'
    key11="0"
    rune="t"
    jump='alt'
    tp="space"
    rope="1"
    press_key="c"
    rune='t'
#########################
#       Commands        #
#########################
def step(direction, target):
    """
    Performs one movement step in the given DIRECTION towards TARGET.
    Should not press any arrow keys, as those are handled by Auto Maple.
    """
    if global_var.map_id==runearrow.map_():
        if global_var.buff_stop==0:
            if global_var.stop==False:
                num_presses = 2
                if direction == 'up' or direction == 'down':
                    num_presses = 1
                if config.stage_fright and direction != 'up' and utils.bernoulli(0.75):
                    time.sleep(utils.rand_float(0.05, 0.15))
                if num_presses==2:
                    d_x = target[0] - config.player_pos[0]
                    threshold = settings.move_tolerance
                    if runearrow.action_()>=12:
                        while True:
                            key_down("up")
                            time.sleep(0.5)
                            if not runearrow.action_()>=12:
                                key_up("up")
                                break
                    walk_counter = 0
                    if d_x < 0:
                        key_down('left')
                        while config.enabled and d_x <-1 * threshold and walk_counter < 600:
                            if abs(d_x)>350:
                                press(Key.jump, num_presses)
                                time.sleep(0.10+ 0.03 * random())
                                press(Key.jump, num_presses)
                                # time.sleep(0.15+ 0.03 * random())
                                # press(Key.jump, num_presses)
                            
                                    # time.sleep(0.05+ 0.03 * random())
                            time.sleep(0.01)
                            
                            d_x = target[0] - config.player_pos[0]
                            if abs(d_x)<threshold:
                                key_up('left')
                                break
                            walk_counter+=1
                        key_up('left')
                    elif d_x>0:
                        key_down('right')
                        while config.enabled and d_x > threshold and walk_counter < 600 :
                            if abs(d_x)>350:
                                press(Key.jump, num_presses)
                                time.sleep(0.1+ 0.03 * random())
                                press(Key.jump, num_presses)
                                    # time.sleep(0.05+ 0.03 * random())
                            time.sleep(0.01)
                            
                            d_x = target[0] - config.player_pos[0]
                            if abs(d_x)<threshold:
                                key_up('right')
                                break
                            walk_counter+=1
                        key_up('right')
                        
                if config.bot.rune_active == True:
                    time.sleep(0.05 + 0.01 * random())
            d_y = target[1] - config.player_pos[1]
            if abs(d_y)>settings.adjust_tolerance:
                if direction == 'down':
                    if abs(d_y) >200:
                        Jump('down').main()
                        if runearrow.action_()>=12:
                            while True:
                                key_down(direction)
                                time.sleep(0.5)
                                if not runearrow.action_()>=12:
                                    key_up(direction)
                                    break
                elif direction == 'up':
                    if abs(d_y) >700:
                        up_jump_press(Key.jump, 1)
                        time.sleep(0.1)
                        up_jump_press('2', 2)
                        press(Key.rope,down_time=1)
                        time.sleep(2.5)
                    elif abs(d_y) >400:
                        press(Key.rope,down_time=1)
                        time.sleep(1.5)
                    else:
                        up_jump_press('2', 1)
                        time.sleep(0.8 + 0.2 * random())
                    if runearrow.action_()>=12:
                        while True:
                            key_down(direction)
                            time.sleep(0.5)
                            if not runearrow.action_()>=12:
                                key_up(direction)
                                break


class Adjust(Command):
    """Fine-tunes player position using small movements."""

    def __init__(self, x, y, max_steps=1):
        super().__init__(locals())
        self.target = (float(x), float(y))
        self.max_steps = settings.validate_nonnegative_int(max_steps)

    def main(self):
        counter = self.max_steps
        toggle = True
        if global_var.map_id==runearrow.map_():
            while config.enabled and counter > 0:
                if toggle:
                    d_x = self.target[0] - config.player_pos[0]
                    threshold = settings.adjust_tolerance
                    if abs(d_x) > threshold:
                        if runearrow.action_()>=12:
                            while True:
                                key_down("up")
                                time.sleep(0.5)
                                if not runearrow.action_()>=12:
                                    key_up("up")
                                    break
                    walk_counter = 0
                    if d_x < 0:
                        key_down('left')
                        while config.enabled and d_x < -1 * threshold and walk_counter < 600:
                            time.sleep(0.01)
                            d_x = self.target[0] - config.player_pos[0]
                            if abs(d_x)>350:
                                press(Key.jump)
                                time.sleep(0.6+ 0.03 * random())
                                press(Key.jump)
                            if abs(d_x)<=threshold:
                                key_up('left')
                                break
                            walk_counter+=1
                        key_up('left')
                    
                    elif d_x > 0:
                        key_down('right')
                        while config.enabled and d_x > threshold and walk_counter < 600:
                            time.sleep(0.01)
                            d_x = self.target[0] - config.player_pos[0]
                            if abs(d_x)>350:
                                press(Key.jump)
                                time.sleep(0.6+ 0.03 * random())
                                press(Key.jump)
                            if abs(d_x)<=threshold:
                                key_up('right')
                                break
                            walk_counter+=1
                        key_up('right')
                    counter -= 1
                if config.bot.rune_active == True:
                    time.sleep(0.05 + 0.1 * random())
            else:
                d_y = self.target[1] - config.player_pos[1]
                if abs(d_y) > settings.adjust_tolerance:
                    if d_y < 0:
                        if abs(d_y) >700:
                            key_down('up')
                            time.sleep(0.1)
                            up_jump_press('2', 2)
                            key_up('up')
                            press(Key.rope,down_time=1)
                            time.sleep(2.5)
                        elif abs(d_y) >350:

                            press(Key.rope,down_time=1)
                            time.sleep(1.5)
                        else:
                            key_down('up')
                            time.sleep(0.5)
                            up_jump_press('2', 2)
                            # time.sleep(0.1)
                            # press(Key.jump, 5, down_time=0.001,up_time=0.001)
                            # time.sleep(0.005)
                            key_up('up')
                            time.sleep(0.9 + 0.2 * random())
                    elif d_y>0:
                            key_down('down')
                            time.sleep(0.05)
                            press(Key.jump, 2, down_time=0.3)
                            time.sleep(0.05 + 0.1 * random())
                            key_up('down')
                            time.sleep(0.9 + 0.1 * random())
                    if runearrow.action_()>=12:
                        d_y = self.target[1] - config.player_pos[1]
                        while True:
                            if d_y>0:
                                key_down("down")
                                time.sleep(0.5)
                                if not runearrow.action_()>=12:
                                    key_up("down")
                                    break
                            else:
                                key_down("up")
                                time.sleep(0.5)
                                if not runearrow.action_()>=12:
                                    key_up("up")
                                    break
                    counter -= 1
                
                toggle = not toggle

class Jump(Command):
    """Performs a flash jump or 'Detonate' in the given direction."""

    def __init__(self, direction):
        super().__init__(locals())
        self.direction = settings.validate_arrows(direction)

    def main(self):
        key_down(self.direction)
        time.sleep(0.1)
        press(Key.jump, 1)
        if self.direction == 'up':
            press(Key.jump, 2)
        else:
            press(Key.jump, 1)
        key_up(self.direction)
        time.sleep(0.5)

class Buff(Command):
    """Uses each of Kanna's buffs once. Uses 'Haku Reborn' whenever it is available."""
    pass
        # if now%int()==0:
        #     if buff1!="":
        #         press(Key.buff1,1)


        # if now%int(self.buff_time2)==0:
        #     if buff2!="":
        #         press(Key.buff2,1)


        # if now%int(self.buff_time3)==0:
        #     if buff3!="":
        #         press(Key.buff3,1)


        # if now%int(self.buff_time4)==0:
        #     if buff4!="":
        #         press(Key.buff4,1)


        # if now%int(self.buff_time5)==0:
        #     if buff5!="":
        #         press(Key.buff5,1)


        # if now%int(self.buff_time6)==0:
        #     if buff6!="":
        #         press(Key.buff6,1)


        # if now%int(self.buff_time7)==0:
        #     if buff7!="":
        #         press(Key.buff7,1)


        # if now%int(self.buff_time8)==0:
        #     if buff8!="":
        #         press(Key.buff8,1)


        # if now%int(self.buff_time9)==0:
        #     if buff9!="":
        #         press(Key.buff9,1)


        # if now%int(self.buff_time10)==0:
        #     if buff10!="":
        #         press(Key.buff10,1)


        # if now - self.decent_buff_time > settings.buff_cooldown:
        #     for key in buffs:
        #         press(key, 3, up_time=0.3)
        #     self.decent_buff_time = now		

			
			
# class ShadowAssault(Command):
#     """
#     ShadowAssault in a given direction, jumping if specified. Adds the player's position
#     to the current Layout if necessary.
#     """

#     def __init__(self, direction, jump='False'):
#         super().__init__(locals())
#         self.direction = settings.validate_arrows(direction)
#         self.jump = settings.validate_boolean(jump)

#     def main(self):
#         num_presses = 3
#         time.sleep(0.05)
#         if self.direction in ['up', 'down']:
#             num_presses = 2
#         if self.direction != 'up':
#             key_down(self.direction)
#             time.sleep(0.05)
#         if self.jump:
#             if self.direction == 'down':
#                 press(Key.JUMP, 3, down_time=0.1)
#             else:
#                 press(Key.JUMP, 1)
#         if self.direction == 'up':
#             key_down(self.direction)
#             time.sleep(0.05)
#         press(Key.SHADOW_ASSAULT, num_presses)
#         key_up(self.direction)
#         if settings.record_layout:
# 	        config.layout.add(*config.player_pos)


# class CruelStab(Command):
#     """Attacks using 'CruelStab' in a given direction."""

#     def __init__(self, direction, attacks=2, repetitions=1):
#         super().__init__(locals())
#         self.direction = settings.validate_horizontal_arrows(direction)
#         self.attacks = int(attacks)
#         self.repetitions = int(repetitions)

#     def main(self):
#         time.sleep(0.05)
#         key_down(self.direction)
#         time.sleep(0.05)
#         if config.stage_fright and utils.bernoulli(0.7):
#             time.sleep(utils.rand_float(0.1, 0.3))
#         for _ in range(self.repetitions):
#             press(Key.CRUEL_STAB, self.attacks, up_time=0.05)
#         key_up(self.direction)
#         if self.attacks > 2:
#             time.sleep(0.3)
#         else:
#             time.sleep(0.2)


# class MesoExplosion(Command):
#     """Uses 'MesoExplosion' once."""

#     def main(self):
#         press(Key.MESO_EXPLOSION, 1, up_time=0.05)
		
# class CruelStabRandomDirection(Command):
#     """Uses 'CruelStab' once."""

#     def main(self):
#         press(Key.CRUEL_STAB, 1, up_time=0.05)	
        
# class DarkFlare(Command):
#     """
#     Uses 'DarkFlare' in a given direction, or towards the center of the map if
#     no direction is specified.
#     """

#     def __init__(self, direction=None):
#         super().__init__(locals())
#         if direction is None:
#             self.direction = direction
#         else:
#             self.direction = settings.validate_horizontal_arrows(direction)

#     def main(self):
#         if self.direction:
#             press(self.direction, 1, down_time=0.1, up_time=0.05)
#         else:
#             if config.player_pos[0] > 0.5:
#                 press('left', 1, down_time=0.1, up_time=0.05)
#             else:
#                 press('right', 1, down_time=0.1, up_time=0.05)
#         press(Key.DARK_FLARE, 3)

# class ShadowVeil(Command):
#     """
#     Uses 'ShadowVeil' in a given direction, or towards the center of the map if
#     no direction is specified.
#     """

#     def __init__(self, direction=None):
#         super().__init__(locals())
#         if direction is None:
#             self.direction = direction
#         else:
#             self.direction = settings.validate_horizontal_arrows(direction)

#     def main(self):
#         if self.direction:
#             press(self.direction, 1, down_time=0.1, up_time=0.05)
#         else:
#             if config.player_pos[0] > 0.5:
#                 press('left', 1, down_time=0.1, up_time=0.05)
#             else:
#                 press('right', 1, down_time=0.1, up_time=0.05)
#         press(Key.SHADOW_VEIL, 3)        		

# class ErdaShower(Command):
#     """
#     Uses 'ErdaShower' in a given direction, or down if
#     no direction is specified.
#     """

#     def __init__(self, direction=None):
#         super().__init__(locals())
#         if direction is None:
#             self.direction = 'down'
#         else:
#             self.direction = settings.validate_horizontal_arrows(direction)

#     def main(self):
#         if self.direction:
#             press(self.direction, 1, down_time=0.1, up_time=0.05)
#         else:
#             if config.player_pos[0] > 0.5:
#                 press('down', 1, down_time=0.1, up_time=0.05)
#             else:
#                 press('down', 1, down_time=0.1, up_time=0.05)
#         press(Key.ERDA_SHOWER, 3)


# class SuddenRaid(Command):
#     """Uses 'SuddenRaid' once."""

#     def main(self):
#         press(Key.SUDDEN_RAID, 3)


# class Arachnid(Command):
#     """Uses 'True Arachnid Reflection' once."""

#     def main(self):
#         press(Key.ARACHNID, 3)

# class TrickBlade(Command):
#     """Uses 'TrickBlade' once."""

#     def main(self):
#         press(Key.TRICKBLADE, 3)

# class SlashShadowFormation(Command):
#     """Uses 'SlashShadowFormation' once."""

#     def main(self):
#         press(Key.SLASH_SHADOW_FORMATION, 3)
		
# class SonicBlow(Command):
#     """Uses 'SonicBlow' once."""

#     def main(self):
#         press(Key.SONIC_BLOW, 3)

class key1(Command):

        def main(self):
            if Key.key1!="f12":
                press(Key.key1, 1, down_time=0.05,up_time=0.05)  
    
class key2(Command):

    def main(self):
        if Key.key2!="f12":
            press(Key.key2, 1, down_time=0.05)  

class key3(Command):

    def main(self):
        if Key.key3!="f12":
            press(Key.key3, 1)

class key4(Command):

        def main(self):
            if Key.key4!="f12":
                press(Key.key4, 1, down_time=0.05) 


class key5(Command):

    def main(self):
        if Key.key5!="f12":
            press(Key.key5, 1 ,down_time=1)


class key6(Command):

    def main(self):
        if Key.key6!="f12":
            press(Key.key6, 3)


class key7(Command):

    def main(self):
        if Key.key7!="f12":
            press(Key.key7, 3)


class key8(Command):

    def main(self):
        if Key.key8!="f12":
            press(Key.key8, 3)


class key9(Command):

    def main(self):
        if Key.key9!="f12":
            press(Key.key9, 3)

class skill_400041055(Command):#間隙破壞
    def __init__(self,):
        super().__init__(locals())
        self.skill_400041055=0
    def main(self):
        now=time.time()
        if Key.skill_400041055!="f12":
            #if self.skill_400041055==0 or (now-self.skill_400041055)>30:
                key_down("down")
                time.sleep(0.1)
                press(Key.skill_400041055, 1,down_time=0.05)
                time.sleep(0.1)
                key_down("down")
                self.skill_400041055=now
        

class skill_400041022(Command):#黑傑克
    def __init__(self):
        super().__init__(locals())
        self.skill_400041022=0
    
    def main(self):
        now=time.time()
        if Key.skill_400041022!="f12":
            #if self.skill_400041022==0 or (now-self.skill_400041022)>15:
                press(Key.skill_400041022, 1)
                self.skill_400041022=now
class rune(Command):#
    def main(self):
        now=time.time()
        if Key.rune!="f12":
            if (now-self.rune)>=300:
                press(Key.rune, 3,down_time=1)
                self.rune=now
class rune(Command):
    
    def main(self):
        if Key.rune!="":
            time.sleep(0.5)
            press(Key.rune, 1,down_time=3)
class press_key_down(Command):
    def main(self):
        if Key.press_key!="f12":
            key_down(Key.press_key)
class press_key_up(Command):
    def main(self):
        if Key.press_key!="f12":
            key_up(Key.press_key)
class ird(Command):
    def __init__(self):
        super().__init__(locals())
        self.ir=0
    def main(self):
        now=time.time()
        if Key.key11!="f12":
            if self.ir==0 or (now-self.ir)>60:
                key_down("down")
                time.sleep(0.05)
                press(Key.key11, 3)
                time.sleep(0.05)
                key_up("down")
class position(Command):
    def main(self):
        runearrow.go_shop(1)
        global_var.ss=1

class close(Command):
    def main(self):
        runearrow.go_shop(0)
        
class switch_rune_stop(Command):
    def __init__(self,value):
        super().__init__(locals())
        self.switch=value
    def main(self):
        global_var.switch=int(self.switch)

class nd(Command):
    def __init__(self,value):
        super().__init__(locals())
        self.autokey=value
    def main(self):
        press(self.autokey,nd=1)
class kuren(Command):
    def __init__(self,value):
        super().__init__(locals())
        self.autokey=value
    def main(self):
        for i in range(10):
            key_down("x")
            key_down("v")
            press('c',nd=1)
            time.sleep(0.125)
            press('f',nd=1)
            time.sleep(0.125)
            # press('f',nd=1)
            # time.sleep(0.02)
            key_up("x")
            key_down("x")
            press('c',nd=1)
            time.sleep(0.125)
            press('f',nd=1)
            time.sleep(0.125)
            # press('f',nd=1)
            # time.sleep(0.02)
            key_up("v")
            key_down("v")
class kunren_c(Command):
    def __init__(self,value):
        super().__init__(locals())
        self.autokey=value
    def main(self):
        for i in range(10):
            key_down("x")
            press('c',nd=1)
            # press('f',nd=1)
            # time.sleep(0.02)
            key_up("x")
            key_down("x")
        
        