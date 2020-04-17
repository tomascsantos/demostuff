# %% codecell
import vtkplotter as vtk
import numpy as np

# %% codecell
p = 1
c =12
num_vecs = 2000

def main():
    vp = vtk.Plotter(size=(800, 800), axes=0, interactive=0)
    vp += vtk.Grid(sx=2, sy=2)
    origin = [0,0,0]

    #Define hypercube (shown in red in visualization)
    A = np.array([
        [p, p, 0],
        [p, -p, 0],
        [-p, p, 0],
        [-p,-p, 0]
    ]).astype("float").T

    """
    Conceptually: How much a vector is allowed to go
    in the direction of the corresponding hypercube axis
    """
    b = np.array([
        [2],
        [4],
        [9],
        [1]
    ])


    #add a bunch of x vectors with 0 in z direction
    xs = np.random.normal(size=(num_vecs,2))
    z = np.zeros((num_vecs,1))
    xs = np.block([xs, z])

    #all the vectors that obey the constrains
    s = np.array([x for x in xs if np.all(np.greater(np.ravel(b), np.ravel(x@A)))])

    #add the constrain obeying vectors to the visualization
    vp += [vtk.shapes.Tube([origin, np.ravel(x)], r=0.001, c="b") for x in s]

    #add the hypercube defining vectors to the visualization
    vp += [vtk.shapes.Tube([origin, np.ravel(a)], r=0.01, c="r") for a in A.T]

    #show visualization
    vp.show(interactive=1)

if __name__ == "__main__":
# %% codecell
    main()
