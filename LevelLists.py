from cmu_graphics import *
#Level 1
waterGroup1A = Group()
obstacleGroup1A = Group(Line(135, 375, 265, 375, lineWidth = 100))
groundGroup1A = Group(
    Line(0, 400, 400, 400, lineWidth = 20), Line(135, 325, 265, 325)
)
breakWallGroup1A = Group()
keyDoorGroup1A = Group()
windGroup1A = Group()
coinGroup1A = Group()
enemyGroup1A = Group()
level1AGroupList = [
    waterGroup1A, obstacleGroup1A, groundGroup1A, 
    coinGroup1A, breakWallGroup1A, keyDoorGroup1A, 
    windGroup1A, enemyGroup1A
]
level1GroupListDict = {"C": [], "B": [], "A": level1AGroupList}
#Level 2
obstacleGroup2A = Group(
    Line(290, 265, 360, 265, lineWidth = 10), Line(160, 210, 240, 210, lineWidth = 10), 
    Line(160, 245, 170, 245, lineWidth = 80), Line(0, 280, 170, 280, lineWidth = 10), 
    Line(25, 135, 55, 135, lineWidth = 10), Line(25, 55, 55, 55, lineWidth = 10), 
    Line(135, 375, 265, 375, lineWidth = 100)
)
groundGroup2A = Group(
    Line(160, 245, 170, 245, lineWidth = 80), Line(115, 240, 170, 240, lineWidth = 10, opacity = 85), 
    Line(0, 400, 400, 400, lineWidth = 20)
)
coinGroup2A = Group()
level2AGroupList = [
    obstacleGroup2A, groundGroup2A, coinGroup2A, 
    breakWallGroup1A, keyDoorGroup1A, windGroup1A, 
    enemyGroup1A
]
level2GroupListDict = {"C": [], "B": [], "A": level2AGroupList}
#Level 3
obstacleGroup3A = Group(
    Line(290, 265, 360, 265, lineWidth = 10), Line(160, 210, 240, 210, lineWidth = 10), 
    Line(160, 245, 170, 245, lineWidth = 80), Line(0, 280, 170, 280, lineWidth = 10), 
    Line(25, 135, 55, 135, lineWidth = 10), Line(25, 55, 55, 55, lineWidth = 10), 
    Line(135, 375, 265, 375, lineWidth = 100)
)
groundGroup3A = Group(
    Line(160, 245, 170, 245, lineWidth = 80), Line(115, 240, 170, 240, lineWidth = 10, opacity = 85), 
    Line(0, 400, 400, 400, lineWidth = 20)
)
lavaGroup3A = Group()
coinGroup3A = Group()
level3AGroupList = [
    obstacleGroup3A, groundGroup3A, coinGroup3A, 
    lavaGroup3A, breakWallGroup1A, keyDoorGroup1A, 
    windGroup1A, enemyGroup1A
]
level3GroupListDict = {"C": [], "B": [], "A": level3AGroupList}
#Level 4
obstacleGroup4A = Group(
    Line(100, 390, 100, 200, lineWidth = 40), Line(0, -200, 0, 330, lineWidth = 40), 
    Line(100, -200, 100, 150, lineWidth = 40), Line(0, -200, 400, -200, lineWidth = 300), 
    Line(200, 390, 200, 125, lineWidth = 40), Line(200, -200, 200, 65, lineWidth = 40), 
    Line(220, 240, 330, 240, lineWidth = 20), Line(270, -200, 270, 160, lineWidth = 20), 
    Line(340, 250, 340, 50, lineWidth = 20), Line(400, 320, 260, 320, lineWidth = 20), 
    Line(400, 310, 400, -200, lineWidth = 20)
)
groundGroup4A = Group(Line(0, 400, 400, 400, lineWidth = 20))
coinGroup4A = Group()
level4AGroupList = [
    obstacleGroup4A, groundGroup4A, coinGroup4A, 
    breakWallGroup1A, keyDoorGroup1A, windGroup1A, 
    enemyGroup1A
]
level4GroupListDict = {"C": [], "B": [], "A": level4AGroupList}
#Level 5
obstacleGroup5A = Group(
    Line(100, 390, 100, 200, lineWidth = 40), Line(0, -200, 0, 330, lineWidth = 40), 
    Line(100, -200, 100, 150, lineWidth = 40), Line(0, -200, 400, -200, lineWidth = 300), 
    Line(200, 390, 200, 125, lineWidth = 40), Line(200, -200, 200, 65, lineWidth = 40), 
    Line(220, 240, 330, 240, lineWidth = 20), Line(270, -200, 270, 160, lineWidth = 20), 
    Line(340, 250, 340, 50, lineWidth = 20), Line(400, 320, 260, 320, lineWidth = 20), 
    Line(400, 310, 400, -200, lineWidth = 20)
)
groundGroup5A = Group(Line(0, 400, 400, 400, lineWidth = 20))
lavaGroup5A = Group()
coinGroup5A = Group()
level5AGroupList = [
    obstacleGroup5A, groundGroup5A, coinGroup5A, 
    lavaGroup5A, breakWallGroup1A, keyDoorGroup1A, 
    windGroup1A, enemyGroup1A
]
level5GroupListDict = {"C": [], "B": [], "A": level5AGroupList}
#Level 6
groundGroup6A = Group(
    Line(330, 370, 400, 370, lineWidth = 60), Line(0, 370, 70, 370, lineWidth = 60)
)
obstacleGroup6A = Group(
    Line(320, 370, 400, 370, lineWidth = 60), Line(0, 370, 80, 370, lineWidth = 60), 
    Line(200, -200, 200, 400, lineWidth = 20), Line(0, -200, 400, -200, lineWidth = 400)
)
portalGroup6A = Group()
jumpGroup6A = Group()
coinGroup6A = Group()
level6AGroupList = [
    obstacleGroup6A, groundGroup6A, coinGroup6A, 
    jumpGroup6A, portalGroup6A, breakWallGroup1A, 
    keyDoorGroup1A, windGroup1A, enemyGroup1A
]
level6GroupListDict = {"C": [], "B": [], "A": level6AGroupList}
#Level 7
groundGroup7A = Group(Line(0, 410, 400, 410, lineWidth = 30))
obstacleGroup7A = Group(
    Line(40, 400, 40, 335, lineWidth = 10), Line(0, 360, 0, 315, lineWidth = 10), 
    Line(0, 157.5, 80, 157.5, lineWidth = 315), Line(75, 365, 75, 315, lineWidth = 10), 
    Line(80, 360, 160, 360, lineWidth = 10), Line(125, 355, 125, 400, lineWidth = 10), 
    Line(205, 140, 205, 400, lineWidth = 10), Line(155, 365, 155, 140, lineWidth = 10), 
    Line(80, 222.5, 150, 222.5, lineWidth = 165), Line(85, 140, 85, 90, lineWidth = 10), 
    Line(80, 45, 210, 45, lineWidth = 90)
)
portalGroup7A = Group()
jumpGroup7A = Group()
lavaGroup7A = Group()
enemyGroup7A = Group()
coinGroup7A = Group()
hiddenGroup7A = Group()
level7AGroupList = [
    groundGroup7A, obstacleGroup7A, portalGroup7A, 
    jumpGroup7A, lavaGroup7A, coinGroup7A, 
    hiddenGroup7A, enemyGroup7A, breakWallGroup1A, 
    keyDoorGroup1A, windGroup1A
]
level7GroupListDict = {"C": [], "B": [], "A": level7AGroupList}
#Level 8
windGroup8A = Group()
portalGroup8A = Group()
obstacleGroup8A = Group(
    Line(0, 350, 0, 400, lineWidth = 10), Line(50, 350, 50, 400, lineWidth = 10), 
    Line(0, 350, 20, 350, lineWidth = 10), Line(30, 350, 50, 350, lineWidth = 10), 
    Line(15, 325, 15, 355, lineWidth = 10), Line(35, 325, 35, 355, lineWidth = 10), 
    Line(0, 325, 20, 325, lineWidth = 10), Line(30, 325, 50, 325, lineWidth = 10), 
    Line(0, 275, 0, 325, lineWidth = 10), Line(50, 275, 50, 325, lineWidth = 10), 
    Line(0, 270, 55, 270, lineWidth = 10), Line(0, 225, 0, 260, lineWidth = 10), 
    Line(50, 225, 50, 260, lineWidth = 10), Line(0, 225, 20, 225, lineWidth = 10), 
    Line(35, 195, 35, 220, lineWidth = 10), Line(15, 195, 15, 220, lineWidth = 10), 
    Line(0, 150, 0, 290, lineWidth = 10), Line(50, 190, 50, 200, lineWidth = 10), 
    Line(50, 150, 50, 175, lineWidth = 10), Line(0, 147.5, 30, 147.5, lineWidth = 15), 
    Line(40, 147.5, 50, 147.5, lineWidth = 15), Line(50, 100, 50, 145, lineWidth = 10), 
    Line(0, 100, 0, 145, lineWidth = 10), Line(0, 100, 50, 100, lineWidth = 10), 
    Line(30, 225, 50, 225, lineWidth = 10), Line(60, 190, 60, 230, lineWidth = 10), 
    Line(60, 140, 60, 175, lineWidth = 10), Line(60, 137.5, 85, 137.5, lineWidth = 15), 
    Line(120, 140, 120, 230, lineWidth = 10), Line(95, 137.5, 120, 137.5, lineWidth = 15), 
    Line(60, 100, 60, 135, lineWidth = 10), Line(120, 100, 120, 135, lineWidth = 10), 
    Line(60, 100, 120, 100, lineWidth = 10), Line(60, 232.5, 120, 232.5, lineWidth = 15), 
    Line(60, 235, 60, 325, lineWidth = 10), Line(120, 320, 120, 325, lineWidth = 10), 
    Line(120, 235, 120, 310, lineWidth = 10), Line(125, 235, 125, 310, lineWidth = 10), 
    Line(185, 235, 185, 325, lineWidth = 10), Line(127.5, 95, 127.5, 235, lineWidth = 5), 
    Line(280, 225, 300, 225, lineWidth = 10), Line(190, 240, 260, 240, lineWidth = 10), 
    Line(320, 210, 340, 210, lineWidth = 10), Line(190, 175, 270, 175, lineWidth = 10), 
    Line(200, 135, 220, 135, lineWidth = 10), Line(132.5, 50, 132.5, 100, lineWidth = 15), 
    Line(90, 330, 90, 385, lineWidth = 10), Line(155, 330, 155, 385, lineWidth = 10), 
    Line(220, 245, 220, 385, lineWidth = 10), Rect(190, 245, 25, 140), 
    Rect(160, 330, 30, 55), Rect(95, 330, 55, 55), 
    Rect(55, 325, 30, 30), Rect(225, 245, 35, 140), 
    Line(220, 95, 240, 95, lineWidth = 10), Line(200, 55, 220, 55, lineWidth = 10)
)
groundGroup8A = Group(
    Line(0, 450, 400, 450, lineWidth = 110), Line(20, 322.5, 30, 322.5, lineWidth = 5, opacity = 85), 
    Line(0, 270, 55, 270, lineWidth = 10), Line(0, 265, 50, 265, lineWidth = 10), 
    Line(20, 197.5, 30, 197.5, lineWidth = 5, opacity = 85), Line(0, 200, 20, 200, lineWidth = 10), 
    Line(30, 200, 50, 200, lineWidth = 10), Line(0, 152.5, 30, 152.5, lineWidth = 5), 
    Line(0, 142.5, 50, 142.5, lineWidth = 5), Line(90, 320, 90, 330, lineWidth = 60), 
    Line(115, 320, 115, 325, lineWidth = 30), Line(155, 320, 155, 330, lineWidth = 60), 
    Line(90, 95, 90, 105, lineWidth = 60), Line(60, 100, 120, 100, lineWidth = 10), 
    Line(40, 152.5, 50, 152.5, lineWidth = 5), Line(85, 132.5, 95, 132.5, lineWidth = 5), 
    Line(0, 225, 50, 225, lineWidth = 10)
)
coinGroup8A = Group()
jumpGroup8A = Group()
lavaGroup8A = Group()
enemyGroup8A = Group()
hiddenGroup8A = Group()
level8AGroupList = [
    coinGroup8A, groundGroup8A, obstacleGroup8A, 
    hiddenGroup8A, portalGroup8A, lavaGroup8A, 
    jumpGroup8A, windGroup8A, breakWallGroup1A, 
    keyDoorGroup1A, enemyGroup8A
]
level8GroupListDict = {"C": [], "B": [], "A": level8AGroupList}
#Level 9
portalGroup9A = Group()
obstacle9A001 = Line(205, 325, 205, 390, lineWidth = 10, fill = 'deepPink', opacity = 90)
obstacle9A002 = Line(307.5, 355, 307.5, 325, lineWidth = 5, fill = 'deepPink', opacity = 90)
obstacle9A003 = Line(297.5, 355, 297.5, 325, lineWidth = 5, fill = 'deepPink', opacity = 90)
obstacle9A004 = Line(85, 287.5, 105, 287.5, lineWidth = 15, fill = 'deepPink', opacity = 75)
obstacle9A005 = Line(177.5, 295, 177.5, 230, lineWidth = 5, fill = 'deepPink', opacity = 90)
obstacle9A006 = Line(147.5, 295, 147.5, 230, lineWidth = 5, fill = 'deepPink', opacity = 90)
obstacle9A007 = Line(197.5, 295, 197.5, 230, lineWidth = 5, fill = 'deepPink', opacity = 90)
obstacle9A008 = Line(205, 305, 205, 315, lineWidth = 10, fill = 'deepPink', opacity = 90)
obstacle9A009 = Line(125, 325, 125, 335, lineWidth = 10, fill = 'deepPink', opacity = 90)
obstacleGroup9A = Group(
    Line(135, 320, 135, 350, lineWidth = 10), Line(400, 320, 0, 320, lineWidth = 10), 
    Line(175, 385, 185, 385, lineWidth = 10), Rect(240, 355, 70, 35), 
    Line(392.5, 375, 392.5, 325, lineWidth = 15), Line(80, 305, 200, 305, lineWidth = 20), 
    Line(0, 225, 300, 225, lineWidth = 10), Line(235, 290, 235, 230, lineWidth = 10), 
    Rect(0, 140, 150, 80), Rect(250, 140, 50, 80), 
    Line(250, 150, 150, 150, lineWidth = 20), Rect(320, 140, 80, 90), 
    Line(0, 400, 20, 400, lineWidth = 20), Line(30, 400, 400, 400, lineWidth = 20), 
    Line(0, 130, 400, 130, lineWidth = 20), obstacle9A001, 
    obstacle9A002, obstacle9A003, 
    obstacle9A004, obstacle9A005, 
    obstacle9A006, obstacle9A007, 
    obstacle9A008, obstacle9A009
)
ground9A001 = Line(20, 400, 30, 400, lineWidth = 20)
groundGroup9A = Group(ground9A001)
breakWallGroup9A = Group()
keyGroup9A = Group()
keyDoorGroup9A = Group()
cannonGroup9A = Group()
coinGroup9A = Group()
switchGroup9A = Group()
checkpointGroup9A = Group()
hiddenGroup9A = Group()
missileGroupShoot = Group()
level9AGroupList = [
    keyDoorGroup9A, checkpointGroup9A, keyGroup9A, 
    groundGroup9A, obstacleGroup9A, cannonGroup9A, 
    breakWallGroup9A, coinGroup9A, hiddenGroup9A, 
    portalGroup9A, switchGroup9A
]
level9GroupListDict = {"C": [], "B": [], "A": level9AGroupList}
#Level 10
healSpaceGroup10A = Group()
portalGroup10A = Group()
checkpointGroup10A = Group()
ground10A001 = Line(185, 362.5, 160, 362.5, lineWidth = 5, visible = False)
ground10A002 = Line(0, 205, 10, 205, lineWidth = 10, visible = False)
groundGroup10A = Group(
    Line(30, 390, 30, 365, lineWidth = 10), ground10A001, 
    ground10A002
)
obstacle10A001 = Line(275, 200, 275, 220, lineWidth = 10)
obstacle10A002 = Line(335, 200, 335, 220, lineWidth = 10)
obstacle10A003 = Line(15, 220, 15, 200, lineWidth = 10, visible = False)
obstacle10A004 = Line(260, 390, 260, 375, lineWidth = 10)
obstacle10A005 = Line(290, 390, 290, 375, lineWidth = 10)
obstacle10A006 = Line(275, 390, 275, 375, lineWidth = 10)
obstacle10A007 = Line(220, 390, 220, 375, lineWidth = 10)
obstacle10A008 = Line(205, 390, 205, 375, lineWidth = 10)
obstacleGroup10A = Group(
    Line(0, 500, 400, 500, lineWidth = 220), Line(30, 390, 30, 365, lineWidth = 10), 
    Line(0, 310, 400, 310, lineWidth = 10), Line(145, 315, 145, 365, lineWidth = 30), 
    Line(190, 390, 190, 360, lineWidth = 10), Line(250, 230, 250, 305, lineWidth = 10), 
    Line(345, 315, 345, 365, lineWidth = 40), Line(30, 305, 30, 280, lineWidth = 10), 
    Line(0, 225, 400, 225, lineWidth = 10), Line(382.5, 390, 382.5, 375, lineWidth = 5), 
    Line(180, 230, 180, 280, lineWidth = 30), Line(0, 85, 400, 85, lineWidth = 50), 
    Line(165, 0, 165, 40, lineWidth = 10), Line(0, -5, 400, -5, lineWidth = 10), 
    RegularPolygon(30, 60, 10, 4), RegularPolygon(60, 10, 10, 4), 
    RegularPolygon(90, 60, 10, 4), RegularPolygon(120, 10, 10, 4), 
    obstacle10A001, obstacle10A002, 
    obstacle10A003, obstacle10A004, 
    obstacle10A005, obstacle10A006, 
    obstacle10A007, obstacle10A008
)
keyDoorGroup10A = Group()
breakWallGroup10A = Group()
triggerGroup10A = Group()
enemyGroup10A = Group()
boss10A001Group = Group()
keyGroup10A = Group()
sawGroup10A = Group()
spikeGroup10A = Group()
coinGroup10A = Group()
itemGroup10A = Group()
hiddenGroup10A = Group()
level10AGroupList = [
    groundGroup10A, obstacleGroup10A, breakWallGroup10A, 
    sawGroup10A, spikeGroup10A, keyDoorGroup10A, 
    healSpaceGroup10A, checkpointGroup10A, hiddenGroup10A, 
    portalGroup10A, keyGroup10A, enemyGroup10A, 
    coinGroup10A, boss10A001Group, itemGroup10A, 
    triggerGroup10A
]
level10GroupListDict = {"C": [], "B": [], "A": level10AGroupList}
obstacle10A003.ground = False
obstacle10A003.obstacle = True
ground10A001.ground = True
ground10A001.obstacle = False
ground10A002.ground = True
ground10A002.obstacle = False
#Level 11
# Room A
exitGroup11A = Group()
triggered11A001 = Line(205, 380, 205, 390, lineWidth = 10, fill = 'purple')
triggered11A002 = Line(265, 380, 265, 390, lineWidth = 10, fill = 'purple')
obstacleGroup11A = Group(
    Line(0, 400, 400, 400, lineWidth = 20), Line(0, 130, 0, 350, lineWidth = 20), 
    Line(0, 85, 80, 85, lineWidth = 10), Line(70, 90, 70, 390, lineWidth = 20), 
    Line(0, 35, 250, 35, lineWidth = 10), Line(80, 130, 210, 130, lineWidth = 10), 
    Line(245, 40, 245, 250, lineWidth = 10), Line(85, 245, 240, 245, lineWidth = 10),
   Line(85, 210, 210, 210, lineWidth = 10), Line(195, 135, 195, 205, lineWidth = 10), 
    Line(90, 250, 90, 290, lineWidth = 10), Line(85, 285, 150, 285, lineWidth = 10), 
    Line(80, 305, 150, 305, lineWidth = 10), Line(145, 310, 145, 390, lineWidth = 10), 
    Line(325, 240, 325, 390, lineWidth = 10), Line(330, 245, 362.5, 245, lineWidth = 10), 
    Line(367.5, 245, 400, 245, lineWidth = 10), Line(370, 250, 370, 280, lineWidth = 5), 
    Line(360, 250, 360, 280, lineWidth = 5), Line(250, 220, 400, 220, lineWidth = 10), 
    triggered11A001, triggered11A002
)
groundGroup11A = Group(Line(330, 310, 400, 310, lineWidth = 10))
breakWallGroup11A = Group()
lavaGroup11A = Group()
sawGroup11A = Group()
trackGroup11A = Group()
windGroup11A = Group()
healSpaceGroup11A = Group()
checkpointGroup11A = Group()
enemyGroup11A = Group()
cannonGroup11A = Group()
itemGroup11A = Group()
coinGroup11A = Group()
hiddenGroup11A = Group()
level11AGroupList = [
    exitGroup11A, obstacleGroup11A, groundGroup11A, 
    lavaGroup11A, sawGroup11A, trackGroup11A, 
    windGroup11A, healSpaceGroup11A, checkpointGroup11A, 
    itemGroup11A, coinGroup11A, enemyGroup11A, 
    cannonGroup11A, hiddenGroup11A
]
# Room B
exitGroup11B = Group()
obstacleGroup11B = Group(
    Line(215, 85, 410, 85, lineWidth = 10), Line(315, 0, 315, 80, lineWidth = 10), Line(365, 35, 400, 35, lineWidth = 10), 
    Line(370, 0, 370, 30, lineWidth = 10), Line(350, 135, 400, 135, lineWidth = 10), Line(270, 0, 270, 55, lineWidth = 10), 
    Line(220, 0, 220, 55, lineWidth = 10), Line(355, 140, 355, 370, lineWidth = 10), Line(245, 295, 350, 295, lineWidth = 10), 
    Line(250, 90, 250, 200, lineWidth = 10), Line(250, 250, 250, 290, lineWidth = 10), Line(220, 290, 220, 325, lineWidth = 10), 
    Line(220, 350, 220, 400, lineWidth = 10), Line(225, 395, 400, 395, lineWidth = 10), Line(405, 130, 405, 400, lineWidth = 10), 
    Line(275, 0, 310, 0, lineWidth = 10), Line(405, 0, 405, 40, lineWidth = 10), Line(0, 50, 200, 50, lineWidth = 10), 
    Line(85, 0, 85, 45, lineWidth = 170))
