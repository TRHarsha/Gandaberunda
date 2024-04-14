import streamlit as st

# Title of the app
st.title("Gandaberunda - AI-based Helping Hands for Police Investigation")

# Case details
st.write("### About the case")
st.write("Date: 18-02-2024, at 07:00 am, the complainant/injured, Mr. Eshwarappa K H, son of Hanumanthappa, appeared at the police station and provided a statement regarding the incident.")
st.write("The summary of the complaint is as follows: On the date 15-02-2024, when the complainant was riding his motorcycle, KA-14 EW-8286, around 2:15 pm, near the Tungabhadra River bridge in the Shivamogga, Holaluru village area on the Holaluru-Holehonnuru tar road, he met his relative Rudregowda, who was also on a motorcycle. The complainant parked his bike on the left side of the road and was speaking with Rudregowda when a car, KA-01 MF-9153, driven by Nagarjuna, was coming from Sanyasikodamagri towards Holaluru at a high speed and without caution. It collided with the complainant's motorcycle.")

st.write("### Departments involved")
departments = {
    "Local Police Station": "The incident was reported at a police station, so the local police will be the primary department involved in investigating the case. They will gather evidence, interview witnesses, and file a prosecution report based on the complaint filed by Mr. Hanumanthappa.",
    "Traffic Police": "Since the incident involves a road accident, the traffic police department may also be involved in assessing the scene of the accident, analyzing any traffic violations, and gathering information related to vehicle movement and speed.",
    "Forensic Science Laboratories (FSL)": "FSL may provide scientific analysis and expertise to support the investigation, such as examining the vehicle involved in the accident for any mechanical faults or analyzing forensic evidence related to the incident.",
    "Medical Services": "Medical services may be required to provide treatment to the injured party, Mr. Eshwarappa K H. The hospital where Mr. Eshwarappa was admitted, Surji Hospital in Shimoga, may also be involved in providing medical records and assessments related to his injuries.",
    "Legal Department": "Legal experts may be consulted to review the prosecution report and provide guidance on legal proceedings against the accused, Nagarjuna, the driver of car No. 9153.",
    "Witness Protection Unit": "If there are witnesses to the incident, the witness protection unit may provide support and ensure their safety during the investigation and legal proceedings.",
    "Specialized Investigation Units": "Depending on the complexity of the case and any specific issues involved, specialized investigation units such as the Crime Branch or Special Task Force may also provide support in gathering evidence and conducting investigations."
}

for department, response in departments.items():
    st.write(f"- {department}")
    st.write(f"    {response}")

# Display the response from the departments
st.write("### Departments' responses")
responses = {
    "Local Police Station": "We have gathered evidence, interviewed witnesses, and filed a prosecution report based on the complaint filed by Mr. Hanumanthappa.",
    "Traffic Police": "We have analyzed the scene of the accident and found that the driver of the car, Nagarjuna, was driving at a high speed and without caution. We have also gathered information related to vehicle movement and speed.",
    "Forensic Science Laboratories (FSL)": "We have analyzed the vehicle involved in the incident for any mechanical faults and found no issues. We have also analyzed the forensic evidence related to the incident and provided our report to the investigating team.",
    "Medical Services": "Mr. Eshwarappa K H was admitted to Surji Hospital in Shimoga and received medical treatment. We have provided medical records and assessments related to his injuries to the investigating team.",
    "Legal Department": "We have reviewed the prosecution report and provided our guidance on legal proceedings against the accused, Nagarjuna, the driver of car No. 9153. The accused has been charged with rash driving, causing grievous hurt, and other relevant sections of the Indian Penal Code.",
    "Witness Protection Unit": "There were no witnesses to the incident. If any witnesses come forward, we will ensure their safety during the investigation and legal proceedings.",
    "Specialized Investigation Units": "We are not involved in this case as it does not require our expertise."
}

for department, response in responses.items():
    st.write(f"- {department}")
    st.write(f"    {response}")