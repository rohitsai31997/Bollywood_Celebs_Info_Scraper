import pandas as pd

dataset = pd.read_csv(r"C:\Users\rohit\PycharmProjects\Bollywood_Celebs\bollywood\celeb-names.csv")

# url = dataset["Link"].iloc[0]
import cv2
import numpy as np
import urllib.request
import time

start_time = time.time()
for i in range(0,50):
    try:
        name = dataset["Name"].iloc[i]
        url = dataset["Link"].iloc[i]
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        binary_str = response.read()
        byte_array = bytearray(binary_str)
        numpy_array = np.asarray(byte_array, dtype="uint8")
        image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
        cv2.imwrite(r'C:\Users\rohit\Desktop\Bollywood\ ' + str(name) + '.png', image)
        print("Saved Image")
    except Exception as e:
        print(str(e))

end_time = time.time()
print("Done")
print("Time Taken :" + str(end_time - start_time) + "sec")