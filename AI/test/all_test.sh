#!bin/bash

# api Test
echo API TEST
echo hand detection TEST
coverage run AI/test/apiTest/apiTest.py
echo "\n"
coverage report -m AI/src/*.py

# module Test
echo "\n\n\n"
echo MODULE TEST
echo hand detection TEST
coverage run AI/test/moduleTest/hand_detection_moduleTest.py
echo "\n"
coverage report -m AI/src/hand_detection/*.py

echo "\n"
echo identification TEST
coverage run AI/test/moduleTest/identification_moduleTest.py
echo "\n"
coverage report -m AI/src/student_identification/*.py