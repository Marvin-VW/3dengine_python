.. _shape_module:

Object Initialization and Loading
==================================

This module contains classes that represent basic 3D shapes and operations. The primary classes are :mod:`Triangle4D`, :mod:`Cube`, and :mod:`Rectangle`. 

.. note::
    You can use cubes or rectangles, or you can use the :ref:`OBJ Importer <import_module>`

In this module we are dealing with the following code snippet of the Engine Loop:

    .. code-block:: python
        :caption: :mod:`main` method
        :linenos:

        def main(self):

            ...

            cube = Cube(size=1, pos_x=0, pos_y=0, pos_z=0)
            self.mesh_list.extend(cube.mesh)

            ...

-----------------------------------------------------------------------------------------------------------------------------

- `Triangle4D`: A class representing a triangle in 4D space.

- `Cube`: A class for creating a 3D cube.

- `Rectangle`: A class for creating a 3D rectangle.

.. class:: Triangle4D()

   Initializes a :mod:`Triangle4D` instance with three points.

   **Parameters**:

   - `p1` (tuple/list): Coordinates of the first point of the triangle.
   - `p2` (tuple/list): Coordinates of the second point of the triangle.
   - `p3` (tuple/list): Coordinates of the third point of the triangle.

   **Attributes**:

   - `points` (list): A list containing the three points of the triangle.
   - `world_points` (None): Placeholder for points in world coordinates.
   - `camera_points` (None): Placeholder for points in camera coordinates.
   - `normal` (None): Placeholder for the normal vector of the triangle.
   - `ilm` (None): Placeholder for illumination model.
   - `color` (None): Placeholder for the color of the triangle.
   - `centroids` (None): Placeholder for centroid information.

   **Code**:

   .. code-block:: python

     class Triangle4D:
         def __init__(self, p1, p2, p3):
             self.points = [p1, p2, p3]
             self.world_points = None
             self.camera_points = None
             self.normal = None
             self.ilm = None
             self.color = None
             self.centroids = None



-----------------------------------------------------------------------------------------------------------------------------

