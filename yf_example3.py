import os

import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    tic = 'QAN.AX'
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    datadir = r'/Users/h/PycharmProjects/toolkit/data'
    pth = f'{datadir}/qan_stk_prc.csv'
    df = yf_example2.yf_prc_to_csv(
        tic =  tic,
        pth = pth
        start = start,
        end = end)

if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)

print(f"The value of __name__ is: '{__name__}'")

