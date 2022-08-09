import streamlit as st
import yfinance as yf  
import matplotlib.pyplot as plt
import datetime 
import random

from greedy import greedy
from dp import dp
from brute_force import brute_force
import statistics


tenure = int(st.selectbox('Please select what duration to maximize profits',('7', '14', '28')))

#st.write('You selected:', tenure)

delta = int(tenure)*5

tod = datetime.datetime.now()
d = datetime.timedelta(days = delta)
a = tod - d
a = a.date()

stock = st.text_input('Stock name', 'SPY')

algo = st.selectbox('Please select what algorithm to be used',('Brute Force', 'Greedy Algorithm', 'Dynamic Programming'))

if algo and stock:

    data = yf.download('SPY',a,tod)
    
    # Plot the close prices
    st.line_chart(data["Adj Close"])

    req = data[0:tenure*3]

    product = req['Adj Close'].values.tolist()

    batch1= product[:7]
    batch2= product[7:14]
    batch3= product[14:]

    def max_generator():
  
        num = random.sample(range(1, tenure), random.randint(1, int(tenure/2.5))*2)
        return num

    l = sorted(max_generator())


    if algo=='Brute Force':
        
        batch1_profit = brute_force(batch1)
        batch2_profit =  brute_force(batch2)
        batch3_profit = brute_force(batch3)
        
        
            
    if algo=='Greedy Algorithm':
        batch1_profit = greedy(batch1)
        batch2_profit =  greedy(batch2)
        batch3_profit = greedy(batch3)
    
    if algo=='Dynamic Programming':
        batch1_profit = dp(batch1)
        batch2_profit =  dp(batch2)
        batch3_profit = dp(batch3)

    profits = [batch1_profit,batch2_profit,batch3_profit]
        
    st.write('Batch 1 max profit', batch1_profit)
    st.write('Batch 2 max profit', batch2_profit)
    st.write('Batch 3 max profit', batch3_profit)
    
    st.write('The average max profit you can get from last 3 batches:', statistics.mean(profits))

    j = 1
    for i in range(0,len(l),2):
        st.write("Step ", j)
        st.write("Buy it on day ", l[i], " and sell it on day ", l[i+1])
        j+=1
        
