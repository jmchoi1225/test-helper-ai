#!bin/bash

# api Test
echo API TEST
echo hand detection TEST
python AI/test/apiTest/hand_detection_apiTest.py
echo "\n"
echo identification TEST
python AI/test/apiTest/identification_apiTest.py


# module Test
echo "\n\n\n"
echo MODULE TEST
echo hand detection TEST
python AI/test/moduleTest/hand_detection_moduleTest.py
echo "\n"
echo identification TEST
python AI/test/moduleTest/identification_moduleTest.py