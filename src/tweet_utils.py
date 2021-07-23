import pandas as pd
from multiprocessing import Pool
import json
from pathlib import Path


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]


def save_chunk(argstuple):
    ''''
    Save a chunk in format of json and csv
    '''
    chunk = argstuple[0]
    filename_prefix = argstuple[1]
    indx = argstuple[2]
    filename_prefix = filename_prefix+'_'+str(indx)

    # Check if filename_prefix contains folder + create it if necessary
    if Path(filename_prefix).parent != Path():
        folder = Path(filename_prefix).parent
        folder.mkdir(parents=True, exist_ok=True)

    # Save all chunks as .json
    lst = []
    with open(filename_prefix + '.json', 'a', encoding='utf-8') as f:
        for ch in chunk:
            json.dump(ch, f)
            f.write('\n')
            lst.append(ch)

    # Save all chunks as .csv
    df = pd.DataFrame(lst)
    df.to_csv(filename_prefix + '.csv', index=False, sep=';')

    # Clean output
    clean_output(filename_prefix, lst)

    print('Status Update based on {}'.format(filename_prefix))


def clean_output(filename_prefix, lst):
    '''
    Clean csv file: one row per tweet, no dictionaries
    '''
    # Unpack data dictionaries
    try:
        df_data = pd.DataFrame(lst[0]['data'])
        for col in df_data.columns:
            if type(df_data[col][0]) == dict:
                df_data = pd.concat(
                    [df_data.drop([col], axis=1), df_data[col].apply(pd.Series)], axis=1)
        df = df_data
    except KeyError:
        pass

    # Extract all extensions
    try:
        df_incl = pd.DataFrame()
        for incl in lst[0]['includes']:
            if df_incl.empty:
                df_incl = pd.DataFrame(lst[0]['includes'][incl])
            else:
                df_incl = df_incl.join(pd.DataFrame(lst[0]['includes'][incl]))
            if 'id' in df_incl.columns:
                df_incl = df_incl.rename(columns={'id': f'{incl}_id'})
        df_data = df_data.join(df_incl)
    except KeyError:
        pass

    # Merge data and extensions together in one csv file
    try:
        df_data.to_csv(filename_prefix + '_cleaned.csv', index=False, sep=';')
    except NameError:
        pass


def save_list(chunklist, filename_prefix):

    argslist = ((chk, filename_prefix, i) for i, chk in enumerate(chunklist))
    print(argslist)
    pool = Pool(2)  # run 2 task at most in parallel
    pool.map(save_chunk, argslist)
    print('Done')