.. class:: Cube()

   The :mod:`Cube` class represents a 3D cube that can be positioned in space.

   **Methods**

   .. method:: create_point(x: float, y: float, z: float) -> np.array:

      A static method to create a 4D point from 3D coordinates.

      **Parameters**:

      - `x` (float): X-coordinate of the point.
      - `y` (float): Y-coordinate of the point.
      - `z` (float): Z-coordinate of the point.

      **Returns**: A 4D point as a NumPy array.

      **Code**:

      .. code-block:: python

         @staticmethod  
         def create_point(x: float, y: float, z: float) -> np.array:
             return np.array([
                 [x],
                 [y],
                 [z],
                 [1]
             ])

   .. method:: __init__(self, size: float, pos_x: float, pos_y: float, pos_z: float):

      The constructor initializes the cube with a given size and position.

      **Parameters**:

      - `size` (float): The size of the cube.
      - `pos_x` (float): X-coordinate of the cube's position.
      - `pos_y` (float): Y-coordinate of the cube's position.
      - `pos_z` (float): Z-coordinate of the cube's position.

      **Code**:

      .. code-block:: python

         def __init__(self, size: float, pos_x: float, pos_y: float, pos_z: float):
             self.generate_vertices(size)
             self.set_position(pos_x, pos_y, pos_z)

   .. method:: generate_vertices(self, size: float):

      Generates the vertices of the rectangle based on its size. After that, the mesh of the object is generated using the :mod:`Triangle4D` class, with each face consisting of 2 triangles.

      **Parameters**:

      - `size` (float): The size of the cube.

      **Code**:

      .. code-block:: python

        def generate_vertices(self, size: float):
            self.Cube_cubeP0 = self.create_point(-size, size, -size)
            self.Cube_cubeP1 = self.create_point(-size, -size, -size)
            self.Cube_cubeP2 = self.create_point(size, -size, -size)
            self.Cube_cubeP3 = self.create_point(size, size, -size)
            self.Cube_cubeP4 = self.create_point(-size, size, size)
            self.Cube_cubeP5 = self.create_point(-size, -size, size)
            self.Cube_cubeP6 = self.create_point(size, -size, size)
            self.Cube_cubeP7 = self.create_point(size, size, size)

            self.cube_points = [
                self.Cube_cubeP0, self.Cube_cubeP1,
                self.Cube_cubeP2, self.Cube_cubeP3,
                self.Cube_cubeP4, self.Cube_cubeP5,
                self.Cube_cubeP6, self.Cube_cubeP7
            ]

            triangle_top_1 = Triangle4D(self.Cube_cubeP4, self.Cube_cubeP5, self.Cube_cubeP6)
            triangle_top_2 = Triangle4D(self.Cube_cubeP4, self.Cube_cubeP6, self.Cube_cubeP7)

            triangle_bottom_1 = Triangle4D(self.Cube_cubeP1, self.Cube_cubeP0, self.Cube_cubeP2)
            triangle_bottom_2 = Triangle4D(self.Cube_cubeP2, self.Cube_cubeP0, self.Cube_cubeP3)

            triangle_left_1 = Triangle4D(self.Cube_cubeP3, self.Cube_cubeP0, self.Cube_cubeP7)
            triangle_left_2 = Triangle4D(self.Cube_cubeP7, self.Cube_cubeP0, self.Cube_cubeP4)

            triangle_right_1 = Triangle4D(self.Cube_cubeP5, self.Cube_cubeP1, self.Cube_cubeP6)
            triangle_right_2 = Triangle4D(self.Cube_cubeP6, self.Cube_cubeP1, self.Cube_cubeP2)

            triangle_front_1 = Triangle4D(self.Cube_cubeP4, self.Cube_cubeP0, self.Cube_cubeP5)
            triangle_front_2 = Triangle4D(self.Cube_cubeP5, self.Cube_cubeP0, self.Cube_cubeP1)

            triangle_back_1 = Triangle4D(self.Cube_cubeP2, self.Cube_cubeP3, self.Cube_cubeP6)
            triangle_back_2 = Triangle4D(self.Cube_cubeP6, self.Cube_cubeP3, self.Cube_cubeP7)

            self.mesh = [
                triangle_top_1, triangle_top_2,
                triangle_bottom_1, triangle_bottom_2,
                triangle_left_1, triangle_left_2,
                triangle_right_1, triangle_right_2,
                triangle_front_1, triangle_front_2,
                triangle_back_1, triangle_back_2
            ]

   .. method:: set_position(self, pos_x: float, pos_y: float, pos_z: float):

      Sets the position of the cube in 3D space.

      **Parameters**:

      - `pos_x` (float): The new X-coordinate.
      - `pos_y` (float): The new Y-coordinate.
      - `pos_z` (float): The new Z-coordinate.

      **Code**:

      .. code-block:: python

             def set_position(self, pos_x, pos_y, pos_z):
              translation_matrix = np.array([
                  [1, 0, 0, pos_x],
                  [0, 1, 0, pos_y],
                  [0, 0, 1, pos_z],
                  [0, 0, 0, 1]
              ])

              for pos, point in enumerate(self.cube_points):
                  translated_vec = translation_matrix @ point
                  self.cube_points[pos] = translated_vec

              for triangle in self.mesh:
                  triangle.points = [translation_matrix @ vertex for vertex in triangle.points]



-----------------------------------------------------------------------------------------------------------------------------

