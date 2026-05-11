from gamelib import*
game = Game(1100,600,"slime")

# Functions
# LEVEL 1
def hero_update():
    game.scrollBackground("still")
    hero.draw()
    king.move()

    # move left and right
    if keys.Pressed[K_LEFT]:
        game.scrollBackground("right",3)
        king.x+=1.5
        hero.draw()
        king.draw()
        for i in range(len(health)):
            health[i].x += 3
            health[i].draw()
        for i in range(len(mb)):
            mb[i].x += 3
            mb[i].draw()
        for i in range(len(bubble)):
            bubble[i].x += 3
            bubble[i].draw()
        for i in range(len(balls)):
            balls[i].draw()
            
    if keys.Pressed[K_RIGHT]:
        hero.visible=True
        game.scrollBackground("left",3)
        king.x -=1.5
        hero.draw()
        king.draw()
        for i in range(len(health)):
            health[i].x -= 3
            health[i].draw()
        for i in range(len(mb)):
            mb[i].x -= 3
            mb[i].draw()
        for i in range(len(bubble)):
            bubble[i].x -= 3
            bubble[i].draw()
        for i in range(len(balls)):
            balls[i].draw()

    # jump
    if keys.Pressed[K_SPACE] and hero.y > 350:
        hero.y-=20
    else:
        hero.y=470

    # healthbar & ammobar & bosshealthbar
    healthbar.moveTo(hero.x-20,hero.y-55)
    healthbar.width = hero.health/2
    magicbar.moveTo(hero.x-20,hero.y-65)
    magicbar.width = hero.ammo*3
    king_healthbar = Shape("bar",game,king.health,15,red)
    king_healthbar.moveTo(100,10)
    king_healthbar = king.health/15

    if mouse.LeftClick and magic.visible == False:
        magic.moveTo(hero.x,hero.y)
        magic.visible = True
        magic.move()

# LEVEL 2
def hero_update2():
    game.scrollBackground("still")
    hero.draw()
    king.move()
    if king.x<400:
        king.setSpeed(8,270)
    if king.x>800:
        king.setSpeed(8,90)

    # move left and right
    if keys.Pressed[K_LEFT]:
        game.scrollBackground("right",3)
        king.x+=1.5
        hero.draw()
        king.draw()
        for i in range(len(health)):
            health[i].x += 3
            health[i].draw()
        for i in range(len(mb)):
            mb[i].x += 3
            mb[i].draw()
        for i in range(len(bubble)):
            bubble[i].x += 3
            bubble[i].draw()
        for i in range(len(balls)):
            balls[i].draw()
            
    if keys.Pressed[K_RIGHT]:
        hero.visible=True
        game.scrollBackground("left",3)
        king.x -=1.5
        hero.draw()
        king.draw()
        for i in range(len(health)):
            health[i].x -= 3
            health[i].draw()
        for i in range(len(mb)):
            mb[i].x -= 3
            mb[i].draw()
        for i in range(len(bubble)):
            bubble[i].x -= 3
            bubble[i].draw()
        for i in range(len(balls)):
            balls[i].draw()

    # jump
    if keys.Pressed[K_SPACE] and hero.y > 350:
        hero.y-=20
    else:
        hero.y=470

    # healthbar & ammobar & bosshealthbar
    healthbar.moveTo(hero.x-20,hero.y-55)
    healthbar.width = hero.health/2
    magicbar.moveTo(hero.x-20,hero.y-65)
    magicbar.width = hero.ammo*3
    king_healthbar = Shape("bar",game,king.health,15,red)
    king_healthbar.moveTo(100,10)
    king_healthbar = king.health/15

    if mouse.LeftClick and magic.visible == False:
        magic.moveTo(hero.x,hero.y)
        magic.visible = True
        magic.move()



# Main Game ------------------------------------------------------------------------

# backgrounds
bg1 = Image("images/bg.jpg",game)
bg1.resizeTo(1100,600)

bg2 = Image("images/bg2.png",game)
bg2.resizeTo(1100,600)

