import pandas as pd

def normalize_text(serie):
    # to ascii:
    serie = serie.str.normalize('NFKD')
    serie = serie.str.encode("ascii","ignore")
    serie = serie.str.decode('ascii')
    # to lowercase:
    serie = serie.str.lower()
    return serie

def expandir_periodo(serie):

    mapeo_cod_semestres = { '10':'semestre 1',
                        '20':'semestre 2',
                        '11':'intersemestral 1',
                        '21':'intersemestral 2'}

    año = serie.str.slice(0,4)
    semestre = serie.str.slice(4).map(mapeo_cod_semestres)
    return año, semestre

def fecha_de_semestre(años, semestres):

    mapeo_cod_meses = { '10':'02',    # Febrero
                        '20':'06',    # Junio
                        '11':'08',    # Agosoto
                        '21':'12'}    # Diciembre

    mapeo_semestres_meses = {   'semestre 1':'02',          # Febrero
                                'intersemestral 1':'06',    # Junio
                                'semestre 2':'08',          # Agosoto
                                'intersemestral 2':'12'}    # Diciembre

    mapeo_completo = {}
    mapeo_completo.update(mapeo_cod_meses)
    mapeo_completo.update(mapeo_semestres_meses)

    fecha = años + '-' + semestres.map(mapeo_completo)
    fecha = pd.to_datetime(fecha)
    return fecha

def fill_digits(serie):

    ndigits = serie.str.len().max()
    filled = serie.str.zfill(ndigits)
    if serie.nunique() == filled.nunique():
        return filled
    else:
        return serie

def fix_factor_codes(col):
    factores = col.unique()
    cod_factores = {factor:str(i+1) for i, factor in enumerate(factores)}
    return col.map(cod_factores)

if __name__ == "__main__":

    # Loading the tables

    docentes_periodo = pd.read_csv('data/raw/docentes_periodo.csv', ';', encoding='ISO-8859-1')
    eval_docentes_periodo = pd.read_csv('data/raw/eval_docentes_periodo.csv', ';', encoding='ISO-8859-1')
    #mat_cursadas_rend_academico = pd.read_csv('data/raw/mat_cursadas_rend_academico.csv', ';', encoding='ISO-8859-1')
    #perfil_ingreso = pd.read_csv('data/raw/perfil_ingreso.csv', ';')
    rendimiento_academico = pd.read_csv('data/raw/rendimiento_academico.csv', ';', encoding='ISO-8859-1')

    area_icfes = pd.read_excel('data/raw/area_icfes.xlsx')
    creditos_periodo = pd.read_excel('data/raw/CREDITOS_PERIODO.xlsx')
    perfil_ingreso_v2 = pd.read_excel('data/raw/perfil_ingreso_v2.xlsx')
    materias_por_programa = pd.read_excel('data/raw/materias_por_programa.xlsx')
    pre_correquisito = pd.read_excel('data/raw/pre_correquisito.xlsx')
    mat_cursadas_rend_academico_v2 = pd.read_excel('data/raw/mat_cursadas_rend_academico_v2.xlsx')
    reingreso_aplazamiento = pd.read_excel('data/raw/reingreso_aplazamiento.xlsx')

    # fill missing values:
    nan_mask_CRED_INSCRITOS = mat_cursadas_rend_academico_v2.CRED_INSCRITOS.isna()
    mat_cursadas_rend_academico_v2[nan_mask_CRED_INSCRITOS] = mat_cursadas_rend_academico_v2[nan_mask_CRED_INSCRITOS].fillna(0)
    
    nan_mask_CRED_APROBADOS = mat_cursadas_rend_academico_v2.CRED_APROBADOS.isna()
    mat_cursadas_rend_academico_v2[nan_mask_CRED_APROBADOS] = mat_cursadas_rend_academico_v2[nan_mask_CRED_APROBADOS].fillna(0)
    
    perfil_ingreso_v2.EDAD = perfil_ingreso_v2.EDAD.fillna(22)

    # Dictinary with the tables, for iterating in next step:
    dfs = { "docentes_periodo":docentes_periodo,
            "eval_docentes_periodo":eval_docentes_periodo,
            "rendimiento_academico":rendimiento_academico,
            "area_icfes":area_icfes,
            "creditos_periodo":creditos_periodo,
            "perfil_ingreso_v2":perfil_ingreso_v2,
            "materias_por_programa":materias_por_programa,
            "pre_correquisito":pre_correquisito,
            "mat_cursadas_rend_academico_v2":mat_cursadas_rend_academico_v2,
            "reingreso_aplazamient":reingreso_aplazamiento}

    # For every table:
    for table_name, df in dfs.items():

        # make all numerical categorical variables a string:
        cols = df.columns
        num_categorical = [col for col in cols if 'COD' in col or 'PERIODO' in col]
        df[num_categorical] = df[num_categorical].astype(str)

        # fixing float variables:
        float_cols = [col for col in cols if 'NOTA' in col or 'CALIFICACION' in col]
        for col in df[float_cols]:
            df[col] = df[col].str.replace(',', '.').astype(float)
        #df[float_cols] = df[float_cols].str.replace(',', '.').astype(float)

        # getting column lists by type for the next steps
        cols_by_type = {k.name: v for k, v in (df.columns.to_series().groupby(df.dtypes).groups).items()}

        # fixing integers that loaded as float:
        fake_float_cols = [col for col in cols_by_type.pop('float64', []) if col not in float_cols]
        df[fake_float_cols] = df[fake_float_cols].astype(int)

        # Normalizing text
        text_cols = cols_by_type.pop('object', [])
        df[text_cols] = df[text_cols].apply(normalize_text, axis=0)

        # expandir datos: año y semestre
        periodo_col = [col for col in cols if col == 'PERIODO' or col == 'PERIODO_COHORTE']
        if periodo_col:
            df['AÑO'], df['SEMESTRE'] = expandir_periodo(df[periodo_col[0]])

            # expandir datos: fecha (datetime para series temporales)
            df['FECHA'] = fecha_de_semestre(df['AÑO'], df['SEMESTRE'])

    # Fix "COD_FACTOR" - "NOM_FACTOR" in "eval_docentes_periodo" table:
    eval_docentes_periodo['COD_FACTOR'] = fix_factor_codes(eval_docentes_periodo.NOM_FACTOR)
   
    # save each df to a csv
    for table_name, df in dfs.items():
        df.to_csv(f'data/cleaned/{table_name}.csv', index=False)