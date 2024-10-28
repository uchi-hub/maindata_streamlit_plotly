import streamlit as st
import pandas as pd
import altair as alt
from wait_for_getting_csv import wait_for_getting_csv

# CSVファイルを読み込む関数
def load_csv(file_path):
    df = pd.read_csv(file_path, header=None)
    # 列数が2の場合のみ列名を設定
    if df.shape[1] == 2:
        df.columns = ["時間", "前日比"]
    return df

# 各CSVファイルを読み込む
df1 = load_csv('diffavg_5w.csv')
df2 = load_csv('diffavg_5s.csv')
df3 = load_csv('diffavg_6s.csv')
df4 = load_csv('diffavg_6w.csv')
df5 = load_csv('diffavg_7.csv')

# タイトルを表示
st.title('地震発生日からの為替レートの変動')

# データの更新
if st.button("最新のデータに更新"):
    st.info("CSVファイルのダウンロード待機中...")
    wait_for_getting_csv("diffavg")
    df1 = load_csv('diffavg_5w.csv')
    df2 = load_csv('diffavg_5s.csv')
    df3 = load_csv('diffavg_6s.csv')
    df4 = load_csv('diffavg_6w.csv')
    df5 = load_csv('diffavg_7.csv')
    st.success("CSVファイルのダウンロードが完了しました。")

# タブを作成
tab1, tab2, tab3, tab4, tab5 = st.tabs(["震度5弱", "震度5強", "震度6弱", "震度6強", "震度7"])

# グラフ描画関数
def render_chart(df):
    if df.shape[1] == 2:  # データが2列の場合のみ表示
        chart = alt.Chart(df).mark_line().encode(
            x=alt.X('時間', title='時間'),
            y=alt.Y('前日比', title='前日比')
        )
        st.altair_chart(chart, use_container_width=True)
    else:
        st.error("データ形式が正しくありません。")

# 各タブにグラフとデータ表示のボタンを追加
with tab1:
    render_chart(df1)
    if st.button("表形式で表示", key='1'):
        st.dataframe(df1)

with tab2:
    render_chart(df2)
    if st.button("表形式で表示", key='2'):
        st.dataframe(df2)

with tab3:
    render_chart(df3)
    if st.button("表形式で表示", key='3'):
        st.dataframe(df3)

with tab4:
    render_chart(df4)
    if st.button("表形式で表示", key='4'):
        st.dataframe(df4)

with tab5:
    render_chart(df5)
    if st.button("表形式で表示", key='5'):
        st.dataframe(df5)
