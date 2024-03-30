import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler((0,1))

with open('mushroom_classification.pkl','rb') as f:
    model = pickle.load(f)

st.title("Mushroom Classification")
st.write("This is a Mushroom classification model that can predict 'Weather the mushroom is poisonous or Edible.'")

text = '''cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s
cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s
cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y
bruises: bruises=t,no=f
odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s
gill-attachment: attached=a,descending=d,free=f,notched=n
gill-spacing: close=c,crowded=w,distant=d
gill-size: broad=b,narrow=n
gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y
stalk-shape: enlarging=e,tapering=t
stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?
stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s
stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s
stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
veil-type: partial=p,universal=u
veil-color: brown=n,orange=o,white=w,yellow=y
ring-number: none=n,one=o,two=t
ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z
spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y
population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y
habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d'''

mapping_list={}
with open('mapping.txt','r') as file:
    data = file.readlines()
    for i in data:
        mapping_list[i[:-3]] = i[-2]

# print(mapping_list)

arr=[]
for text in text.split('\n'):
    split = text.split(": ")
    head = split[0]
    tail = split[1].split(',')
    for i in range(len(tail)):
        tail[i] = tail[i][:-2]
    ans = st.selectbox(head, tail)
    if ans in mapping_list:
        arr.append(mapping_list[ans])
print(arr)

def prediction(arr):
    arr = np.array(arr).reshape(-1,1)
    print("numpy array ",arr.shape)
    arr=scaler.fit_transform(arr).reshape(-1,)
    print("After fit tranformation ",arr.shape)
    output = model.predict([arr])
    if output[0]==1.:
        st.write("Prediction: The Mushroom is Edible")
    else:
        st.write("Prediction: The Mushroom is Poisonous",)

if st.button("submit"):
    prediction(arr)
