import numpy as np
from copy import copy

def make_table(titles:list, rows:list):
    """
    Generates a markdown table
    """
    if len(titles) != len(rows[0]):
        raise ValueError("Title array and rows array must be same length")
    str_ = ""
    max_col = dict(zip(range(len(titles)), [0 for i in titles])) #dict of max col length
    
    # Find max col len
    titles_rows = copy(rows)
    titles_rows.append(titles)
    transposed = np.array(titles_rows).T.tolist()
    for ind, x in enumerate(transposed):
        max_col[ind] = max([len(y) for y in x])
    print(max_col)

    # Make table
    for ind, x in enumerate(rows):
        if ind == 0:
            str_ += "| "+" | ".join([str(x).ljust(max_col[i]) for i,x in enumerate(titles)])+ " |\n"
            str_ += "| "+" | ".join([ "-"*max_col[i] for i, z in enumerate(x)])+ " |\n"
        str_ += "| "+" | ".join([str(y).ljust(max_col[i]) for i, y in enumerate(x)])+" |\n"
    return str_