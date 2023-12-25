"""
The grapher for the stock works as the visual component of the program. Essentially stock_printer gets passed an open file containing
stocks in the format as below 
Agg(open=130.28, high=131, low=130.28, close=131, volume=8174, vwap=130.8541, timestamp=1672736400000, transactions=208, otc=None)

each on a individual line it will parse that and continue reading the file through. Graphing the closing and the changes that occur.


"""


import shutil
import time
import os

"""
Very simple program the goal is simple it will read from a file that it's passed


"""

# ANSI color codes
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    

# Agg class contains all of the information for each agg that is supplied by Polygon
class Agg:
    
    def __init__(self, opening, high, low, close, volume, vwap, timestamp, transactions, otc):
        self.opening = float(opening)
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)
        self.volume = float(volume)
        self.vwap = float(vwap)
        self.timestamp = int(timestamp)
        self.transactions = int(transactions)
        self.otc = otc

 
    
"""
get_next_agg will take a file name and return the next line of the aggregate data in the agg object type    
"""
def get_next_agg(aggregate_file):
    line = aggregate_file.readline()
    if len(line) == 0:
        return None
        
    agg_array = [0] * 9
    
    for i in range(9):
        #print(line)
        equal_index = line.find('=')
        space_index = line.find(',')
        agg_array[i] = line[equal_index + 1 : space_index]
        line = line[space_index + 1:]
    
    return Agg(agg_array[0], agg_array[1], agg_array[2], agg_array[3], agg_array[4], agg_array[5], agg_array[6], agg_array[7], None)


# prints the agg collection up to the current agg (following the given color, count, and agg collection that's passed)
def print_current_agg(agg_collection, color_to_print, count):
    
    # clear the terminal
    os.system('clear')
    
    # get the terminals CURRENT sizes
    terminal_size = os.get_terminal_size()
    terminal_height = terminal_size.lines - 3
    
    # get the index of the current aggregate data
    most_current_agg = len(agg_collection) - 1
    matrix_slot_for_agg = 0
    
    # string to hold the header (to see if it fits within the terminal)
    header_string = ""

    # we need to make enough space such that we account for the potential of a large float for the y axis
    terminal_width = terminal_size.columns - len(str(agg_collection[most_current_agg].close))
    matrix = [[' ' for _ in range(terminal_width)] for _ in range(terminal_height)]
    
    # default interval is 1
    iterval_amount = 1
    
    # if we're a few aggregate data in then we find a good interval for the most recent aggregate data
    if len(agg_collection) > 1:
        iterval_amount = abs(agg_collection[most_current_agg].close - agg_collection[most_current_agg - 1].close)
        if iterval_amount == 0:
            iterval_amount = .1
        
        
    # set up the header string with the expectation we can go long
    header_string =  ("Count: " + str(count) + " Opening: " + str(agg_collection[most_current_agg].opening) + " High: " + str(agg_collection[most_current_agg].high) + " Low: " + str(agg_collection[most_current_agg].low) + 
    " Close: " + str(agg_collection[most_current_agg].close) + " Volume: " + str(agg_collection[most_current_agg].volume) + " vwap: " + str(agg_collection[most_current_agg].vwap) + " Transactions: " + str(agg_collection[most_current_agg].transactions))
    
    # if we need to strip some characters from the header do so
    if len(header_string) > terminal_width:
        header_string =  ("C: " + str(count) + " O: " + str(agg_collection[most_current_agg].opening) + " H: " + str(agg_collection[most_current_agg].high) + " L: " + str(agg_collection[most_current_agg].low) + 
        " C: " + str(agg_collection[most_current_agg].close) + " V: " + str(agg_collection[most_current_agg].volume) + " v: " + str(agg_collection[most_current_agg].vwap) + " T: " + str(agg_collection[most_current_agg].transactions))
    
    # print out the header
    print(header_string)
    
    # for the y axis add the range to the matrix
    for i in range(terminal_height):
        matrix[i][0] = round(agg_collection[most_current_agg].close + ((int(terminal_height / 2) * iterval_amount) - (i * iterval_amount)), 1)
        
        
    # if we're at the first aggregate data then just do a star
    if len(agg_collection) == 1:
        matrix[int(terminal_height / 2)][1] = "*"
    
    # if we're a few deep then place them in their corresponding socket making sure to specifiy the current aggregate data
    else:
        for i in range(len(agg_collection)):
            for j in range(terminal_height):
                if agg_collection[i].close < matrix[j][0]:
                    matrix_slot_for_agg = j - 1
            if i == most_current_agg:
                matrix[matrix_slot_for_agg][i + 1] = "*"
            else:
                matrix[matrix_slot_for_agg][i + 1] = "_"
          
        
    # lastly print out the matrix following the color we've been given
    for i in matrix:
        #print(i)
        for j in i:
            print(color_to_print + str(j) + Color.RESET, end='')
        print()
    
  
"""
stock_printer will recieve a file name containing the aggregation of data it will then nicely print it to the terminal
"""
def stock_printer(opened_file):
    # make our aggregate data list
    agg = []
    # read in the first aggregate data
    agg.append(get_next_agg(opened_file))
    # default the color to white
    agg_color = Color.WHITE
    # start our counter
    count = 1
    
    # while we haven't gone through the whole file 
    while agg[0] != None:
        # get the terminal width so we know if we need to trim our list some
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns - 1
        if len(agg) >= int(terminal_width / 2):
            agg = agg[10:]
        
        # if we're all good in terms of length then determine the color based on the closing of the most recent agg data
        if len(agg) > 1:
            if agg[len(agg) - 2].close < agg[len(agg) - 1].close:
                agg_color = Color.GREEN
            elif agg[len(agg) - 2].close > agg[len(agg) - 1].close:
                agg_color = Color.RED
            else:
                agg_color = Color.YELLOW
        else:
            agg_color = Color.YELLOW 
            
        # call to print out the current aggregate list
        print_current_agg(agg, agg_color, count)
        # increment our count
        count += 1
        # sleep a second
        time.sleep(.5)
        # get the next aggregate data
        agg.append(get_next_agg(opened_file))
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        