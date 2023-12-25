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
# Example usage
print(Color.RED + "This text will be in red color!" + Color.RESET)
print(Color.GREEN + "This text will be in green color!" + Color.RESET)
print(Color.BLUE + "This text will be in blue color!" + Color.RESET)
"""
    
    
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


def print_current_agg(agg_collection, color_to_print):
    
    
    os.system('clear')
    terminal_size = os.get_terminal_size()
    terminal_height = terminal_size.lines - 2
    
    most_current_agg = len(agg_collection) - 1
    matrix_slot_for_agg = 0
    
    header_string = ""

    terminal_width = terminal_size.columns - len(str(agg_collection[most_current_agg].close))
    
    matrix = [[' ' for _ in range(terminal_width)] for _ in range(terminal_height)]
    
    iterval_amount = 1
    print(terminal_height)
    print(terminal_width)
    
    if len(agg_collection) > 1:
        iterval_amount = abs(agg_collection[most_current_agg].close - agg_collection[most_current_agg - 1].close)
        if iterval_amount == 0:
            iterval_amount = .1
        
        
    header_string =  ("Count: " + str(len(agg_collection)) + " Opening: " + str(agg_collection[most_current_agg].opening) + " High: " + str(agg_collection[most_current_agg].high) + " Low: " + str(agg_collection[most_current_agg].low) + 
    " Close: " + str(agg_collection[most_current_agg].close) + " Volume: " + str(agg_collection[most_current_agg].volume) + " vwap: " + str(agg_collection[most_current_agg].vwap) + " Transactions: " + str(agg_collection[most_current_agg].transactions))
    
    if len(header_string) > terminal_width:
        header_string =  ("C: " + str(len(agg_collection)) + " O: " + str(agg_collection[most_current_agg].opening) + " H: " + str(agg_collection[most_current_agg].high) + " L: " + str(agg_collection[most_current_agg].low) + 
        " C: " + str(agg_collection[most_current_agg].close) + " V: " + str(agg_collection[most_current_agg].volume) + " v: " + str(agg_collection[most_current_agg].vwap) + " T: " + str(agg_collection[most_current_agg].transactions))
    
    
    print(header_string)
    
    for i in range(terminal_height):
        matrix[i][0] = round(agg_collection[most_current_agg].close + ((int(terminal_height / 2) * iterval_amount) - (i * iterval_amount)), 1)
        
        
    if len(agg_collection) == 1:
        matrix[int(terminal_height / 2)][1] = "*"
        
    else:
        for i in range(len(agg_collection)):
            for j in range(terminal_height):
                if agg_collection[i].close < matrix[j][0]:
                    matrix_slot_for_agg = j - 1
            if i == most_current_agg:
                matrix[matrix_slot_for_agg][i + 1] = "*"
            else:
                matrix[matrix_slot_for_agg][i + 1] = "_"
          
        
    for i in matrix:
        #print(i)
        for j in i:
            print(color_to_print + str(j) + Color.RESET, end='')
        print()
    
  
"""
stock_printer will recieve a file name containing the aggregation of data it will then nicely print it to the terminal
"""
def stock_printer(opened_file):
    agg = []
    agg.append(get_next_agg(opened_file))
    agg_color = Color.WHITE
    count = 1
    
    while agg[0] != None:
        terminal_size = os.get_terminal_size()
        terminal_height = terminal_size.lines - 1
    
        if len(agg) >= int(terminal_height * .75):
            agg = agg[5:]
            
        if len(agg) > 1:
            if agg[len(agg) - 2].close < agg[len(agg) - 1].close:
                agg_color = Color.GREEN
            elif agg[len(agg) - 2].close > agg[len(agg) - 1].close:
                agg_color = Color.RED
            else:
                agg_color = Color.YELLOW
        else:
            agg_color = Color.YELLOW 
            
        print_current_agg(agg, agg_color)
        count += 1
        time.sleep(.1)
        agg.append(get_next_agg(opened_file))
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        