import os, win32api
import pygame as pg
from math import *
from tkinter import *
import tkinter.messagebox as tkmb

#----------Global Variables----------#

slowColor = (  0,255,255)
fastColor = (255,  0,255)
currentDir = os.path.dirname(os.path.realpath('__file__'))
saveDir = currentDir + '\\Tracked Images'

if not os.path.exists(saveDir):
    os.makedirs(saveDir)

lastSaved = open(currentDir + '\\lastSaved.txt', 'r')
lastSavedLine = lastSaved.readline()

if lastSavedLine == '':
    lastSaved.close()
    lastSaved = open(currentDir + '\\lastSaved.txt', 'w+')
    lastSaved.write(saveDir)
    lastSavedLine = saveDir

saveDir = lastSavedLine

#----------Functions----------#



#----------Classes----------#

class openWindow():

    def __init__(self):

        global slowColor, fastColor, saveDir

        print(saveDir)
        self.window = Tk()
        self.window.config(bg='#1e1e1e')
        self.window.title('Mouse Tracker')
        self.window.title = 'Mouse Tracker'
        self.saveLocGood = False

        labelSlow = Label(self.window, text='Slow Color', bg='#1e1e1e', fg='#cecece')
        labelSlowCol = Label(self.window, bg='#%02x%02x%02x' % slowColor, border=2)
        rLabelL = Label(self.window, text='R', bg='#1e1e1e', fg='#cecece')
        gLabelL = Label(self.window, text='G', bg='#1e1e1e', fg='#cecece')
        bLabelL = Label(self.window, text='B', bg='#1e1e1e', fg='#cecece')
        labelFast = Label(self.window, text='Fast Color', bg='#1e1e1e', fg='#cecece')
        labelFastCol = Label(self.window, bg='#%02x%02x%02x' % slowColor, border=2)
        rLabelR = Label(self.window, text='R', bg='#1e1e1e', fg='#cecece')
        gLabelR = Label(self.window, text='G', bg='#1e1e1e', fg='#cecece')
        bLabelR = Label(self.window, text='B', bg='#1e1e1e', fg='#cecece')
        rSliderL = Scale(self.window, length='200', from_=255, to=0, bg='#1e1e1e', fg='#cecece')
        gSliderL = Scale(self.window, length='200', from_=255, to=0, bg='#1e1e1e', fg='#cecece')
        bSliderL = Scale(self.window, length='200', from_=255, to=0, bg='#1e1e1e', fg='#cecece')
        rSliderR = Scale(self.window, length='200', from_=255, to=0, bg='#1e1e1e', fg='#cecece')
        gSliderR = Scale(self.window, length='200', from_=255, to=0, bg='#1e1e1e', fg='#cecece')
        bSliderR = Scale(self.window, length='200', from_=255, to=0, bg='#1e1e1e', fg='#cecece')
        labelSaveLoc = Label(self.window, text='Save Location:', bg='#1e1e1e', fg='#cecece')
        self.textBoxSaveLoc = Entry(self.window, width=40, bg='#cecece', fg='#1e1e1e')
        self.textBoxSaveLoc.insert(0, saveDir)
        buttonStart = Button(self.window, text='Start!', bg='#cecece', command=self.tryToRun)
        spacerTopLeft = Label(self.window, text='     ', bg='#1e1e1e')
        spacerTopMiddle = Label(self.window, text='          ', bg='#1e1e1e')
        spacerBottomRight = Label(self.window, text='     ', bg='#1e1e1e', fg='#cecece')
        spacerMiddleMiddle = Label(self.window, text='', bg='#1e1e1e')
        spacerBottomMiddle = Label(self.window, text='', bg='#1e1e1e')

        labelSlow.grid(row=1, column=3, columnspan=5)
        labelSlowCol.grid(row=2, column=1, rowspan=2, columnspan=9, sticky=NW+SE)
        rLabelL.grid(row=4, column=2)
        gLabelL.grid(row=4, column=5)
        bLabelL.grid(row=4, column=8)
        labelFast.grid(row=1, column=14, columnspan=5)
        labelFastCol.grid(row=2, column=12, rowspan=2, columnspan=9, sticky=NW+SE)
        rLabelR.grid(row=4, column=13)
        gLabelR.grid(row=4, column=16)
        bLabelR.grid(row=4, column=19)
        rSliderL.set(0)
        rSliderL.grid(row=5, column=2, rowspan=6)
        gSliderL.set(255)
        gSliderL.grid(row=5, column=5, rowspan=6)
        bSliderL.set(255)
        bSliderL.grid(row=5, column=8, rowspan=6)
        rSliderR.set(255)
        rSliderR.grid(row=5, column=13, rowspan=6)
        gSliderR.set(0)
        gSliderR.grid(row=5, column=16, rowspan=6)
        bSliderR.set(255)
        bSliderR.grid(row=5, column=19, rowspan=6)
        labelSaveLoc.grid(row=13, column=1, columnspan=7, sticky=W)
        self.textBoxSaveLoc.grid(row=13, column=6, columnspan=16)
        buttonStart.grid(row=15, column=8, columnspan=6, sticky=W+E)
        spacerTopLeft.grid(row=0)
        spacerTopMiddle.grid(row=0, column=10, columnspan=2)
        spacerBottomRight.grid(row=16, column=22)
        spacerMiddleMiddle.grid(row=11, column=10)
        spacerBottomMiddle.grid(row=14, column=10)

        rSliderL['command'] = lambda scale_value: self.updateSlow(rSliderL, gSliderL, bSliderL, labelSlowCol)
        gSliderL['command'] = lambda scale_value: self.updateSlow(rSliderL, gSliderL, bSliderL, labelSlowCol)
        bSliderL['command'] = lambda scale_value: self.updateSlow(rSliderL, gSliderL, bSliderL, labelSlowCol)
        rSliderR['command'] = lambda scale_value: self.updateFast(rSliderR, gSliderR, bSliderR, labelFastCol)
        gSliderR['command'] = lambda scale_value: self.updateFast(rSliderR, gSliderR, bSliderR, labelFastCol)
        bSliderR['command'] = lambda scale_value: self.updateFast(rSliderR, gSliderR, bSliderR, labelFastCol)

        self.window.mainloop()

    def tryToRun(self):

        global saveDir, currentDir

        self.saveLocGood = os.path.exists(self.textBoxSaveLoc.get())

        if self.saveLocGood:
            saveDir = self.textBoxSaveLoc.get()
            lastSaved = open(currentDir + '\\lastSaved.txt', 'w')
            lastSaved.write(saveDir)
            self.window.destroy()
            runWindow()

        else:
            tkmb.showerror(title='Invalid Save Location!', message='Invalid Save Location!')

    def updateSlow(self, sl1, sl2, sl3, label):

        global slowColor

        slowColor = (sl1.get(), sl2.get(), sl3.get())
        label.config(bg='#%02x%02x%02x' % slowColor)

    def updateFast(self, sl1, sl2, sl3, label):

        global fastColor

        fastColor = (sl1.get(), sl2.get(), sl3.get())
        label.config(bg='#%02x%02x%02x' % fastColor)

