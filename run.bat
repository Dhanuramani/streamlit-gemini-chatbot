@echo off
echo Compiling Student Management System...
javac *.java

if %errorlevel% equ 0 (
    echo Compilation successful!
    echo.
    echo Starting Student Management System...
    echo.
    java StudentManagementSystem
) else (
    echo Compilation failed!
    pause
)