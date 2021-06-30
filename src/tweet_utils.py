import pandas as pd
from multiprocessing import Pool
import json

def chunks(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

def save_chunk(argstuple):
    ''''
    Save a chunk in format of json and csv
    '''
    chunk = argstuple[0]
    filename_prefix = argstuple[1]
    indx = argstuple[2]
    filename_prefix = filename_prefix+'_'+str(indx)

    lst = []
    with open(filename_prefix, 'a', encoding='utf-8') as f:
        for ch in chunk:
            json.dump(ch, f)
            f.write('\n')
            lst.append(ch)
    df = pd.DataFrame(lst)
    df.to_csv(filename_prefix + '.csv', index=False)
    print('Status Update based on {}'.format(filename_prefix))



def save_list(chunklist,filename_prefix):

    argslist = ((chk, filename_prefix,i) for i, chk in enumerate(chunklist))
    print(argslist)
    pool = Pool(2)  # run 2 task at most in parallel
    pool.map(save_chunk, argslist)
    print('Done')
