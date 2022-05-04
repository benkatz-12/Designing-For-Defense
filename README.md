# Simlualted LEO Satellite Network Normal Communication

This software is used to generate "normal" satellilte communication in a multi-node network for the purpose of generating datasets for the Machine Learning algorithm. All code written in python and can be run by any version. 



### Contents

- GSImages
  - Storage of images recieved at GroundStation.py
- SATImages
  - Folder meant for a set of images to be sent by Satellite.py
- comm.zip
  - This folder
- GroundStation.py
  - Program simulating a ground station recieving images from a satellite.
- Satellite.py
  - Program simulating a satellite sending images to the ground station. 



### How To Run
1. Add images to SATImages
2. Correct host and port on each Satellite.py
3. Run GroundStation.py
    python GroundStation.py
4. Start packet capture device on the machine running GroundStation.py
4. Run Satellite.py to begin capturing "normal" satellite communication
