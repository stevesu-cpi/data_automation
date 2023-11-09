

import sys
import tempRise
import pandas as pd
import matplotlib.pyplot as plt

def main(input_csv_file, data_path, index_list):
    
    input_df = pd.read_csv(input_csv_file)
    if index_list != None:
        input_df = input_df.iloc[index_list, : ]
    newclass = tempRise.dataGroup(input_df, data_path)
    new_dict_df = newclass.dict_df

    while True:
        print('\n')
        print('input choices: p = plot, d = derate table, e = exit')
        inp =  input('type request: ')

        if inp == 'p':
            fig, ax = newclass.plotchart2('title', new_dict_df)
            plt.show()

            while True:
                replot = input('do you want to replot? y/n: ')
                if replot == 'y' or replot == 'Y':
                    xdata_str = input('enter "[xmin, xmax]" include brackets ')
                    ydata_str = input('enter ["ymin, ymax]" include brackets ')
                    xdata_list = convert_to_list(xdata_str)
                    ydata_list = convert_to_list(ydata_str)
                    xdata_tup = (xdata_list[0], xdata_list[1])
                    ydata_tup = (ydata_list[0], ydata_list[1])
                    plt.close()
                    fig, ax = newclass.plotchart2('title', new_dict_df)
                    fig, ax = newclass.resize(fig, ax, xdata_tup, ydata_tup)
                    plt.show()
                else:
                    plt.close()
                    break
                    

        elif inp == 'd':
            derate_dict = newclass.make_derate_table()
            for k in derate_dict.keys():
                print('\n')
                print(derate_dict[k])
                
        else:
            break        
    return


def convert_to_list(list_str):
    list_str = list_str[1:]
    new_list = []
    temp_str = ''
    for ch in list_str:
        if ch != ',' and ch != ' ' and ch != ']':
            temp_str += ch
        if ch == ',' or ch == ']':
            new_list.append(float(temp_str))
            temp_str = ''
    return new_list

if __name__ == '__main__':
    input_csv = sys.argv[1]
    path = sys.argv[2] + '/'
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
    