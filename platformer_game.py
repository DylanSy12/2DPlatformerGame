from cmu_graphics import *
# Setup
app.level=1
app.room = "A"
app.reset = False
app.keys = 0
app.score = 0
app.stepsPerSecond = 45
app.width = 400
app.height = 440
app.game_paused = False
from Character import *
from Fireball import *
from Sword import *
from Shield import *
from Coin import *
from Key import *
from LevelFunctions import *
from Level import *
from TrackMissile import *
from Enemy import *
app.resetableList = [
    Key.keyList, KeyDoor.keyDoorList, BreakWall.breakWallList, 
    Enemy.enemyList, TrackMissile.trackMissileList, MovingPlatform.movePlatList, 
    LinkedWall.wallList, Switch.switchList, ResetButton.buttonList, 
    Trigger.triggerList
]
levelList = [
    Level1(), Level2(), Level3(), 
    Level4(), Level5(), Level6(), 
    Level7(), Level8(), Level9(), 
    Level10(), Level11()
]
border = Line(-800, 425, 1200, 425, fill = 'white', lineWidth = 35)
#Info Display
cheatBox = Rect(110, 0, 180, 20, border = 'red', opacity = 75, borderWidth = 1)
cheatDisplay = Label("aAbBcCdDfFhHIJmMqQsStTwW", 200, 10, fill = 'red')
cheatDisplayGroup = Group(cheatBox, cheatDisplay)
cheatDisplayGroup.visible = False
characterStatBox = Rect(0, 120, 110, 180, border = 'red', opacity = 75, borderWidth = 1)
characterDisplay = Label("character: ", 55, 130, fill = 'red')
characterMaxHealthDisplay = Label("MaxHP: " + str(character.maxHP), 55, 140, fill = 'red')
characterHealthDisplay = Label("CurrentHP: " + str(character.hp), 55, 150, fill = 'red')
characterHPRegenSpeedDisplay = Label("HPRegenSpeed: " + str(character.hpRegenSpeed), 55, 160, fill = 'red')
characterHPRegenTimeDisplay = Label("HPRegenTime: " + str(character.hpRegenTime), 55, 170, fill = 'red')
characterHPRegenAmountDisplay = Label("HPRegenAmount: " + str(character.hpRegenAmount), 55, 180, fill = 'red')
characterMaxMPDisplay = Label("MaxMP: " + str(character.maxMP), 55, 190, fill = 'red')
characterMPDisplay = Label("CurrentMP: " + str(character.mp), 55, 200, fill = 'red')
characterMPRegenSpeedDisplay = Label("MPRegenSpeed: " + str(character.mpRegenSpeed), 55, 210, fill = 'red')
characterMPRegenTimeDisplay = Label("MPRegenTime: " + str(character.mpRegenTime), 55, 220, fill = 'red')
characterMPRegenAmountDisplay = Label("MPRegenAmount: " + str(character.mpRegenAmount), 55, 230, fill = 'red')
characterInvincibilityTimeDisplay = Label("InvTime: " + str(character.maxInv), 55, 240, fill = 'red')
characterMaxJumpDisplay = Label("MaxJump: " + str(character.maxJump), 55, 250, fill = 'red')
scoreDisplay = Label("Score: " + str(app.score), 55, 260, fill= 'red')
keyDisplay = Label("Keys: " + str(app.keys), 55, 270, fill = 'red')
levelDisplay = Label("Level: " + str(app.level), 55, 280, fill = 'red')
deathDisplay = Label("Deaths: " + str(character.deaths), 55, 290, fill = 'red')
statBox = Rect(110, 120, 290, 200, border = 'red', opacity = 75, borderWidth = 1)
shieldDisplay = Label("Shield: ", 250, 130, fill = 'cyan')
shieldTimeDisplay = Label("TimeLeft: " + str(shield.time) + "   TimeMax: " + str(shield.maxTime), 255, 140, fill = 'cyan')
shieldHealthDisplay = Label("HealthLeft: " + str(shield.health) + "   HealthMax: " + str(shield.maxHealth), 255, 150, fill = 'cyan')
shieldCooldownDisplay = Label("CooldownLeft: " + str(shield.cooldownTime) + "   CooldownMax: " + str(shield.maxCooldown), 255, 160, fill = 'cyan')
shieldRadiusDisplay = Label("Size: " + str(shield.shape.radius), 255, 170, fill = 'cyan')
shieldDamageDisplay = Label("Damage: " + str(shield.damage), 255, 180, fill = 'cyan')
shieldPushDisplay = Label("Push Strength: " + str(shield.pushMulti), 255, 190, fill = 'cyan')
swordDisplay = Label("Sword: ", 255, 200, fill = 'silver')
swordRangeDisplay = Label("Range: " + str(sword.shape.width), 255, 210, fill = 'silver')
swordDamageDisplay = Label("Damage: " + str(sword.damage), 255, 220, fill = 'silver')
fireballDisplay = Label("Fireball: ", 255, 230, fill = 'orange')
fireballSizeDisplay = Label("Size: " + str(Fireball.size), 255, 240, fill = 'orange')
fireballLifeDisplay = Label("Life: " + str(Fireball.life), 255, 250, fill = 'orange')
fireballSpeedDisplay = Label("Speed: " + str(Fireball.speed), 255, 260, fill = 'orange')
fireballMPCostDisplay = Label("MPCost: " + str(Fireball.cost), 255, 270, fill = 'orange')
fireballDamageDisplay = Label("Damage: " + str(Fireball.damage), 255, 280, fill = 'orange')
weaponDisplay = Label("Weapon: ", 255, 300, fill = 'red')
currentWeapon = Label(character.weapon, 255, 310, fill = 'silver')
displayGroup = Group(
    statBox, shieldDisplay, shieldTimeDisplay, 
    shieldHealthDisplay, shieldCooldownDisplay, shieldRadiusDisplay, 
    shieldDamageDisplay, swordDisplay, swordRangeDisplay, 
    swordDamageDisplay, weaponDisplay, currentWeapon, 
    characterStatBox, characterDisplay, characterMaxHealthDisplay, 
    characterHealthDisplay, scoreDisplay, keyDisplay, 
    levelDisplay, deathDisplay, characterMaxMPDisplay, 
    characterMPDisplay, characterMPRegenSpeedDisplay, characterMPRegenTimeDisplay, 
    characterMPRegenAmountDisplay, fireballDisplay, fireballSizeDisplay, 
    fireballLifeDisplay, fireballSpeedDisplay, fireballMPCostDisplay, 
    fireballDamageDisplay, characterHPRegenSpeedDisplay, characterHPRegenTimeDisplay, 
    characterHPRegenAmountDisplay, shieldPushDisplay, characterInvincibilityTimeDisplay, 
    characterMaxJumpDisplay
)
displayGroup.visible = False
# Status Bar
hpRegenBar = Line(20, 410, 140, 410, fill = 'lightcyan', lineWidth = 8)
hpBar = Line(20, 410, 140, 410, fill = 'aqua', lineWidth = 12)
mpRegenBar = Line(260, 410, 380, 410, fill = 'lightcoral', lineWidth = 8)
mpBar = Line(260, 410, 380, 410, fill = 'crimson', lineWidth = 12)
weaponStatus = Label("Sword", 200, 424, size = 12, border = 'black', borderWidth = 0.15)
statusBars = Group(
    Line(0, 420, 400, 420, fill = 'silver', lineWidth = 40),
    Label("HP", 8.75, 410, fill = 'blue', size = 9),
    Label("MP", 391.25, 410, fill = 'firebrick', size = 9),
    Line(257.5, 410, 382.5, 410, fill = 'darkred', lineWidth = 16),
    Line(17.5, 410, 142.5, 410, fill = 'navy', lineWidth = 16),
    hpRegenBar, 
    hpBar, 
    mpRegenBar, 
    mpBar, 
    weaponStatus
)
Key.keyLabel.toFront()
Coin.score.toFront()
roomLevelChange()
mousePosLabel = Label("0, 0", 50, 425)

