import os
import random

def filter_only_characters(unfiltered_filename):
    filtered_filename = ""

    for character in unfiltered_filename:
        if character.isalpha() or character == ".":
            filtered_filename += character;


    return filtered_filename

print("Please enter a filename (or type exit) : ")

filename = filter_only_characters(input())

while filename != "exit":

    if os.path.isfile(filename):

        file = open(filename, "r")

        # Save the first word up to a colon " : ". That is the set.
        # Save each letter up to a comma " , ". That is a name in the list of the set.
        # Save each each word up to " ; ". That is the list of names for that set.
        dict_of_names = {}
        current_key = ""
        current_list_of_names = []

        getting_key = True
        getting_name = False

        current_letter_stream = ""

        for line in file:
            line = line.rstrip()
            for character in line:
                if getting_key:
                    if character == ':':
                        current_key = current_letter_stream
                        current_letter_stream = ""
                        getting_key = False
                        getting_name = True
                        continue
                    else:
                        current_letter_stream += character

                if getting_name:
                    if character == ',':
                        current_list_of_names.append(current_letter_stream)
                        current_letter_stream = ""
                    elif character == ';':
                        current_list_of_names.append(current_letter_stream)
                        dict_of_names[current_key] = current_list_of_names
                        while (len(current_list_of_names) < 2):
                            current_list_of_names.append("    ")

                        current_list_of_names = []
                        current_letter_stream = ""
                        getting_name = False
                        getting_key = True
                    else:
                        current_letter_stream += character

        file.close()


        print('{:<8} {:<13} {:<4} {:<12}'.format("", "Blue", "vs", "Red"))

        # choose 2 random names from each set
        for key in dict_of_names:
            two_random_names = random.sample(dict_of_names[key], 2)

            # Print the key and the two random names
            print('{:<7} {:<13} {:<4} {:<12}'.format(key + ':', two_random_names[0], " ", two_random_names[1]))
    else:
        print(filename + " doesn't exist.")

    print("Please enter a filename (or type exit) : ")
    filename = filter_only_characters(input())