# start buttons
start = Image("images/start.png",game)
story = Image("images/story.png",game)
instructions = Image("images/instructions.png",game)

story_text = Image("images/story_text.png",game)
story_text.resizeTo(1100,600)

instructions_text = Image("images/instructions_text.png",game)
instructions_text.resizeTo(1100,600)

# hero
hero = Animation("images/hero_walk.png",8,game,954/8,142,5,use_alpha=False)

# font
f = Font(black,95,red,"Comic Sans MS")
f1 = Font(white,45,black,"Roboto Mono")

# health
health=[]
for i in range (18):
    h = Animation("images/health2.png",10,game,960/5,348/2,3,use_alpha=False)
    health.append(h)
    x = randint(700,8000)
    y = randint(300,500)
    health[i].resizeBy(-70)
    health[i].moveTo(x,y)
# Health bar
healthbar = Shape("bar",game,hero.health,10,green)

# magic ball
mb=[]
for i in range(35):
    m = Animation("images/orb2.png",8,game,642/4,342/2,3,use_alpha=False)
    mb.append(m)
    x = randint(700,8000)
    y = randint(300,500)
    mb[i].resizeBy(-70)
    mb[i].moveTo(x,y)
# Magic bar
hero.ammo = 0
magicbar = Shape("bar",game,hero.ammo,10,blue)

# Bubble
bubble=[]
for i in range(10):
    b = Animation("images/bubble2.png",10,game,1231/5,417/2,3,use_alpha=False)
    b.resizeBy(-60)
    bubble.append(b)
    x = randint(1000,8000)
    y = randint(300,500)
    bubble[i].moveTo(x,y)

# Protection
protect = Animation("images/protection_ani.png",10,game,1387/5,554/2,3,use_alpha=False)
protect.resizeBy(-15)

# arrow
arrow = Image("images/arrow.png",game,use_alpha=False)

# platform
p = Image("images/p.png",game,use_alpha=False)
p.resizeTo(300,180)

# King Slime
king = Animation("images/King_slime.jpg",7,game,480/3,480/3,5,use_alpha=False)
king.resizeBy(40)
king.x = 200

# King Slime (angry)
king2 = Animation("images/King_slime_angry.jpg",7,game,480/3,480/3,4,use_alpha=False)
king2.resizeBy(35)
king2.visible=False

#King Slime Wings
wings = Animation("images/wings.png",6,game,386/3,202/2,4)
wings.resizeBy(250)

# King Slime's health bar
king_healthbar = Shape("bar",game,king.health,15,red)
    
# magic
magic = Animation("images/magic2.png",9,game,736/3,456/3,2,use_alpha=False)
magic.resizeBy(-30)
magic.setSpeed(15,90)
magic.invisible = False

#BOOM
boom = Animation("images/boom.png",12,game,699/4,554/3,1,use_alpha=False)
boom.visible =False

#BOOM2
boom2 = Animation("images/boom.png",12,game,699/4,554/3,1,use_alpha=False)
boom2.resizeBy(50)
boom2.visible =False

# regular & difficult buttons
regular_bg = Image("images/regular_bg.png",game)
regular_bg.resizeTo(550,600)
diff_bg = Image("images/diff_bg.png",game)
diff_bg.resizeTo(550,600)

normal = Image("images/normal.bu.png",game,use_alpha=False)
normal.resizeTo(250,110)
hard = Image("images/hard.bu.png",game,use_alpha=False)
hard.resizeTo(250,110)
                   
# game win and lose images
win = Image("images/win.png",game,use_alpha=False)
win.resizeBy(10)
lose = Image("images/lose.png",game,use_alpha=False)
lose.resizeBy(10)


# MUSIC
boom_music = Sound("music/boom sound.mp3",0)
bubble1 = Sound("music/button1.mp3",1)
button2 = Sound("music/button2.mp3",2)

# Variables
shoot = 0
collided_balls = 0
score = 0

