import os
import numpy as np
import pandas as pd
import face_recognition

name = []
face = []
res = set()

def init(csv, cache):
    df = pd.read_csv(csv, names=['name', 'sex', 'sno', 'photo', 'dep', 'sign', 'unsinged_time'])

    for idx, row in df.iterrows():
        if row['name'] in name:
            continue
        if (os.path.exists(os.path.join(cache, row['name'] + '.npy'))):
            arr = np.load(os.path.join(cache, row['name'] + '.npy'))
        else:
            img = face_recognition.load_image_file(row['photo'])
            arr = face_recognition.face_encodings(img)[0]
            np.save(os.path.join(cache, row['name'] + '.npy'), arr)
        name.append(row['name'])
        face.append(arr)

def test(path, threshold):
    try:
        img = face_recognition.load_image_file(path)
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