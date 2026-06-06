from setup import *
from ctypes import c_float, cast, c_void_p, byref


GLSL_VERSION = 330

screenWidth = 800
screenHeight = 450

rl.set_config_flags(rl.FLAG_WINDOW_RESIZABLE)
rl.init_window(screenWidth, screenHeight, "raylib [shaders] example - raymarching rendering")

camera = rl.make_camera(
    rl.Vector3(2.5, 2.5, 3),
    rl.Vector3(0,0,0.7),
    rl.Vector3(0,1,0),
    65,
    rl.CAMERA_PERSPECTIVE
)

shader = rl.load_shader("", "assets/raymarching.fs")

viewEyeLoc = rl.get_shader_location(shader, "viewEye")
viewCenterLoc = rl.get_shader_location(shader, "viewCenter")
runTimeLoc = rl.get_shader_location(shader, "runTime")
resolutionLoc = rl.get_shader_location(shader, "resolution")

resolution = (c_float * 2)(screenWidth, screenHeight)

rl.set_shader_value(shader, resolutionLoc, byref(resolution), rl.SHADER_UNIFORM_VEC2)