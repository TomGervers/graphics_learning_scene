# import requirements
import numpy as np

class LightSource:
    '''
    Base class for maintaining a light source in the scene.
    '''
    def __init__(self, scene, position=[2.,2.,0.], Ia=[0.2,0.2,0.2], Id=[0.9,0.9,0.9], Is=[1.0,1.0,1.0]):
        '''
        :param scene: The scene in which the light source exists.
        :param position: the position of the light source
        :param Ia: The ambient illumination it provides (may not be dependent on the light source itself)
        :param Id: The diffuse illumination
        :param Is: The specular illumination
        '''

        self.position = np.array(position,'f')
        self.Ia = Ia
        self.Id = Id
        self.Is = Is

    def update(self, position=None):
        '''
        update the position of the light source.
        :param position: [optional] sets the new light source position.
        '''
        if position is not None:
            self.position = position