def onStep(): 
    Coin.score.value = "Score: " + str(app.score)
    Coin.score.left = 147.5
    Key.keyLabel.right = 252.5
    if not app.game_paused:
        sword.use()
        shield.cooldown()
        character.mpRegen()
        character.hpRegen()
        weaponStatus.value = character.weapon
        if character.weapon == "Sword": 
            weaponStatus.fill = 'silver'
        elif character.weapon == "Shield": 
            weaponStatus.fill = 'cyan'
        elif character.weapon == "Fireball": 
            weaponStatus.fill = 'orange'
        if character.invTime > 0: 
            invFrames(character)
        if character.hp <= 0 or (character.shape.hitsShape(border)): 
            character.respawn()
        if character.jump <= character.maxJump: 
            character.moveUp()
        else: 
            character.gravity()
        character.bounce()
        if hitCheck(coinGroupList, character.shape): 
            for i in currentGroup(Coin.coinList): 
                i.getCoin()
        for i in Fireball.fireballList: 
            i.travel()
        levelList[app.level - 1].run()
        hpBar.x2 = 20 + (character.hp * (120 / character.maxHP))
        mpBar.x2 = 260 + (character.mp * (120 / character.maxMP))
        hpRegenBar.x2 = 140 - (character.hpRegenTime * (120 / character.hpRegenSpeed))
        mpRegenBar.x2 = 380 - (character.mpRegenTime * (120 / character.mpRegenSpeed))

