# Snake_game
Snake Game using Inheritance and OOPs Concepts
This Python project implements the popular Snake game using inheritance and OOPs concepts. The game is built using four classes, which use conditional loops and lists to create a functioning game. The turtle graphics library is used to create the game's graphics.

Prerequisites
To run this project, you need to have the following installed on your computer:

Python 3.x
Turtle Graphics Library
How to Run
To run the game, simply run the main.py file using Python 3. The game will start automatically, and you can use the arrow keys to control the snake.

Classes
This project uses four classes to implement the game:

Snake: This class represents the snake in the game. It uses a list to keep track of the snake's body, and it has methods to move the snake, check if it has collided with anything, and grow the snake when it eats food.

Food: This class represents the food that the snake needs to eat to grow. It has methods to generate random positions for the food and to check if the snake has eaten it.

Scoreboard: This class keeps track of the player's score and displays it on the screen.

Game: This class controls the overall game flow. It initializes the snake, food, and scoreboard objects, and it has methods to handle key presses, update the game, and check if the game is over.

How it Works
When the game starts, the Game class initializes the Snake, Food, and Scoreboard objects. It then enters a loop where it continuously updates the game state and redraws the screen.

On each iteration of the loop, the Game class checks for key presses and moves the snake accordingly. It also checks if the snake has collided with anything (such as the edge of the screen or its own body), and it updates the score and generates new food as needed.

When the game is over (i.e., the snake has collided with something), the Game class displays a game over message and waits for the player to press a key to restart the game.

Conclusion
This Python project demonstrates how inheritance and OOPs concepts can be used to implement a simple game. By using classes to represent the different elements of the game (snake, food, scoreboard, etc.), the code becomes more organized and easier to read and maintain. The use of conditional loops and lists allows for more complex game logic, while the turtle graphics library provides a simple way to create graphics in Python
