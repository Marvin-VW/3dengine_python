.. _import_module:

OBJ_Importer Module
===================

This module contains the classes and functions related to handling 4D objects and importing them from OBJ files.

In this module we are dealing with the following **optional** code snippet of the Engine Loop:


    .. code-block:: python
        :caption: :mod:`main` method
        :linenos:

        def main(self):

            ...

            file_path = r"utils\resources\VideoShip.obj"
            struc = Structure_Generator.load_from_obj(file_path)
            self.mesh_list.extend(struc)

            ...

.. note::
    The `Triangle4D` class is defined in the :ref:`Shape Module <shape_module>`.


The :mod:`OBJ_Importer` class provides methods to import 3D vertices and faces from an OBJ file and create corresponding 4D points and triangles.
If the OBJ file is structured as a triangle mesh, the file contains :mod:`v` entries representing the vertices of an object. It also contains :mod:`f` entries, which represent faces. These faces contain numbers referring to the vertices, allowing a vertex to be reused multiple times.
.. class:: OBJ_Importer


    .. method:: load_from_obj(filename: str) -> list

        This method loads a 3D model from an OBJ file and converts the vertices and faces into 4D points and triangles.

        **Parameters**:
          - `filename (str)`: The path to the OBJ file.

        **Returns**:
          - `list`: A list of `Triangle4D` objects representing the 3D model.

        **Example Usage**:
        
        .. code-block:: python
            :emphasize-lines: 4
            
            from utils.shape import Triangle4D
            import numpy as np
            
            tris = OBJ_Importer.load_from_obj("path/to/model.obj")
            for tri in tris:
                print(tri)


        **Full Code**:

        .. code-block:: python

                @staticmethod
                def load_from_obj(filename):
                    try:
                        with open(filename, 'r') as f:
                            verts = []
                            tris = []

                            for line in f:
                                if line.startswith('v '):
                                    parts = line.strip().split()
                                    v = OBJ_Importer.create_point(float(parts[1]), float(parts[2]), float(parts[3]))
                                    verts.append(v)

                                if line.startswith('f '):
                                    parts = line.strip().split()
                                    f = [int(parts[1]), int(parts[2]), int(parts[3])]
                                    tris.append(Triangle4D(verts[f[0] - 1], verts[f[1] - 1], verts[f[2] - 1]))

                            return tris
                        
                    except Exception as e:
                        print(f"Failed to load {e}")
                        
        .. warning::
            Ensure that the OBJ file is well-formatted and contains only triangular faces. Check the :mod:`Triangulated Mesh` option on how to export `Wavefront OBJ Blender <https://docs.blender.org/manual/en/latest/files/import_export/obj.html>`_ 