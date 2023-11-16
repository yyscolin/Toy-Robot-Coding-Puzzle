# Toy Robot Coding Puzzle

This is a solution for the challenge posted in the blog post (https://joneaves.wordpress.com/2014/07/21/toy-robot-coding-test/).

## Description
. The application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units.<br>
. There are no other obstructions on the table surface.<br>
. The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement
that would result in the robot falling from the table must be prevented, however further valid movement commands must still
be allowed.

. Create an application that can read in commands of the following form:<br>
PLACE X,Y,F<br>
MOVE<br>
LEFT<br>
RIGHT<br>
REPORT

. PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.<br>
. The origin (0,0) can be considered to be the SOUTH WEST most corner.<br>
. The first valid command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed.<br>
. MOVE will move the toy robot one unit forward in the direction it is currently facing.<br>
. LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.<br>
. REPORT will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient.<br>
. A robot that is not on the table can choose the ignore the MOVE, LEFT, RIGHT and REPORT commands.<br>
. Input can be from a file, or from standard input, as the developer chooses.<br>
. Provide test data to exercise the application.

## Constraints
The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot.<br>
Any move that would cause the robot to fall must be ignored.

## Solution
Software: Python 3.10.12<br>
Functional: toy_robot.py<br>
OOP: toy_tobot_oop.py

### To run the program
`py toy_robot.py`<br>
`python3 toy_robot.py`

The program will prompt you for inputs.

### To exit the program
press `ctrl + c`

## Example Input and Output:
a)<br>
PLACE 0,0,NORTH<br>
MOVE<br>
REPORT<br>
Output: 0,1,NORTH<br>

b)<br>
PLACE 0,0,NORTH<br>
LEFT<br>
REPORT<br>
Output: 0,0,WEST<br>

c)<br>
PLACE 1,2,EAST<br>
MOVE<br>
MOVE<br>
LEFT<br>
MOVE<br>
REPORT<br>
Output: 3,3,NORTH
