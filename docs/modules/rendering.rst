.. _rendering:

Rendering
=====================

Here we are in the rendering module of the main loop. In this module, we draw the cube’s lines and points in the frame, and then fill in the faces.

In this module we are dealing with the following code snippet of the Engine Loop:


    .. code-block:: python
        :caption: :mod:`main` method
        :linenos:

        def main(self):

            ...

                self.camera_model.draw_all_cube_lines(clipped_triangles)
                if self.window.show_points:
                    self.camera_model.draw_all_cube_points(clipped_triangles)
                if self.window.show_planes:
                    self.camera_model.fill_cube_faces(clipped_triangles)
                ...

Let's dive into the detailed explanations of the implementation.

------------------------------------------------------------------------------------

    .. method:: draw_all_cube_points(triangles: List) -> None

        Draws all points of the cube on the camera image.

        .. note::
            This method handles only the triangle points; the actual drawing will be performed in the :mod:`draw_camera_image_point` method.

        **Parameters:**

        - `triangles`: A list of triangles representing the cube.

        .. code-block:: python
            :caption: :mod:`draw_all_cube_points` method

            def draw_all_cube_points(self, triangles: List) -> None:

                for triangle in triangles:
                    for point in triangle.camera_points:
                        self.draw_camera_image_point(point)

------------------------------------------------------------------------------------

    .. method:: draw_camera_image_point(C_point: np.array) -> None

        Draws a single point on the camera image using the camera coordinates from the :mod:`draw_all_cube_points` method.

        **Parameters:**

        - `C_point`: The point in camera coordinates.

        .. code-block:: python
            :caption: :mod:`draw_camera_image_point` method

            def draw_camera_image_point(self, C_point: np.array) -> None:
                I_point = np.matmul(self.I_T_C, C_point)
                u = int(I_point[0] / I_point[2])
                v = int(I_point[1] / I_point[2])
                cv.circle(self.camera_image, (u, v), 5, (255, 0, 0), 2)

------------------------------------------------------------------------------------

    .. method:: draw_all_cube_lines(triangles: List) -> None

        Draws all edges of the cube on the camera image.

        .. note::
            This method handles only the triangle points; the actual drawing will be performed in the :mod:`draw_camera_image_line` method.

        **Parameters:**

        - `triangles`: A list of triangles representing the cube.

        .. code-block:: python
            :caption: :mod:`draw_all_cube_lines` method

            def draw_all_cube_lines(self, triangles : List) -> None:

                for triangle in triangles:
                    for i in range(3):
                        C_point0 = triangle.camera_points[i]
                        C_point1 = triangle.camera_points[(i + 1) % 3]
                        self.draw_camera_image_line(C_point0, C_point1)

------------------------------------------------------------------------------------

    .. method:: draw_camera_image_line(C_point0: np.array, C_point1: np.array) -> None

        Draws a line between two points on the camera image using the camera coordinates given by the :mod:`draw_all_cube_lines` method.

        **Parameters:**

        - `C_point0`: The first point in camera coordinates.

        - `C_point1`: The second point in camera coordinates.

        .. code-block:: python
            :caption: :mod:`draw_camera_image_line` method

            def draw_camera_image_line(self, C_point0: np.array, C_point1: np.array) -> None:
                I_point0 = np.matmul(self.I_T_C, C_point0)
                I_point1 = np.matmul(self.I_T_C, C_point1)

                u0 = int(I_point0[0] / I_point0[2])
                v0 = int(I_point0[1] / I_point0[2])

                u1 = int(I_point1[0] / I_point1[2])
                v1 = int(I_point1[1] / I_point1[2])

                cv.line(self.camera_image, (u0, v0), (u1, v1), (0, 0, 0), 1)

------------------------------------------------------------------------------------

    .. method:: draw_camera_image_arrow(C_point0: np.array, C_point1: np.array) -> None

        Draws an arrow from one point to another on the camera image.

        **Parameters:**

        - `C_point0`: The starting point in camera coordinates.

        - `C_point1`: The ending point in camera coordinates.

        .. code-block:: python
            :caption: :mod:`draw_camera_image_arrow` method

            def draw_camera_image_arrow(self, C_point0: np.array, C_point1: np.array) -> None:
                try:
                    I_point0 = np.matmul(self.I_T_C, C_point0)
                    I_point1 = np.matmul(self.I_T_C, C_point1)

                    u0 = int(I_point0[0] / I_point0[2])
                    v0 = int(I_point0[1] / I_point0[2])

                    u1 = int(I_point1[0] / I_point1[2])
                    v1 = int(I_point1[1] / I_point1[2])

                    cv.arrowedLine(self.camera_image, (u0, v0), (u1, v1), (0, 255, 0), 2)
                except:
                    raise ValueError(f"Could draw normal {C_point0}, {C_point1}")

------------------------------------------------------------------------------------

    .. method:: fill_cube_faces(triangles: List) -> None

        Fills the faces of the cube with a specified color on the camera image.

        **Parameters:**

        - `triangles`: A list of triangles representing the cube.

        .. code-block:: python
            :caption: :mod:`fill_cube_faces` method

            def fill_cube_faces(self, triangles: List) -> None:
                for triangle in triangles:
                    I_points = []

                    for C_point in triangle.camera_points:
                        I_point = np.matmul(self.I_T_C, C_point)
                        
                        u = int(I_point[0] / I_point[2])
                        v = int(I_point[1] / I_point[2])

                        I_points.append((u, v))
                    
                    Poly_Points = np.array(I_points, np.int32)
                    cv.fillPoly(self.camera_image, [Poly_Points], triangle.color)

------------------------------------------------------------------------------------

    .. method:: draw_poly(points: List[np.array]) -> None

        Draws a polygon defined by a list of points on the camera image.
        **Parameters:**

        - `points`: A list of points representing the polygon.

        .. code-block:: python
            :caption: :mod:`draw_poly` method

            def draw_poly(self, points: List[np.array]) -> None:

                I_points = []

                for point in points:

                    I_point = np.matmul(self.I_T_C, point)
                        
                    u = int(I_point[0] / I_point[2])
                    v = int(I_point[1] / I_point[2])

                    I_points.append((u, v))
                    
                Poly_Points = np.array(I_points, np.int32)
                hull = cv.convexHull(Poly_Points)
                cv.fillPoly(self.camera_image, [hull], (50,50,50))
