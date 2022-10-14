import os
import base64
import numpy as np
import pandas as pd
import face_recognition

name = []
face = []
res = set()

def init(csv, cache):
    df = pd.read_csv(csv, names=['name', 'sex', 'sno', 'college', 'signed'])

    for idx, row in df.iterrows():
        if row['sno'] in name:
            continue
        arr = np.load(os.path.join(cache, row['sno'] + '.npy'))
        name.append(row['sno'])
        face.append(arr)

def test(photo, threshold, tmp):
    try:
        b = base64.b64decode(photo)
        f = open(tmp, 'wb')
        f.write(b)
        f.close()
        img = face_recognition.load_image_file(tmp)
        loc = face_recognition.face_locations(img)

        for i in range(len(loc)):
            up = loc[i][0]
            right = loc[i][1]
            down = loc[i][2]
            left = loc[i][3]
            crop = img[up:down, left:right]
            arr = face_recognition.face_encodings(crop)
            if len(arr):
                dis = face_recognition.face_distance(face, arr[0])
                idx = np.argmin(dis)
                if min(dis) < threshold:
                    res.add(name[idx])

        return res

    except Exception as e:
        return None