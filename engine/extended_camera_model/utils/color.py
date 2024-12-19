# Copyright (C) 2024 Marvin-VW
import random
import numpy as np
import colorsys

class Color:
    ALICE_BLUE = (255, 248, 240)
    ANTIQUE_WHITE = (215, 235, 250)
    AQUA = (255, 255, 0)
    AQUAMARINE = (212, 255, 127)
    AZURE = (255, 255, 240)
    BEIGE = (220, 245, 245)
    BISQUE = (196, 228, 255)
    BLACK = (0, 0, 0)
    BLANCHED_ALMOND = (205, 235, 255)
    BLUE = (255, 0, 0)
    BLUE_VIOLET = (226, 43, 138)
    BROWN = (42, 42, 165)
    BURLYWOOD = (135, 184, 222)
    CADET_BLUE = (160, 158, 95)
    CHARTREUSE = (0, 255, 127)
    CHOCOLATE = (30, 105, 210)
    CORAL = (80, 127, 255)
    CORNFLOWER_BLUE = (237, 149, 100)
    CORNSILK = (220, 248, 255)
    CRIMSON = (60, 20, 220)
    CYAN = (255, 255, 0)
    DARK_BLUE = (139, 0, 0)
    DARK_CYAN = (139, 139, 0)
    DARK_GOLDENROD = (11, 134, 184)
    DARK_GRAY = (169, 169, 169)
    DARK_GREEN = (0, 100, 0)
    DARK_KHAKI = (107, 183, 189)
    DARK_MAGENTA = (139, 0, 139)
    DARK_OLIVE_GREEN = (47, 107, 85)
    DARK_ORANGE = (0, 140, 255)
    DARK_ORCHID = (204, 50, 153)
    DARK_RED = (0, 0, 139)
    DARK_SALMON = (122, 150, 233)
    DARK_SEA_GREEN = (143, 188, 143)
    DARK_SLATE_BLUE = (139, 61, 72)
    DARK_SLATE_GRAY = (79, 79, 47)
    DARK_TURQUOISE = (209, 206, 0)
    DARK_VIOLET = (211, 0, 148)
    DEEP_PINK = (147, 20, 255)
    DEEP_SKY_BLUE = (255, 191, 0)
    DIM_GRAY = (105, 105, 105)
    DODGER_BLUE = (255, 144, 30)
    FIREBRICK = (34, 34, 178)
    FLORAL_WHITE = (240, 250, 255)
    FOREST_GREEN = (34, 139, 34)
    FUCHSIA = (255, 0, 255)
    GAINSBORO = (220, 220, 220)
    GHOST_WHITE = (255, 248, 248)
    GOLD = (0, 215, 255)
    GOLDENROD = (32, 165, 218)
    GRAY = (128, 128, 128)
    GREEN = (0, 128, 0)
    GREEN_YELLOW = (47, 255, 173)
    HONEYDEW = (240, 255, 240)
    HOT_PINK = (180, 105, 255)
    INDIAN_RED = (92, 92, 205)
    INDIGO = (130, 0, 75)
    IVORY = (240, 255, 255)
    KHAKI = (140, 230, 240)
    LAVENDER = (250, 230, 230)
    LAVENDER_BLUSH = (245, 240, 255)
    LAWNGREEN = (0, 252, 124)
    LEMON_CHIFFON = (205, 250, 255)
    LIGHT_BLUE = (230, 216, 173)
    LIGHT_CORAL = (128, 128, 240)
    LIGHT_CYAN = (255, 255, 224)
    LIGHT_GOLDENROD_YELLOW = (210, 250, 250)
    LIGHT_GRAY = (211, 211, 211)
    LIGHT_GREEN = (144, 238, 144)
    LIGHT_PINK = (193, 182, 255)
    LIGHT_SALMON = (122, 160, 255)
    LIGHT_SEA_GREEN = (170, 178, 32)
    LIGHT_SKY_BLUE = (250, 206, 135)
    LIGHT_SLATE_GRAY = (153, 136, 119)
    LIGHT_STEEL_BLUE = (222, 196, 176)
    LIGHT_YELLOW = (224, 255, 255)
    LIME = (0, 255, 0)
    LIME_GREEN = (50, 205, 50)
    LINEN = (230, 240, 250)
    MAGENTA = (255, 0, 255)
    MAROON = (0, 0, 128)
    MEDIUM_AQUAMARINE = (170, 205, 102)
    MEDIUM_BLUE = (205, 0, 0)
    MEDIUM_ORCHID = (211, 85, 186)
    MEDIUM_PURPLE = (219, 112, 147)
    MEDIUM_SEA_GREEN = (113, 179, 60)
    MEDIUM_SLATE_BLUE = (238, 104, 123)
    MEDIUM_SPRING_GREEN = (154, 250, 0)
    MEDIUM_TURQUOISE = (204, 209, 72)
    MEDIUM_VIOLET_RED = (133, 21, 199)
    MIDNIGHT_BLUE = (112, 25, 25)
    MINT_CREAM = (250, 255, 245)
    MISTY_ROSE = (225, 228, 255)
    MOCCASIN = (181, 228, 255)
    NAVAJO_WHITE = (173, 222, 255)
    NAVY = (128, 0, 0)
    OLD_LACE = (230, 245, 253)
    OLIVE = (0, 128, 128)
    OLIVE_DRAB = (35, 142, 107)
    ORANGE = (0, 165, 255)
    ORANGE_RED = (0, 69, 255)
    ORCHID = (214, 112, 218)
    PALE_GOLDENROD = (170, 232, 238)
    PALE_GREEN = (152, 251, 152)
    PALE_TURQUOISE = (238, 238, 175)
    PALE_VIOLET_RED = (147, 112, 219)
    PAPAYA_WHIP = (213, 239, 255)
    PEACH_PUFF = (185, 218, 255)
    PERU = (63, 133, 205)
    PINK = (203, 192, 255)
    PLUM = (221, 160, 221)
    POWDER_BLUE = (230, 224, 176)
    PURPLE = (128, 0, 128)
    RED = (0, 0, 255)
    ROSY_BROWN = (143, 143, 188)
    ROYAL_BLUE = (225, 105, 65)
    SADDLE_BROWN = (19, 69, 139)
    SALMON = (114, 128, 250)
    SANDY_BROWN = (96, 164, 244)
    SEA_GREEN = (87, 139, 46)
    SEA_SHELL = (238, 245, 255)
    SIENNA = (45, 82, 160)
    SILVER = (192, 192, 192)
    SKY_BLUE = (235, 206, 135)
    SLATE_BLUE = (205, 90, 106)
    SLATE_GRAY = (144, 128, 112)
    SNOW = (250, 250, 255)
    SPRING_GREEN = (127, 255, 0)
    STEEL_BLUE = (180, 130, 70)
    TAN = (140, 180, 210)
    TEAL = (128, 128, 0)
    THISTLE = (216, 191, 216)
    TOMATO = (71, 99, 255)
    TURQUOISE = (208, 224, 64)
    VIOLET = (238, 130, 238)
    WHEAT = (179, 222, 245)
    WHITE = (255, 255, 255)
    WHITE_SMOKE = (245, 245, 245)
    YELLOW = (0, 255, 255)
    YELLOW_GREEN = (50, 205, 154)

    @classmethod
    def RandomColor(cls):
        color_names = [attr for attr in dir(cls) if not callable(getattr(cls, attr))]
        random_color_name = random.choice(color_names)
        return getattr(cls, random_color_name)

    @staticmethod
    def intensity(light_direction, normal):
        norm = np.linalg.norm(light_direction)
        normalized_light_direction = light_direction / norm
        intensity = np.dot(normalized_light_direction, normal) * (-1)
        return intensity
    
    @staticmethod
    def bgr_to_hsl(b, g, r):
        return colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
    
    @staticmethod
    def hsl_to_bgr( h, l, s):
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return int(b * 255), int(g * 255), int(r * 255)

    @staticmethod
    def adjust_bgr_intensity(base_color, intensity):
        B, G, R = base_color
        H, L, S = Color.bgr_to_hsl(B, G, R)
        new_L = L * intensity
        new_B, new_G, new_R = Color.hsl_to_bgr(H, new_L, S)
        return (new_B, new_G, new_R)