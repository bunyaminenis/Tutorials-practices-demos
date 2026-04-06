🐢 Turtle Crossing Game – Frogger Clone in Python
This is a classic Frogger-inspired crossing game built using Python's built-in turtle graphics module. The goal is to help the turtle cross the road while avoiding an increasingly fast stream of cars. The game includes multiple levels, keyboard controls, collision detection, and a simple scoring system.

🎮 Features
Player controls a turtle character with W, A, S, D keys

Randomly generated cars with varying colors

Levels increase as the turtle successfully crosses the road

Collision detection and game over screen

Clean Object-Oriented Programming (OOP) architecture

📁 Project Structure
📦 turtle-crossing/
├── main.py           # Game engine and main loop
├── player.py         # Player class and controls
├── car_manager.py    # Handles car generation and movement
├── scoreboard.py     # Tracks and displays levels and game over

▶️ How to Run
Make sure you have Python 3.x installed. Then:
git clone https://github.com/bunyaminenis/turtle-crossing.git
cd turtle-crossing
python main.py

Use:

W = move up

S = move down

A = move left

D = move right

📌 Requirements
Python 3.x

No external libraries required – uses built-in turtle module

🛠️ Implementation Details
player.py: Manages the player turtle’s movement and finish line logic.

car_manager.py: Generates cars randomly across the y-axis and moves them left. Cars speed up as levels increase.

scoreboard.py: Displays current level and handles the “Game Over” screen.

main.py: Brings everything together. Handles keypresses, game loop, collisions, and level-up logic.

💡 Future Improvements
Add a start menu or difficulty selector

Add sound effects or background music

Create different lanes with different car speeds

Add a leaderboard with high scores
