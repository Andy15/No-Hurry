import os
import cv2
import numpy as np
import pandas as pd
import face_recognition

name = []
face = []
res = set()
cache = 'cache'
threshold = 0.8

def test(csv, image):
    try:
        df = pd.read_csv(csv)

        for idx, row in df.iterrows():
            if (os.path.exists(os.path.join(cache, row['name'] + '.npy'))):
                array = np.load(os.path.join(cache, row['name'] + '.npy'))
            else:
                image = face_recognition.load_image_file(row['photo'])
                array = face_recognition.face_encodings(image, model="large")[0]
                np.save(os.path.join(cache, row['name'] + '.npy'), array)
            name.append(row['name'])
            face.append(array)

        test_image = face_recognition.load_image_file(image)
        test_image_locations = face_recognition.face_locations(test_image, model="cnn")

        for i in range(len(test_image_locations)):
            up = test_image_locations[i][0]
            right = test_image_locations[i][1]
            down = test_image_locations[i][2]
            left = test_image_locations[i][3]
            face_image = test_image[up:down, left:right]
            face_image_encodings = face_recognition.face_encodings(face_image, model="large")
            if len(face_image_encodings):
                dis = face_recognition.face_distance(face, face_image_encodings[0])
                idx = np.argmin(dis)
                if min(dis) < threshold:
                    res.add(name[idx])

        return res

    except Exception as e:
        return None