def onKeyPress(key): 
    if not app.game_paused:
        if key == 'up': 
            character.jumpSet()
        elif key == 'space': 
            if character.weapon == "Sword": 
                sword.swing()
            elif character.weapon == "Fireball": 
                fireball.cast()
        elif key == 'tab': 
            if character.weapon == "Sword": 
                character.weapon = "Shield"
                sword.time = 0
                sword.goOut = True
                sword.shape.visible = False
            elif character.weapon == "Shield": 
                character.weapon = "Fireball"
            elif character.weapon == "Fireball": 
                character.weapon = "Sword"
    if key == 'r': 
        character.respawn()
    elif key == 'R': 
        character.levelReset()
    elif key == 'L': 
        app.level = int(app.getTextInput("Set level:  "))
        app.room = 'A'
        roomLevelChange()
        if app.level < 7: 
            character.shape.width = 10
            character.shape.height = 20
            goal.lineWidth = 20
            goal.x2 = goal.x1 + 20
        else: 
            character.shape.width = 5
            character.shape.height = 10
            goal.lineWidth = 10
            goal.x2 = goal.x1 + 10
        goal.centerX = goalPosList[app.level - 1][0]
        goal.centerY = goalPosList[app.level - 1][1]
        character.shape.centerX = characterSpawnList[app.level - 1][0]
        character.shape.centerY = characterSpawnList[app.level - 1][1]
    elif key == 's': 
        sword.damageUp(int(app.getTextInput("Increase Sword Damage By: ")))
    elif key == 'S': 
        sword.widthUp(int(app.getTextInput("Increase Sword Length By: ")))
    elif key == 'f': 
        fireball.lifeUp(int(app.getTextInput("Increase Fireball Life By: ")))
    elif key == 'F': 
        fireball.sizeUp(int(app.getTextInput("Increase Fireball Size By: ")))
    elif key == 'w': 
        shield.healthUp(int(app.getTextInput("Increase Shield Health By: ")))
    elif key == 'W': 
        shield.sizeUp(int(app.getTextInput("Increase Shield Size By: ")))
    elif key == 'H': 
        character.maxHPUp(int(app.getTextInput("Increase character Max Health By: ")))
    elif key == 'h': 
        character.hpRestore(int(app.getTextInput("Restore character Health By: ")))
    elif key == 'M': 
        character.maxMPUp(int(app.getTextInput("Increase character Max MP By: ")))
    elif key == 'm': 
        character.mpRestore(int(app.getTextInput("Restore character MP By: ")))
    elif key == 't': 
        character.hpRegenTimeDown(int(app.getTextInput("Increase character HP Regen Speed By: ")))
    elif key == 'T': 
        character.mpRegenTimeDown(int(app.getTextInput("Increase character MP Regen Speed By: ")))
    elif key == 'a': 
        character.hpRegenAmountUp(int(app.getTextInput("Increase character HP Regen Amount By: ")))
    elif key == 'A': 
        character.mpRegenAmountUp(int(app.getTextInput("Increase character MP Regen Amount By: ")))
    elif key == 'I': 
        character.invTimeUp(int(app.getTextInput("Increase character Invincibility Time By: ")))
    elif key == 'J': 
        character.maxJumpUp(int(app.getTextInput("Increase character Max Jump Height By: ")))
    elif key == 'd': 
        shield.damageUp(int(app.getTextInput("Increase Shield Damage By: ")))
    elif key == 'D': 
        fireball.damageUp(int(app.getTextInput("Increase Fireball Damage By: ")))
    elif key == 'C': 
        shield.timeUp(int(app.getTextInput("Increase Shield Time By: ")))
    elif key == 'c': 
        shield.cooldownDown(int(app.getTextInput("Decrease Shield Cooldown Time By: ")))
    elif key == 'q': 
        fireball.costDown(int(app.getTextInput("Decrease Fireball Cost By: ")))
    elif key == 'B': 
        fireball.damageUp(int(app.getTextInput("Increase Fireball Damage By: ")))
    elif key == 'b': 
        fireball.speedUp(int(app.getTextInput("Increase Fireball Speed By: ")))
    elif key == 'Q': 
        fireball.lightUp(int(app.getTextInput("Increase Fireball Light By: ")))

