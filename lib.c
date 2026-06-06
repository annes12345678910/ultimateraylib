#define RAYGUI_IMPLEMENTATION
#include "raylib.h"
#include "raygui.h"
#include "raymath.h"
#define RLIGHTS_IMPLEMENTATION
#include "rlights.h"

#ifdef _WIN32
#define dea __declspec(dllexport) __attribute__((used))
#else
#define dea
#endif

dea void poop() {
    TraceLog(LOG_WARNING, "oh yea");
}