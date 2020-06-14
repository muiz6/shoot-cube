from bge import logic, render
camList = logic.getCurrentScene().cameras

cont = logic.getCurrentController()
own = cont.owner
cam1 = camList[own['cam1']]
cam2 = camList[own['cam2']]

width = render.getWindowWidth()
height = render.getWindowHeight()

cam1.setViewport(0, 0, int(width/2), height)
cam2.setViewport(int(width/2), 0, width, height)

cam1.useViewport = True
cam2.useViewport = True