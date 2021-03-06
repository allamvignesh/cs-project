import pygame
from pygame.locals import *
import random, time
from free_play import Free_play
from online_muiltiplayer import online

pygame.init()
pygame.mixer.init()

size =[1000, 550]
screen = pygame.display.set_mode(size)
pygame.display.set_icon(pygame.image.load("idle.png"))
pygame.display.set_caption("Among US Project")

clock = pygame.time.Clock()
fps = 50
pygame.mixer.music.load("bgs/Among Us Theme.wav") 

Free_play = Free_play()

Theme = pygame.mixer.Sound('bgs/Among Us Theme.wav')
Theme.set_volume(0.5)
pygame.mixer.Channel(0).play(Theme)


class Screens():
	def __init__(self):
		if self.TitleScreen() != 0:
			while True:

				if pygame.mixer.Channel(0).get_busy() == 0:
					pygame.mixer.Channel(0).play(Theme)

				Theme.set_volume(0.5)

				self.nextScreen = self.mainScreen()

				Theme.set_volume(0.1)

				if self.nextScreen == 1:
					try:
						online().run()
					except:
						pass

				elif self.nextScreen == 2:
					pygame.mixer.music.stop() 
					Free_play.run()

				else:
					pygame.mixer.Channel(2).play(pygame.mixer.Sound('bgs/Among Us General Sounds/Panel_GenericDisappear.wav'))
					time.sleep(0.5)
					pygame.quit()
					exit()

	def TitleScreen(self):

		im1 = pygame.image.load("models/titleScreen/1.png")
		im2 = pygame.image.load("models/titleScreen/2.jpeg")
		b = 0
		a = 0
		g = 1

		while True:

			b += g
			
			if b == 255:
				g = -1

			if b == 0:
				return 1

			screen.fill(0)

			imcopy = im1.copy()
			imcopy.fill((255, 255, 255, b), None, pygame.BLEND_RGBA_MULT)

			screen.blit(im2, (-50, 0))
			screen.blit(imcopy, (291, 208))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 0

			pygame.display.update()
			clock.tick(fps)

	def mainScreen(self):
		im1 = pygame.image.load("models/titleScreen/1.png")
		online = pygame.image.load("images/main_screen/2.png")
		freeplay = pygame.image.load("images/main_screen/3.png")

		online_rect = online.get_rect()
		freeplay_rect = freeplay.get_rect()

		hover1 = 0
		hover2 = 0

		colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0), (255, 128, 0), 
				(255, 255, 255), (255, 0, 255), (0, 255, 255), (102, 51, 0), (0, 204, 0)]
		plys = [self.colorchanger(pygame.image.load(f'images/main_screen/mainscreenCrew{i}.png'), random.choice(colors)) for i in range(1,7)]
		bliting = [[random.choice(plys), random.randint(-500, 1000), random.randint(-100, 560)] for i in range(len(plys))]

		while True:

			screen.fill(0)

			if pygame.mixer.Channel(0).get_busy() == 0:
					pygame.mixer.Channel(0).play(Theme)

			for i in range(len(bliting)):
				bliting[i][1] += 1
				if bliting[i][1] > 1000:
					bliting[i][1] = -100
					bliting[i][2] = random.randint(-100, 560)

			for i in range(len(bliting)):
				screen.blit(bliting[i][0], (bliting[i][1], bliting[i][2]))

			screen.blit(im1, (281, 74))
			screen.blit(online, (583, 298))
			screen.blit(freeplay, (239, 298))

			if 584<pygame.mouse.get_pos()[0]<774 and 299<pygame.mouse.get_pos()[1]<377:
				if hover1 == 0:
					hover1 += 1
					pygame.mixer.Channel(1).play(pygame.mixer.Sound('bgs/Among Us General Sounds/UI_Hover.wav'))
				
				if pygame.mouse.get_pressed()[0]:
					pygame.mixer.Channel(2).play(pygame.mixer.Sound('bgs/Among Us General Sounds/UI_Select.wav'))
					return 1
			else:
				hover1 = 0

			if 239<pygame.mouse.get_pos()[0]<429 and 299<pygame.mouse.get_pos()[1]<377:
				if hover2 == 0:
					hover2 += 1
					pygame.mixer.Channel(1).play(pygame.mixer.Sound('bgs/Among Us General Sounds/UI_Hover.wav'))
				
				if pygame.mouse.get_pressed()[0]:
					pygame.mixer.Channel(2).play(pygame.mixer.Sound('bgs/Among Us General Sounds/UI_Select.wav'))
					return 2
			else:
				hover2 = 0
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 0
			
			pygame.display.update()
			clock.tick(fps)


	def colorchanger(self, surface, color):
		"""Fill all pixels of the surface with color, preserve transparency."""
		surface = surface.convert_alpha()
		w, h = surface.get_size()
		r, g, b = color
		for x in range(w):
			for y in range(h):
				if surface.get_at((x,y)) == (255, 255, 255, 255):
					surface.set_at((x, y), pygame.Color(r, g, b, 255))
		return surface

Screens()