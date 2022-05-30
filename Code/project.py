# Imports pygame
import pygame

# import the scene class
from scene import Scene

# Imports the lightSource class
from lightSource import LightSource

# Imports the load_obj_file function to use to load the files
from blender import load_obj_file

# Import the function that draws each model from its meshes
from BaseModel import DrawModelFromMesh

# Import everything from the shaders
from shaders import *


'''
Declaring an object of the scene class.
'''
class ProjectScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        # Load a light source object representing the sun values other than position left at default.
        self.light = LightSource(self, position=[5., 3., -5.])
        
        # Load the car obj file as an object by drawing each model as a mesh.
        car1 = load_obj_file('models/car2.obj')
        self.car1 = [DrawModelFromMesh(scene=self, M=translationMatrix([5.5,-4.4,16]), mesh=mesh, shader=FlatShader()) for mesh in car1]

        # Same for the street obj file.
        street = load_obj_file('models/test.obj')
        self.street = [DrawModelFromMesh(scene=self, M=translationMatrix([0,-5,-10]), mesh=mesh, shader=FlatShader()) for mesh in street]

    def keyboard(self, event):
        '''
        Process keyboard events for this demo.
        '''
        Scene.keyboard(self, event)
        
        '''
        Handle keys 0-9 that translate and rotate the car.
        '''
        if event.key == pygame.K_1:
            # print what is happening.
            print('########################')
            print('### Applying Translation ###')

            # iterate through each model in the car object.
            for model in self.car1:

                # apply the new position as a translation matrix to the model.
                model.M = translationMatrix([5.5,-4.4,8])
        
        # repeat for the rest using different positions and rotations.
        elif event.key == pygame.K_2:
            print('########################')
            print('### Applying Translation ###')
            for model in self.car1:
                model.M = translationMatrix([5.5,-4.4,0])
        elif event.key == pygame.K_3:
            print('########################')
            print('### Applying Translation ###')
            for model in self.car1:
                model.M = translationMatrix([5.5,-4.4,-8])
        elif event.key == pygame.K_4:
            print('########################')
            print('### Applying Translation ###')
            for model in self.car1:
                model.M = translationMatrix([5.5,-4.4,-16])
        elif event.key == pygame.K_5:
            print('########################')
            print('### Applying Translation ###')
            for model in self.car1:

                # calculate the overall position matrix with the translation matrix and rotation matrix of pi radians.
                model.M = np.matmul(translationMatrix([10,-4.4,-16]), rotationMatrixY(np.pi))
        elif event.key == pygame.K_6:
            print('########################')
            print('### Applying Translation ###')
            for model in self.car1:
                model.M = np.matmul(translationMatrix([10,-4.4,-8]), rotationMatrixY(np.pi))
        elif event.key == pygame.K_7:
            print('########################')
            print('### Applying Translation ###')
            for model in self.car1:
                model.M = np.matmul(translationMatrix([10,-4.4,0]), rotationMatrixY(np.pi))
        elif event.key == pygame.K_8:
            print('########################')
            print('### Applying Translation ###')
            for model in self.car1:
                model.M = np.matmul(translationMatrix([10,-4.4,8]), rotationMatrixY(np.pi))
        elif event.key == pygame.K_9:
            print('########################')
            print('### Applying Translation ###')
            for model in self.car1:
                model.M = np.matmul(translationMatrix([10,-4.4,16]), rotationMatrixY(np.pi))
        elif event.key == pygame.K_0:
            print('########################')
            print('### Applying Translation ###')
            for model in self.car1:
                model.M = translationMatrix([5.5,-4.4,16])


    def draw(self):
        '''
        Draw all models in the scene
        '''
        # clear the scene and the depth buffer.
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # update camera.
        self.camera.update()

        # draw each model in the car object.
        for model in self.car1:
            model.draw()
        
        # and draw each model in the street object as well.
        for model in self.street:
            model.draw()

        # display the scene, uses double buffering so draw on different buffer to one displayed and flip.
        pygame.display.flip()


if __name__ == '__main__':
    # initialise the scene object.
    scene = ProjectScene()

    # start drawing the scene.
    scene.run()
