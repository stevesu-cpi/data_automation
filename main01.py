

import sys
import tempRise
import pandas as pd
import matplotlib.pyplot as plt

def main(input_csv, path, index_list):
    path = path + '/'
    input_df = pd.read_csv(path + input_csv)
    if index_list != None:
        input_df = input_df.iloc[index_list, : ]

    newclass = tempRise.dataGroup(input_df, path)
    new_dict_df = newclass.dict_df
    newclass.dict_samplerate
    fig, ax = newclass.plotchart2('title', new_dict_df)
    fig, ax = newclass.resize(fig, ax, (0,3), (0,90))
    plt.show()
    return


if __name__ == '__main__':
    input_csv = sys.argv[1]
    path = sys.argv[2]
    index_str = sys.argv[3]
    if index_str == 'None':
        index_list = None
    else:
        index_str = index_str[1:]
        index_list = []
        temp_str = ''
        for ch in index_str:
            if ch != ',' and ch != ' ' and ch != ']':
                temp_str += ch
            if ch == ',' or ch == ']':
                index_list.append(int(temp_str))
                temp_str = ''
        print(index_list)
    main(input_csv, path, index_list)   
    