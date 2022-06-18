# Modelling and control of Piano Keystroke with a Soft Particle Jamming Finger
Hi! This repo includes Yuyi's final year project for Engineering Tripos @Cambridge. 

## Introduction 
We built a robotic finger that performs a human-like piano keystroke! You probably have an image of a robot that is hard, metallic, and moves in choppy motions. This isn't always the case with soft robots. We have a soft finger with particle jamming chambers. It can replicate the way a human plays the piano and push the piano keys with various strengths while being completely passive.

Modelling the movement of soft robots is challenging due to the non-linearity of soft materials. We constructed a mass-spring-damper model for the keystroke action that properly described the movement of the piano key when pressed by varying stiffness soft fingers. You will have a chance to see how the model meets reality in a simple keystroke action made by our soft robotic finger. 

## Documents
* [A guide of soft particle jamming finger fabrication](https://github.com/zhangyuyi99/soft_robot_piano_playing/blob/03de25b16103423019f65ed40931b359439d3d77/particle%20jammed%20soft%20finger%20building%20manual.md)
* [Final report](https://github.com/zhangyuyi99/soft_robot_piano_playing/blob/03de25b16103423019f65ed40931b359439d3d77/Zhang,%20Yuyi_yz655_final_report.pdf)
* [Intermium milestone report](https://github.com/zhangyuyi99/soft_robot_piano_playing/blob/03de25b16103423019f65ed40931b359439d3d77/ZHANG_yz655_TMR_report.pdf)
* [Full poster](https://github.com/zhangyuyi99/soft_robot_piano_playing/blob/03de25b16103423019f65ed40931b359439d3d77/large_poster.pdf)
* [Short poster](https://github.com/zhangyuyi99/soft_robot_piano_playing/blob/03de25b16103423019f65ed40931b359439d3d77/piano%20project%20poster_new.pdf)

## Experiments
The [experiments](https://github.com/zhangyuyi99/soft_robot_piano_playing/tree/main/experiments) folder includes Python code for keystroke data collection, demo music pieces, and system identification. 

## Data 
All keystroke data is in [data](https://github.com/zhangyuyi99/soft_robot_piano_playing/tree/main/data). It is divided into data produced with rigid finger and soft finger. The .txt file name includes the finger stiffness (in KPa) and finger incline angle. 

## Models
### Mass-spring-damper model
The mass-spring-damper runs in MATLAB Simulink, with all code and models in [model](https://github.com/zhangyuyi99/soft_robot_piano_playing/tree/main/mass-spring-damper%20model). 

### Data-driven model
Before using the mass-spring-damper model, we also tried various data-driven models for piano keystroke which mainly includes Densely Connected Neural Network and LSTM. Codes are included in [nn model](https://github.com/zhangyuyi99/soft_robot_piano_playing/tree/main/nn%20model).

## Data analysis
Data preprocessing is mainly done with Python. Further analysis and plotting is finished with Jupyter Notebook. All code is in [data analysis](https://github.com/zhangyuyi99/soft_robot_piano_playing/tree/main/data_analysis). 








