#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
from recettes import add_recipes, print_recipe
import pickle

# TODO: Définissez vos fonctions ici

def compare_texts(text1, text2):
    with open(text1, "r", encoding="utf-8") as f1, open(text2, "r", encoding="utf-8") as f2:
        for index, line_text1 in enumerate(f1):
            line_text2 = f2.readline()
            if line_text2 != line_text1:
                print("These two texts are not identical. Line {} is different.".format(index + 1))
                print(line_text2)
                print("!=")
                print(line_text1)
    return 0

def triple_spaces(text):
    with open(text, "r", encoding="utf-8") as f1, open("fable_copy.txt", "w", encoding="utf-8") as f2:
        for line in f1:
            modified_line = line.replace(" ", "   ")
            f2.write(modified_line)
    return 0

def numeric_to_alpha_grade(grades):
    grade_list = []

    with open(grades, "r", encoding="utf-8") as f1, open("alpha_grades.txt", "w", encoding="utf-8") as f2:
        for line in f1:
            grade_list.append(int(line))

        for grade in grade_list:
            for alpha_grade in PERCENTAGE_TO_LETTER:
                if PERCENTAGE_TO_LETTER[alpha_grade][0] < grade and grade < PERCENTAGE_TO_LETTER[alpha_grade][1]:
                    f2.write("{0} which is equivalent to {1}\n".format(str(grade), alpha_grade))
    return 0

def manipulate_recipes(recipes):
    return print("desespoir et desolation")

def count_numbers(text):
    numbers = []
    with open(text, "r", encoding="utf-8") as f:
        word = f.read().strip().split()

        for thing in word:
            if thing.isnumeric():
                numbers.append(int(thing))

    return sorted(numbers)

def one_two(text):
    with open(text, "r", encoding="utf-8") as f1, open("fable_1_2.txt", "w", encoding="utf-8") as f2:
        for index, line in enumerate(f1):
            if index % 2 == 0:
                f2.write(line)
            else:
                continue

    return 0


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #compare_texts("lecorbeauetlerenard.txt", "lecorbeauetlerenard2.txt")
    #triple_spaces("lecorbeauetlerenard.txt")
    #numeric_to_alpha_grade("notes.txt")
    #manipulate_recipes("recipes.p")
    #print(count_numbers("exemple.txt"))
    one_two("lecorbeauetlerenard.txt")
