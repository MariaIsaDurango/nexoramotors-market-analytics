import pandas as pd
import numpy as np

print("Iniciando fusión de datasets...")

# ── CARGA ────────────────────────────────────────────
df_milan = pd.read_csv('data/coches_clean.csv')
df_flexi = pd.read_csv('data/used_cars_data.csv',
                        encoding='latin1', sep=';',
                        on_bad_lines='skip')

print(f'Milanuncios: {df_milan.shape[0]} filas')
print(f'Flexicar:    {df_flexi.shape[0]} filas')

# ── LIMPIEZA FLEXICAR ────────────────────────────────
ANO_REFERENCIA = 2021

df_flexi = df_flexi.rename(columns={
    'brand':         'marca',
    'model':         'modelo',
    'price (eur)':   'precio_eur',
    'year':          'ano_vehic',
    'mileage (kms)': 'km',
    'fuel':          'combustible',
    'gearbox':       'transmision',
    'location':      'ubicacion'
})

df_flexi['precio']     = (df_flexi['precio_eur'] / 1000).round(2)
df_flexi['antiguedad'] = ANO_REFERENCIA - df_flexi['ano_vehic'].astype(int)
df_flexi['marca']      = df_flexi['marca'].str.upper()
df_flexi['ubicacion']  = df_flexi['ubicacion'].str.title()
df_flexi['combustible'] = df_flexi['combustible'].str.capitalize()
df_flexi['combustible'] = df_flexi['combustible'].replace({
    'Diésel': 'Diesel', 'Díesel': 'Diesel'
})
df_flexi['transmision'] = df_flexi['transmision'].str.lower()
df_flexi['puertas']           = 5.0
df_flexi['cv']                = np.nan
df_flexi['particular']        = 'Profesional'
df_flexi['stats_visto']       = 0
df_flexi['stats_favorito']    = 0
df_flexi['stats_contactado']  = 0
df_flexi['engagement_score']  = 0.0

df_flexi = df_flexi.drop(columns=['precio_eur', 'engine'])

# ── SEGMENTOS Y RANGOS ───────────────────────────────
bins   = [0, 5, 10, 20, 35, 999]
labels = ['Económico (<5K)','Accesible (5-10K)',
          'Medio (10-20K)','Premium (20-35K)','Lujo (>35K)']
df_flexi['segmento_precio'] = pd.cut(
    df_flexi['precio'], bins=bins, labels=labels)

bins_ant   = [0, 3, 7, 12, 999]
labels_ant = ['Casi nuevo (0-3a)','Reciente (4-7a)',
              'Seminuevo (8-12a)','Clásico (>12a)']
df_flexi['rango_antiguedad'] = pd.cut(
    df_flexi['antiguedad'], bins=bins_ant,
    labels=labels_ant, include_lowest=True)

df_flexi['precio_por_cv'] = np.nan

# ── AÑADIR COLUMNA FUENTE ────────────────────────────
df_milan['fuente'] = 'Milanuncios'
df_flexi['fuente'] = 'Flexicar'

# ── ALINEAR COLUMNAS ─────────────────────────────────
cols_finales = [
    'marca','modelo','ano_vehic','antiguedad','rango_antiguedad',
    'km','combustible','puertas','cv','transmision',
    'ubicacion','particular','precio','segmento_precio',
    'precio_por_cv','stats_visto','stats_favorito',
    'stats_contactado','engagement_score','fuente'
]

df_milan['fuente'] = 'Milanuncios'
df_milan_final = df_milan.reindex(columns=cols_finales)
df_flexi_final  = df_flexi.reindex(columns=cols_finales)

# ── FUSIÓN ───────────────────────────────────────────
df_total = pd.concat([df_milan_final, df_flexi_final],
                      ignore_index=True)

# ── LIMPIEZA FINAL ───────────────────────────────────
df_total = df_total.dropna(subset=['precio','km','ano_vehic'])
df_total = df_total.drop_duplicates()

# ── GUARDAR ──────────────────────────────────────────
df_total.to_csv('data/coches_fusionado.csv', index=False)

print()
print('=' * 50)
print('RESULTADO FINAL')
print('=' * 50)
print(f'Total filas:      {df_total.shape[0]}')
print(f'Total columnas:   {df_total.shape[1]}')
print(f'Nulos totales:    {df_total.isnull().sum().sum()}')
print(f'Duplicados:       {df_total.duplicated().sum()}')
print()
print('Por fuente:')
print(df_total['fuente'].value_counts())
print()
print('Precio medio:     ', round(df_total['precio'].mean(), 2))
print('Segmentos:')
print(df_total['segmento_precio'].value_counts().sort_index())
print()
print('✅ Dataset fusionado guardado en data/coches_fusionado.csv')