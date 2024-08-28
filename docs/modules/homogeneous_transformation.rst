.. _homogeneous_module:

Homogeneous Transformation Module
=================================

These Module allow us to allows us to transform objects within our 3D space. This module combines translation, rotation, and scaling into a single matrix operation.


- **Translation Matrix**: Moves the object in 3D space by shifting its position along the x, y, and z axes.


   .. image:: ../resources/matrix/translation_matrix.png
    :width: 800

- **Rotation Matrices**: Three separate matrices for rotating the object around the roll, pitch, and yaw axes (corresponding to rotations around the x, y, and z axes).
   
    .. image:: ../resources/matrix/real_rotation.png
        :width: 800

- **Scale Matrix**: Scales the object uniformly along all axes, which is especially useful for resizing objects in a 3D scene.
    
    .. image:: ../resources/matrix/scaling_matrix.png
        :width: 800

------------------------------------------------------------------------------------------------------------------------

The following code snippets implement the creation of a homogeneous transformation matrix and its application to a camera system and a 3D cube:

.. method:: create_homogeneous_transformation_matrix()

    .. code-block:: python
        :caption: :mod:`Matrix_Functions` class
        :linenos:

        def create_homogeneous_transformation_matrix(
                translation_x: float, translation_y: float, translation_z: float,
                rotation_roll: float, rotation_pitch: float, rotation_yaw: float, 
                scale: int) -> np.array:

            rotation_matrix_roll = np.array([
                [1, 0, 0, 0],
                [0, cos(rotation_roll), -sin(rotation_roll), 0],
                [0, sin(rotation_roll), cos(rotation_roll), 0],
                [0, 0, 0, 1]
            ])

            rotation_matrix_pitch = np.array([
                [cos(rotation_pitch), 0, sin(rotation_pitch), 0],
                [0, 1, 0, 0],
                [-sin(rotation_pitch), 0, cos(rotation_pitch), 0],
                [0, 0, 0, 1]
            ])

            rotation_matrix_yaw = np.array([
                [cos(rotation_yaw), -sin(rotation_yaw), 0, 0],
                [sin(rotation_yaw), cos(rotation_yaw), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])

            translation_matrix = np.array([
                [1, 0, 0, translation_x],
                [0, 1, 0, translation_y],
                [0, 0, 1, translation_z],
                [0, 0, 0, 1]
            ])

            if scale == 0:
                scale = 1

            scale_matrix = np.array([
                [scale, 0, 0, 0],
                [0, scale, 0, 0],
                [0, 0, scale, 0],
                [0, 0, 0, 1]
            ])

            transformation_matrix = np.matmul(
                translation_matrix,
                np.matmul(
                    scale_matrix,
                    np.matmul(
                        rotation_matrix_yaw,
                        np.matmul(rotation_matrix_pitch, rotation_matrix_roll)
                    )
                )
            )
            return transformation_matrix


These matrices are multiplied in a specific order to generate one final :mod:`transformation matrix`.

Each time the loop runs, it calls the homogeneous_transformation method. This method grabs the slider/input parameters and uses them as arguments to create an instance of the 
:mod:`transformation matrix` (e.g., V_T_C, C_T_V, V_T_Cube).

------------------------------------------------------------------------------------------------------------------------

.. method:: homogeneous_transformation Method()

    .. code-block:: python
        :caption: :mod:`Matrix_Functions` class
        :linenos:

        def homogeneous_transformation(cls, window):
        V_T_C = cls.create_homogeneous_transformation_matrix(
            (window.get_camera_system_translation_x() - 10000) / 1000.0,
            (window.get_camera_system_translation_y() - 10000) / 1000.0,
            (window.get_camera_system_translation_z() - 10000) / 1000.0,
            cls.DEG_TO_RAD(window.get_camera_system_rotation_roll() / 10.0),
            cls.DEG_TO_RAD(window.get_camera_system_rotation_pitch() / 10.0),
            cls.DEG_TO_RAD(window.get_camera_system_rotation_yaw() / 10.0),
            1
        )


        C_T_V = np.linalg.inv(V_T_C)

        V_T_Cube = cls.create_homogeneous_transformation_matrix(
            (window.get_cube_system_translation_x() - 10000) / 1000.0,
            (window.get_cube_system_translation_y() - 10000) / 1000.0,
            (window.get_cube_system_translation_z() - 10000) / 1000.0,
            cls.DEG_TO_RAD(window.get_cube_system_rotation_roll() / 10.0),
            cls.DEG_TO_RAD(window.get_cube_system_rotation_pitch() / 10.0),
            cls.DEG_TO_RAD(window.get_cube_system_rotation_yaw() / 10.0),
            window.get_cube_system_scale()
        )

        return V_T_C, C_T_V, V_T_Cube

This class method generates the homogeneous transformation matrix to both the camera system and a 3D cube within the scene.

- **Camera System**: The camera's transformation matrix (:mod:`V_T_C`) is used to position and rotate the camera but also to convert world space points into camera space. The inverse matrix (:mod:`C_T_V`) allows objects to be transformed from camera space back to world space.

- **Object Transformation** : The cube's transformation matrix (:mod:`V_T_Cube`) is applied to the 3D cube to position, rotate, and scale it within the scene relative to the camera's viewpoint. It is also later used to convert points from world space to cube space, and cube to world space using its inverse.