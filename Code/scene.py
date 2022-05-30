# pygame is just used to create a window with the operating system on which to draw.
import pygame

# imports all openGL functions
from OpenGL.GL import *

# import the shader class
from shaders import *

# import the camera class
from camera import Camera

# and we import a bunch of helper functions
from matutils import *

from lightSource import LightSource

class Scene:
    '''
    This is the main class for drawing an OpenGL scene using the PyGame library
    '''
    def __init__(self, width=1800, height=960, shaders='None'):
        '''
        Initialise the scene
        '''

        # define the size of the pygame window as the given width and height.
        self.window_size = (width, height)

        #  wireframe mode disabled by default.
        self.wireframe = False

        # initialise the pygame window.
        pygame.init()
        screen = pygame.display.set_mode(self.window_size, pygame.OPENGL | pygame.DOUBLEBUF, 24)

        # initialise the window in OpenGL.
        glViewport(0, 0, self.window_size[0], self.window_size[1])

        # set the background colour, this corresponds to a light blue for a sky appearance.
        glClearColor(0.1, 0.7, 1.0, 1.0)

        # enable back face culling.
        glEnable(GL_CULL_FACE)

        # enable vertex array capability.
        glEnableClientState(GL_VERTEX_ARRAY)

        # enable depth test for clean output.
        glEnable(GL_DEPTH_TEST)

        # set the default shader program, flat as default because it is the fastest.
        self.shaders = 'flat'

        # initialise the projective transformation.
        near = 1.5
        far = 50
        left = -1.0
        right = 1.0
        top = -1.0
        bottom = 1.0

        # cycle through models.
        self.show_model = -1

        # use a frustum projection.
        self.P = frustumMatrix(left,right,top,bottom,near,far)

        # initialise the camera object.
        self.camera = Camera()

        # initialise the light source.
        self.light = LightSource(self, position=[5., 5., 5.])

        # rendering mode for the shaders.
        self.mode = 1

        # list of models to draw in the scene.
        self.models = []

    def draw(self):
        '''
        Draw all models in the scene
        :return: None
        '''

        # clear the scene and depth buffer.
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # ensure that the camera view matrix is up to date.
        self.camera.update()

        # loop over all models in the list and draw each.
        for model in self.models:
            model.draw()

        # display the scene, uses double buffering so draw on different buffer to one displayed and flip.
        pygame.display.flip()

    def keyboard(self, event):
        '''
        Method to process keyboard events.
        '''

        # if q is pressed, stop running.
        if event.key == pygame.K_q:
            self.running = False

        # if space is pressed switch between fill and wireframe rendering.
        elif event.key == pygame.K_SPACE:
            if self.wireframe:
                print('--> Rendering using colour fill')
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
                self.wireframe = False
            else:
                print('--> Rendering using colour wireframe')
                glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
                self.wireframe = True

    def pygameEvents(self):
        '''
        Method to handle PyGame events for user interaction.
        '''
        # check whether the window has been closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # keyboard events
            elif event.type == pygame.KEYDOWN:
                self.keyboard(event)

            # move light and scroll camera.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mods = pygame.key.get_mods()
                if event.button == 4:
                    #pass
                    if mods & pygame.KMOD_CTRL:
                        self.light.position *= 1.1
                        self.light.update()
                    else:
                        self.camera.distance = max(1, self.camera.distance - 1)

                elif event.button == 5:
                    #pass
                    if mods & pygame.KMOD_CTRL:
                        self.light.position *= 0.9
                        self.light.update()
                    else:
                        self.camera.distance += 1

            # move camera.
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    if self.mouse_mvt is not None:
                        self.mouse_mvt = pygame.mouse.get_rel()
                        self.camera.center[0] -= (float(self.mouse_mvt[0]) / self.window_size[0])
                        self.camera.center[1] -= (float(self.mouse_mvt[1]) / self.window_size[1])
                    else:
                        self.mouse_mvt = pygame.mouse.get_rel()

                elif pygame.mouse.get_pressed()[2]:
                    if self.mouse_mvt is not None:
                        self.mouse_mvt = pygame.mouse.get_rel()
                        self.camera.phi -= (float(self.mouse_mvt[0]) / self.window_size[0])
                        self.camera.psi -= (float(self.mouse_mvt[1]) / self.window_size[1])
                    else:
                        self.mouse_mvt = pygame.mouse.get_rel()
                else:
                    self.mouse_mvt = None

    def run(self):
        '''
        Draws the scene in a loop until exit.
        '''

        # program loop.
        self.running = True
        while self.running:

            self.pygameEvents()

            # continue drawing while running.
            self.draw()