from pickle import load
import streamlit as st

model = load(open('../models/decision_tree_regressor_42_pca.sav', 'rb'))
pca = load(open('../models/pca_42.sav', 'rb'))

st.title('Predicción de notas en el examen')

#'Hours_Studied', 'Attendance', 'Sleep_Hours', 'Previous_Scores',
#      'Tutoring_Sessions', 'Physical_Activity', 'Motivation_Level_num',
#      'Learning_Disabilities_num', 'Extracurricular_Activities_num',
#       'School_Type_num', 'Parental_Education_Level_num',
#       'Distance_from_Home_num', 'Family_Income_num', 'Gender_num',
#       'Internet_Access_num', 'Parental_Involvement_num',
#       'Teacher_Quality_num', 'Access_to_Resources_num',
#       'Peer_Influence_num']

#Esto se basa en el describe de explore
horas_estudio =st.slider('Horas de estudio', min_value= 0, max_value= 44, step=1)
asistencia = st.slider('Asistencia', min_value= 60, max_value= 100, step=1)
sueño = st.slider('Horas de sueño', min_value= 4, max_value= 10, step=1)
notas_previas = st.slider('Notas previas', min_value= 50, max_value= 100, step=5)
tutoria = st.slider('Sesiones de tutoría', min_value= 0, max_value= 8, step=1)