def onKeyHold(keys): 
    if not app.game_paused:
        if 'left' in keys: 
            character.moveLeft()
        if 'right' in keys: 
            character.moveRight()
        if 'down' in keys: 
            character.jump = character.maxJump + 1
            character.gravity()
        if 'space' in keys: 
            if character.weapon == "Shield": 
                shield.use()
            else: 
                shield.shape.visible = False
    if '1' in keys and '5' in keys: 
        cheatDisplayGroup.visible = True
    if 'i' in keys: 
        displayGroup.visible = True
        app.game_paused = True
        shieldTimeDisplay.value = "TimeLeft: " + str(shield.time) + "   MaxTime: " + str(shield.maxTime)
        shieldHealthDisplay.value = "CurrentHealth: " + str(shield.health) + "   MaxHealth: " + str(shield.maxHealth)
        shieldCooldownDisplay.value = "CooldownLeft: " + str(shield.cooldownTime) + "   MaxCooldown: " + str(shield.maxCooldown)
        shieldRadiusDisplay.value = "Size: " + str(shield.shape.radius)
        shieldDamageDisplay.value = "Damage: " + str(shield.damage)
        swordRangeDisplay.value = "Range: " + str(sword.shape.width)
        swordDamageDisplay.value = "Damage: " + str(sword.damage)
        currentWeapon.value = character.weapon
        characterMaxHealthDisplay.value = "MaxHP: " + str(character.maxHP)
        characterHealthDisplay.value = "CurrentHP: " + str(character.hp)
        characterInvincibilityTimeDisplay.value = "InvTime: " + str(character.maxInv)
        characterMaxJumpDisplay.value = "MaxJump: " + str(character.maxJump)
        scoreDisplay.value = "Score: " + str(app.score)
        keyDisplay.value = "Keys: " + str(app.keys)
        levelDisplay.value = "Level: " + str(app.level)
        deathDisplay.value = "Deaths: " + str(character.deaths)
        fireballSizeDisplay.value = "Size: " + str(Fireball.size)
        fireballLifeDisplay.value = "Life: " + str(Fireball.life)
        fireballSpeedDisplay.value = "Speed: " + str(Fireball.speed)
        fireballMPCostDisplay.value = "MPCost: " + str(Fireball.cost)
        fireballDamageDisplay.value = "Damage: " + str(Fireball.damage)
        characterMaxMPDisplay.value = "MaxMP: " + str(character.maxMP)
        characterMPDisplay.value = "CurrentMP: " + str(character.mp)
        characterMPRegenSpeedDisplay.value = "MPRegenSpeed:" + str(character.mpRegenSpeed)
        characterMPRegenTimeDisplay.value = "MPRegenTime:" + str(character.mpRegenTime)
        characterMPRegenAmountDisplay.value = "MPRegenAmount:" + str(character.mpRegenAmount)
        characterHPRegenSpeedDisplay.value = "HPRegenSpeed:" + str(character.hpRegenSpeed)
        characterHPRegenTimeDisplay.value = "HPRegenTime:" + str(character.hpRegenTime)
        characterHPRegenAmountDisplay.value = "HPRegenAmount:" + str(character.hpRegenAmount)
        if character.weapon == "Sword": 
            currentWeapon.fill = 'silver'
        elif character.weapon == "Shield": 
            currentWeapon.fill = 'cyan'
        elif character.weapon == "Fireball": 
            currentWeapon.fill = 'orange'

def onKeyRelease(key): 
    if not app.game_paused:
        if key == 'space': 
            if character.weapon == "Shield": 
                shield.shape.visible = False
    if key == 'i': 
        displayGroup.visible = False
        app.game_paused = False
    elif key == '1' or key == '5': 
        cheatDisplayGroup.visible = False

def onMousePress(mouseX, mouseY): 
    if not app.game_paused:
        if app.level <= 6: 
            character.shape.centerX = rounded(mouseX / 5) * 5
            character.shape.centerY = rounded(mouseY / 5) * 5
        else: 
            character.shape.centerX = rounded(mouseX / 2.5) * 2.5
            character.shape.centerY = rounded(mouseY / 2.5) * 2.5
        mousePosLabel.value = str(mouseX) + ", " + str(mouseY)

cmu_graphics.run()