# Copyright (C) 2024 twyleg, Daniel-VW, Marvin-VW
import cv2 as cv
import numpy as np
import time


class Window:

    def __init__(self):
        self.camera_system_translation_x = 10000
        self.camera_system_translation_y = 13000
        self.camera_system_translation_z = 3000
        self.camera_system_rotation_roll = 1500
        self.camera_system_rotation_pitch = 1800
        self.camera_system_rotation_yaw = 0

        self.cube_system_translation_x = 10000
        self.cube_system_translation_y = 10000
        self.cube_system_translation_z = 10000
        self.cube_system_rotation_roll = 0
        self.cube_system_rotation_pitch = 500
        self.cube_system_rotation_yaw = 0
        self.cube_system_scale = 1

        self.camera_window_name = "camera settings"
        self.cube_window_name = "cube settings"

        self.mouse_is_pressed = False
        self.right_button_mode = False
        self.last_mouse_position = (0, 0)

        self.last_update_time = time.time()
        self.update_interval = 0.05
        
        self.show_normals = False
        self.show_planes = False
        self.show_points = False

        self.window_creator()
    
    def window_creator(self):
        cv.namedWindow("image window", cv.WINDOW_AUTOSIZE)
        cv.namedWindow("camera settings", cv.WINDOW_NORMAL)
        cv.namedWindow("cube settings", cv.WINDOW_NORMAL)
        cv.resizeWindow("camera settings", 400, 300)
        cv.resizeWindow("cube settings", 400, 300)

        cv.createTrackbar("X", "camera settings", 0, 20000, self.nothing)
        cv.createTrackbar("Y", "camera settings", 0, 20000, self.nothing)
        cv.createTrackbar("Z", "camera settings", 0, 20000, self.nothing)
        cv.createTrackbar("Roll", "camera settings", 0, 3600, self.nothing)
        cv.createTrackbar("Pitch", "camera settings", 0, 3600, self.nothing)
        cv.createTrackbar("Yaw", "camera settings", 0, 3600, self.nothing)

        cv.createTrackbar("X", "cube settings", 0, 20000, self.nothing)
        cv.createTrackbar("Y", "cube settings", 0, 20000, self.nothing)
        cv.createTrackbar("Z", "cube settings", 0, 20000, self.nothing)
        cv.createTrackbar("Roll", "cube settings", 0, 3600, self.nothing)
        cv.createTrackbar("Pitch", "cube settings", 0, 3600, self.nothing)
        cv.createTrackbar("Yaw", "cube settings", 0, 3600, self.nothing)
        cv.createTrackbar("Scale", "cube settings", 1, 10, self.nothing)

        cv.createTrackbar("Normals", "cube settings", 0, 1, self.toggle_normal)
        cv.createTrackbar("Planes", "cube settings", 0, 1, self.toggle_planes)
        cv.createTrackbar("Points", "cube settings", 0, 1, self.toggle_points)


        # Set initial positions of the trackbars
        cv.setTrackbarPos("X", "camera settings", self.camera_system_translation_x)
        cv.setTrackbarPos("Y", "camera settings", self.camera_system_translation_y)
        cv.setTrackbarPos("Z", "camera settings", self.camera_system_translation_z)
        cv.setTrackbarPos("Roll", "camera settings", self.camera_system_rotation_roll)
        cv.setTrackbarPos("Pitch", "camera settings", self.camera_system_rotation_pitch)
        cv.setTrackbarPos("Yaw", "camera settings", self.camera_system_rotation_yaw)

        cv.setTrackbarPos("X", "cube settings", self.cube_system_translation_x)
        cv.setTrackbarPos("Y", "cube settings", self.cube_system_translation_y)
        cv.setTrackbarPos("Z", "cube settings", self.cube_system_translation_z)
        cv.setTrackbarPos("Roll", "cube settings", self.cube_system_rotation_roll)
        cv.setTrackbarPos("Pitch", "cube settings", self.cube_system_rotation_pitch)
        cv.setTrackbarPos("Yaw", "cube settings", self.cube_system_rotation_yaw)
        cv.setTrackbarPos("Scale", "cube settings", self.cube_system_scale)

        cv.setTrackbarPos("Normals", "cube settings", 0)
        cv.setTrackbarPos("Planes", "cube settings", 1)
        cv.setTrackbarPos("Points", "cube settings", 0)


    def toggle_normal(self, value):
        self.show_normals = not self.show_normals

    def toggle_planes(self, value):
        self.show_planes = not self.show_planes

    def toggle_points(self, value):
        self.show_points = not self.show_points

    def window_show(self, class_cam):
        cv.imshow("image window", class_cam.camera_image)
        cv.waitKey(1)

    def get_camera_system_translation_x(self):
        return cv.getTrackbarPos("X", self.camera_window_name)

    def get_camera_system_translation_y(self):
        return cv.getTrackbarPos("Y", self.camera_window_name)

    def get_camera_system_translation_z(self):
        return cv.getTrackbarPos("Z", self.camera_window_name)

    def get_camera_system_rotation_roll(self):
        return cv.getTrackbarPos("Roll", self.camera_window_name)

    def get_camera_system_rotation_pitch(self):
        return cv.getTrackbarPos("Pitch", self.camera_window_name)

    def get_camera_system_rotation_yaw(self):
        return cv.getTrackbarPos("Yaw", self.camera_window_name)

    def get_cube_system_translation_x(self):
        return cv.getTrackbarPos("X", self.cube_window_name)

    def get_cube_system_translation_y(self):
        return cv.getTrackbarPos("Y", self.cube_window_name)

    def get_cube_system_translation_z(self):
        return cv.getTrackbarPos("Z", self.cube_window_name)

    def get_cube_system_rotation_roll(self):
        return cv.getTrackbarPos("Roll", self.cube_window_name)

    def get_cube_system_rotation_pitch(self):
        return cv.getTrackbarPos("Pitch", self.cube_window_name)

    def get_cube_system_rotation_yaw(self):
        return cv.getTrackbarPos("Yaw", self.cube_window_name)
    
    def get_cube_system_scale(self):
        return cv.getTrackbarPos("Scale", self.cube_window_name)

    @staticmethod
    def nothing(value):
        pass
