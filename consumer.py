from re import M
from time import sleep
import streamlit as st
import pandas as pd
import numpy as np
import threading
import json
from kafka import KafkaConsumer
my_map = st.map()

#my_nd_arr = np.array([[1, 2]])
# my_nd_arr = np.array([
#         [5.98,32.5],
#         ])
my_nd_arr = np.array([
        [45.08127861241874, 18.160400390625]])
def getdf(msg):
    global my_nd_arr
    print(msg)
    print(msg[0])
    print(msg[1])
    print("---")
    novi = np.array([[float(msg[1]),float(msg[0])]])
    # my_nd_arr = np.array([
    #     [float(msg[0]),float(msg[1])],
    #     ])
    # my_nd_arr = 
    my_nd_arr = np.append(my_nd_arr,novi,axis=0)
    #my_nd_arr.append(my_nd_arr,[float(msg[1]),float(msg[0])])
    #my_nd_arr = np.append(my_nd_arr,[float(msg[1]),float(msg[0])])
    print(my_nd_arr)
    # df = pd.DataFrame(
    #     my_nd_arr,
    #     columns=['lat', 'lon']
    # )
        
    df = pd.DataFrame(
        my_nd_arr,
        columns=['lat', 'lon']
    )
    my_map.map(df)

consumer = KafkaConsumer('sample',bootstrap_servers='localhost:29092',value_deserializer=lambda v: json.loads(v.decode('utf-8')))
for msg in consumer:
    print(msg.value)
    print(type(msg.value))
    getdf(msg.value)





    
    # return pd.DataFrame(
    #     np.random.randn(1, 2) / [50, 50] + [37.76, -122.4],
    #     columns=['lat', 'lon'])
# my_map = st.map()
# while True:
#     #my_map = st.map(getdf())
#     sleep(5)
#     my_map.map(getdf())