.. class:: Rectangle()

   The :mod:`Rectangle` class represents a 3D Rectangle that can be positioned in space.

   **Methods**

   .. method:: create_point(x: float, y: float, z: float) -> np.array:

      A static method to create a 4D point from 3D coordinates.

      **Parameters**:

      - `x` (float): X-coordinate of the point.
      - `y` (float): Y-coordinate of the point.
      - `z` (float): Z-coordinate of the point.

      **Returns**: A 4D point as a NumPy array.

      **Code**:

      .. code-block:: python

         @staticmethod  
         def create_point(x: float, y: float, z: float) -> np.array:
             return np.array([
                 [x],
                 [y],
                 [z],
                 [1]
             ])

   .. method:: __init__(self, size: float, pos_x: float, pos_y: float, pos_z: float):

      The constructor initializes the Rectangle with a given size and position.

      **Parameters**:

      - `size_x` (float): The x-size of the Rectangle.
      - `size.y` (float): The y-size of the Rectangle.
      - `size_z` (float): The z-size of the Rectangle.
      - `pos_x` (float): X-coordinate of the Rectangle's position.
      - `pos_y` (float): Y-coordinate of the Rectangle's position.
      - `pos_z` (float): Z-coordinate of the Rectangle's position.

      **Code**:

      .. code-block:: python

         def __init__(self, size_x, size_y, size_z, pos_x, pos_y, pos_z):
            self.generate_vertices(size_x, size_y, size_z)
            self.set_position(pos_x, pos_y, pos_z)

   .. method:: generate_vertices(self, size: float):

      Generates the vertices of the Rectangle based on its size. After that, the mesh of the object is generated using the :mod:`Triangle4D` class, with each face consisting of 2 triangles.

      **Parameters**:

      - `size` (float): The size of the Rectangle.

      **Code**:

      .. code-block:: python

        def generate_vertices(self, size_x, size_y, size_z):
            self.Cube_cubeP0 = self.create_point(-size_x, size_y, -size_z)
            self.Cube_cubeP1 = self.create_point(-size_x, -size_y, -size_z)
            self.Cube_cubeP2 = self.create_point(size_x, -size_y, -size_z)
            self.Cube_cubeP3 = self.create_point(size_x, size_y, -size_z)
            self.Cube_cubeP4 = self.create_point(-size_x, size_y, size_z)
            self.Cube_cubeP5 = self.create_point(-size_x, -size_y, size_z)
            self.Cube_cubeP6 = self.create_point(size_x, -size_y, size_z)
            self.Cube_cubeP7 = self.create_point(size_x, size_y, size_z)

            self.cube_points = [
                self.Cube_cubeP0, self.Cube_cubeP1,
                self.Cube_cubeP2, self.Cube_cubeP3,
                self.Cube_cubeP4, self.Cube_cubeP5,
                self.Cube_cubeP6, self.Cube_cubeP7
            ]

            triangle_top_1 = Triangle4D(self.Cube_cubeP4, self.Cube_cubeP5, self.Cube_cubeP6)
            triangle_top_2 = Triangle4D(self.Cube_cubeP4, self.Cube_cubeP6, self.Cube_cubeP7)

            triangle_bottom_1 = Triangle4D(self.Cube_cubeP1, self.Cube_cubeP0, self.Cube_cubeP2)
            triangle_bottom_2 = Triangle4D(self.Cube_cubeP2, self.Cube_cubeP0, self.Cube_cubeP3)

            triangle_left_1 = Triangle4D(self.Cube_cubeP3, self.Cube_cubeP0, self.Cube_cubeP7)
            triangle_left_2 = Triangle4D(self.Cube_cubeP7, self.Cube_cubeP0, self.Cube_cubeP4)

            triangle_right_1 = Triangle4D(self.Cube_cubeP5, self.Cube_cubeP1, self.Cube_cubeP6)
            triangle_right_2 = Triangle4D(self.Cube_cubeP6, self.Cube_cubeP1, self.Cube_cubeP2)

            triangle_front_1 = Triangle4D(self.Cube_cubeP4, self.Cube_cubeP0, self.Cube_cubeP5)
            triangle_front_2 = Triangle4D(self.Cube_cubeP5, self.Cube_cubeP0, self.Cube_cubeP1)

            triangle_back_1 = Triangle4D(self.Cube_cubeP2, self.Cube_cubeP3, self.Cube_cubeP6)
            triangle_back_2 = Triangle4D(self.Cube_cubeP6, self.Cube_cubeP3, self.Cube_cubeP7)

            self.mesh = [
                triangle_top_1, triangle_top_2,
                triangle_bottom_1, triangle_bottom_2,
                triangle_left_1, triangle_left_2,
                triangle_right_1, triangle_right_2,
                triangle_front_1, triangle_front_2,
                triangle_back_1, triangle_back_2
            ]

   .. method:: set_position(self, pos_x: float, pos_y: float, pos_z: float):

      Sets the position of the Rectangle in 3D space.

      **Parameters**:

      - `pos_x` (float): The new X-coordinate.
      - `pos_y` (float): The new Y-coordinate.
      - `pos_z` (float): The new Z-coordinate.

      **Code**:

      .. code-block:: python

             def set_position(self, pos_x, pos_y, pos_z):
              translation_matrix = np.array([
                  [1, 0, 0, pos_x],
                  [0, 1, 0, pos_y],
                  [0, 0, 1, pos_z],
                  [0, 0, 0, 1]
              ])

              for pos, point in enumerate(self.cube_points):
                  translated_vec = translation_matrix @ point
                  self.cube_points[pos] = translated_vec

              for triangle in self.mesh:
                  triangle.points = [translation_matrix @ vertex for vertex in triangle.points]