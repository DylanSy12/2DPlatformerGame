from cmu_graphics import *
from Character import *
from Portal import *
from EnemyT import *
from EnemyX import *
from EnemyY import *
from MovingPlatform import *
from Lava import *
from Saw import *
from Spike import *
from InstantDeathZone import *
from TrackMissile import *
from Missile import *
from LineCannon import *
from Trigger import *
from Coin import *
from BreakWall import *
from Checkpoint import *
from HealZone import *
from Key import *
from UpgradeItems import *
from HiddenArea import *
from JumpPad import *
from KeyDoor import *
from LinkedWall import *
from Switch import *
from WindZone import *
from ResetButton import *
from Slope import *
from Crumble import *
from RoomSwitcher import *
from LevelLists import *
from Levels import *
def invFrames(s):
    s.invTime -= 1
    if s.invTime % 2 == 0 and s.invTime != 0:
        s.shape.opacity = 50
    else:
        s.shape.opacity = 100
def spikePlace(amount, startX, startY, disX, disY, damage, level, room, group):
    i = 0
    while i < amount:
        Spike(startX + (disX * i), startY + (disY * i), damage, level, room, group)
        i += 1
def goalCheck():
    if goal.hitsShape(character.shape):
        if app.level == 6:
            character.shape.width = 5
            character.shape.height = 10
            goal.lineWidth = 10
            goal.x1 += 10
        goal.centerX = goalPosList[app.level][0]
        goal.centerY = goalPosList[app.level][1]
        character.spawnSet(characterSpawnList[app.level][0], characterSpawnList[app.level][1])
        roomLevelChange()
def level1():
    goalCheck()
def level2():
    goalCheck()
def level3():
    if currentGroup(lavaGroupList).hitsShape(character.shape):
        for i in currentGroup(Lava.lavaList):
            i.lavaCheck()
    goalCheck()
def level4():
    goalCheck()
def level5():
    if currentGroup(lavaGroupList).hitsShape(character.shape):
        for i in currentGroup(Lava.lavaList):
            i.lavaCheck()
    goalCheck()
def level6():
    for i in currentGroup(JumpPad.jumpPadList):
        i.bounce()
    for i in currentGroup(MovingPlatform.movePlatList):
        i.move()
    for i in currentGroup(Portal.portalList):
        i.teleport()
    goalCheck()
def level7():
    if currentGroup(lavaGroupList).hitsShape(character.shape):
        for i in currentGroup(Lava.lavaList):
            i.lavaCheck()
    for i in currentGroup(JumpPad.jumpPadList):
        i.bounce()
    for i in currentGroup(MovingPlatform.movePlatList):
        i.move()
    for i in currentGroup(Portal.portalList):
        i.teleport()
    for i in currentGroup(HiddenArea.hiddenAreaList):
        i.reveal()
    for i in currentGroup(EnemyX.enemyXList):
        i.move()
        if i.health > 0 and i.invTime > 0:
            invFrames(i)
    groupShapes(platform7A001.shape, jump7A001.shape, -3, 0)
    goalCheck()
def level8():
    if currentGroup(lavaGroupList).hitsShape(character.shape):
        for i in currentGroup(Lava.lavaList):
            i.lavaCheck()
    if character.shape.centerX <= 130 or character.shape.centerY <= 50:
        if currentGroup(jumpGroupList).hitsShape(character.shape):
            for i in currentGroup(JumpPad.jumpPadList):
                i.bounce()
    for i in currentGroup(Portal.portalList):
        i.teleport()
    for i in currentGroup(HiddenArea.hiddenAreaList):
        i.reveal()
    for i in currentGroup(EnemyX.enemyXList):
        i.move()
        if i.health > 0 and i.invTime > 0:
            invFrames(i)
    if 115 <= character.shape.centerX:
        for i in currentGroup(WindZone.windZoneList):
            i.push()
    goalCheck()