# ***********Game Start Screen*********** --------------------------------
instructions_text.visible = False
story_text.visible = False


while not game.over:
    game.processInput()
    bg1.draw()
    # title
    game.drawText("SLIME INVASION",130,70,f)
    start.draw()
    start.y = 250
    story.draw()
    story.y = 350
    instructions.draw()
    instructions.y = 450
    instructions_text.draw()
    story_text.draw()


    # Start & story & instructions
    if mouse.collidedWith(start):
        start.resizeTo(250,125)
    else:
        start.resizeTo(200,100)

    if mouse.collidedWith(story):
        story.resizeTo(250,125)
    else:
        story.resizeTo(200,100)

    if mouse.collidedWith(instructions):
        instructions.resizeTo(250,125)
    else:
        instructions.resizeTo(200,100)

    # other images or next level
    if mouse.LeftClick and mouse.collidedWith(start,"rectangle"):
        button2.play()
        game.over = True

    if mouse.LeftClick and mouse.collidedWith(story,"rectangle"):
        button2.play()
        story_text.visible = True
    if keys.Pressed[K_SPACE]:
        button2.play()
        story_text.visible = False

    if mouse.LeftClick and mouse.collidedWith(instructions,"rectangle"):
        button2.play()
        instructions_text.visible = True
    if keys.Pressed[K_SPACE]:
        button2.play()
        instructions_text.visible = False
        
    game.update(30)


# ***********Choose Difficulty*************----------------------------------
game.over = False
regular_bg.moveTo(275,300)
diff_bg.moveTo(825,300)
normal.moveTo(275,300)
hard.moveTo(825,300)
while not game.over:
    game.processInput()
    
    regular_bg.draw()
    diff_bg.draw()
    normal.draw()
    hard.draw()

    if mouse.collidedWith(normal,"rectangle"):
        normal.resizeTo(300,130)
    else:
        normal.resizeTo(250,110)

    if mouse.collidedWith(hard,"rectangle"):
        hard.resizeTo(300,130)
    else:
        hard.resizeTo(250,110)
        
    if mouse.collidedWith(normal,"rectangle") and mouse.LeftClick:
        button2.play()
        game.over=True
        variable = 0
    if mouse.collidedWith(hard,"rectangle") and mouse.LeftClick:
        button2.play()
        game.over=True
        variable = 1
    
    game.update(30)

# ***********Level 1 Game*********** ------------------------------------

# slime balls
if variable==0: #noraml
    slime_balls = 180
    king.health = 600
    balls=[]
    for i in range(180):
        b = Image("images/balls.png",game,use_alpha=False)
        b.resizeBy(-70)
        x = -randint(200,12000)
        b.moveTo(x,300)
        balls.append(b)
        balls[i].setSpeed(5,270)
if variable==1: #hard
    slime_balls = 260
    king.health = 1000
    balls=[]
    for i in range(260):
        b = Image("images/balls.png",game,use_alpha=False)
        b.resizeBy(-70)
        x = -randint(300,13000)
        b.moveTo(x,300)
        balls.append(b)
        balls[i].setSpeed(5,270)
        
game.over = False
game.setBackground(bg2)
king.y=430
king.setSpeed(1.3,270)

magic.visible = False
protect.visible = False
protect.health = 50

