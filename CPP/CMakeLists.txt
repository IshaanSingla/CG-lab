cmake_minimum_required(VERSION 4.0)
project(CG_lab)

set(CMAKE_CXX_STANDARD 14)

include_directories(include)
include_directories(include/glad)
include_directories(include/KHR)

add_executable(CG_lab_glad
        glad.c
        test_glad.cpp)

add_executable(CG_lab_glew
        test_glew.cpp)


target_link_libraries(CG_lab_glad
        glfw3
        glew32
        opengl32
        gdi32
        user32
        kernel32
)


target_link_libraries(CG_lab_glew
        glfw3
        glew32
        opengl32
        gdi32
        user32
        kernel32
)

