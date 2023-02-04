import streamlit as st
import json
import csv
import pandas as pd
import firebase_admin
from firebase_admin import db
import string
import random

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1

def make_json(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
       
        for rows in csvReader:
            key = rows['Sample']
            data[key] = rows
 

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
 

def generateRandom():
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))

    return res

st.title("Sensory Evaluation of Food Samples")

st.info('Questionnaire For Faith Oriarewo')
st.text("___"*100)
st.write("""
## Dear Panelist
""")


st.write("""
    Kindly evaluate the following samples using the scale provided below. 
    Information generated from this exercise is strictly for research purpose. 
    Individual perceptions on the texture (hand/ mouth feel), appearance (color), aroma (flavor) and 
    general acceptability as well as contributions (comment) on what else you feel about the samples will be most welcomed. 
    Wash your hands in the basin of water provided after evaluating each sample to avoid bias.

""")

st.text("___"*100)

st.subheader("""Instruction: Rate samples using  the scale provided below""")

st.text("___"*100)
st.text("""""""9 –point Hedonic ranking scale (Ihenkoronye and Ngoddy, 1985) """"""")
st.text("""

9- liked extremely
8-liked very much
7- liked moderately
6- liked slightly
5- Neither liked nor disliked
4-disliked slightly
3-disliked moderately
2-disliked very much
1-disliked extremely 

""")

st.text("___"*100)

point_her = ["null", "disliked extremely", "disliked very much", "disliked moderately",
                "disliked slightly", "Neither liked nor disliked", "liked slightly", "liked moderately",
                        "liked very much", "liked extremely"]

st.subheader("Sample A")
a1 = st.slider('Taste for Sample(A)', 1, 9)
a2 = st.slider('Texture for Sample(A)', 1, 9)
a3 = st.slider('Appearance for Sample(A)', 1, 9)
a4 = st.slider('Aroma for Sample(A)', 1, 9)
a5 = st.slider('General Acceptability for Sample(A)', 1, 9)

st.text("___"*100)

st.subheader("Sample B")
b1 = st.slider('Taste for Sample(B)', 1, 9)
b2 = st.slider('Texture for Sample(B)', 1, 9)
b3 = st.slider('Appearance for Sample(B)', 1, 9)
b4 = st.slider('Aroma for Sample(B)', 1, 9)
b5 = st.slider('General Acceptability for Sample(B)', 1, 9)

st.text("___"*100)

st.subheader("Sample C")
c1 = st.slider('Taste for Sample(C)', 1, 9)
c2 = st.slider('Texture for Sample(C)', 1, 9)
c3 = st.slider('Appearance for Sample(C)', 1, 9)
c4 = st.slider('Aroma for Sample(C)', 1, 9)
c5 = st.slider('General Acceptability for Sample(C)', 1, 9)

st.text("___"*100)

st.subheader("Sample D")
d1 = st.slider('Taste for Sample(D)', 1, 9)
d2 = st.slider('Texture for Sample(D)', 1, 9)
d3 = st.slider('Appearance for Sample(D)', 1, 9)
d4 = st.slider('Aroma for Sample(D)', 1, 9)
d5 = st.slider('General Acceptability for Sample(D)', 1, 9)

st.subheader("Sample E")
e1 = st.slider('Taste for Sample(E)', 1, 9)
e2 = st.slider('Texture for Sample(E)', 1, 9)
e3 = st.slider('Appearance for Sample(E)', 1, 9)
e4 = st.slider('Aroma for Sample(E)', 1, 9)
e5 = st.slider('General Acceptability for Sample(E)', 1, 9)

st.subheader("Sample F")
f1 = st.slider('Taste for Sample(F)', 1, 9)
f2 = st.slider('Texture for Sample(F)', 1, 9)
f3 = st.slider('Appearance for Sample(F)', 1, 9)
f4 = st.slider('Aroma for Sample(F)', 1, 9)
f5 = st.slider('General Acceptability for Sample(F)', 1, 9)