#NORMAL!!!!!
while not game.over and variable == 0:
    game.processInput()
    hero_update()

    protect.draw()
    boom.draw(False)

    game.drawText("King Slime",10,10)

    
    # collect health and ammo and bubble
    for i in range(len(health)):
        health[i].draw()
        if hero.collidedWith(health[i]):
            hero.health+=5
            health[i].visible=False
            
    for i in range(len(mb)):
        mb[i].draw()
        if hero.collidedWith(mb[i]):
            bubble1.play()
            hero.ammo +=1
            mb[i].visible=False

    for i in range(len(bubble)):
        bubble[i].draw()
        if hero.collidedWith(bubble[i]):
            bubble[i].visible=False
            protect.moveTo(hero.x,hero.y)
            protect.health = 50
            protect.visible = True
            
            
    # King Slime shoot slime balls
    for i in range(len(balls)):
        balls[i].move()
        if balls[i].x > -50 and balls[i].x < -20:
            balls[i].moveTo(king.x,king.y)
            angle1 = randint(290,340)
            balls[i].setSpeed(8,angle1)
        if balls[i].x > 350 and balls[i].x < 400:
            angle2 = randint(225,260)
            balls[i].setSpeed(8,angle2)
        if hero.collidedWith(balls[i]): #hero
            collided_balls +=1
            balls[i].visible = False
            hero.health-=3
        if protect.collidedWith(balls[i]): #protection
            balls[i].visible = False
            protect.health -= 10
        if balls[i].x >1200:
            balls[i].visible = False
        if magic.collidedWith(balls[i]): #magic
            balls[i].visible = False

    # Protection
    protect.x = hero.x
    protect.y = hero.y
    if protect.health < 0:
        protect.visible = False
        
    # avoid the boss
    if hero.collidedWith(king):
        hero.health -=5

    # shoot fireballs
    magic.move()
    if hero.ammo > 0 and keys.Pressed[K_s] and magic.visible == False:
        magic.visible = True
        magic.moveTo(hero.x-30,hero.y)
        magic.rotateTowards(king)
        magic.moveTowards(king,15)
        hero.ammo -= 1
        shoot += 1

    if magic.collidedWith(king,"rectangle"):
        boom.visible=True
        boom.moveTo(king.x+30,king.y)
        boom_music.play()
        king.health -= 30
        magic.visible = False

    # go into level 2
    if king.health < 300:
        game.over = True

    if hero.health <= 0:
        game.over = True

    game.update(30)

# HARD!!!!!
while not game.over and variable == 1:
    game.processInput()
    hero_update()

    protect.draw()
    boom.draw(False)

    game.drawText("King Slime",10,10)
    
    # collect health and ammo and bubble
    for i in range(len(health)):
        health[i].draw()
        if hero.collidedWith(health[i]):
            hero.health+=5
            health[i].visible=False
            
    for i in range(len(mb)):
        mb[i].draw()
        if hero.collidedWith(mb[i]):
            bubble1.play()
            hero.ammo +=1.5
            mb[i].visible=False

    for i in range(len(bubble)):
        bubble[i].draw()
        if hero.collidedWith(bubble[i]):
            bubble[i].visible=False
            protect.moveTo(hero.x,hero.y)
            protect.health = 50
            protect.visible = True
            
    # King Slime shoot slime balls
    for i in range(len(balls)):
        balls[i].move()
        if balls[i].x > -50 and balls[i].x < -20:
            balls[i].moveTo(king.x,king.y)
            angle1 = randint(290,320)
            balls[i].setSpeed(8,angle1)
        if balls[i].x > 350 and balls[i].x < 400:
            angle2 = randint(235,250)
            balls[i].setSpeed(8,angle2)
        if hero.collidedWith(balls[i]): #hero
            collided_balls +=1
            balls[i].visible = False
            hero.health-=3
        if protect.collidedWith(balls[i]): #protection
            balls[i].visible = False
            protect.health -= 10
        if balls[i].x >1200:
            balls[i].visible = False
        if magic.collidedWith(balls[i]): #magic
            balls[i].visible = False

    # Protection
    protect.x = hero.x
    protect.y = hero.y
    if protect.health < 0:
        protect.visible = False
        
    # avoid the boss
    if hero.collidedWith(king):
        hero.health -=5

    # shoot fireballs
    magic.move()
    if hero.ammo > 0 and keys.Pressed[K_s] and magic.visible == False:
        magic.visible = True
        magic.moveTo(hero.x-30,hero.y)
        magic.rotateTowards(king)
        magic.moveTowards(king,15)
        hero.ammo -= 1
        shoot += 1

    if magic.collidedWith(king,"rectangle"):
        boom.visible=True
        boom.moveTo(king.x+30,king.y)
        boom_music.play()
        king.health -= 30
        magic.visible = False

    # go into level 2
    if king.health < 500:
        game.over = True

    if hero.health <= 0:
        game.over = True

    game.update(30)


