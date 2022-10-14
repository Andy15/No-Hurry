import os
import base64
import numpy as np
import pandas as pd
import face_recognition

def add(csv, name, sex, sno, college, photo, cache, tmp):
    b = base64.b64decode(photo)
    f = open(tmp, 'wb')
    f.write(b)
    f.close()
    img = face_recognition.load_image_file(tmp)
    arr = face_recognition.face_encodings(img)[0]
    np.save(os.path.join(cache, sno + '.npy'), arr)
    pd.concat([pd.read_csv(csv, names=['name', 'sex', 'sno', 'college', 'signed']),
               pd.DataFrame([[name, sex, sno, college, '0']],
                            columns=['name', 'sex', 'sno', 'college', 'signed'])],
               ignore_index=True).to_csv(csv, header=None, index=False)

def delete(csv, sno):
    df = pd.read_csv(csv, names=['name', 'sex', 'sno', 'college', 'signed'])
    df.drop(index=df[df['sno'] == int(sno)].index.tolist()).to_csv(csv, header=None, index=False)

def manual(csv, sno):
    df = pd.read_csv(csv, names=['name', 'sex', 'sno', 'college', 'signed'])
    df.loc[df['sno'] == int(sno), 'signed'] = '1'
    df.to_csv(csv, header=None, index=False)

def all(csv):
    out = []
    df = pd.read_csv(csv, names=['name', 'sex', 'sno', 'college', 'signed'])
    for idx, row in df.iterrows():
        out.append({'name': str(row['name']), 'sex': str(row['sex']), 'sno': str(row['sno']), 'college': str(row['college']), 'signed': str(row['signed'])})
    return out