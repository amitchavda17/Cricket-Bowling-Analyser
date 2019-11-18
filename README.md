# Cricket-Bowling-Analyser


Cricket Bolwing analyser is  a low cost embedded system  that can be used for analysing bolwers perfromance analysis in Cricket.The system is capable of measuring line length and speed of delivery.
The system consist of an  sensor matrix integrated with embedded system for measuring line and length of delivery and uses ultrasonic sensor for measuring the speed of dleivery.
A basic GUI is designed for  providing performance  analysis to user.

## The [Report](https://github.com/amitchavda17/Cricket-Bowling-Analyser/blob/master/Report.pdf) file contians following
* Detail explanation of project with required components and  results  
* Process of designing sensor matrix using velostat with measurments 
* Block diagram for system 
* Schematic Diagram for [PCB](https://github.com/amitchavda17/Cricket-Bowling-Analyser/tree/master/Circuit)
* Circuit diagram for sesnor arduino interfacing

## Code files
* [sensor interfacing](https://github.com/amitchavda17/Cricket-Bowling-Analyser/blob/master/sensor_matrix.ino) this file contains code for data acqusition from sensor matrix and generating results
* [Speed measrument](https://github.com/amitchavda17/Cricket-Bowling-Analyser/blob/master/speed_measurment.ino) code for speed measrument using ultrasonic sensor
* [Live visualization](https://github.com/amitchavda17/Cricket-Bowling-Analyser/blob/master/live_visualization.pde) Processing3 code written in java for visualzing results in real time
* [GUI](https://github.com/amitchavda17/Cricket-Bowling-Analyser/tree/master/GUI) using pyQt in python and webased using html