st.subheader("Sample G")
g1 = st.slider('Taste for Sample(G)', 1, 9)
g2 = st.slider('Texture for Sample(G)', 1, 9)
g3 = st.slider('Appearance for Sample(G)', 1, 9)
g4 = st.slider('Aroma for Sample(G)', 1, 9)
g5 = st.slider('General Acceptability for Sample(G)', 1, 9)

st.subheader("Sample H")
h1 = st.slider('Taste for Sample(H)', 1, 9)
h2 = st.slider('Texture for Sample(H)', 1, 9)
h3 = st.slider('Appearance for Sample(H)', 1, 9)
h4 = st.slider('Aroma for Sample(H)', 1, 9)
h5 = st.slider('General Acceptability for Sample(H)', 1, 9)

st.subheader("Sample I")
i1 = st.slider('Taste for Sample(I)', 1, 9)
i2 = st.slider('Texture for Sample(I)', 1, 9)
i3 = st.slider('Appearance for Sample(I)', 1, 9)
i4 = st.slider('Aroma for Sample(I)', 1, 9)
i5 = st.slider('General Acceptability for Sample(I)', 1, 9)

st.subheader("Sample J")
j1 = st.slider('Taste for Sample(J)', 1, 9)
j2 = st.slider('Texture for Sample(J)', 1, 9)
j3 = st.slider('Appearance for Sample(J)', 1, 9)
j4 = st.slider('Aroma for Sample(J)', 1, 9)
j5 = st.slider('General Acceptability for Sample(J)', 1, 9)

st.subheader("Sample K")
k1 = st.slider('Taste for Sample(K)', 1, 9)
k2 = st.slider('Texture for Sample(K)', 1, 9)
k3 = st.slider('Appearance for Sample(K)', 1, 9)
k4 = st.slider('Aroma for Sample(K)', 1, 9)
k5 = st.slider('General Acceptability for Sample(K)', 1, 9)

st.subheader("Sample L")
l1 = st.slider('Taste for Sample(L)', 1, 9)
l2 = st.slider('Texture for Sample(L)', 1, 9)
l3 = st.slider('Appearance for Sample(L)', 1, 9)
l4 = st.slider('Aroma for Sample(L)', 1, 9)
l5 = st.slider('General Acceptability for Sample(L)', 1, 9)

st.subheader("Sample M")
m1 = st.slider('Taste for Sample(M)', 1, 9)
m2 = st.slider('Texture for Sample(M)', 1, 9)
m3 = st.slider('Appearance for Sample(M)', 1, 9)
m4 = st.slider('Aroma for Sample(M)', 1, 9)
m5 = st.slider('General Acceptability for Sample(M)', 1, 9)

st.subheader("Sample N")
n1 = st.slider('Taste for Sample(N)', 1, 9)
n2 = st.slider('Texture for Sample(N)', 1, 9)
n3 = st.slider('Appearance for Sample(N)', 1, 9)
n4 = st.slider('Aroma for Sample(N)', 1, 9)
n5 = st.slider('General Acceptability for Sample(N)', 1, 9)

st.subheader("Sample O")
o1 = st.slider('Taste for Sample(O)', 1, 9)
o2 = st.slider('Texture for Sample(O)', 1, 9)
o3 = st.slider('Appearance for Sample(O)', 1, 9)
o4 = st.slider('Aroma for Sample(O)', 1, 9)
o5 = st.slider('General Acceptability for Sample(O)', 1, 9)

st.subheader("Sample P")
p1 = st.slider('Taste for Sample(P)', 1, 9)
p2 = st.slider('Texture for Sample(P)', 1, 9)
p3 = st.slider('Appearance for Sample(P)', 1, 9)
p4 = st.slider('Aroma for Sample(P)', 1, 9)
p5 = st.slider('General Acceptability for Sample(P)', 1, 9)

