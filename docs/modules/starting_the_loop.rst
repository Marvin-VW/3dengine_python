.. _starting_the_loop:

Starting the Loop
=====================

Now we're at the beginning of the main loop. First, we handle the movement, then update the FPS counter, and finally reset the camera image.

In this module we are dealing with the following code snippet of the Engine Loop:


    .. code-block:: python
        :caption: :mod:`main` method
        :linenos:

        def main(self):

            ...

                self.window.handle_movement()
                self.fps_counter.update()
                self.camera_model.reset_camera_image()
                ...

Let's dive into the detailed explanations of the implementation.

------------------------------------------------------------------------------------------------


.. method:: handle_movement()

    The :mod:`handle_movement` method manages the camera's movement in response to keyboard inputs.

    .. code-block:: python
        :caption: :mod:`handle_movement` method

        def handle_movement(self):
            camera_speed = 100
            current_time = time.time()
            if current_time - self.last_update_time >= self.update_interval:
                self.last_update_time = current_time
                
                key = cv.waitKey(30) & 0xFF
            
                if key == ord('d'):
                    self.move_camera('forward', camera_speed)
                if key == ord('a'):
                    self.move_camera('backward', camera_speed)
                if key == ord('w'):
                    self.move_camera('left', camera_speed)
                if key == ord('s'):
                    self.move_camera('right', camera_speed)
                if key == ord('q'):
                    self.move_camera('down', camera_speed)
                if key == ord('e'):
                    self.move_camera('up', camera_speed)


--------------------------------------------------------------------------------------------------------------

.. method:: move_camera()

    The :mod:`move_camera` method calculates the direction vectors based on the camera's current yaw and pitch and updates the camera's position accordingly.

    .. note::
        This way, the camera movement using W, A, S, and D is not influenced by the direction you're looking at.

    .. code-block:: python
        :caption: :mod:`move_camera` method

        def move_camera(self, direction, speed):
            # Calculate vectors
            yaw = np.deg2rad(self.camera_system_rotation_yaw / 10.0)
            pitch = np.deg2rad(self.camera_system_rotation_pitch / 10.0)

            forward_x = np.cos(pitch) * np.cos(yaw)
            forward_y = np.cos(pitch) * np.sin(yaw)
            forward_z = np.sin(pitch)

            right_x = np.sin(yaw)
            right_y = -np.cos(yaw)
            right_z = 0

            up_x = 0
            up_y = 0
            up_z = 1

            if direction == 'forward':
                self.camera_system_translation_x += int(forward_x * speed)
                self.camera_system_translation_y += int(forward_y * speed)
                self.camera_system_translation_z += int(forward_z * speed)
            elif direction == 'backward':
                self.camera_system_translation_x -= int(forward_x * speed)
                self.camera_system_translation_y -= int(forward_y * speed)
                self.camera_system_translation_z -= int(forward_z * speed)
            elif direction == 'left':
                self.camera_system_translation_x -= int(right_x * speed)
                self.camera_system_translation_y -= int(right_y * speed)
            elif direction == 'right':
                self.camera_system_translation_x += int(right_x * speed)
                self.camera_system_translation_y += int(right_y * speed)
            elif direction == 'up':
                self.camera_system_translation_z += int(up_z * speed)
            elif direction == 'down':
                self.camera_system_translation_z -= int(up_z * speed)
                
            self.camera_system_translation_x = np.clip(self.camera_system_translation_x, 0, 20000)
            self.camera_system_translation_y = np.clip(self.camera_system_translation_y, 0, 20000)
            self.camera_system_translation_z = np.clip(self.camera_system_translation_z, 0, 20000)
            cv.setTrackbarPos("X", self.camera_window_name, self.camera_system_translation_x)
            cv.setTrackbarPos("Y", self.camera_window_name, self.camera_system_translation_y)
            cv.setTrackbarPos("Z", self.camera_window_name, self.camera_system_translation_z)

---------------------------------------------------------------------------------------------------------------

.. method:: mouse_event_handler()

    The :mod:`mouse_event_handler` method handles the mouse interactions with the window, allowing users to rotate the camera view by dragging or clicking inside the window by right-click.

    .. note:: 
        With the left click, you can drag your view like on Google Maps. With the right click, your mouse movement will control the camera, and a double right-click will exit this mode.

    .. code-block:: python
        :caption: :mod:`mouse_event_handler` method

        def mouse_event_handler(self, event, x, y, flags, param):
            if event == cv.EVENT_LBUTTONDOWN:
                self.mouse_is_pressed = True
                self.last_mouse_position = (x, y)
            elif event == cv.EVENT_LBUTTONUP:
                self.mouse_is_pressed = False
            elif event == cv.EVENT_RBUTTONDOWN:
                self.right_button_mode = True
            elif event == cv.EVENT_RBUTTONDBLCLK:
                self.right_button_mode = False
                self.last_mouse_position = (x, y)
            elif event == cv.EVENT_MOUSEMOVE:
                if self.mouse_is_pressed or self.right_button_mode:
                    dx = x - self.last_mouse_position[0]
                    dy = y - self.last_mouse_position[1]
                    self.camera_system_rotation_yaw += dx
                    self.camera_system_rotation_roll += dy 
                    if self.camera_system_rotation_yaw > 3600:
                        self.camera_system_rotation_yaw -= 3599
                    if self.camera_system_rotation_roll > 3600:
                        self.camera_system_rotation_roll -= 3599
                    if self.camera_system_rotation_yaw < 0:
                        self.camera_system_rotation_yaw += 3599
                    if self.camera_system_rotation_roll < 0:
                        self.camera_system_rotation_roll += 3599
                    cv.setTrackbarPos("Yaw", self.camera_window_name, self.camera_system_rotation_yaw)
                    cv.setTrackbarPos("Roll", self.camera_window_name, self.camera_system_rotation_roll)
                    self.last_mouse_position = (x, y)


------------------------------------------------------------------------------------------------

    .. method:: fps_counter.update()

    - The method updates the current FPS value. It calculates the time difference between the last update and the current one to determine the FPS:
        
        - `delta_time`: Time difference between the current and the last frame.
        - `fps`: Calculated as `1.0 / delta_time`, representing the frames per second.

    .. code-block:: python
        :caption: :mod:`fps_counter.update` method

        def update(self) -> None:
            timestamp = time.time()
            delta_time = timestamp - self.last_timestamp
            self.last_timestamp = timestamp
            try:
                self.fps = 1.0 / delta_time
            except:
                self.fps = 0
            self.fps_history.append(self.fps)
            if len(self.fps_history) > self.filter_window_size:
                self.fps_history.pop(0)

------------------------------------------------------------------------------------------------

Lastly, in this module, we resets the camera image to a blank (white) image.

    .. method:: reset_camera_image()

    .. code-block:: python
        :caption: :mod:`reset_camera_image` method

        def reset_camera_image(self) -> None:
            self.camera_image.fill(255)