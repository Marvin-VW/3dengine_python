.. _display:

Display
=====================

Now we're at the final module of the main loop, where we build the final window. In this window, we display the FPS counter and the camera image.

.. image:: ../resources/final.png
    :width: 800

In this module we are dealing with the following code snippet of the Engine Loop:


    .. code-block:: python
        :caption: :mod:`main` method
        :linenos:

        def main(self):

            ...

                self.fps_setter()
                self.window.window_show(self.camera_model)
                
                ...

Let's dive into the detailed explanations of the implementation.

------------------------------------------------------------------------------------------------

    .. code-block:: python

        self.fps_setter()

In this line, we set our final fps counter.

    .. method:: fps_setter()
    
    Updates and displays the current frames per second (FPS) on the camera image.

    .. code-block:: python
        :caption: :mod:`fps_setter` method

        def fps_setter(self):
            fps = self.fps_counter.get_fps_filtered()
            cv.putText(self.camera_model.camera_image, f"FPS: {fps:.0f}", (10, 30), cv.FONT_HERSHEY_PLAIN, 1.2, (0, 255, 0), 1)


------------------------------------------------------------------------------------------------

    .. method:: window_show()

    - The method displays the current frame of the camera using the cv2 libary.
    
    .. code-block:: python
        :caption: :mod:`window_show` method

        def window_show(self, class_cam):
            cv.imshow("image window", class_cam.camera_image)
            cv.waitKey(1)