from pickle import load
import streamlit as st

model = load(open('C:/Users/felip/repos/streamlit_proyect/streamlit_proyect/models/decision_tree_regressor_42_pca.sav', 'rb'))
pca = load(open('C:/Users/felip/repos/streamlit_proyect/streamlit_proyect/models/pca_4.sav', 'rb'))

st.title('Predicción de notas en el examen')

# Inputs
horas_estudio = st.slider('Horas de estudio', min_value=0, max_value=44, step=1)
asistencia = st.slider('Asistencia', min_value=60, max_value=100, step=1)
sueño = st.slider('Horas de sueño', min_value=4, max_value=10, step=1)
notas_previas = st.slider('Notas previas', min_value=50, max_value=100, step=5)
tutoria = st.slider('Sesiones de tutoría', min_value=0, max_value=8, step=1)
act_fisica = st.slider('Actividad física', min_value=0, max_value=6, step=1)
act_extracurriculares = st.toggle('Actividades extracurriculares')  # devuelve True/False
env_parental = st.radio('Involucramiento parental', ['Bajo', 'Medio', 'Alto'], index=0)
tipo_escuela = st.radio('Tipo de escuela', ['Pública', 'Privada'], index=0)
nivel_educacion_padres = st.radio('Nivel de educación de los padres', ['Media', 'Bachillerato', 'Universitario', 'Ninguna'], index=0)
influencia_compañeros = st.radio('Influencia de compañeros', ['Positiva', 'Negativa', 'Neutral'], index=0)

# Diccionarios
env_parental_dict = {'Bajo': 0, 'Medio': 1, 'Alto': 2}
tipo_escuela_dict = {'Pública': 0, 'Privada': 1}
nivel_educacion_padres_dict = {'Media': 0, 'Bachillerato': 1, 'Universitario': 2, 'Ninguna': -1}
influencia_compañeros_dict = {'Positiva': 0, 'Negativa': 1, 'Neutral': 2}

# Variables dummy no incluidas en el formulario
extras = [0] * 8

if st.button('Predecir'):
    try:
        input_data = [[
            horas_estudio,
            asistencia,
            sueño,
            notas_previas,
            tutoria,
            act_fisica,
            int(act_extracurriculares),  # directamente convertimos el booleano
            env_parental_dict[env_parental],
            tipo_escuela_dict[tipo_escuela],
            nivel_educacion_padres_dict[nivel_educacion_padres],
            influencia_compañeros_dict[influencia_compañeros],
            *extras
        ]]

        conversion_pca = pca.transform(input_data)
        prediccion = model.predict(conversion_pca)[0]
        st.success(f'Nota predecida: {prediccion:.2f}')
    except Exception as e:
        st.error(f'Ocurrió un error: {e}')


