#!/usr/bin/env python3
# Find the percent of occurance of each word
# Released under GNU General Public License

# import essential libraries
import argparse # this will allow us to pass command line arguments


# function to find percent of words
def find_word_percent(raw_text):
    # declare essential variables
    word_count = {}
    word_percent_output = ''

    # read text and do some formatting
    raw_text = raw_text.lower()
    raw_text = raw_text.replace('.', ' ')   # replace full stops with spaces
    raw_text = raw_text.replace('\n', ' ')  # replace newlines with spaces

    # separata words and remove extra spaces
    splitted_text = raw_text.split(' ')
    for index in range(0, len(splitted_text)):
        splitted_text[index] = splitted_text[index].strip()
    
    # remove empty strings in list
    while splitted_text.count('') > 0:
        splitted_text.remove('')

    # initialize each word's count as zero
    for word in splitted_text:
        word_count[word] = 0
    
    # count each word's occurance
    for word in splitted_text:
        word_count[word] += 1
    
    # convert count into percentage
    total_words = len(splitted_text)
    for word in word_count:
        word_percent = str(word_count[word] / total_words * 100)

        if len(word_percent) > 5:
            word_percent = word_percent[0:5]

        word_percent_output += word + ', occuring ' + str(word_count[word]) + ' times, ' + word_percent + '%\n'

    # return the word percent to calling function
    return word_percent_output


# main function
def main():
    # define arguments
    parser = argparse.ArgumentParser(description=
        'Simple program to find percentage of occurance of words')
    parser.add_argument('-i', '--input', help='select the input file')
    parser.add_argument('-o', '--output', help='select the output file')
    arguments = parser.parse_args()

    if arguments.input:
        input_file = open(arguments.input, 'r')
        input_text = input_file.read()
        input_file.close()
        word_percent = find_word_percent(input_text)
        
        if arguments.output:
            output_file = open(arguments.output, 'w')
            output_file.write(word_percent)
            output_file.close()        
        else:
            print(word_percent)
    
    else:
        print('kindly specify an input file')


# call the main function
main()