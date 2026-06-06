from setup import *

screenWidth = 800
screenHeight = 450

rl.init_window(screenWidth, screenHeight, "raylib [models] example - loading gltf")

camera = rl.make_camera(
    rl.Vector3(6, 6, 6),
    rl.Vector3(0, 2, 0),
    rl.Vector3(0, 1, 0),
    45,
    rl.CAMERA_PERSPECTIVE
)

model = rl.load_model("assets/robot.glb")
position = rl.Vector3( 0,0,0 )

animsCount = 14
animIndex = 0
animCurrentFrame = 0
modelAnimations = rl.load_model_animations("assets/robot.glb")

rl.set_target_fps(60)

while not rl.window_should_close():
    rl.update_camera(camera, rl.CAMERA_ORBITAL)
    '''
        if (IsMouseButtonPressed(MOUSE_BUTTON_RIGHT)) animIndex = (animIndex + 1)%animsCount;
        else if (IsMouseButtonPressed(MOUSE_BUTTON_LEFT)) animIndex = (animIndex + animsCount - 1)%animsCount;

        // Update model animation
        ModelAnimation anim = modelAnimations[animIndex];
        animCurrentFrame = (animCurrentFrame + 1)%anim.frameCount;
        UpdateModelAnimation(model, anim, animCurrentFrame);
    '''

    if rl.is_mouse_button_pressed(rl.MOUSE_BUTTON_RIGHT):
        animIndex = (animIndex + 1)%animsCount
    elif rl.is_mouse_button_pressed(rl.MOUSE_BUTTON_LEFT):
        animIndex = (animIndex + animsCount - 1)%animsCount
    
    anim = modelAnimations[animIndex]
    animCurrentFrame = (animCurrentFrame + 1)%anim.frameCount
    rl.update_model_animation(model, anim, animCurrentFrame)

    '''
            BeginDrawing();

            ClearBackground(RAYWHITE);

            BeginMode3D(camera);
                DrawModel(model, position, 1.0f, WHITE);    // Draw animated model
                DrawGrid(10, 1.0f);
            EndMode3D();

            DrawText("Use the LEFT/RIGHT mouse buttons to switch animation", 10, 10, 20, GRAY);
            DrawText(TextFormat("Animation: %s", anim.name), 10, GetScreenHeight() - 20, 10, DARKGRAY);

        EndDrawing();
    '''
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)

    rl.begin_mode_3d(camera)
    rl.draw_model(model, position, 1,rl.WHITE)
    rl.draw_grid(10, 1)
    rl.end_mode_3d()

    rl.draw_text("Use the LEFT/RIGHT mouse buttons to switch animation", 10, 10, 20, rl.GRAY)
    rl.draw_text(f"Animation: {anim.name.decode()}", 10, rl.get_screen_height() - 20, 10, rl.DARKGRAY)

    rl.end_drawing()

rl.close_window()