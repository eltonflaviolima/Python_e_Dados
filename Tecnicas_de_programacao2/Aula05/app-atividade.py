import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
from funcoes import carregar_dataset


# CORPO
## CORPO - Título da Aplicação
st.title("iNalyze")
st.subheader("A sua ferramenta de análise de dados")
st.write('---')


## CORPO - Carregando o dataset
nome_dataset = \
    st.text_input('Qual é o nome do dataset?', 
                  value='penguins')
if nome_dataset:
    df = carregar_dataset(nome_dataset)

        
# SIDEBAR
## SIDEBAR - Filtro dos campos
with st.sidebar:
    st.title('Filtros')
    cols_selected = \
        st.multiselect('Filtre os campos que deseja para a análise', 
                   options=list(df.columns),
                   default=list(df.columns))
        
    frac_sample = \
        st.slider('Define o percentual do dataset para análise',
                  min_value=1, max_value=100, value=50, step=1)

# filtra os campos selecionados
df_selected = df[cols_selected].sample(frac=frac_sample/100)
    
    
## CORPO - Info do dataset
with st.expander('Dados do Dataset'):
    st.header('Dados do Dataset')
    st.subheader('Primeiros Registros')
    st.dataframe(df_selected.head())

    st.subheader('Colunas')
    for col in df_selected.columns:
        st.markdown(f'- {col}')
        
    st.subheader('Dados Faltantes')
    st.write(df_selected.isna().sum()[df_selected.isna().sum() > 0])

    st.subheader('Estatísticas Descritivas')
    st.write(df_selected.describe())
    
## CORPO - Análise Univariada
st.header('Análise Univariada')
univar_campo = \
    st.selectbox(label='Selecione um campo numérico para avaliar a sua distribuição:',
             options=df_selected.select_dtypes(include=np.number).columns)

st.plotly_chart(px.histogram(data_frame=df_selected, x=univar_campo))
st.plotly_chart(px.box(data_frame=df_selected, y=univar_campo))

## CORPO - Análise Bivariada


### CORPO - Análise Bivariada - gráfico de dispersão

        
### CORPO - Análise Bivariada - gráfico de boxplot


### CORPO - Análise Bivariada - gráfico de pairplot