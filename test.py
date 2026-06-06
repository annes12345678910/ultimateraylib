import ultimateraylib as rl
import ultimateraylib.light as rll
import random

screenWidth = 800
screenHeight = 450

rl.set_config_flags(rl.FLAG_MSAA_4X_HINT)
rl.set_config_flags(rl.FLAG_WINDOW_RESIZABLE)
rl.init_window(screenWidth, screenHeight, "raylib [shaders] example - basic lighting")

camera = rl.make_camera(
    rl.Vector3(2, 4, 6),
    rl.Vector3(0, 0.5, 0),
    rl.Vector3(0, 1, 0),
    45,
    rl.CAMERA_PERSPECTIVE
)

shader = rl.load_shader("resources/lighting.vs", "resources/lighting.fs")

shader.locs[rl.SHADER_LOC_VECTOR_VIEW] = rl.get_shader_location(shader, "viewPos")

ambientLoc = rl.get_shader_location(shader, "ambient")
rl.set_shader_value(shader, ambientLoc, [0.1, 0.1, 0.1, 1], rl.SHADER_UNIFORM_VEC4)

lights: list[rll.Light] = []

lights.append(rll.create_light(rll.LIGHT_DIRECTIONAL, rl.Vector3(random.randint(-10, 10), 1, random.randint(-10, 10)), rl.Vector3(0,0,0), rl.WHITE, shader))

rl.set_target_fps(60)

doobig = rl.load_model("ramen.glb")
#doobig.materials[1].shader = shader

for i in range(doobig.materialCount):
    doobig.materials[i].shader = shader

#py_list = [doobig.materials[i] for i in range(doobig.materialCount)]
#print(py_list)

while not rl.window_should_close():
    print(rl.is_gamepad_button_down(0, 7))
    rl.update_camera(camera, rl.CAMERA_THIRD_PERSON)

    rl.set_mouse_position(100, 100) if not rl.is_key_down(rl.KEY_M) else None

    #lights[1].position = camera.position
    cameraPos = [camera.position.x, camera.position.y, camera.position.z]
    rl.set_shader_value(shader, shader.locs[rl.SHADER_LOC_VECTOR_VIEW], cameraPos, rl.SHADER_UNIFORM_VEC3)

    if rl.is_key_pressed(rl.KEY_SPACE): lights[0].enabled = not lights[0].enabled
    #if rl.is_key_pressed(rl.KEY_G): lights[1].enabled = not lights[1].enabled

    for i in lights:
        rll.update_light_values(shader, i)
    
    rl.begin_drawing()

    rl.clear_background(rl.RAYWHITE)

    rl.begin_mode_3d(camera)
    rl.begin_shader_mode(shader)

    rl.draw_plane(rl.Vector3(0,0,0), rl.Vector2(100, 100), rl.RED)
    rl.draw_cube(rl.Vector3(0,0,0), 1, 1, 1, rl.ORANGE)
    rl.draw_model(doobig, rl.Vector3(1, 0, 1), 1, rl.WHITE)

    rl.end_shader_mode()
    rl.end_mode_3d()

    rl.end_drawing()
