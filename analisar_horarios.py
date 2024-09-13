""" Script que verifica conflitos nos horários listados no arquivo horarios.csv"""

import argparse
import pandas as pd
from schedule_mg.schedule import verifica_horario,converte_para_turmas


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('arquivo', type=str, help="Arquivo .csv contendo a descrição dos horários por disciplina.")

    args = parser.parse_args()

    horarios = pd.read_csv(args.arquivo)

    horarios = horarios.dropna()

    todas_turmas = converte_para_turmas(horarios)
    verifica_horario(todas_turmas, todas_turmas)