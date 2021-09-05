import numpy as np

x_max = 80 #x_max length of the words Matrix
y_letter = 27 # a-z (0-25) + # (26) = 27
n_max = 100000 # max number of words
param = -1 # param of to set all values as empty

class Process (object):
    def __init__(self): # init function of the process, executed once
        self.stateCount = 0 # Set the stateCount to 0
        self.matrix = np.zeros( (x_max, y_letter), dtype=np.int32) # Create matrix of x_max = X and 27 = Y

    def clear(self): # clear function of the process
        self.stateCount = 1 # Set the stateCount to 1

        for x in range(x_max): # goes from 0 to x_max
            for y in range(y_letter): # goes from 0 to 27
                self.matrix[x][y] = param # Setting the matrix all with the param

    def add(self, string): # add Process to the matrix
        state = 0 # set the state to  0
        id = 0 # set the identification to 0

        for char in string: # get each caracter of a string(word)
            id = self.get_char_id(char) # get the specific id of the character

            if ( self.matrix[state][id] == param ): # verify if in the position of the matrix[state][id] is empity
                self.matrix[state][id] = self.stateCount # Set the actual stateCount to the position
                self.stateCount = self.stateCount + 1 # add 1 to the current stateCount

            state = self.matrix[state][id] # State is set from the postion of the matrix

    def count(self, string):
        state = 0 # set the state to 0
        total = 0 # set the total to 0
        cont = 0 # set the cont to 0 (used t1o getting )

        for char in string: # get each character of a string(word)
            word = len(string) - cont - 1 # take 1 caracter of the word at time
            cont = cont + 1 # add 1 to the counter of the word
            c = 0 # set the count to 0

            if (word > 0): # verify the length of the word without the # (that identifies the end of the word)
                for j in range(0, y_letter): # Goes from 0 to 26
                    if (self.matrix[state][j] != param): # Verify if the value is diffent from empty (-1)
                        c = c + 1 # if the value of the matrix exists one state add 1 to the counter

            if (c > 1 or (c == 1 and state == 0)):
                total = total + 1 # if the above expresions is valid add 1 to the total

            id = self.get_char_id(char) # Get the id of the current character of the word
            state = self.matrix[state][id] # Get the state of the matrix[state][id]

        return total #return the number of total of the string (word)

    def get_char_id(self, char): # Get the id of the char
        # a = 97 | z = 97 + 25 = 122
        # subtract 97 of the value, so a = 0, z = 25 and # = 26

        if (char == '#'): # if char is # (end of the word)
            id = 26 # identify as the end
        else: # if char is not #
            id = ord(char) - 97 # Get the current id of the char

        return id

def main():
    p = Process() #Create object Process that will be responsable for all process

    while True:
        values_input = [] # Cleanning the vector of the input
        n = int(input("")) # Getting the number of the input

        while not (n >= 1  and n <= n_max):
            print ("Out of the dictionary, inform between 1 to 10⁵...")
            n = int(input(""))

        p.clear() # Cleanning the variables inside of the object process

        for index in range(0, n): # Goes from 0 to n, index get the current value
            input_value = str(input("")) # Get a word (input) and set to the variable input_value

            while (len(input_value) == 0):
                print("Please repeat value...")
                input_value = str(input(""))

            input_value = input_value.lower()+'#' # Lower the value inside input_value and add an caracter to identify the end
            values_input.append(input_value) # Add to the vector the variable input_value
            p.add(values_input[index]) # Execute the add Process

        total = 0  # Total receve the value 0
        for index in range(0, n): # Goes from 0 to n, index get the current value
            total = total + p.count(values_input[index]) # Calculate the current value in the count Process and add to the total

        res = total/float(n) # Get the exacly value for the response
        print(res) # present the response to the output

    return 0

if __name__ == "__main__":

    main() # execute the main function