class runWindow:

    def __init__(self):

        topBar = 25
        pg.font.init()
        myFontSmall = pg.font.SysFont("Arial", 11)
        self.width = win32api.GetSystemMetrics(0)
        self.height = win32api.GetSystemMetrics(1)
        self.versionRunning = myFontSmall.render("v.0.1.0.0 (Copyright BenTech(TM) February 2018)", False, (255, 255, 255))

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, topBar)
        pg.display.init()
        self.scrInfo = pg.display.Info()
        self.window = pg.display.set_mode((self.width, self.height))
        pg.display.iconify()

        self.FPS = 300
        self.clock = pg.time.Clock()

        self.partSecond = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.timeInSecs = 0
        self.timeInMins = 0

        self.black = (  0,  0,  0)
        self.white = (255,255,255)

        self.window.fill(self.black)

        self.running = True
        self.alt = False

        cursor = win32api.GetCursorPos()
        self.xOld = cursor[0]
        self.yOld = cursor[1]

        self.circleImgs = self.loadCircles()

        self.heldL = False
        self.heldM = False
        self.heldR = False

        self.nameNum = 1

        self.lClicks = 0
        self.mClicks = 0
        self.rClicks = 0

        self.gCircles = []
        self.rCircles = []
        self.yCircles = []

        self.firstLoop = True

        self.run()

    def span(self, num, col1, col2):

        if col1 < col2:

            if num < col1:
                num = col1

            if num > col2:
                num = col2

        if col2 < col1:

            if num > col1:
                num = col1

            if num < col2:
                num = col2

        return num

    def loadCircles(self):

        circleG = pg.image.load("img\circleGreen.png")
        circleR = pg.image.load("img\circleRed.png")
        circleY = pg.image.load("img\circleYellow.png")
        tup = (circleG, circleR, circleY)

        return tup

    def run(self):

        global slowColor, fastColor

        running = True

        while running:

            for event in pg.event.get():

                if event.type == pg.QUIT:

                    self.end(self.nameNum)

                elif event.type == pg.KEYDOWN:

                    if event.key == pg.K_LALT or event.key == pg.K_RALT: self.alt = True

                    if event.key == pg.K_F4 and self.alt: self.end(self.nameNum)

            if self.firstLoop:

                self.gCircles = []
                self.rCircles = []
                self.yCircles = []

            self.clock.tick(self.FPS)

            cursor = win32api.GetCursorPos()
            xNow = cursor[0]
            yNow = cursor[1]

            speed = sqrt((xNow - self.xOld) ** 2 + (yNow - self.yOld) ** 2) / 135

            unitsR = int(fastColor[0] - slowColor[0])
            unitsG = int(fastColor[1] - slowColor[1])
            unitsB = int(fastColor[2] - slowColor[2])

            colR = self.span((slowColor[0] + speed * unitsR), slowColor[0], fastColor[0])
            colG = self.span((slowColor[1] + speed * unitsG), slowColor[1], fastColor[1])
            colB = self.span((slowColor[2] + speed * unitsB), slowColor[2], fastColor[2])

            color = (colR, colG, colB)

            pg.draw.line(self.window, color, (xNow, yNow), (self.xOld, self.yOld))

            mouseL = win32api.GetKeyState(0x01)
            mouseR = win32api.GetKeyState(0x02)
            mouseM = win32api.GetKeyState(0x04)

            if mouseL >= 0:
                self.heldL = True

            if mouseR >= 0:
                self.heldR = True

            if mouseM >= 0:
                self.heldM = True

            xy = (xNow - 4, yNow - 4)

            if mouseL < 0 and self.heldL:
                self.gCircles.append(xy)
                self.window.blit(self.circleImgs[0], xy)
                self.heldL = False
                self.lClicks += 1

            if mouseR < 0 and self.heldR:
                self.rCircles.append(xy)
                self.window.blit(self.circleImgs[1], xy)
                self.heldR = False
                self.rClicks += 1

            if mouseM < 0 and self.heldR:
                self.yCircles.append(xy)
                self.window.blit(self.circleImgs[2], xy)
                self.heldM = False
                self.mClicks += 1

            if self.firstLoop:
                self.window.fill(self.black)

            self.xOld = xNow
            self.yOld = yNow

            self.partSecond += 1

            if self.partSecond >= 300:
                self.partSecond = 0
                self.seconds += 1
                self.timeInSecs += 1

            if self.seconds >= 60:
                self.seconds = 0
                self.minutes += 1
                self.timeInMins += 1

            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1

            self.window.blit(self.versionRunning, (5, self.height - 15))
            self.firstLoop = False

            pg.display.update()

    def end(self, num):

        global saveDir

        myFont = pg.font.SysFont("Arial", 14)

        timeInMins = float(self.timeInSecs/60)
        avgLClicks = (len(self.gCircles)/timeInMins)
        avgRClicks = (len(self.rCircles)/timeInMins)
        avgMClicks = (len(self.yCircles)/timeInMins)

        showDefS = myFont.render("Slow =", False, (255, 255, 255))
        showDefF = myFont.render("Fast =", False, (255,255,255))
        showDefL = myFont.render("Left-click =", False, (255,255,255))
        showDefR = myFont.render("Right-click =", False, (255,255,255))
        showDefM = myFont.render("Middle-click =", False, (255,255,255))
        lClicksNum = myFont.render("Number of left-clicks: " + str(self.lClicks), False, (255,255,255))
        rClicksNum = myFont.render("Number of right-clicks: " + str(self.rClicks), False, (255,255,255))
        mClicksNum = myFont.render("Number of middle-clicks: " + str(self.mClicks), False, (255,255,255))
        sessionTime = myFont.render("Length of session: " + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds), False, (255,255,255))
        avgLClicksNum = myFont.render("Avg left-clicks per minute: " + str(round(avgLClicks,1)), False, (255,255,255))
        avgRClicksNum = myFont.render("Avg right-clicks per minute: " + str(round(avgRClicks,1)), False, (255,255,255))
        avgMClicksNum = myFont.render("Avg middle-clicks per minute: " + str(round(avgMClicks,1)), False, (255,255,255))

        for xy in self.gCircles:
            self.window.blit(self.circleImgs[0], xy)
        for xy in self.rCircles:
            self.window.blit(self.circleImgs[1], xy)
        for xy in self.yCircles:
            self.window.blit(self.circleImgs[2], xy)

        keyLineSlow = showDefS.get_size()[0] + 8
        keyLineFast = showDefF.get_size()[0] + 8
        keyCircleGreen = showDefL.get_size()[0] + 8
        keyCircleRed = showDefR.get_size()[0] + 8
        keyCircleYellow = showDefM.get_size()[0] + 8
        width = avgMClicksNum.get_size()[0]

        s = pg.Surface((width + 10, 230), pg.SRCALPHA)
        s.fill((0, 0, 0, 200))
        self.window.blit(s, (0, 0))

        self.window.blit(showDefS, (0, 0))
        self.window.blit(showDefF, (0, 15))
        self.window.blit(sessionTime, (0, 30))
        self.window.blit(showDefL, (0, 60))
        self.window.blit(showDefR, (0, 75))
        self.window.blit(showDefM, (0, 90))
        self.window.blit(lClicksNum, (0, 120))
        self.window.blit(avgLClicksNum, (0, 135))
        self.window.blit(rClicksNum, (0, 155))
        self.window.blit(avgRClicksNum, (0, 170))
        self.window.blit(mClicksNum, (0, 190))
        self.window.blit(avgMClicksNum, (0, 200))
        pg.draw.line(self.window, (0, 255, 255), (keyLineSlow, 9), (keyLineSlow + 50, 9))
        pg.draw.line(self.window, (255, 0, 255), (keyLineFast, 24), (keyLineFast + 50, 24))
        self.window.blit(self.circleImgs[0], (keyCircleGreen, 67))
        self.window.blit(self.circleImgs[1], (keyCircleRed, 82))
        self.window.blit(self.circleImgs[2], (keyCircleYellow, 97))

        self.window.blit(self.versionRunning, (5, self.height - 15))

        save = False

        while not save:

            try:
                pg.image.load(saveDir + '\screenshot(' + str(num) + ').png')
                num += 1

            except:
                fileName = saveDir + '\screenshot(' + str(num) + ').png'
                pg.image.save(self.window, fileName)
                save = True

        pg.quit()
        sys.exit()

window = openWindow()
