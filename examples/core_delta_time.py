from setup import *

rl.init_window(800, 450, "raylib [core] example - delta time")



delta_circle = rl.Vector2(
    0, 450 / 3
)
frame_circle = rl.Vector2(
    0, 450 * (2/3)
)
speed = 10
circle_radius = 32
current_fps = 60
rl.set_target_fps(current_fps)
while not rl.window_should_close():
    mouse_wheel = rl.get_mouse_wheel_move()
    if mouse_wheel != 0:
        current_fps += mouse_wheel
        if current_fps < 0: current_fps = 0
        rl.set_target_fps(int(current_fps))
    
    delta_circle.x += rl.get_frame_time()*6*speed
    frame_circle.x += 0.1*speed
    if (delta_circle.x > 800): delta_circle.x = 0
    if (frame_circle.x > 800): frame_circle.x = 0
    if rl.is_key_pressed(rl.KEY_R):
        delta_circle.x = 0
        frame_circle.x = 0
    
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)
    rl.draw_circle_v(delta_circle, circle_radius, rl.RED)
    rl.draw_circle_v(frame_circle, circle_radius, rl.BLUE)

    fps_text = ""
    if current_fps <= 0: fps_text = f"FPS: unlimited ({rl.get_fps()})"
    else: fps_text = f"FPS: {rl.get_fps()} (target: {current_fps})"

    rl.draw_text(fps_text, 10, 10, 20, rl.DARKGRAY)
    rl.draw_text(f"Frame time: {rl.get_frame_time():.2f}", 10, 30, 20, rl.DARKGRAY)
    rl.draw_text("Use the scroll wheel to change the fps limit, r to reset", 10, 50, 20, rl.DARKGRAY)

    rl.draw_text("FUNC: x += rl.get_frame_time()*speed", 10, 90, 20, rl.RED)
    rl.draw_text("FUNC: x += speed", 10, 240, 20, rl.BLUE)
    
    rl.end_drawing()
rl.close_window()