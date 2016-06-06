# -*- coding: utf-8 -*-

from p6_demo_func import *
     
if __name__ == '__main__':
 
    filenames=glob.glob(r'./Anscombe*.txt')

    processing_data_TextFiles(filenames)
    processing_table_TextFiles(filenames)
    processing_plot_TextFiles(filenames)
