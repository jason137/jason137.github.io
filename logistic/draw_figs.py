#!/usr/bin/env python3
import numpy as np
import pandas as pd
from ggplot import *

INPUT_FILE = '/Users/jason/gits/jason137.github.io/data/lemeshow.tsv'

# cf lemeshow c1

def load_extended_data(input_file=INPUT_FILE):

    data = pd.read_csv(input_file, sep='\t')

    age_groups = list()

    # groups defined in table 1.1
    for age in data.age:
        if age < 30:
            group = 1
        elif 30 <= age < 35:
            group = 2
        elif 35 <= age < 40:
            group = 3
        elif 40 <= age < 45:
            group = 4
        elif 45 <= age < 50:
            group = 5
        elif 50 <= age < 55:
            group = 6
        elif 55 <= age < 60:
            group = 7
        else:
            group = 8

        age_groups.append(group)

    data['age_group'] = age_groups

    return data

def draw_fig11(data):

    plot = (ggplot(data, aes('age', 'chd'))
        + geom_point()
        + xlab('age (yrs)')
        + ylab('chd (mean)')
        + ggtitle('fig 1.1 - scatterplot (dichotomous dep var)'))

    return plot

def draw_fig12(data):

    groups = data.groupby(['age_group'])
    plot_data = groups.aggregate(np.mean).reset_index()     # NOTE ggplot won't work without resetting index

    plot = (ggplot(plot_data, aes('age', 'chd'))
        + geom_point() + geom_line()
        + xlab('age (yrs)')
        + ylab('chd (mean)')
        + ggtitle('fig 1.2 - approximation to E(Y|X)'))

    return plot

def main():

    data = load_extended_data()

    fig11 = draw_fig11(data)
    fig12 = draw_fig12(data)

    ggsave('fig11.png', fig11)
    ggsave('fig12.png', fig12)

if __name__ == '__main__':
    main()
