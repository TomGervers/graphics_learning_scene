# import a useful matrix functions for positioning
from matutils import *


class Camera:
    '''
    Base class for handling camera.
    '''

    def __init__(self):
        self.V = np.identity(4)
        self.phi = 0.               # azimuth angle.
        self.psi = 0.               # zenith angle.
        self.distance = 20.         # distance of the camera to the centre point.
        self.center = [0., 0., 0.]  # position of the centre.
        self.update()               # calculate the view matrix.

    def update(self):
        '''
        Update the camera view matrix from parameters. Set the point to look at as centre of the coordinate system,
        then rotate the coordinate system according to phi and psi angles and move the camera to the set distance from
        the point.
        '''
        # calculate the translation matrix for the view center.
        T0 = translationMatrix(self.center)

        # calculate the rotation matrix from the angles phi (azimuth) and psi (zenith) angles.
        R = np.matmul(rotationMatrixX(self.psi), rotationMatrixY(self.phi))

        # calculate translation for the camera distance to the center point.
        T = translationMatrix([0., 0., -self.distance])

        # calculate the view matrix by combining the three matrices.
        self.V = np.matmul(np.matmul(T, R), T0)