st.subheader("Sample Q")
q1 = st.slider('Taste for Sample(Q)', 1, 9)
q2 = st.slider('Texture for Sample(Q)', 1, 9)
q3 = st.slider('Appearance for Sample(Q)', 1, 9)
q4 = st.slider('Aroma for Sample(Q)', 1, 9)
q5 = st.slider('General Acceptability for Sample(Q)', 1, 9)

st.subheader("Sample R")
r1 = st.slider('Taste for Sample(R)', 1, 9)
r2 = st.slider('Texture for Sample(R)', 1, 9)
r3 = st.slider('Appearance for Sample(R)', 1, 9)
r4 = st.slider('Aroma for Sample(R)', 1, 9)
r5 = st.slider('General Acceptability for Sample(R)', 1, 9)

st.subheader("Sample S")
s1 = st.slider('Taste for Sample(S)', 1, 9)
s2 = st.slider('Texture for Sample(S)', 1, 9)
s3 = st.slider('Appearance for Sample(S)', 1, 9)
s4 = st.slider('Aroma for Sample(S)', 1, 9)
s5 = st.slider('General Acceptability for Sample(S)', 1, 9)

st.subheader("Sample T")
t1 = st.slider('Taste for Sample(T)', 1, 9)
t2 = st.slider('Texture for Sample(T)', 1, 9)
t3 = st.slider('Appearance for Sample(T)', 1, 9)
t4 = st.slider('Aroma for Sample(T)', 1, 9)
t5 = st.slider('General Acceptability for Sample(T)', 1, 9)

st.text("___"*100)

if st.button("Submit Questionnare"):
    if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
        cred_obj = firebase_admin.credentials.Certificate('qdataapp-firebase.json')
        firebase_admin.initialize_app(cred_obj, {
        'databaseURL':"https://qdataapp-default-rtdb.firebaseio.com/"
        })

    try:
        ref2 = db.reference("/Users/Q0X3NK0ZiFQgDaly4GQ4XdDhaQ43/Questionnaires/Diamond20L1QThq/Count")
        a = ref2.get()
        print(type(a))
        n_a = int(a) + 1

        myData = {
            generateRandom() : {
                "Sample": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20",
                "Taste": str([a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1, n1, o1, p1, 
                                q1, r1, s1, t1]),
                "Texture": str([a2, b2, c2, d2, e2, f2, g2, h2, i2, j2, k2, l2, m2, n2, o2, p2, 
                                q2, r2, s2, t2]),
                "Appearance": str([a3, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, 
                                q3, r3, s3, t3]),
                "Aroma": str([a4, b4, c4, d4, e4, f4, g4, h4, i4, j4, k4, l4, m4, n4, o4, p4, 
                                q4, r4, s4, t4]),
                "General Acceptability": str([a5, b5, c5, d5, e5, f5, g5, h5, i5, j5, k5, l5, m5, n5, o5, p5, 
                                q5, r5, s5, t5]),
                "Pendant":  str([int(n_a), int(n_a), int(n_a), int(n_a), int(n_a), int(n_a), int(n_a), int(n_a),
                                    int(n_a), int(n_a), int(n_a), int(n_a), int(n_a),
                                        int(n_a), int(n_a), int(n_a), int(n_a), int(n_a), int(n_a), int(n_a)])
            }
        }



        with open("jsondata.json", "w") as sd:
                    json.dump(myData, sd)

        ref2.set(str(n_a))


        ref = db.reference("/Users/Q0X3NK0ZiFQgDaly4GQ4XdDhaQ43/Questionnaires/Diamond20L1QThq/CollectedData/" + generateRandom())
        with open("jsondata.json", "r") as f:
            file_contents = json.load(f)

        for key, value in file_contents.items():
            ref.set(value)

        

        st.success('Data added Successfully')   
    except Exception:
        st.error('An Error Occurred')
    

