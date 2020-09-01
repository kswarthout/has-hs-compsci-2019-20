import math
import pygame


class Ball(pygame.sprite.Sprite):
    '''Represents an Arkanoid Ball'''

    speed = 10
    angleleft = 45
    angleright = 135

    def __init__(self, arena, paddle, bricks):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.arena = arena
        self.paddle = paddle
        self.bricks = bricks
        self.rect = self.image.get_rect()
        self.update = self.start

    def start(self):
        '''When the ball is introduced, places it on top of the paddle'''
        self.rect.centerx = self.paddle.rect.centerx
        self.rect.bottom = self.paddle.rect.top

        # check for mouse clicks from start state to allow update to switch to move state
        if pygame.mouse.get_pressed()[0] == 1:
            self.dx = 0
            self.dy = 1
            self.update = self.move

    def move(self):
        '''Updates the display when ball is not on paddle'''
        if self.rect.colliderect(self.paddle.rect) and self.dy > 0:
            # ballpos represents the ball's x position relative to paddle
            # ballmax is the max pos of ball on the paddle
            # factor is a ratio that represents where the ball is on the paddle
            ballpos = self.rect.width + self.rect.left - self.paddle.rect.left - 1
            ballmax = self.rect.width + self.paddle.rect.width - 2
            factor = float(ballpos) / ballmax
            angle = math.radians(self.angleright - factor *
                                 (self.angleright - self.angleleft))
            self.dx = self.speed*math.cos(angle)
            self.dy = -self.speed*math.sin(angle)

        self.rect.centerx = int(self.rect.centerx + self.dx)
        self.rect.centery = int(self.rect.centery + self.dy)

        # we have to check for the case when the ball hits the arena walls
        if not self.arena.rect.contains(self.rect):
            # print('self.rect.top: ' + str(self.rect.top))
            # print('self.arena.rect.bottom: ' + str(self.arena.rect.bottom))
            # check if the ball went out of the bottom part of the arena (player did not catch the ball)
            if self.rect.bottom > self.arena.rect.bottom:
                self.kill()
            else:
                if self.rect.left < self.arena.rect.left:
                    self.rect.left = self.arena.rect.left
                    self.dx = -self.dx
                if self.rect.right > self.arena.rect.right:
                    self.rect.right = self.arena.rect.right
                    self.dx = -self.dx
                if self.rect.top < self.arena.rect.top:
                    self.rect.top = self.arena.rect.top
                    self.dy = -self.dy
                if self.rect.top > self.arena.rect.bottom:
                    # print(self.rect.top)
                    # print(self.arena.rect.bottom)
                    self.update = self.start

                # Since the ball went out of bounds, we want to bring it back in the arena
                self.rect.clamp_ip(self.arena.rect)

        # destroy bricks
        brickscollided = pygame.sprite.spritecollide(self, self.bricks, False)
        if brickscollided:
            oldrect = self.rect
            left = right = up = down = 0
            for brick in brickscollided:
                brick.hit_count += 1
                # [] - brick, () - ball

                # ([)]
                if oldrect.left < brick.rect.left < oldrect.right < brick.rect.right:
                    self.rect.right = brick.rect.left
                    # self.setint()
                    left = -1

                # [(])
                if brick.rect.left < oldrect.left < brick.rect.right < oldrect.right:
                    self.rect.left = brick.rect.right
                    # self.setint()
                    right = 1

                # top ([)] bottom
                if oldrect.top < brick.rect.top < oldrect.bottom < brick.rect.bottom:
                    self.rect.bottom = brick.rect.top
                    # self.setint()
                    up = -1

                # top [(]) bottom
                if brick.rect.top < oldrect.top < brick.rect.bottom < oldrect.bottom:
                    self.rect.top = brick.rect.bottom
                    # self.setint()
                    down = 1

                if brick.color == 8:
                    if brick.hit_count == 2:
                        self.arena.add_score(brick.color)
                        brick.kill()
                else:
                    if brick.color != 9:
                        self.arena.add_score(brick.color)
                        brick.kill()

            # if the ball is asked to go both ways, then do not change direction
            # self.prevdx = self.dx
            # self.prevdy = self.dy
            if left + right != 0:
                # print((left + right)*abs(self.dx))
                self.dx = (left + right)*abs(self.dx)
            if up + down != 0:
                # print((up + down) * abs(self.dy))
                self.dy = (up + down) * abs(self.dy)

        # check for win
        # print(len(self.bricks))
        only_unbrekable = True
        if len(self.bricks) == 0:
            self.arena.level_cleared = True
        else:
            for brick in self.bricks:
                if brick.color != 9:
                    only_unbrekable = False

        if only_unbrekable:
            self.arena.level_cleared = True

        # print(self.dx == self.prevdx)
        # if self.dx == -self.prevdx:
        #     self.stuck_count += 1
        #     print(self.stuck_count)
        # if self.stuck_count >= 5:
        #     print('stuck')