def level9():
    for i in currentGroup(Portal.portalList):
        i.teleport()
    for i in currentGroup(HiddenArea.hiddenAreaList):
        i.reveal()
    for i in currentGroup(Checkpoint.checkpointList):
        i.setSpawn()
    for i in currentGroup(TrackMissile.trackMissileList):
        i.shoot()
        if i.health > 0 and i.invTime > 0:
            i.invFrames()
    for i in currentGroup(BreakWall.breakWallList):
        i.wallBreak()
    for i in currentGroup(Item.itemList):
        i.obtain()
    for i in currentGroup(KeyDoor.keyDoorList):
        i.openDoor()
    for i in currentGroup(Switch.switchList):
        if i.shape.hitsShape(character.shape):
            i.switch()
        else:
            i.switched = False
    goalCheck()
def level10():
    print("New Step")
    for i in currentGroup(Portal.portalList):
        i.teleport()
    for i in currentGroup(HiddenArea.hiddenAreaList):
        i.reveal()
    if character.shape.centerX <= 160 and 315 <= character.shape.centerY:
        for i in currentGroup(EnemyY.enemyYList):
            i.move()
            if i.health > 0 and i.invTime > 0:
                invFrames(i)
    elif character.shape.centerX <= 245 and 230 <= character.shape.centerY <= 305:
        for i in currentGroup(EnemyX.enemyXList):
            if 230 <= i.shape.centerY <= 305:
                i.move()
                if i.health > 0 and i.invTime > 0:
                    invFrames(i)
    elif 160 <= character.shape.centerX and 315 <= character.shape.centerY:
        a = 1
        for i in currentGroup(EnemyT.enemyTList):
            if 315 <= i.shape.centerY:
                print("New Enemy" + str(a))
                a += 1
                i.move()
                if i.health > 0 and i.invTime > 0:
                    invFrames(i)
    elif 110 <= character.shape.centerY <= 220:
        for i in currentGroup(BreakWall.breakWallList):
            i.wallBreak()
        for i in currentGroup(EnemyT.enemyTList):
            if 110 <= i.shape.centerY <= 220:
                i.move()
                if i.health > 0 and i.invTime > 0:
                    invFrames(i)
        for i in currentGroup(EnemyX.enemyXList):
            if 110 <= i.shape.centerY <= 220:
                i.move()
                if i.health > 0 and i.invTime > 0:
                    invFrames(i)
        if boss10A001.health > 0:
            groupShapes(boss10A001.shape,boss10A001Cannon.shape, -20, 0)
        else:
            boss10A001Cannon.health = 0
            groupShapes(boss10A001.shape, bossPortal.portal2, 0, 0)
            groupShapes(boss10A001.shape, bossPortal.portalClose2, 0, 0)
        for i in currentGroup(TrackMissile.trackMissileList):
            i.shoot()
            if i.health > 0 and i.invTime > 0:
                i.invFrames()
    elif character.shape.centerY <= 60:
        for i in currentGroup(KeyDoor.keyDoorList):
            i.openDoor()
        if character.shape.centerX <= 160:
            for i in currentGroup(Saw.sawList):
                i.rotate()
        elif 170 <= character.shape.centerX:
            for i in currentGroup(Spike.spikeList):
                i.damageCheck()
    for i in currentGroup(Checkpoint.checkpointList):
        i.setSpawn()
    for i in currentGroup(Item.itemList):
        i.obtain()
    for i in currentGroup(HealZone.healZoneList):
        i.heal()
    for i in currentGroup(Trigger.triggerList):
        i.trigger()
    for i in currentGroup(LinkedWall.wallList):
        i.linkCheck()
    for i in currentGroup(ResetButton.buttonList):
        i.push()
    goalCheck()
