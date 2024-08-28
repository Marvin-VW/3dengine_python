.. _depth_sorting:

Depth Sorting
=====================

Here we're at the depth sorting module of the main loop. In this module we sort our triangles in the right order.

We are dealing with the following code snippet of the Engine Loop:


    .. code-block:: python
        :caption: :mod:`main` method
        :linenos:

        def main(self):

            ...

                sorted_list = sorted(visiable_triangles, key=lambda triangle: triangle.centroids[2], reverse=True)
                ...

In this line we sort the list visiable_triangles in descending order based on the z component of our triangles. The result is stored in a new list called sorted_list.

.. note::
    Sorting by Z is a simplified method but works well for our purposes. For a professional engine, you would use a pixel shader.