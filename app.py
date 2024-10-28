import streamlit as st
import pandas as pd
from wait_for_getting_csv import wait_for_getting_csv
# import time


# CSVファイルを読み込む
df1 = pd.read_csv('diffavg_5w.csv', header=None)
df2 = pd.read_csv('diffavg_5s.csv', header=None)
df3 = pd.read_csv('diffavg_6s.csv', header=None)
df4 = pd.read_csv('diffavg_6w.csv', header=None)
df5 = pd.read_csv('diffavg_7.csv', header=None)

# タイトルを表示
st.title('地震発生日からの為替レートの変動')

if st.button("最新のデータに更新"):
    st.info("CSVファイルのダウンロード待機中...")
    wait_for_getting_csv("diffavg")
    df1 = pd.read_csv('diffavg_5w.csv', header=None)
    df2 = pd.read_csv('diffavg_5s.csv', header=None)
    df3 = pd.read_csv('diffavg_6s.csv', header=None)
    df4 = pd.read_csv('diffavg_6w.csv', header=None)
    df5 = pd.read_csv('diffavg_7.csv', header=None)
    st.success("CSVファイルのダウンロードが完了しました。")

# タブを作成
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "震度5弱", "震度5強", "震度6弱", "震度6強", "震度7"
])

with tab1:
    st.line_chart(df1)
    if st.button("表形式で表示", key='1'):
        st.dataframe(df1)

with tab2:
    st.line_chart(df2)
    if st.button("表形式で表示", key='2'):
        st.dataframe(df2)

with tab3:
    st.line_chart(df3)
    if st.button("表形式で表示", key='3'):
        st.dataframe(df3)

with tab4:
    st.line_chart(df4)
    if st.button("表形式で表示", key='4'):
        st.dataframe(df4)

with tab5:
    st.line_chart(df5)
    if st.button("表形式で表示", key='5'):
        st.dataframe(df5)

