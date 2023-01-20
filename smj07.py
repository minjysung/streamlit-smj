import streamlit as st

st.title(':money_with_wings: :green[MONEY] :money_with_wings:')


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#plt.figure(figsize=(12,8))

money = pd.read_csv("money_data7.csv")



option = st.selectbox(
    'How would you like to choice year ?',
    ('2020', '2021', '2022'))
                   
option2 = int(option)

st.write('You selected:', option)

money = money[:] [money['A_YEAR']== option2]

fig, ax = plt.subplots(2,2, figsize=(12,8))

plt.subplot(221)
plt.plot(  list( money['A_MONTH'] ), list( money['A_RATE'] ), color='salmon' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('America Rate')


plt.subplot(222)
plt.plot(  list( money['A_MONTH'] ), list( money['K_RATE'] ), color='lightskyblue'  , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('Korea Rate')

plt.subplot(223)
plt.plot(  list( money['A_MONTH'] ), list( money['KOSPI'] ),color='lightpink' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('Kospi')

plt.subplot(224)
plt.plot(  list( money['A_MONTH'] ), list( money['HOUSE_PRICE'] ), color='yellow' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('House Price')

st.pyplot(fig)
st.dataframe(money) 