# ***********Level 2 Game*********** -----------------------------------
game.over = False
magic.visible=False
protect.visible=False

king.setSpeed(3.5,270)
for i in range(10):
    king.y -= 25

#NORMAL!!!!! 
while not game.over and variable==0:
    game.processInput()
    hero_update2()
    protect.draw()

    # wings
    wings.moveTo(king.x,king.y)
    
    # angry king slime
    king.visible=False
    king2.visible=True
    king2.moveTo(king.x,king.y)
    

    game.drawText("King Slime",10,10)

    boom.draw(False)
    boom2.draw(False)

    # Collect health and ammo and bubble
    for i in range(len(health)):
        health[i].draw()
        if hero.collidedWith(health[i]):
            hero.health+=5
            health[i].visible=False
            
    for i in range(len(mb)):
        mb[i].draw()
        if hero.collidedWith(mb[i]):
            bubble1.play()
            hero.ammo +=1
            mb[i].visible=False

    for i in range(len(bubble)):
        bubble[i].draw()
        if hero.collidedWith(bubble[i]):
            bubble[i].visible=False
            protect.moveTo(hero.x,hero.y)
            protect.health = 50
            protect.visible = True

    # King Slime shoot slime balls
    for i in range(len(balls)):
        balls[i].move()
        if balls[i].x > -50 and balls[i].x < -20:
            balls[i].moveTo(king.x,king.y)
            angle1 = randint(160,200)
            balls[i].setSpeed(8,angle1)
        if hero.collidedWith(balls[i]): #hero
            collided_balls +=1
            balls[i].visible = False
            hero.health-=3
        if protect.collidedWith(balls[i]): #protection
            balls[i].visible = False
            protect.health -= 10
        if balls[i].x >1200:
            balls[i].visible = False
        if magic.collidedWith(balls[i]):
            balls[i].visible = False

    # Protection
    protect.x = hero.x
    protect.y = hero.y
    if protect.health < 0:
        protect.visible = False

    
    # avoid the boss
    if hero.collidedWith(king) or hero.collidedWith(king2):
        hero.health -=5
        
    # shoot fireballs
    magic.move()
    if hero.ammo > 0 and keys.Pressed[K_s] and magic.visible == False:
        magic.visible = True
        magic.moveTo(hero.x-30,hero.y)
        magic.moveTowards(king,12)
        magic.rotateTowards(king)
        hero.ammo -= 1
        shoot += 1

    if magic.collidedWith(king,"rectangle") or magic.collidedWith(king2,"rectangle"):
        boom.visible=True
        boom.moveTo(king.x,king.y)
        boom_music.play()
        king.health -= 25
        magic.visible = False

    if hero.health <= 0:
        game.over = True

    if king.health < -15:
        king.setSpeed(0,180)
        king.visible = False
        boom2.visible = True
        boom2.moveTo(king.x,king.y)
        game.over=True
        
    game.update(30)

