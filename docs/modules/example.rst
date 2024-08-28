.. _example:


Let's go through an example of how Cartesian and homogeneous coordinates are used in 3D graphics, focusing on a simple operation: **translating a point**.

Example: Translating a Point in 3D Space
=========================================

Using Cartesian Coordinates
---------------------------

Suppose you have a point :math:`P` at coordinates :math:`(2, 3, 4)` in a 3D space. You want to translate this point by a vector :math:`T = (1, 2, 3)`, meaning you want to move the point 1 unit along the X-axis, 2 units along the Y-axis, and 3 units along the Z-axis.

- **Step 1:** Represent the point and the translation vector:

  - Point :math:`P`: :math:`(2, 3, 4)`

  - Translation vector :math:`T`: :math:`(1, 2, 3)`

- **Step 2:** Apply the translation by adding the translation vector to the point:

  .. math::

     P' = P + T = (2+1, 3+2, 4+3) = (3, 5, 7)

  The new point after translation is :math:`P' = (3, 5, 7)`.

This method works fine, but it requires you to separately add the translation vector. If you want to also rotate or scale the point, you would need to apply those transformations separately and in a specific order.

Using Homogeneous Coordinates
-----------------------------

Now, let's use homogeneous coordinates to achieve the same translation.

- **Step 1:** Convert the point :math:`P` into homogeneous coordinates by adding a fourth component, which is typically 1:

  .. math::

     P_h = (2, 3, 4, 1)

- **Step 2:** Define the translation matrix :math:`M_T` that will move the point by the translation vector :math:`(1, 2, 3)`:

  .. math::

     M_T = 
     \begin{pmatrix}
     1 & 0 & 0 & 1 \\
     0 & 1 & 0 & 2 \\
     0 & 0 & 1 & 3 \\
     0 & 0 & 0 & 1 \\
     \end{pmatrix}

- **Step 3:** Apply the translation by multiplying the point’s homogeneous coordinates by the translation matrix:

  .. math::

     P_h' = M_T \times P_h = 
     \begin{pmatrix}
     1 & 0 & 0 & 1 \\
     0 & 1 & 0 & 2 \\
     0 & 0 & 1 & 3 \\
     0 & 0 & 0 & 1 \\
     \end{pmatrix}
     \times
     \begin{pmatrix}
     2 \\
     3 \\
     4 \\
     1 \\
     \end{pmatrix}
     = 
     \begin{pmatrix}
     3 \\
     5 \\
     7 \\
     1 \\
     \end{pmatrix}

  The result :math:`P_h' = (3, 5, 7, 1)` gives the new position of the point after translation. The :math:`w` component remains 1, so the Cartesian coordinates of the new point are :math:`(3, 5, 7)`, exactly the same as we found using Cartesian coordinates.
