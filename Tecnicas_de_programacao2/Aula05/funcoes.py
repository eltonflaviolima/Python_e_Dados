import pandas as pd
import seaborn as sns

def carregar_dataset(nome_dataset:str) -> pd.DataFrame:
    """Função para carregar um dataset do banco de dados do seabonrn

    Args:
        nome_dataset (str): nome do dataset a ser carregado

    Returns:
        pd.DataFrame: dataset
    """
    return sns.load_dataset(nome_dataset)