groundGroup11B = Group(Line(225, 295, 245, 295, lineWidth = 10))
breakWallGroup11B = Group()
lavaGroup11B = Group()
windGroup11B = Group()
enemyGroup11B = Group()
sawGroup11B = Group()
trackGroup11B = Group()
spikeGroup11B = Group()
itemGroup11B = Group()
coinGroup11B = Group()
cannonGroup11B = Group()
checkpointGroup11B = Group()
hiddenGroup11B = Group()
level11BGroupList = [
    exitGroup11B, obstacleGroup11B, groundGroup11B, breakWallGroup11B, lavaGroup11B, windGroup11B, cannonGroup11B, 
    sawGroup11B, trackGroup11B, enemyGroup11B, spikeGroup11B, checkpointGroup11B, itemGroup11B, coinGroup11B, hiddenGroup11B]
# Room C
exitGroup11C = Group()
obstacleGroup11C = Group(
    Line(220, 370, 220, 400, lineWidth = 10), Line(270, 355, 270, 400, lineWidth = 10), 
    Line(315, 370, 315, 400, lineWidth = 10), Line(370, 370, 370, 400, lineWidth = 10), 
    Line(225, 350, 275, 350, lineWidth = 10), Polygon(250, 245, 267.5, 227.5, 275, 235, 257.5, 252.5), 
    Line(125, 170, 125, 380, lineWidth = 10), Line(120, 385, 215, 385, lineWidth = 10), 
    Line(155, 207.5, 205, 207.5, lineWidth = 15), Line(135, 170, 135, 200, lineWidth = 10), 
    Rect(205, 150, 70, 85), Line(140, 130, 275, 130, lineWidth = 10), 
    Line(295, 380, 295, 400, lineWidth = 10), Line(375, 375, 400, 375, lineWidth = 10), 
    Line(282.5, 65, 282.5, 360, lineWidth = 5), Line(270, 0, 270, 135, lineWidth = 10), 
    Polygon(285, 65, 335, 65, 285, 115), Polygon(400, 65, 350, 65, 400, 115), 
    Line(327.5, 300, 327.5, 360, lineWidth = 15), Line(357.5, 300, 357.5, 360, lineWidth = 15), 
    Line(285, 291.25, 400, 291.25, lineWidth = 2.5), Line(275, 20, 400, 20, lineWidth = 40)
)
groundGroup11C = Group(
    Polygon(225, 370, 140, 370, 140, 285), Polygon(225, 355, 225, 320, 190, 320), 
    Polygon(275, 235, 275, 320, 190, 320), Polygon(210, 285, 182.5, 312.5, 182.5, 285), 
    Polygon(155, 285, 182.5, 312.5, 182.5, 285), Polygon(182.5, 285, 182.5, 257.5, 210, 285), 
    Polygon(182.5, 285, 182.5, 257.5, 155, 285), Polygon(267.5, 227.5, 217.5, 277.5, 155, 215, 205, 165), 
    Polygon(140, 200, 205, 135, 140, 135), Polygon(140, 285, 175, 250, 140, 215), 
    Polygon(155, 200, 205, 150, 205, 200), Line(275, 67.5, 280, 67.5, lineWidth = 5), 
    Line(275, 375, 310, 375, lineWidth = 10), Line(300, 395, 310, 395, lineWidth = 10), 
    Polygon(320, 300, 335, 285, 335, 300), Polygon(365, 300, 350, 285, 350, 300)
)
lavaGroup11C = Group()
windGroup11C = Group()
breakWallGroup11C = Group()
enemyGroup11C = Group()
portalGroup11C = Group()
checkpointGroup11C = Group()
coinGroup11C = Group()
cannonGroup11C = Group()
hiddenGroup11C = Group()
level11CGroupList = [
    exitGroup11C, obstacleGroup11C, groundGroup11C, 
    lavaGroup11C, windGroup11C, portalGroup11C, 
    cannonGroup11C, breakWallGroup11C, enemyGroup11C, 
    checkpointGroup11C, coinGroup11C, hiddenGroup11C
]
level11GroupListDict = {"C": level11CGroupList, "B": level11BGroupList, "A": level11AGroupList}
#Level Dictionaries
levelGroupDictList = [
    level1GroupListDict, level2GroupListDict, level3GroupListDict, 
    level4GroupListDict, level5GroupListDict, level6GroupListDict, 
    level7GroupListDict, level8GroupListDict, level9GroupListDict, 
    level10GroupListDict, level11GroupListDict]
