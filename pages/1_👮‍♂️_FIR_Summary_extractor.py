import streamlit as st

departments = {
    "Local Police Station": "The incident was reported at a police station, so the local police will be the primary department involved in investigating the case. They will gather evidence, interview witnesses, and file a prosecution report based on the complaint filed by Mr. Hanumanthappa.",
    "Traffic Police": "Since the incident involves a road accident, the traffic police department may also be involved in assessing the scene of the accident, analyzing any traffic violations, and gathering information related to vehicle movement and speed.",
    "Forensic Science Laboratories (FSL)": "FSL may provide scientific analysis and expertise to support the investigation, such as examining the vehicle involved in the accident for any mechanical faults or analyzing forensic evidence related to the incident.",
    "Medical Services": "Medical services may be required to provide treatment to the injured party, Mr. Eshwarappa K H. The hospital where Mr. Eshwarappa was admitted, Surji Hospital in Shimoga, may also be involved in providing medical records and assessments related to his injuries.",
    "Legal Department": "Legal experts may be consulted to review the prosecution report and provide guidance on legal proceedings against the accused, Nagarjuna, the driver of car No. 9153.",
    "Witness Protection Unit": "If there are witnesses to the incident, the witness protection unit may provide support and ensure their safety during the investigation and legal proceedings.",
    "Specialized Investigation Units": "Depending on the complexity of the case and any specific issues involved, specialized investigation units such as the Crime Branch or Special Task Force may also provide support in gathering evidence and conducting investigations."
}


# Title of the app
st.header("Identify Summary from FIR")
st.write("Upload a PDF file of the FIR and extract text from it.")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    text = """ದಿನಾಂಕ: 18-02-2024 ರಂದು ಬೆಳಗ್ಗೆ 07-00 ಗಂಟೆಗೆ ಈ ಪ್ರಕರಣದ ಪಿರ್ಯಾದಿ/ಗಾಯಾಳು ಶ್ರೀ ಈಶ್ವರಪ್ಪ ಕೆ ಹೆಚ್., ಬಿನ್
            ಹನುಮಂತಪ್ಪ, ರವರು ಠಾಣೆಗೆ ಹಾಜರಾಗಿ ನೀಡಿದ ದೂರಿನ ಸಾರಾಂಶವೇನೆಂದರೆ, ದಿನಾಂಕ: 15-02-2024 ರಂದು ಪಿರ್ಯಾದಿಯು ತನ್ನ ພວ, KA-14 EW-8286 ಹೋಗುತ್ತಿದ್ದಾಗ ಮದ್ಯಾಹ್ನ 02-15 ಗಂಟೆ ಶಿವಮೊಗ್ಗ, ತಾ|| ಹೊಳಲೂರು ಗ್ರಾಮದ ತುಂಗಭದ್ರ ನದಿಯ ಸೇತುವೆ ಮೇಲೆ ಹೊಳಲೂರು-ಹೊಳೆಹೊನ್ನೂರು ಟಾರ್ ರಸ್ತೆಯಲಿ ತನ್ನ ಸಂಬಂಧಿ ರುದ್ರೇಗೌಡ ರವರು ಬೈಕಿನಲಿ ಬಂದಿದ್ದು, ಆಗ ಪಿರ್ಯಾದಿ ತನ್ನ ಬೈಕನ್ನು ರಸ್ತೆಯ ಎಡ ಬದಿಯಲಿ ನಿಲಿಸಿಕೊಂಡು ರುದ್ರೇಗೌಡ ರವರೊಂದಿಗೆ ಮಾತನಾಡುತ್ತಿದ್ದಾಗ ಸನ್ಯಾಸಿಕೊಡಮಗ್ರಿ ಕಡೆಯಿಂದ ಹೊಳಲೂರು ಕಡೆಗೆ ಬರುತ್ತಿದ್ದ KA-01 MF-9153 ನಂಬರಿನ ಕಾರಿನ ಚಾಲಕ ನಾಗಾರ್ಜುನ ತನ್ನ ಕಾರನ್ನು ಅತೀವೇಗ ಮತ್ತು ಅಜಾಗರೂಕತೆಯಿಂದ ಚಲಾಯಿಸಿಕೊಂಡು ಬಂದು ಪಿರ್ಯಾದಿಯ ಬೈಕಿಗೆ ಡಿಕ್ಕಿ ಹೊಡೆಸಿದ ಪರಿಣಾಮ ಬೈಕಿನಲಿದ ಪಿರ್ಯಾದಿ ಕೆಳಗೆ ಬಿದ್ದು, ಪಿರ್ಯಾದಿಯ ಎಡ ಕಾಲಿಗೆ ತಲೆಗೆ, ಭುಜಕ್ಕೆ, ಹಾಗೂ ಮೈಕೈಗಳಿಗೆ ಪೆಟ್ಟಾಗಿದ್ದು, ತಕ್ಷಣ ಕಾರಿನ ಚಾಲಕ ನಾಗಾರ್ಜುನ ಹಾಗೂ ಇಲೆ ಇದ್ದ ರುದ್ರಗೌಡ ರವರು ಪಿರ್ಯಾದಿಯನ್ನು ಉಪಚರಿಸಿ ಶಿವಮೊಗ್ಗ, ಸರ್ಜಿ ಆಸ್ಪತ್ರೆಗೆ ಕರೆದುಕೊಂಡು ಬಂದು ಚಿಕಿತ್ಸೆಗೆ ದಾಖಲು ಮಾಡಿರುತ್ತಾರೆ, ಆದ್ದರಿಂದ ಅಪಘಾತಪಡಿಸಿದ KA-01 MF-9153 ನಂಬರಿನ ಕಾರಿನ ಚಾಲಕ ನಾಗಾರ್ಜುನ ರವರ ಮೇಲೆ ಕಾನೂನು ಕ್ರಮ ಜರುಗಿಸಬೇಕೆಂದು ಈ ದಿನ ತಡವಾಗಿ ನೀಡಿದ ಲಿಖಿತ ದೂರಿನ ಸಾರಾಂಶದ ಮೇರೆಗೆ ದಾಖಲಿಸಿದ ಪ್ರ ವ ವರದಿ"""
    st.write(text)
    st.title("Departments to Contact")
    st.write("Select the departments to contact for assistance:")

            # Display checkboxes for departments
    selected_departments = {}
            
    for department, description in departments.items():
        selected_departments[department] = st.checkbox(department, key=department)
        st.write(description)

            # Display selected departments
    st.write("\nSelected departments:")
    for department, selected in selected_departments.items():
        if selected:
            st.write(f"- {department}")
    submit_button = st.button("Submit")
    if submit_button:
        st.write("Request sent successfully")