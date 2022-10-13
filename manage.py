import pandas as pd

def add(csv, name, sex, sno, photo, college, signed):
    pd.concat([pd.read_csv(csv, names=['name', 'sex', 'sno', 'photo', 'college', 'signed']),
               pd.DataFrame([[name, sex, sno, photo, college, signed]],
                            columns=['name', 'sex', 'sno', 'photo', 'college', 'signed'])],
               ignore_index=True).to_csv(csv, header=None, index=False)

def delete(csv, sno):
    df = pd.read_csv(csv, names=['name', 'sex', 'sno', 'photo', 'college', 'signed'])
    df.drop(index=df[df['sno'] == sno].index.tolist()).to_csv(csv, header=None, index=False)

def manual(csv, sno):
    df = pd.read_csv(csv, names=['name', 'sex', 'sno', 'photo', 'college', 'signed'])
    df.loc[df['sno'] == sno, 'signed'] = '1'
    df.to_csv(csv, header=None, index=False)