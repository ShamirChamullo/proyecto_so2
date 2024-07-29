import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Configurar estilo de los gráficos
sns.set(style="whitegrid")

# Función para generar gráficos
def generate_plots(df):
    # Histograma de la edad
    st.write("### Distribución de Edad")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['age'], bins=10, kde=True, color='skyblue')
    st.pyplot(plt.gcf())
    plt.clf()

    # Gráfico de torta para la variable 'target'
    st.write("### Distribución de Objetivo (Target)")
    target_counts = df['target'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(target_counts, labels=target_counts.index, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'])
    plt.title('Distribución de Objetivo')
    st.pyplot(plt.gcf())
    plt.clf()

    # Gráfico de dispersión con regresión lineal simple
    st.write("### Regresión Lineal: Presión Arterial vs Colesterol")
    plt.figure(figsize=(10, 6))
    sns.lmplot(x='restingBP', y='serumcholestrol', data=df, aspect=1.5, scatter_kws={'s':100}, line_kws={'color':'red'})
    plt.title('Regresión Lineal de Presión Arterial vs Colesterol')
    st.pyplot(plt.gcf())
    plt.clf()

    # Gráfico de barras para el recuento de la variable 'target'
    st.write("### Conteo de Objetivo")
    plt.figure(figsize=(8, 5))
    sns.countplot(x='target', data=df, palette='viridis')
    st.pyplot(plt.gcf())
    plt.clf()

    # Boxplot de 'oldpeak' por 'target'
    st.write("### Oldpeak por Objetivo")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='target', y='oldpeak', data=df, palette='Set2')
    st.pyplot(plt.gcf())
    plt.clf()

# Interfaz de usuario de Streamlit
st.title('Análisis de Datos de Pacientes')

uploaded_file = st.file_uploader("Selecciona un archivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(f"Datos cargados: {uploaded_file.name}")
    
    if not df.empty:
        st.write("### Vista previa de los datos")
        st.write(df.head())

        generate_plots(df)
    else:
        st.error("El archivo CSV está vacío.")
else:
    st.info("Por favor, sube un archivo CSV para analizar.")
