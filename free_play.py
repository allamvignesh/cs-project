import pygame
from pygame.locals import *
from walk_anim import Player
import pickle
from Tasks import Tasks
from threading import Thread

pygame.init()

clock = pygame.time.Clock()
fps = 60
size =[1000, 550]
screen = pygame.display.set_mode(size)

class Free_play():
	def __init__(self):
		pass

	def run(self):

		from walk_anim import Player
		from Tasks import Tasks

		tasksToDo = None

		a = 0
		b = 0
		c = 0

		cam_on = pygame.image.load("models/map parts/cam-on.png")
		cam_off = pygame.image.load("models/map parts/cam-off.png")
		redirect = pygame.image.load("models/map parts/redirect.png")
		electric = pygame.image.load("models/map parts/electric.png")
		upload = pygame.image.load("models/map parts/weapons/upload.png")

		#cafeteria
		bg = pygame.image.load('models/map parts/PC Computer - Among Us - Skeld Cafeteria.png')
		caflev = pygame.transform.flip(pygame.image.load("models/map parts/oxygen/o2-4.png"), True, False)
		cafup = upload
		cafred = pygame.transform.flip(pygame.image.load("models/map parts/weapons/redirect.png"), True, False)

		#weapons
		caf_weap = pygame.image.load("models/map parts/weapons/caf-weapons.png")
		weapons1 = pygame.image.load("models/map parts/weapons/weapons-1.png")
		weapons2 = pygame.image.load("models/map parts/weapons/weapons-2.png")
		weapons3 = pygame.image.load("models/map parts/weapons/weapons-3.png")
		weapons4 = pygame.image.load("models/map parts/weapons/weapons-4.png")
		weapons5 = pygame.image.load("models/map parts/weapons/weapons-5.png")
		weapons6 = pygame.image.load("models/map parts/weapons/weapons-6.png")
		weapons7 = pygame.image.load("models/map parts/weapons/weapons-7.png")
		weapons8 = pygame.image.load("models/map parts/weapons/weapons-8.png")
		weapons9 = pygame.image.load("models/map parts/weapons/weapons-9.png")
		weapons10 = pygame.image.load("models/map parts/weapons/weapons-10.png")
		weaponselectric = pygame.image.load("models/map parts/weapons/redirect.png")
		weaponsupload = upload
		weaponsgreenscreen = pygame.image.load("models/map parts/weapons/greenscreen.png")

		#oxygen
		wep_o2_nav_she = pygame.image.load("models/map parts/oxygen/wep-ox-nav-she.png")
		o21 = pygame.image.load("models/map parts/oxygen/o2-1.png")
		o22 = pygame.image.load("models/map parts/oxygen/o2-2.png")
		o23 = pygame.image.load("models/map parts/oxygen/o2-3.png")
		o24 = pygame.image.load("models/map parts/oxygen/o2-4.png")
		o25 = pygame.image.load("models/map parts/oxygen/o2-5.png")
		o26 = pygame.image.load("models/map parts/oxygen/o2-6.png")
		o27 = pygame.image.load("models/map parts/oxygen/o2-7.png")
		oredirect = redirect
		#navigation
		nav1 = pygame.image.load("models/map parts/navigation/nav-1.png")
		nav2 = pygame.image.load("models/map parts/navigation/nav-2.png")
		nav3 = pygame.image.load("models/map parts/navigation/nav-3.png")
		nav4 = pygame.image.load("models/map parts/navigation/nav-4.png")
		nav5 = pygame.image.load("models/map parts/navigation/nav-5.png")
		nav6 = pygame.image.load("models/map parts/navigation/nav-6.png")
		nav7 = pygame.image.load("models/map parts/navigation/nav-7.png")
		nav8 = pygame.image.load("models/map parts/navigation/nav-8.png")
		nav9 = pygame.image.load("models/map parts/navigation/nav-9.png")
		navredirect = redirect
		navelectric = electric

		#admin
		caf_ad_st = pygame.image.load("models/map parts/admin/admin-4.png")
		admin1 = pygame.image.load("models/map parts/admin/admin-1.png")
		admin2 = pygame.image.load("models/map parts/admin/admin-2.png")
		admin3 = pygame.image.load("models/map parts/admin/admin-3.png")
		admin4 = pygame.image.load("models/map parts/admin/admin-5.png")
		admin5 = pygame.image.load("models/map parts/admin/admin-6.png")
		admin6 = pygame.image.load("models/map parts/admin/admin-7.png")
		admin7 = pygame.image.load("models/map parts/admin/admin-8.png")
		admin8 = pygame.image.load("models/map parts/admin/admin-9.png")
		admin9 = pygame.image.load("models/map parts/admin/admin-10.png")
		admin10 = pygame.image.load("models/map parts/admin/admin-10.png")
		adminelec = electric
		adminupl = upload
		adminox = o23

		#storage
		sto1 = pygame.image.load("models/map parts/storage/storage-1.png")
		sto2 = pygame.image.load("models/map parts/storage/storage-2.png")
		sto3 = pygame.image.load("models/map parts/storage/storage-3.png")
		sto4 = pygame.image.load("models/map parts/storage/storage-4.png")
		sto5 = pygame.image.load("models/map parts/storage/storage-5.png")
		sto6 = electric
		sto7 = pygame.image.load("models/map parts/storage/storage-7.png")

		#commnication
		comm1 = pygame.image.load("models/map parts/communication/comm-1.png")
		comm2 = pygame.image.load("models/map parts/communication/comm-2.png")
		comm3 = pygame.image.load("models/map parts/communication/comm-3.png")
		comm4 = pygame.image.load("models/map parts/communication/comm-4.png")
		comm5 = pygame.image.load("models/map parts/communication/comm-5.png")
		comm6 = pygame.image.load("models/map parts/communication/comm-6.png")
		comm7 = pygame.image.load("models/map parts/communication/comm-7.png")
		comm8 = pygame.image.load("models/map parts/communication/comm-8.png")
		comm9 = pygame.image.load("models/map parts/communication/comm-9.png")
		comm10 = electric
		comm11 = upload

		#electric
		ele1 = pygame.image.load("models/map parts/electric/ele-1.png")
		ele2 = pygame.image.load("models/map parts/electric/ele-2.png")
		ele3 = pygame.image.load("models/map parts/electric/ele-3.png")
		ele4 = pygame.image.load("models/map parts/electric/ele-4.png")
		ele5 = pygame.image.load("models/map parts/electric/ele-5.png")
		ele6 = pygame.image.load("models/map parts/electric/ele-6.png")
		ele7 = electric
		ele8 = redirect
		ele9 = upload

		#lowerengine
		low1 = pygame.image.load("models/map parts/engine/eng-1.png")
		low2 = pygame.image.load("models/map parts/engine/eng-2.png")
		low3 = pygame.image.load("models/map parts/engine/eng-3.png")
		low4 = pygame.image.load("models/map parts/engine/eng-4.png")
		low5 = pygame.image.load("models/map parts/engine/eng-5.png")
		low6 = pygame.image.load("models/map parts/engine/eng-6.png")
		low7 = pygame.image.load("models/map parts/engine/eng-7.png")
		low8 = pygame.image.load("models/map parts/engine/eng-8.png")
		low9 = pygame.image.load("models/map parts/engine/eng-10.png")
		low10 = pygame.image.load("models/map parts/engine/eng-11.png")
		low11 = pygame.image.load("models/map parts/engine/eng-12.png")
		low12 = pygame.image.load("models/map parts/engine/eng-13.png")
		low13 = pygame.image.load("models/map parts/engine/eng-9.png")
		lowred = redirect

		#security
		sec1 = pygame.image.load("models/map parts/security/sec-1.png")
		sec2 = pygame.image.load("models/map parts/security/sec-2.png")
		sec3 = pygame.image.load("models/map parts/security/sec-3.png")
		sec4 = pygame.image.load("models/map parts/security/sec-4.png")
		sec5 = pygame.image.load("models/map parts/security/sec-5.png")
		sec6 = pygame.image.load("models/map parts/security/sec-6.png")
		secele = electric

		#medbay
		med1 = pygame.image.load("models/map parts/medbay/med-1.png")
		med2 = pygame.image.load("models/map parts/medbay/med-2.png")
		med3 = pygame.image.load("models/map parts/medbay/med-3.png")
		med4 = pygame.image.load("models/map parts/medbay/med-4.png")

		#shields
		she1 = pygame.image.load("models/map parts/shields/she-1.png")
		she2 = pygame.image.load("models/map parts/shields/she-2.png")
		she3 = pygame.image.load("models/map parts/shields/she-3.png")
		she4 = pygame.image.load("models/map parts/shields/she-4.png")
		she5 = pygame.image.load("models/map parts/shields/she-5.png")
		she6 = pygame.image.load("models/map parts/shields/she-6.png")
		she7 = pygame.image.load("models/map parts/shields/she-7.png")
		she8 = pygame.image.load("models/map parts/shields/she-8.png")
		she9 = pygame.image.load("models/map parts/shields/she-9.png")
		she10 = redirect

		#reactor
		rec1 = pygame.image.load("models/map parts/reactor/rec-1.png")
		rec2 = pygame.image.load("models/map parts/reactor/rec-2.png")
		rec3 = pygame.image.load("models/map parts/reactor/rec-3.png")

		class Sprite(pygame.sprite.Sprite):
			def __init__(self, sizex = 10, sizey = 10, surface = 'default'):
				pygame.sprite.Sprite.__init__(self)

				if surface == 'default':
					self.image = pygame.Surface((sizex, sizey))
					self.image.fill((255, 0, 0))
				else:
					self.image = surface

				self.rect = self.image.get_rect()

		q = open('collision_points.dat', 'rb')

		coll_loc = pickle.load(q)

		collision = [Sprite(k, l) for i,j,k,l in coll_loc]
		player = Player()
		players = pygame.sprite.Group()
		players.add(player)

		wall_group = pygame.sprite.Group()

		for i in range(len(collision)):
			wall_group.add(collision[i])

		topos = []
		sps = []

		#buttons
		tasks = Sprite(surface = pygame.image.load("models/buttons/tasks.png"))
		taskson = pygame.image.load("models/buttons/tasks.png")
		tasksoff = pygame.image.load("models/buttons/tasks_off.png")
		report = Sprite(surface = pygame.image.load("models/buttons/report.png"))
		reporton = pygame.image.load("models/buttons/report.png")
		reportoff = pygame.image.load("models/buttons/report_off.png")
		sabotage = Sprite(surface = pygame.image.load("models/buttons/sabotage.png"))
		vent = Sprite(surface = pygame.image.load("models/buttons/vent.png"))
		kill = Sprite(surface = pygame.image.load("models/buttons/kill.png"))
		killon = pygame.image.load("models/buttons/kill.png")
		killoff = pygame.image.load("models/buttons/kill_off.png")
		security = Sprite(surface = pygame.image.load("models/buttons/security.png"))

		mousebut = Sprite()

		mousebut.rect.x, mousebut.rect.y = 0, 0

		tasks.rect.x, tasks.rect.y = 897, 446
		report.rect.x, report.rect.y = 892, 333
		sabotage.rect.x, sabotage.rect.y = 897, 446
		vent.rect.x, vent.rect.y = 897, 446
		kill.rect.x, kill.rect.y = 789, 444
		security.rect.x, security.rect.y = 789, 444

		button_group = pygame.sprite.Group()
		button_group.add(tasks)
		button_group.add(report)
		button_group.add(sabotage)
		button_group.add(vent)
		button_group.add(kill)
		button_group.add(security)

		but = [tasks, report, sabotage, vent, kill]
		mous_grp = pygame.sprite.Group()
		mous_grp.add(mousebut)

		imposter = False

		if imposter:
			tasks.rect.x, tasks.rect.y = (0, -200)
		else:
			sabotage.rect.x, sabotage.rect.y = 0, -200
			kill.rect.x, kill.rect.y = 0, -200
			vent.rect.x, vent.rect.y = 0, -200

		tskpos = [(1290, 405, 10, 10), (1290, 233, 10, 10), (1478, 397, 10, 10), 
					(920, 256, 10, 10), (841, 180, 10, 10), (117, 121, 10, 10),
					(1260, 787, 10, 10), (1107, 817, 10, 10), (1035, 827, 10, 10), 
					(964, 860, 10, 10), (1761, 919, 10, 10), (1878, 791, 10, 10), 
					(1967, 776, 10, 10), (2028, 811, 10, 10), (2073, 1021, 10, 10),
					(1409, 1422, 10, 10), (1176, 1769, 10, 10), (1056, 1760, 10, 10), 
					(922, 1972, 10, 10), (887, 1771, 10, 10), (612, 1981, 10, 10), 
					(254, 1724, 10, 10), (-256, 1432, 10, 10), (-266, 1201, 10, 10), 
					(-206, 1201, 10, 10), (-111, 1201, 10, 10), (54, 1201, 10, 10),
					(-67, 997, 10, 10), (-13, 936, 10, 10), (-518, 815, 10, 10), 
					(-475, 833, 10, 10), (-719, 956, 10, 10), (-990, 1626, 10, 10), 
					(-1007, 1617, 10, 10), (-978, 1330, 10, 10), (-1001, 588, 10, 10), 
					(-917, 284, 10, 10), (639, 1091, 10, 10), (738, 1072, 10, 10), 
					(808, 1265, 10, 10), (1012, 1265, 10, 10), (1078, 1088, 10, 10), 
					(362, 1294, 10, 10), (-1316, 1020, 10, 10), (-1156, 799, 10, 10), 
					(-1366, 710, 10, 10), (-1273, 648, 10, 10), (-1278, 1344, 10, 10), 
					(340, 402, 220, 150), (-1071, 610, 10, 10)]


		ToDo = {5:1, 4:3, 3:2, 0:9, 1:3, 2:18, 6:18, 8:5, 9:2, 10:1, 11:18, 12:3, 13:8, 
				14:15, 15:18, 16:14, 17:18, 19:3, 21:12, 20:2, 42:1, 23:1, 24:10, 25:1, 
				26:7, 32:11, 33:6, 34:18, 43:17, 45:16, 31:1, 30:18, 35:11, 36:18, 27:19, 
				28:13, 37:1, 38:4, 40:0, 49:6}

		DoTo = []

		taskmgr = [Sprite(k+40, l+40) for i,j,k,l in tskpos]

		task_group = pygame.sprite.Group()

		for i in range(len(taskmgr)):
			task_group.add(taskmgr[i])

		dead_bodys = [(100, 100, 100, 100)]
		f = []
		Tasks = Tasks()

		#secCam
		secCam = 0
		secC1 = pygame.image.load("models/tasks/Security Camera/sec-2.png")
		secC2 = pygame.image.load("models/tasks/Security Camera/sec-1.png")
		secC3 = pygame.image.load("models/tasks/Security Camera/sec-3.png")
		secCNum = 1

		while True:
			c += 1
			wall_group.draw(screen)
			mousebut.rect.x, mousebut.rect.y = pygame.mouse.get_pos()
			mous_grp.draw(screen)
			task_group.draw(screen)

			screen.fill((0, 0, 0))

			before_pos = a, b

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 1
					exit()
				
				if event.type == pygame.MOUSEBUTTONDOWN:
					for i in range(len(but)):
						smashhit = pygame.sprite.collide_rect(mousebut, but[i])
						if smashhit and pygame.mouse.get_pressed()[0]:
							if tasksToDo in ToDo and not imposter:
								pygame.mixer.Channel(4).play(pygame.mixer.Sound(f'bgs/Among Us General Sounds/task_Inprogress.wav'))
								if ToDo[tasksToDo] == 0:
									Tasks.swipeCard()
								elif ToDo[tasksToDo] == 1:
									Tasks.fixWiring()
								elif ToDo[tasksToDo] == 2:
									Tasks.emptyGarbage()
								elif ToDo[tasksToDo] == 3:
									Tasks.upload()
								elif ToDo[tasksToDo] == 4:
									Tasks.Download(1)
								elif ToDo[tasksToDo] == 5:
									Tasks.clearLeaves()
								elif ToDo[tasksToDo] == 6:
									Tasks.alignEngine()
								elif ToDo[tasksToDo] == 7:
									Tasks.calibrate()
								elif ToDo[tasksToDo] == 8:
									Tasks.chartCourse()
								elif ToDo[tasksToDo] == 9:
									Tasks.weapons()
								elif ToDo[tasksToDo] == 10:
									Tasks.divertPower(1)
								elif ToDo[tasksToDo] == 11:
									Tasks.fualEngine()
								elif ToDo[tasksToDo] == 12:
									Tasks.fillCan()
								elif ToDo[tasksToDo] == 13:
									Tasks.inspectSample()
								elif ToDo[tasksToDo] == 14:
									Tasks.primeShield()
								elif ToDo[tasksToDo] == 15:
									Tasks.stabSteering()
								elif ToDo[tasksToDo] == 16:
									Tasks.unlockManifolds()
								elif ToDo[tasksToDo] == 17:
									Tasks.starReactor()
								elif ToDo[tasksToDo] == 18:
									Tasks.acceptPower()
								elif ToDo[tasksToDo] == 19:
									Tasks.medbayScan()

								pygame.mixer.Channel(4).play(pygame.mixer.Sound(f'bgs/Among Us General Sounds/task_Complete.wav'))	

			keys = pygame.key.get_pressed()

			if keys[K_w]:
				b += 3
			if keys[K_a]:
				a += 5
			if keys[K_s]:
				b -= 3
			if keys[K_d]:
				a -= 5

			#weapons
			screen.blit(bg, (0+a,0+b))
			screen.blit(weapons1, (1100+a, 260+b))
			screen.blit(weapons4, (1137+a, 204+b))
			screen.blit(weapons5, (1136+a, 286+b))
			screen.blit(weapons6, (1383+a, 463+b))
			screen.blit(weapons2, (1122+a, 256+b))
			screen.blit(caf_weap, (979+a, 362+b))
			screen.blit(weapons3, (980+a, 193+b))
			screen.blit(weapons7, (1132+a, 242+b))

			#o2
			screen.blit(wep_o2_nav_she, (1209+a, 652+b))
			screen.blit(o21, (875+a, 707+b))
			screen.blit(o22, (1006+a, 802+b))
			screen.blit(o24, (941+a, 830+b))
			screen.blit(o25, (1067+a, 722+b))
			screen.blit(o23, (1090+a, 806+b))

			if c%2 == 0:
				screen.blit(o26, (891+a, 777+b))
			else:
				screen.blit(o27, (891+a, 777+b))

			screen.blit(oredirect, (1229+a, 771+b))

			#navigation
			screen.blit(nav2, (1809+a, 798+b))
			screen.blit(nav1, (1808+a, 742+b))
			screen.blit(nav3, (1808+a, 752+b))
			screen.blit(nav4, (2008+a, 835+b))
			screen.blit(nav5, (2017+a, 1040+b))
			screen.blit(nav6, (2023+a, 930+b))
			screen.blit(nav7, (2066+a, 905+b))
			screen.blit(nav8, (2021+a, 812+b))
			screen.blit(nav9, (1946+a, 770+b))
			screen.blit(navredirect, (1866+a, 771+b))
			screen.blit(navelectric, (1747+a, 898+b))

			#admin
			screen.blit(caf_ad_st, (414+a, 958+b))
			screen.blit(admin1, (561+a, 1115+b))
			screen.blit(admin2, (578+a, 1056+b))
			screen.blit(admin3, (582+a, 1064+b))
			screen.blit(admin4, (824+a, 1248+b))
			screen.blit(admin5, (824+a, 1259+b))
			screen.blit(admin6, (999+a, 1259+b))
			screen.blit(admin7, (870+a, 1259+b))
			screen.blit(admin9, (831+a, 1081+b))
			screen.blit(admin10, (998+a, 1081+b))
			screen.blit(admin8, (838+a, 1099+b))
			screen.blit(adminelec, (645+a, 1094+b))
			screen.blit(adminupl, (749+a, 1084+b))
			screen.blit(adminox, (1078+a, 1095+b))

			#cafeteria
			screen.blit(caflev, (913+a, 226+b))
			screen.blit(cafup, (832+a, 159+b))
			screen.blit(cafred, (93+a, 104+b))

			#storage
			screen.blit(sto1, (80+a, 1249+b))
			screen.blit(sto2, (194+a, 1471+b))
			screen.blit(sto4, (279+a, 1700+b))
			screen.blit(sto5, (603+a, 1959+b))
			screen.blit(sto6, (365+a, 1298+b))
			screen.blit(sto7, (637+a, 1485+b))
			
			#communication
			screen.blit(comm1, (663+a, 1739+b))
			screen.blit(comm2, (662+a, 1696+b))
			screen.blit(comm3, (676+a, 1729+b))

			if c%2 == 0:
				screen.blit(comm8, (696+a, 1756+b))
			else:
				screen.blit(comm9, (696+a, 1756+b))

			screen.blit(comm10, (1046+a, 1752+b))
			screen.blit(comm11, (856+a, 1736+b))
			
			#electric
			screen.blit(ele3, (-694+a, 1147+b))
			screen.blit(ele6, (-302+a, 1293+b))
			screen.blit(ele1, (-304+a, 1353+b))
			screen.blit(ele4, ( 35+a, 1187+b))
			screen.blit(ele5, (-294+a, 1395+b))
			screen.blit(ele7, (-118+a, 1187+b))
			screen.blit(ele8, (-227+a, 1183+b))
			screen.blit(ele9, (-280+a, 1180+b))
			screen.blit(ele2, (-314+a, 1159+b))

			#security
			screen.blit(sec1, (-1055+a, 723+b))
			screen.blit(sec2, (-700+a, 729+b))
			screen.blit(sec3, (-620+a, 753+b))
			screen.blit(sec4, (-574+a, 809+b))
			screen.blit(sec5, (-475+a, 793+b))
			screen.blit(sec6, (-664+a, 780+b))
			screen.blit(secele, (-737+a, 945+b))

			#lowerengine
			screen.blit(low1, (-1097+a, 1269+b))
			screen.blit(low3, (-832+a, 1432+b))

			if c%2 == 0:
				screen.blit(low4, (-1088+a, 1394+b))
				screen.blit(low5, (-1078+a, 1607+b))
			else:
				screen.blit(low4, (-1087+a, 1389+b))
				screen.blit(low5, (-1077+a, 1606+b))

			
			screen.blit(low2, (-987+a, 1583+b))
			screen.blit(low6, (-993+a, 1592+b))

			if c%7 == 0:
				screen.blit(low9, (-825+a, 1548+b))
				screen.blit(low11, (-895+a, 1411+b))
			elif c%8 == 0:
				screen.blit(low10, (-863+a, 1449+b))
				screen.blit(low12, (-895+a, 1594+b))

			screen.blit(lowred, (-975+a, 1341+b))
			
			#upper engine
			screen.blit(low13, (-1099+a, 256+b))
			screen.blit(low3, (-838+a, 407+b))

			if c%2 == 0:
				screen.blit(low4, (-1089+a, 348+b))
			else:
				screen.blit(low4, (-1088+a, 349+b))

			screen.blit(low2, (-993+a, 556+b))
			screen.blit(low5, (-1081+a, 563+b))
			screen.blit(low6, (-997+a, 569+b))

			if c%7 == 0:
				screen.blit(low9, (-846+a, 383+b))
				screen.blit(low12, (-884+a, 539+b))
			elif c%8 == 0:
				screen.blit(low10, (-918+a, 535+b))
				screen.blit(low11, (-805+a, 433+b))

			screen.blit(ele8, (-906+a, 291+b))
			
			#medbay
			screen.blit(med1, (-706+a, 362+b))
			screen.blit(med2, (-401+a, 563+b))
			screen.blit(med3, (-142+a, 958+b))
			screen.blit(med4, (-52+a, 871+b))

			#shields
			screen.blit(she1, (1106+a, 1436+b))
			screen.blit(she2, (1103+a, 1429+b))
			screen.blit(she3, (1093+a, 1362+b))
			lig = [(1149, 1454), (1164, 1436), (1177, 1417), (1196, 1404), (1494, 1542), 
					(1494, 1513), (1495, 1483)]
			
			for i in lig[::-1]:
				screen.blit(she9, (i[0]+a, i[1]+b))

			screen.blit(she5, (1397+a, 1598+b))
			screen.blit(she6, (1131+a, 1436+b))
			screen.blit(she7, (1153+a, 1713+b))
			screen.blit(she10,(1425+a, 1411+b))

			#reactor
			screen.blit(rec2, (-1505+a, 636+b))
			screen.blit(rec3, (-1483+a, 1187+b))

			#cams
			if secCam == 0:
				screen.blit(cam_off, (-15+a, 385+b))
				screen.blit(cam_off, (-790+a, 927+b))
				screen.blit(cam_off, (577+a, 1076+b))
				screen.blit(cam_off, (1652+a, 878+b))
			else:
				screen.blit(cam_on, (-15+a, 385+b))
				screen.blit(cam_on, (-790+a, 927+b))
				screen.blit(cam_on, (577+a, 1076+b))
				screen.blit(cam_on, (1652+a, 878+b))

			#collision
			for i in range(len(collision)):
				collision[i].rect.x, collision[i].rect.y = coll_loc[i][0]+a, coll_loc[i][1]+b
			
			coll1 = pygame.surface.Surface([150, 100])
			h = coll1.get_rect()

			hit = pygame.sprite.spritecollide(player, wall_group, False)
			did = 0

			prev = a, b

			#tasks
			screen.blit(weaponselectric, (1491+a, 376+b))
			screen.blit(weaponsupload, (1276+a, 216+b))
			screen.blit(weapons10, (1274+a , 360+b))
			s = pygame.surface.Surface([10, 10])
			screen.blit(s, pygame.mouse.get_pos())
			security.rect.x, security.rect.y = 0, -200

			for i in range(len(taskmgr)):
				taskmgr[i].rect.x, taskmgr[i].rect.y = tskpos[i][0]+a, tskpos[i][1]+b

			todo = 0
			for i in range(len(taskmgr)):
				if pygame.sprite.collide_rect(player, taskmgr[i]) == 1:
					todo = 1
					tasksToDo = i
					tasks.image = taskson
					if i == 29:
						security.rect.x, security.rect.y = 789, 444
						if pygame.mouse.get_pressed()[0]:
							cc = a, b
							secCam = 1
					else:
						security.rect.x, security.rect.y = 0, -200
				else:
					tasks.image = tasksoff
			if todo == 1:
				tasks.image = taskson
			else:
				tasksToDo = None

			#dead
			dead = []
			dead_grp = pygame.sprite.Group()
			reportbut = 0
			for i in range(len(dead)):
				ded = dead[i]
				dead[i] = Sprite(100, 100)
				dead[i].rect.x, dead[i].rect.y = ded[0]+a, ded[1]+b
				dead_grp.add(dead[i])

			dead_grp.draw(screen)
			for i in dead:
				if pygame.sprite.collide_rect(player, i) == 1:
					reportbut = 1

			if reportbut == 1:
				report.image = reporton
			else:
				report.image = reportoff

			for i in collision:
				if pygame.sprite.collide_rect(player, i):
					if keys[pygame.K_w]:
						if abs(player.rect.top - i.rect.bottom) < 10 and hit:
							b = before_pos[1]

					if keys[pygame.K_a]:
						if abs(player.rect.left - i.rect.right) < 10 and hit:
							a = before_pos[0]

					if keys[pygame.K_s]:
						if abs(player.rect.bottom - i.rect.top) < 10 and hit:
							b = before_pos[1]

					if keys[pygame.K_d]:
						if abs(player.rect.right - i.rect.left) < 10 and hit:
							a = before_pos[0]


			players.draw(screen)
			coll = a, b

			#on the player
			a, b = prev

			screen.blit(weapons8, (1133+a, 509+b))
			screen.blit(weaponsgreenscreen, (1304+a, 278+b))
			screen.blit(weapons9, (1394+a, 409+b))
			screen.blit(she8, (1397+a, 1448+b))
			screen.blit(she4, (1129+a, 1635+b))
			screen.blit(comm5, (772+a, 1935+b))
			screen.blit(comm4, (792+a, 1970+b))
			screen.blit(comm6, (671+a, 1849+b))
			screen.blit(comm7, (1041+a, 1846+b))
			screen.blit(sto3, (439+a, 1447+b))
			screen.blit(low3, (-832+a, 1432+b))

			if c%2 == 0:
				screen.blit(low4, (-1088+a, 1394+b))
				screen.blit(low5, (-1078+a, 1607+b))
			else:
				screen.blit(low4, (-1087+a, 1389+b))
				screen.blit(low5, (-1077+a, 1606+b))

			if c%7 == 0:
				screen.blit(low9, (-825+a, 1548+b))
				screen.blit(low11, (-895+a, 1411+b))
			elif c%8 == 0:
				screen.blit(low10, (-863+a, 1449+b))
				screen.blit(low12, (-895+a, 1594+b))

			if c%2 == 0:
				screen.blit(low4, (-1089+a, 348+b))
			else:
				screen.blit(low4, (-1088+a, 349+b))

			screen.blit(rec1, (-1466+a, 824+b))
			screen.blit(low5, (-1074+a, 563+b))

			a, b = coll

			#buttons
			button_group.draw(screen)

			if secCam == 1:
				screen.blit(secC1, (-200, 0))
				screen.blit(secC2, (809, 245))
				screen.blit(secC3, (82, 230))

				if 809 < pygame.mouse.get_pos()[0] < 809+60 and 245 < pygame.mouse.get_pos()[1] < 245+60 and pygame.mouse.get_pressed()[0]:
					secCNum += 0.5
					if secCNum > 5:
						secCNum = 1

				if 82 < pygame.mouse.get_pos()[0] < 82+60 and 230 < pygame.mouse.get_pos()[1] < 230+60 and pygame.mouse.get_pressed()[0]:
					secCNum -= 0.5
					if secCNum < 1:
						secCNum = 4.5

				if int(secCNum) == 1:
					a, b = (1365, -720)
				elif int(secCNum) == 2:
					a, b = (785, -99)
				elif int(secCNum) == 3:
					a, b = 5, -825
				else:
					a, b = -1025, -660

				close = pygame.image.load("models/buttons/close.png")
				screen.blit(close, (100, 25))

				if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
					secCam = 0
					a, b = cc
					cc = None

			#wall_group.draw(screen)

			close = pygame.image.load("models/buttons/close.png")
			screen.blit(close, (0, 0))

			if 0 < pygame.mouse.get_pos()[0] < 50 and 0 < pygame.mouse.get_pos()[1] < 50 and pygame.mouse.get_pressed()[0]:
				return 1

			players.update(secCam)
			pygame.display.update()
			clock.tick(fps)
if __name__ == '__main__':
        Free_play().run()
