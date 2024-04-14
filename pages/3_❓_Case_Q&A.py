import streamlit as st

st.title("Chatbot: Police Investigation Inquiry")

questions = [
    "What caused the accident on February 15, 2024, on the Tungabhadra River bridge in Holaluru village?",
    "What injuries or damages were sustained due to the accident?",
    "What evidence was collected at the scene of the accident?",
    "Was the driver of the car, Nagarjuna, under the influence of any substances at the time of the accident?",
    "What were the outcomes or consequences for Nagarjuna following the investigation?"
]

answers = [
    "The accident was caused by Nagarjuna, the driver of a car (KA-01 MF-9153), who was driving at a high speed and without caution. His reckless driving led him to collide with the complainant's motorcycle, which was parked on the left side of the road.",
    "The complainant, Mr. Eshwarappa K H, and his motorcycle (KA-14 EW-8286) sustained damages due to the collision. Mr. Eshwarappa may have suffered injuries as well, but further medical reports would provide precise details on the extent of his injuries.",
    "Evidence collected at the scene included skid marks on the road, vehicle parts or debris, and any CCTV footage from nearby areas. Statements were also taken from the complainant, witnesses, and the driver of the car.",
    "Nagarjuna was subjected to a sobriety test and other assessments at the time of the investigation. The results showed that he was not under the influence of alcohol or any other substances at the time of the accident.",
    "Based on the investigation's findings, Nagarjuna was charged with reckless driving and causing an accident. He was fined for the traffic violations and may face legal consequences, including potential suspension of his driving license and possible criminal charges depending on the severity of the damages and injuries sustained."
]

for i in range(len(questions)):
    st.write("**Question:**", questions[i])
    st.write("**Answer:**", answers[i])
    st.write("---")