def level11():
    for i in currentGroup(Item.itemList):
        i.obtain()
    if currentGroup(lavaGroupList).hitsShape(character.shape):
        for i in currentGroup(Lava.lavaList):
            i.lavaCheck()
    for i in currentGroup(HiddenArea.hiddenAreaList):
        i.reveal()
    for i in currentGroup(EnemyX.enemyXList):
        i.move()
        if i.health > 0 and i.invTime > 0:
            invFrames(i)
    if app.room != "A":
        goal.visible = False
        if app.room == "C":
            for i in currentGroup(EnemyY.enemyYList):
                i.move()
                if i.health > 0 and i.invTime > 0:
                    invFrames(i)
            for i in currentGroup(Portal.portalList):
                i.teleport()
            for i in currentGroup(Slope.slopeList):
                i.slope()
        elif app.room == "B":
            for i in currentGroup(LineCannon.lineCannonList):
                i.shoot()
                if i.health > 0 and i.invTime > 0:
                    i.invFrames()
            for i in Missile.missileList:
                i.shoot()
            for i in currentGroup(Spike.spikeList):
                i.damageCheck()
        for i in currentGroup(BreakWall.breakWallList):
            i.wallBreak()
    else:
        goal.visible = True
        if boss11A.health > 0:
            tCannon11A001.shape.centerX = boss11A.shape.left
            tCannon11A002.shape.centerX = boss11A.shape.left
            tCannon11A003.shape.centerX = boss11A.shape.right
            tCannon11A004.shape.centerX = boss11A.shape.right
            tCannon11A001.shape.centerY = boss11A.shape.top
            tCannon11A002.shape.centerY = boss11A.shape.bottom
            tCannon11A003.shape.centerY = boss11A.shape.top
            tCannon11A004.shape.centerY = boss11A.shape.bottom
        for i in currentGroup(MovingPlatform.movePlatList):
            i.move()
        for i in currentGroup(Trigger.triggerList):
            i.trigger()
        if 150 < character.shape.centerX < 320 and character.shape.centerY > 250:
            for i in currentGroup(HealZone.healZoneList):
                i.heal()
    for i in currentGroup(LinkedWall.wallList):
        i.linkCheck()
    for i in currentGroup(Crumble.crumbleList):
        i.crumble()
    for i in currentGroup(TrackMissile.trackMissileList):
        i.shoot()
        if i.health > 0 and i.invTime > 0:
            i.invFrames()
    for i in currentGroup(Saw.sawList):
        i.rotate()
    for i in currentGroup(Checkpoint.checkpointList):
        i.setSpawn()
    for i in currentGroup(WindZone.windZoneList):
        i.push()
    for i in currentGroup(Track.trackList):
        i.move()
    for i in currentGroup(RoomSwitcher.switcherList):
        i.switch()
def level12():
    groupShapes(character.shape, character.light, 0, 0)
    if app.room == "A":
        for i in currentGroup(EnemyX.enemyXList):
            i.move()
            if i.health > 0 and i.invTime > 0:
                invFrames(i)
        currentGroup(Spike.spikeList).damageCheck()
    else:
        for i in currentGroup(LinkedWall.wallList):
            i.linkCheck()
    for i in currentGroup(WindZone.windZoneList):
        i.push()
    for i in currentGroup(Checkpoint.checkpointList):
        i.setSpawn()
    for i in currentGroup(RoomSwitcher.switcherList):
        i.switch()
    for i in currentGroup(Item.itemList):
        i.obtain()
    for i in currentGroup(Crumble.crumbleList):
        i.crumble()
    for i in currentGroup(BreakWall.breakWallList):
        i.wallBreak()
    for i in currentGroup(Slope.slopeList):
        i.slope()
    for i in currentGroup(EnemyY.enemyYList):
        i.move()
        if i.health > 0 and i.invTime > 0:
            invFrames(i)
    if currentGroup(lavaGroupList).hitsShape(character.shape):
        for i in currentGroup(Lava.lavaList):
            i.lavaCheck()
    for i in currentGroup(HiddenArea.hiddenAreaList):
        i.reveal()
goal = Line(360, 380, 380, 380, lineWidth = 20, fill = gradient('silver', 'gold', 'gold'))