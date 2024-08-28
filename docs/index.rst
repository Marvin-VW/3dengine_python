==============================
Basic 3D Engine Python
==============================

.. image:: /resources/space/world_space.png
  :width: 800

This project is a 3D engine written in Python using OpenCV and NumPy. The engine includes features such as backface culling, object clipping, basic lighting, and FPS calculation. Below, you will find comprehensive documentation covering the various modules and classes used in this project.

.. note::

   This project is under development.

Getting Started
===============

Before diving into the details, make sure to follow the setup instructions in the installation guide.

.. toctree::
   :maxdepth: 1

   installation

Understanding the Render Pipeline
=================================

For a better grasp of how this 3D engine works, check out the render pipeline. It outlines the step-by-step process that the engine follows to transform and render 3D objects onto the screen.

.. toctree::
   :maxdepth: 1

   modules/3dengine_theo
   modules/example
   pipeline

Exploring the Modules
=====================

If you're interested in understanding the inner workings of the engine, take a deeper look into the documentation for each module. These sections will provide detailed explanations of the core components, including shapes, camera models, matrix transformations, and more.

.. toctree::
   :maxdepth: 1

   modules/init
   modules/importer
   modules/starting_the_loop
   modules/homogeneous_transformation
   modules/backface_culling
   modules/lighting_calculations
   modules/depth_sorting
   modules/shadow
   modules/clipping
   modules/rendering
   modules/display

Indices and Tables
==================

Use the indices and search functionality to quickly locate specific information within the documentation.
