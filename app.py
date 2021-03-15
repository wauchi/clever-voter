from VotingCalculator import VotingCalculator

import operator
import matplotlib.pyplot as plt
import matplotlib as mpl
import streamlit as st

mpl.style.use('seaborn-pastel')

st.title("Clever Voting")
st.write("Make fair votes great again! A simple voting system based on graph theory")

st.subheader("Categories")
st.write("Enter your categories which are available for selection")
categories = st.text_area("Categories (newline-separated)")
categories_prepared = categories.split("\n")

st.subheader("Votes")
st.write(
    "Enter your votes  \nEach line represents the votes of a single person in decreasing preference order  \nEach category has to be seperated with a ','")
st.write("Following categories are available: ")
st.write("  \n".join("• " + i if i else "" for i in categories_prepared))
votes = st.text_area("Votes (newline-separated)")
votes_prepared = votes.split("\n")

if st.button("Calucalte results"):
    try:
        calculator = VotingCalculator(categories_prepared, votes_prepared)
        results = calculator.calculate()
        st.header("The winner is: " + max(results.items(), key=operator.itemgetter(1))[0].capitalize())
        labels = []
        values = []
        for x,y in results.items():
            labels.append(x.capitalize())
            values.append(y)

        fig = plt.figure()
        plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, rotatelabels=True)
        st.pyplot(fig)
    except ValueError as e:
        st.error("Please enter a valid input. " + e.args[0].split(" ", 1)[0] + " is not a category")

