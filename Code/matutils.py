# import requirements
import numpy as np

# matrix to define scale of the object.
def scaleMatrix(s):
    s.append(1)
    return np.diag(s)

# matrix to define translation of the object.
def translationMatrix(t):
    n = len(t)
    T = np.identity(n+1,dtype='f')
    T[:n,-1] = t
    return T

# matrix to define rotation about the Z axis of the object.
def rotationMatrixZ(angle):
    c = np.cos(angle)
    s = np.sin(angle)
    R = np.identity(4)
    R[0,0] = c
    R[0,1] = s
    R[1,0] = -s
    R[1,1] = c
    return R

# matrix to define rotation about the X axis of the object.
def rotationMatrixX(angle):
    c = np.cos(angle)
    s = np.sin(angle)
    R = np.identity(4)
    R[1,1] = c
    R[1,2] = s
    R[2,1] = -s
    R[2,2] = c
    return R

# matrix to define rotation about the Y axis of the object.
def rotationMatrixY(angle):
    c = np.cos(angle)
    s = np.sin(angle)
    R = np.identity(4)
    R[0,0] = c
    R[0,2] = s
    R[2,0] = -s
    R[2,2] = c
    return R


def poseMatrix(position=[0,0,0], orientation=0, scale=1):
    '''
    Returns a combined TRS matrix for the pose of a model.
    :param position: the position of the model
    :param orientation: the model orientation around the Z axis
    :param scale: the model scale, either a scalar for isotropic scaling, or vector of scale factors
    :return: 4x4 TRS matrix
    '''
    # apply the position and orientation of the object.
    R = rotationMatrixZ(orientation)
    T = translationMatrix(position)

    # scale factor.
    if np.isscalar(scale):
        scale = [scale, scale, scale]

    S = scaleMatrix(scale)
    return np.matmul(np.matmul(T,R),S)

def frustumMatrix(l,r,t,b,n,f):
    '''
    Returns an frustum projection matrix
    :param l: left clip plane
    :param r: right clip plane
    :param t: top clip plane
    :param b: bottom clip plane
    :param n: near clip plane
    :param f: far clip plane
    :return: A 4x4 orthographic projection matrix
    '''
    return np.array(
        [
            [ 2*n/(r-l),      0,          (r+l)/(r-l),    0 ],
            [ 0,              -2*n/(t-b),  (t+b)/(t-b),    0 ],
            [ 0,              0,          -(f+n)/(f-n),   -2*f*n/(f-n) ],
            [ 0,              0,          -1,             0 ]
            ]
    )

# homogeneous coordinates helpers for use in shaders.
def homog(v):
    return np.hstack([v,1])

def unhomog(vh):
    return vh[:-1]/vh[-1]
