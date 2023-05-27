import streamlit as st
import pandas as pd
import json


df = pd.read_csv('../CleanData/final-data.csv', sep='\t')


input_text = st.text_input("Enter student's ID")
if st.button("Search"):
    st.write("Text submitted:", input_text)

    # 3. Display the output
    df_sub = df[df['mssv'] == input_text]

    dict = {
        'mssv': df_sub['mssv'].values[0],
        'namsinh': df_sub['namsinh'].values[0],
        'gioitinh': df_sub['gioitinh'].values[0],
        'lopsh': df_sub['lopsh'].values[0],
        'khoa': df_sub['khoa'].values[0],
        'khoahoc': df_sub['khoahoc'].values[0],
        'chuyennganh2': df_sub['chuyennganh2'].values[0],
        'tinhtrang': df_sub['tinhtrang'].values[0],
        'drl': json.loads(df_sub['drl'].values[0].replace("'", '"')),
        'diem': json.loads(df_sub['diem'].values[0].replace("'", '"')),
        'thpt': json.loads(df_sub['thpt'].values[0].replace("'", '"')),
        'loai_tn': df_sub['loai_tn'].values[0],
        'xlhv': json.loads(df_sub['xlhv'].values[0].replace("'", '"'))
    }
    st.json(dict)