#HARD!!!!!
while not game.over and variable==1:
    game.processInput()
    hero_update2()
    protect.draw()

    # wings
    wings.moveTo(king.x,king.y)
    
    # angry king slime
    king.visible=False
    king2.visible=True
    king2.moveTo(king.x,king.y)
    

    game.drawText("King Slime",10,10)

    boom.draw(False)
    boom2.draw(False)

    # Collect health and ammo and bubble
    for i in range(len(health)):
        health[i].draw()
        if hero.collidedWith(health[i]):
            hero.health+=5
            health[i].visible=False
            
    for i in range(len(mb)):
        mb[i].draw()
        if hero.collidedWith(mb[i]):
            bubble1.play()
            hero.ammo +=1.5
            mb[i].visible=False

    for i in range(len(bubble)):
        bubble[i].draw()
        if hero.collidedWith(bubble[i]):
            bubble[i].visible=False
            protect.moveTo(hero.x,hero.y)
            protect.health = 50
            protect.visible = True

    # King Slime shoot slime balls
    for i in range(len(balls)):
        balls[i].move()
        if balls[i].x > -50 and balls[i].x < -20:
            balls[i].moveTo(king.x,king.y)
            angle1 = randint(160,200)
            balls[i].setSpeed(8,angle1)
        if hero.collidedWith(balls[i]): #hero
            collided_balls +=1
            balls[i].visible = False
            hero.health-=3
        if protect.collidedWith(balls[i]): #protection
            balls[i].visible = False
            protect.health -= 10
        if balls[i].x >1200:
            balls[i].visible = False
        if magic.collidedWith(balls[i]):
            balls[i].visible = False

    # Protection
    protect.x = hero.x
    protect.y = hero.y
    if protect.health < 0:
        protect.visible = False

    
    # avoid the boss
    if hero.collidedWith(king) or hero.collidedWith(king2):
        hero.health -=5
        
    # shoot fireballs
    magic.move()
    if hero.ammo > 0 and keys.Pressed[K_s] and magic.visible == False:
        magic.visible = True
        magic.moveTo(hero.x-30,hero.y)
        magic.moveTowards(king,12)
        magic.rotateTowards(king)
        hero.ammo -= 1
        shoot += 1

    if magic.collidedWith(king,"rectangle") or magic.collidedWith(king2,"rectangle"):
        boom.visible=True
        boom.moveTo(king.x,king.y)
        boom_music.play()
        king.health -= 25
        magic.visible = False

    if hero.health <= 0:
        game.over = True

    if king.health < -10:
        king.setSpeed(0,180)
        king.visible = False
        boom2.visible = True
        boom2.moveTo(king.x,king.y)
        game.over=True
        
    game.update(30)

# Lose & Win BG
lose_bg = Image("images/lose_bg.png",game)
lose_bg.resizeTo(1100,600)
win_bg = Image("images/happy.png",game)
win_bg.resizeTo(1100,600)


# ***********Game End Screen*********** ------------------------------------
game.over = False
if hero.health > 0 and king.health <= 0:
    game.setMusic("music/win music.mp3")
if hero.health <= 0 and king.health > 0:
    game.setMusic("music/lose music.mp3")

game.playMusic()

while not game.over:
    game.processInput()
    bg2.draw()
    
    if hero.health > 0 and king.health < 0:
        win_bg.draw()
        win.draw()
        win.y = 150
        game.drawText("Press [q] to leave",900,550)
        if variable ==0:
            
            score= 300 + 5*(hero.health) + 10*(shoot) + 5*(slime_balls - collided_balls) - 10*(collided_balls)

        if variable ==1:
            
            score= (500 + 5*(hero.health) + 10*(shoot) + 5*(slime_balls - collided_balls) - 10*(collided_balls))*1.5
            
        if keys.Pressed[K_q]:
            game.over = True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

    if hero.health < 0 and king.health > 0:
        lose_bg.draw()
        lose.draw()
        lose.y = 150
        game.drawText("Press [q] to leave",900,550)
        if variable ==0:
            
            score= 5*(hero.health) + 10*(shoot) + 5*(slime_balls - collided_balls) - 10*(collided_balls) - 300

        if variable ==1:
            
            score=(5*(hero.health) + 10*(shoot) + 5*(slime_balls - collided_balls) - 10*(collided_balls) - 500)*1.5
            
        if keys.Pressed[K_q]:
            game.over = True

    game.drawText("Hero Final Health:" + str(hero.health),400,250,f1)
    game.drawText("Fireballs shot:" + str(shoot),400,290,f1)
    game.drawText("Slime Balls Avoided:" + str(slime_balls - collided_balls),400,330,f1)
    game.drawText("Slime Balls Hit:" + str(collided_balls),400,370,f1)
    game.drawText("SCORE:" + str(score),400,410,f1)
    game.update(30)

game.quit()
