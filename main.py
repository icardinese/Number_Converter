import numpy
import sys

number_formats = {
    'binary': {'elements': {'0': 0,'1': 1}, 'base': 2},
    'octal': {'elements': {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 7,'7': 7}, 'base': 8},
    'decimal': {'elements': {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}, 'base': 10},
    'hexadecimal': {'elements': {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'A': 10,'B': 11,'C': 12,'D': 13,'E': 14,'F': 15}, 'base': 16}
}

# This code is for constructing the possible format text.
index = 1
format_options = ''
for formats in number_formats:
    if (index == len(number_formats)):
        format_options += formats
    else:
        format_options += formats + '/'
    index += 1

# This function is for checking if the format inputted is a valid format name!
def Format_check(Input):
    valid_format_check = False
    for formats in number_formats:
        if (formats == Input.lower()):
            valid_format_check = True
    if (valid_format_check == False):
        print(f'Your format {Input} did not match a valid number format option from ({format_options})')
        sys.exit(0)

def Main():
    
    user_number_format = input(f'What number system is inputted? ({format_options})')
    Format_check(user_number_format)
    output_number_format = input(f'What number system is outputted? ({format_options})')
    Format_check(output_number_format)
    number_of_inputs = int(input('How many numbers of this format do you want?'))
    if isinstance(number_of_inputs, int):
        number_of_inputs = int(number_of_inputs)
    else:
        print('Expected an integer for the number of values that is desired!')
        sys.exit(0)
    
    for i in range(number_of_inputs):
        Number = []
        number_inputted = str(input('Enter the number that you desire to convert: '))
        for element in number_inputted:
            try:
                Number.append(number_formats[user_number_format.lower()]['elements'][element])
            except KeyError:
                if (element == ' '):
                    0 #Place holder value for nothing happening!
                else:
                    print(f'The inputted element of {element} is not a part of the valid elements of format type {user_number_format.lower()}')
                    sys.exit(0)
        # This algorithmn is to convert the inputted number format to decimal!
        decimal_number = 0
        n = len(Number)
        for each_base_element in Number:
            decimal_number += int(number_formats[user_number_format.lower()]['base']**(n-1)) * int(each_base_element)
            n -= 1
        # Now this algorithmn will convert decimal to the desired format. Or if decimal was selected just output decimal. 
        if (output_number_format.lower() == 'decimal'):
            print(decimal_number)
        else:
            # This is to find out how many digits the output would have.
            converted_number_of_elements = 0
            converted_number_test = 0
            base_converted_number = []
            Converted_number = []
            max_base_position_values = []
            highest_element = list(number_formats[output_number_format.lower()]['elements'])[-1]
            while (converted_number_test < decimal_number):
                base_number = int(number_formats[output_number_format.lower()]['base']**converted_number_of_elements) * int(number_formats[output_number_format.lower()]['elements'][highest_element])
                converted_number_test += base_number
                max_base_position_values.append(base_number)
                converted_number_of_elements += 1
            
            for k in range(converted_number_of_elements):
                max_trailing_value = 0
                prior_value = 0
                base_position = (converted_number_of_elements - 1) - k
                for trailing_index in range(base_position):
                    max_trailing_value += max_base_position_values[trailing_index]
                for prior_index in range(k):
                    prior_value += base_converted_number[prior_index]
                for elements in number_formats[output_number_format.lower()]['elements']:
                    current_position_value = (number_formats[output_number_format.lower()]['elements'][elements]) * int(number_formats[output_number_format.lower()]['base'] ** base_position)
                    if ((max_trailing_value + current_position_value + prior_value) >= decimal_number):
                        base_converted_number.append(current_position_value)
                        Converted_number.append(elements)
                        break
                Answer = ''
                for elements in Converted_number:
                    Answer += str(elements)
        print(Answer)

Main()