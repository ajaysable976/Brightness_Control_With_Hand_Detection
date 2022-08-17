# Brightness_Control_With_Hand_Detection
Based on hands finger movement we can control the brightness of of pc/laptop

# Install library
- cv2
- mediapipe
- math 
- screen_brightness_control 
- numpy 

# Approach
Building a Brightness Controller with OpenCV can be accomplished in just 3 simple steps:
- Step 1. Detect Hand landmarks
- Step 2. Calculate the distance between thumb tip and index finger tip.
- Step 3. Map the distance of thumb tip and index finger tip with volume range. For my case, distance between thumb tip and index finger tip was within the range of 15 – 220 and the volume range was from 0 – 100.

# App
![Untitled](https://user-images.githubusercontent.com/108600694/185095135-faa75cc4-ffce-409c-8131-4651d54ed3f5.png)

![b1](https://user-images.githubusercontent.com/108600694/185095743-1ee2000a-cb98-4724-a588-e0ce98d666e8.png)


# Summary
Gesture recognition helps computers to understand human body language. This helps to build a more potent link between humans and machines, rather than just the basic text user interfaces or graphical user interfaces (GUIs).
In this project for gesture recognition, the human body’s motions are read by computer camera. The computer then makes use of this data as input to handle applications.