obstacleGroupList = [
    {"A": obstacleGroup1A}, 
    {"A": obstacleGroup2A}, 
    {"A": obstacleGroup2A}, 
    {"A": obstacleGroup4A}, 
    {"A": obstacleGroup4A}, 
    {"A": obstacleGroup6A}, 
    {"A": obstacleGroup7A}, 
    {"A": obstacleGroup8A}, 
    {"A": obstacleGroup9A}, 
    {"A": obstacleGroup10A}, 
    {
        "A": obstacleGroup11A, 
        "B": obstacleGroup11B, 
        "C": obstacleGroup11C
    }
]
groundGroupList = [
    {"A": groundGroup1A}, 
    {"A": groundGroup2A}, 
    {"A": groundGroup2A}, 
    {"A": groundGroup4A}, 
    {"A": groundGroup4A}, 
    {"A": groundGroup6A}, 
    {"A": groundGroup7A}, 
    {"A": groundGroup8A}, 
    {"A": groundGroup9A}, 
    {"A": groundGroup10A}, 
    {
        "A": groundGroup11A, 
        "B": groundGroup11B, 
        "C": groundGroup11C
    }
]
breakWallGroupList = [
    {"A": breakWallGroup1A}, 
    {"A": breakWallGroup1A}, 
    {"A": breakWallGroup1A}, 
    {"A": breakWallGroup1A}, 
    {"A": breakWallGroup1A}, 
    {"A": breakWallGroup1A}, 
    {"A": breakWallGroup1A}, 
    {"A": breakWallGroup1A}, 
    {"A": breakWallGroup9A}, 
    {"A": breakWallGroup10A}, 
    {
        "A": breakWallGroup11A, 
        "B": breakWallGroup11B, 
        "C": breakWallGroup11C
    }
]
keyDoorGroupList = [
    {"A": keyDoorGroup1A}, 
    {"A": keyDoorGroup1A}, 
    {"A": keyDoorGroup1A}, 
    {"A": keyDoorGroup1A}, 
    {"A": keyDoorGroup1A}, 
    {"A": keyDoorGroup1A}, 
    {"A": keyDoorGroup1A}, 
    {"A": keyDoorGroup1A}, 
    {"A": keyDoorGroup9A}, 
    {"A": keyDoorGroup10A}, 
    {
        "A": keyDoorGroup1A, 
        "B": keyDoorGroup1A, 
        "C": keyDoorGroup1A
    }
]
waterGroupList = [
    {"A": waterGroup1A}, 
    {"A": waterGroup1A}, 
    {"A": waterGroup1A}, 
    {"A": waterGroup1A}, 
    {"A": waterGroup1A}, 
    {"A": waterGroup1A}, 
    {"A": waterGroup1A}, 
    {"A": waterGroup1A}, 
    {"A": waterGroup1A}, 
    {"A": waterGroup1A}, 
    {
        "A": waterGroup1A, 
        "B": waterGroup1A, 
        "C": waterGroup1A
    }
]
windZoneGroupList = [
    {"A": windGroup1A}, 
    {"A": windGroup1A}, 
    {"A": windGroup1A}, 
    {"A": windGroup1A}, 
    {"A": windGroup1A}, 
    {"A": windGroup1A}, 
    {"A": windGroup1A}, 
    {"A": windGroup8A}, 
    {"A": windGroup1A}, 
    {"A": windGroup1A}, 
    {
        "A": windGroup11A, 
        "B": windGroup11B, 
        "C": windGroup11C
    }
]
enemyGroupList = [
    {"A": enemyGroup1A}, 
    {"A": enemyGroup1A}, 
    {"A": enemyGroup1A}, 
    {"A": enemyGroup1A}, 
    {"A": enemyGroup1A}, 
    {"A": enemyGroup1A}, 
    {"A": enemyGroup7A}, 
    {"A": enemyGroup8A}, 
    {"A": enemyGroup1A}, 
    {"A": enemyGroup10A}, 
    {
        "A": enemyGroup11A, 
        "B": enemyGroup11B, 
        "C": enemyGroup11C
    }
]
lavaGroupList = [
    {}, 
    {}, 
    {"A": lavaGroup3A}, 
    {}, 
    {"A": lavaGroup5A}, 
    {}, 
    {"A": lavaGroup7A}, 
    {"A": lavaGroup8A}, 
    {}, 
    {}, 
    {
        "A": lavaGroup11A, 
        "B": lavaGroup11B, 
        "C": lavaGroup11C
    }
]
jumpGroupList = [
    {}, 
    {}, 
    {}, 
    {}, 
    {}, 
    {"A": jumpGroup6A}, 
    {"A": jumpGroup7A}, 
    {"A": jumpGroup8A}, 
    {}, 
    {}, 
    {}
]
hiddenGroupList = [
    {}, 
    {}, 
    {}, 
    {}, 
    {}, 
    {}, 
    {"A": hiddenGroup7A}, 
    {"A": hiddenGroup8A}, 
    {"A": hiddenGroup9A}, 
    {"A": hiddenGroup10A}, 
    {
        "A": hiddenGroup11A, 
        "B": hiddenGroup11B, 
        "C": hiddenGroup11C
    }
]
portalGroupList = [
    {}, 
    {}, 
    {}, 
    {}, 
    {}, 
    {"A": portalGroup6A}, 
    {"A": portalGroup7A}, 
    {"A": portalGroup8A}, 
    {"A": portalGroup9A}, 
    {"A": portalGroup10A}, 
    {"C": portalGroup11C}
]
coinGroupList = [
    {"A": coinGroup1A}, 
    {"A": coinGroup2A}, 
    {"A": coinGroup3A}, 
    {"A": coinGroup4A}, 
    {"A": coinGroup5A}, 
    {"A": coinGroup6A}, 
    {"A": coinGroup7A}, 
    {"A": coinGroup8A}, 
    {"A": coinGroup9A}, 
    {"A": coinGroup10A}, 
    {
        "A": coinGroup11A, 
        "B": coinGroup11B, 
        "C": coinGroup11C
    }
]
characterSpawnList  =  [
    [20, 370], [370, 380], [40, 40], 
    [30, 380], [370, 380], [30, 330], 
    [10, 390], [15, 375], [50, 380], 
    [15, 385], [15, 385]
]
goalPosList  =  [
    [370, 380], [40, 40], [30, 380], 
    [370, 380], [30, 380], [380, 30], 
    [380, 30], [5, 90], [395, 310], 
    [395, 55], [395, 235]
]
LevelClassList = []
roomList = ["A", "B", "C"]