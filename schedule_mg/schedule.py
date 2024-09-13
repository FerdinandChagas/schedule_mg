import pandas as pd
import re

class Turma:

    def __init__(self,codigo,disciplina,professor,turma,periodo,curso,ch,horario,bloco,tipo):
        self.codigo = codigo
        self.disciplina = disciplina
        self.professor = professor
        self.turma = turma
        self.periodo = periodo
        self.curso = curso
        self.ch = ch
        self.horario = horario
        self.bloco = bloco
        self.tipo = tipo
    
    def __repr__(self):
        return f'Turma(codigo={self.codigo}, disciplina={self.disciplina}, professor={self.professor}, turma={self.turma}, periodo={self.periodo}, curso={self.curso}, carga-horaria={self.ch}, horario={self.horario}, bloco={self.bloco}, tipo={self.tipo})'

def verifica_horario(horarios_professor, horarios):
    
    for turma_professor in horarios_professor:
        for outra_turma in horarios:
            if (turma_professor.professor != outra_turma.professor) and (turma_professor.periodo==outra_turma.periodo) and (turma_professor.bloco==outra_turma.bloco) and (turma_professor.curso==outra_turma.curso):
                if verificar_choque(turma_professor.horario, outra_turma.horario):
                    descreve_choque(turma_professor, outra_turma)

def verificar_choque(horario1, horario2):
    dias1, turno1, horarios1 = extrair_componentes(horario1)
    dias2, turno2, horarios2 = extrair_componentes(horario2)

    if turno1 != turno2:
        return False  

    if any(dia in dias2 for dia in dias1):
        if any(horario in horarios2 for horario in horarios1):
            return True
    return False

def extrair_componentes(expressao):
    turno_match = re.search(r'[MTN]', expressao)
    
    if turno_match:
        idx_turno = turno_match.start()
        
        dias = expressao[:idx_turno]
        turno = expressao[idx_turno]
        horarios = expressao[idx_turno + 1:]

        dias = list(map(int, list(dias)))
        horarios = list(map(int, list(horarios)))

        return dias, turno, horarios
    else:
        raise ValueError("A expressão não contém um turno válido (M, T, N).")

def validar_horario(expressao):
    padrao = r"^[2-6]+[MTN][1-9]+$"
    return bool(re.match(padrao, expressao))

def descreve_choque(turma1, turma2):
    print(f"Choque de horários no {turma1.periodo}o período:")
    print(f"{turma1.codigo} - {turma1.disciplina} - {turma1.professor} - {turma1.horario} - {turma1.bloco}")
    print(f"{turma2.codigo} - {turma2.disciplina} - {turma2.professor} - {turma2.horario} - {turma2.bloco}")

def converte_para_turmas(horarios):

    turmas = horarios.apply(lambda row: Turma(row['codigo'],row['disciplina'],row['professor'],row['turma'],row['periodo'],row['curso'],row['ch'],row['horario'],row['bloco'],row['tipo']), axis=1)
    return turmas