#!/usr/bin/python3

import sys
import os

class Statistic:
    instances = []
    def __init__(self, name, required_vars, func):
        self.__class__.instances.append(self)
        self.name = name
        self.required_vars = required_vars
        self.func = func

def clear():
    os.system("cls" if os.name == "nt" else "clear")

mean = Statistic("Mean",
        ["variable"],
        lambda args: sum(args[0]) / len(args[0]))

st_dev = Statistic("Standard deviation",
        ["variable"],
        lambda args: pow(sum((item - mean.func(args)) ** 2 for item in args[0])  / len(args[0]), 0.5))

# TODO
"""
pcc = Statistic("Pearson correlation coefficient",
    ["first variable", "second variable"],
    lambda args:)
"""

def main(argv):
    variables_list = []
    
    def vars_to_text(var_indices):
        len_vari = len(var_indices)
        match len_vari:
            case 0:
                raise ValueError("There must be at least one variable.")
            case 1:
                return variables_list[var_indices[0]]
            case 2:
                return "%s and %s" % (variables_list[var_indices[0]], variables_list[var_indices[1]])
            case len_vari if len_vari > 2:
                text = ""
                for i in range(len_vari - 1):
                    text += "%s, " % (variables_list[i])
                text += "and %s" % (variables_list[-1])
                return text

    def print_vars_stats():
        print("Indices of variables:")
        for i in range(len(variables_list)):
            print("%d - %s" % (i, variables_list[i]))    
        print("Currently implemented statistics:")
        for i in range(len(Statistic.instances)):
            print("%d - %s" % (i + 1, Statistic.instances[i].name))

    print("Welcome to djnStats!")
    with open(str(argv[0]), 'r') as data:
        # putting data into 2-dimensional list
        print("Reading %s..." % (str(argv[0])))
        lines = [l.rstrip() for l in data]
        variables_list = lines[0].split(",")
        data_list = [[] for i in range(len(variables_list))]
        for line in lines[1:]:
            line_list = line.split(",")
            for i in range(len(variables_list)):
                data_list[i].append(float(line_list[i]))
        print("File read.")

        # analysis selection
        print_vars_stats()
        quit = False
        while not quit:
            option = input("Please type number of statistic to calculate, r to reset console, or q to quit: ")
            if option == "q":
                quit = True
            elif option == "r":
                clear()
                print_vars_stats()
            else:
                statistic = Statistic.instances[int(option) - 1]
                args = []
                var_indices = []
                for var in statistic.required_vars:
                    var_index = int(input("Please type index of %s: " % (var)))
                    args.append(data_list[var_index])
                    var_indices.append(var_index)
                print("%s of %s is %f" % (statistic.name, vars_to_text(var_indices), statistic.func(args)))

        exit()


if __name__ == "__main__" and len(sys.argv) == 2:
        main(sys.argv[1:])
else:
    raise ValueError("Incorrect arguments supplied.")
    exit()
