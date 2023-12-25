Very basic stock grapher. 

Wanted originally to do real time but sadly that always ends up costing something and for a small afternoon project that wasn't realisitic. 

Note tested on python version 3.9

Need to have installed 
https://github.com/polygon-io/client-python

Put simply run the example api (Stock_API_example.py) after plugging in your polygon key. It will grab some Apple Stock and place it in a file Apple.txt.

Then run Stock_Driver.py

Originally I was going to allow for selecting a stock or using a previous cached but since realtime isn't feasible without paying this is the state.

example run

python3 Stock_API_example.py<br>
python3 Stock_Driver.py

Then you will see something extremely similar to below.
Note currently height and width scaling work so you can move your terminal around and have it correctly size and take up the space. 


GIF
![](https://github.com/Mockedarche/Stock_Grapher/blob/main/updateV1.1.gif)

