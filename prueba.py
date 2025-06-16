import streamlit as st
from PIL import Image
import base64
import os
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(
    page_title="NarcoImpact",
    layout="wide",
    page_icon="📊",
)

# Función para crear enlace que ABRE el PDF en nueva pestaña
def get_pdf_view_link(pdf_url, button_text="📄 Ver memoria completa (PDF)"):
    return f'''
    <a href="{pdf_url}" 
       target="_blank" 
       style="background-color: #111827; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: 500; display: inline-block;">
       {button_text}
    </a>
    '''

# CSS personalizado
st.markdown(""" 
<style>
    .stApp { background-color: #f5f5f7; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    h1, h2, h3, h4, h5, h6, .stMarkdown { font-family: -apple-system, BlinkMacSystemFont, sans-serif; color: #1d1d1f; }
    .graph-card { background: white; border-radius: 12px; padding: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: all 0.3s ease; margin-bottom: 30px; border: 1px solid #e0e0e0; }
    .graph-card:hover { transform: scale(1.02); box-shadow: 0 6px 12px rgba(0,0,0,0.15); }
    .graph-title { font-size: 1.4rem; font-weight: 600; margin-bottom: 15px; color: #0066cc; display: flex; align-items: center; gap: 10px; }
    .graph-image-container { border-radius: 8px; overflow: hidden; margin-bottom: 15px; text-align: center; background: #fafafa; padding: 15px; }
    .section { background: white; border-radius: 12px; padding: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 30px; }
    @keyframes subtleZoom { 0% { transform: scale(1); } 100% { transform: scale(1.01); } }
    .zoom-effect:hover { animation: subtleZoom 0.3s forwards; }
    blockquote { border-left: 4px solid #0066cc; padding-left: 15px; color: #333; font-style: italic; margin: 20px 0; }
    
    /* Animaciones para motivación */
    .motivation-container { background: white; border-radius: 12px; padding: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 30px; }
    .motivation-item { padding: 15px; margin-bottom: 15px; border-left: 3px solid #0066cc; transition: all 0.3s; }
    .motivation-item:hover { background-color: #f0f7ff; transform: translateY(-3px); }
    .pulse-button { animation: pulse 2s infinite; }
    @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.03); } 100% { transform: scale(1); } }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    .fade-in { animation: fadeIn 1.5s; }
</style>
""", unsafe_allow_html=True)

# ENCABEZADO
st.markdown("""
<div style='background-color: #111827; padding: 2rem; border-radius: 0 0 12px 12px; margin-bottom: 40px;'>
    <h1 style='color: white; text-align: center; font-weight: 600; letter-spacing: -0.5px;'>NarcoImpact</h1>
    <p style='color: #a1a1a6; text-align: center; font-size: 1.1rem;'>Análisis comparativo de políticas antidroga</p>
</div>
""", unsafe_allow_html=True)

# INTRODUCCIÓN
with st.container():
    st.markdown("""
    <div class="section">
        <h2 style='color: #1d1d1f; margin-bottom: 20px;'>¿Qué es NarcoImpact?</h2>
        <p style='line-height: 1.6; font-size: 20px;'>
        <strong>NarcoImpact</strong> es un proyecto de análisis comparativo que evalúa científicamente los resultados de dos modelos antagónicos:
        </p>
        <ul style='line-height: 1.6; font-size: 20px;'>
            <li><strong>Modelo prohibitivo (EE.UU.):</strong> Basado en la "Guerra contra las Drogas" iniciada en 1970, con enfoque punitivo y altas tasas de encarcelamiento.</li>
            <li><strong>Modelo de Reducción de Daños (Suiza):</strong> Implementado desde 1994 mediante la política de los Cuatro Pilares, tratando la adicción como problema de salud pública.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# SECCIÓN DE MOTIVACIÓN
with st.container():
    st.markdown("""
    <div class="motivation-container fade-in">
        <h2 style='color: #1d1d1f; margin-bottom: 20px;'>💡 Motivación del proyecto</h2>
        <p style='line-height: 1.6; font-size: 20px; margin-bottom: 25px;'>
        Este proyecto nace de la necesidad de abordar el problema de la drogodependencia desde una perspectiva basada en evidencia científica y resultados comprobables. Para ello queremos abordar los siguientes puntos:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Items de motivación
    with st.container():
        st.markdown("""
        <div class="motivation-item">
            <h3 style='color: #1d1d1f;'>El problema multidimensional</h3>
            <p style='font-size: 20px;'> La drogodependencia no es solo un problema de salud pública según la OMS, sino que genera una cadena de problemas que afectan múltiples aspectos sociales, desde la violencia hasta el sistema judicial.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class="motivation-item">
            <h3 style='color: #1d1d1f;'>El fracaso del prohibicionismo</h3>
            <p style= 'font-size: 20px;'> EE.UU. implementó políticas de prohibición categórica en los 90s, resultando en miles de arrestos pero con un aumento constante de adictos y sobredosis, demostrando la inefectividad de este enfoque.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class="motivation-item">
            <h3 style='color: #1d1d1f;'>La alternativa suiza</h3>
            <p style= 'font-size: 20px;'> Suiza adoptó la estrategia de Reducción de Daños (parte de los Cuatro Pilares), obteniendo resultados notablemente mejores en salud pública y reinserción social.</p>
        </div>
        """, unsafe_allow_html=True)
    with st.container():
        st.markdown("""
        <div class="motivation-item">
            <h3 style='color: #1d1d1f;'>Impacto en los ODS (Objetivos de Desarrollo Sostenible) </h3>
            <p style='font-size: 20px;'>
            Como se detalla en el Capítulo 3, este proyecto contribuye directamente a:
            </p>
            <ul style='font-size: 20px;'>
                <li><strong>ODS 3 (Salud):</strong> Reducción del 60% en muertes por sobredosis en Suiza a comparación del aumento del 400% en EE.UU.</li>
                <li><strong>ODS 16 (Justicia):</strong> Encarcelamiento 6-10 veces mayor para afroamericanos por delitos de drogas (Capítulo 2)</li>
                <li><strong>ODS 11 (Ciudades):</strong> Programas suizos redujeron el crimen asociado en un 35% (Federal Office of Public Health, 2008)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# SECCIÓN DE MEMORIA
with st.container():
    st.markdown("""<a name="memoria-completa"></a>""", unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
        <h2 style='color: #1d1d1f; margin-bottom: 20px;'>📑 Memoria completa del proyecto</h2>
        <p style='line-height: 1.6; font-size: 20px;'>
        Para conocer todos los detalles metodológicos, análisis completos y conclusiones detalladas de nuestra investigación, puedes descargar la memoria completa del proyecto:
        </p>
        <div style='text-align: center; margin-top: 25px;'>
    """, unsafe_allow_html=True)
    
    pdf_url = 'https://drive.google.com/file/d/1iDULcqOpAHFk2tJlrPOZN70J-vGdfQuG/view?usp=drive_link'
    st.markdown(get_pdf_view_link(pdf_url), unsafe_allow_html=True)

# SECCIÓN DE TÍTULO DE GRÁFICOS
with st.container():
    st.markdown("""
    <div class="section fade-in">
        <h2 style='color: #1d1d1f; margin-bottom: 20px;'>📈 Estudios / Gráficos</h2>
        <p style='line-height: 1.6; font-size: 20px;'>
        A continuación, se presentan representaciones gráficas que comparan los resultados de las políticas antidroga en EE.UU. y Suiza. Estos estudios visuales nos permiten observar, de forma clara, las consecuencias sanitarias de cada enfoque.
        </p>
    </div>
    """, unsafe_allow_html=True)

# GRÁFICO 1
with st.container():
    st.markdown("""
    <div class="graph-card zoom-effect">
        <div class="graph-title">📊 Muertes por sobredosis por cada 100,000 habitantes – EE.UU vs Suiza</div>
    """, unsafe_allow_html=True)
    img1 = Image.open("evolucion de las sobredosis entre EEUU y Suiza.png")
    st.image(img1, width=1100)
    st.markdown("""
    <div style='line-height: 1.6; font-size: 20px;'>
        <p>El gráfico muestra una tendencia alarmante: en <strong>EE.UU.</strong> las muertes por sobredosis han aumentado significativamente desde 2000, alcanzando más de 30 muertes por cada 100,000 habitantes en 2022.</p>
        <p>En contraste, <strong>Suiza</strong> ha logrado mantener cifras estables y bajas gracias a la adopción de políticas de reducción de daños como salas de consumo supervisado y programas de tratamiento integral.</p>
        <p>Esto evidencia que la estrategia suiza ha sido más efectiva en reducir la mortalidad asociada al consumo de drogas.</p>
    </div>
""", unsafe_allow_html=True)

# GRÁFICO 2 - EVOLUCIÓN DE TASA DE DROGADICCIÓN EN SUIZA
with st.container():
    st.markdown("""
    <div class="graph-card zoom-effect">
        <div class="graph-title">📉 Evolución de la tasa de drogadicción en Suiza (1990-2023)</div>
    """, unsafe_allow_html=True)
    
    img_suiza = Image.open("evolucion_droga_suiza.png")  
    st.image(img_suiza, width=900)
    
    st.markdown("""
        <div style='line-height: 1.6; font-size: 20px;'>
            <p>El gráfico muestra la evolución de las tasas de drogadicción en Suiza tras la implementación de su política de <strong>Reducción de Daños</strong> (1994):</p>
            <h4 style='color: #1d1d1f; margin-top: 15px;'>Tendencias clave:</h4>
            <ul>
                <li><strong>Crisis de los 90s:</strong> Pico máximo coincidiendo con la epidemia de heroína.</li>
                <li><strong>1994-2000:</strong> Implementación de los Cuatro Pilares (prevención, terapia, reducción de daños, represión).</li>
                <li><strong>2000-2023:</strong> Reducción sostenida de casos gracias a:
                    <ul>
                        <li>Salas de consumo supervisado</li>
                        <li>Programas de sustitución (metadona)</li>
                        <li>Reinserción social</li>
                    </ul>
                </li>
            </ul>
            <p><strong>Impacto:</strong> Las muertes relacionadas con drogas disminuyeron un 60% entre 1995 y 2020 (Fuente: Oficina Federal de Estadística Suiza).</p>
            <blockquote>"El modelo suizo demuestra que tratar la adicción como un problema de salud -no penal- salva vidas."</blockquote>
        </div>
    </div>
    """, unsafe_allow_html=True)

# GRÁFICO 3 - MUERTES POR GÉNERO
with st.container():
    img3 = Image.open("grafico donut EEUU.jpg")
    img4 = Image.open("grafico donut Suiza.jpg")

    st.markdown("""
    <div class="graph-card zoom-effect">
        <div class="graph-title">⚖️ Muertes por drogadicción en función del género en EE.UU. y Suiza (1995-2023)</div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(img3, width=500, caption="Muertes por drogadicción en EE.UU.")
    
    with col2:
        st.image(img4, width=500, caption="Muertes por drogadicción en Suiza")

    st.markdown("""
        <div style='line-height: 1.6; font-size: 20px;'>
            <h4 style='color: #1d1d1f; margin-top: 15px;'>Hallazgos clave:</h4>
            <ol>
                <li><strong>Diferencias de género en las muertes relacionadas con drogas:</strong><br>
                   <ul>
                      <li> Tomando los datos obtenidos de los gráficos, y realizando la media: </li>
                      <li>El 68,15 % de las muertes por drogadicción corresponden a hombres.</li>
                      <li>El 31,85 % de las muertes por drogadicción corresponden a mujeres.</li>
                  </ul>

                  <em>Los datos reflejan una marcada disparidad en la mortalidad, posiblemente vinculada a patrones de consumo y acceso a tratamientos.</em>
                </li>
                <li style='margin-top: 10px;'><strong>Evolución temporal y tendencias:</strong><br>
                    - Los hombres representan la mayoría de muertes en todas las décadas<br>
                    - Aunque la brecha de género es persistente, la estabilización de cifras post-2010 sugiere avances en prevención y tratamiento<br>
                </li>
            </ol>
            <p><strong>Interpretación:</strong> El gráfico subraya la necesidad de enfoques diferenciados por género en las políticas de reducción de daños, destacando:</p>
            <ul>
                <li>La mayor vulnerabilidad de los hombres ante el consumo riesgoso</li>
                <li>La importancia de intervenciones específicas para mujeres</li>
                <li>El impacto positivo de las estrategias de salud pública en la estabilidad de las cifras</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Cargar datos para mapas
data = pd.read_csv('datos EEUU.csv', sep=';', encoding='latin1')

# Diccionario de nombres completos a códigos de estado
state_abbr = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
    'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
    'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT',
    'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM',
    'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
    'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}

# ================================
# 📌 GRÁFICO 4: Mapa de Calor de la Media
# ================================
with st.container():
    st.markdown("""
    <div class="graph-card zoom-effect">
        <div class="graph-title">🌡️ Mapa de calor: Promedio de muertes por sobredosis por estado (EE.UU. 1999-2015)</div>
        <div style='line-height: 1.6; font-size: 20px; margin-bottom: 20px;'>
            Este mapa muestra el <strong>promedio histórico</strong> de muertes por sobredosis por cada 100,000 habitantes en cada estado. 
            Los tonos más oscuros indican mayores tasas de mortalidad, revelando patrones geográficos persistentes:
        </div>
    """, unsafe_allow_html=True)

    # Agrupar datos para calcular la media de todos los años
    avg_data = data.groupby('State', as_index=False)[['Deaths', 'Population']].sum()
    avg_data['DeathRate'] = (avg_data['Deaths'] / avg_data['Population']) * 100000
    avg_data['DeathRate'] = avg_data['DeathRate'].round().astype(int)
    avg_data = avg_data[avg_data['State'] != 'United States']
    avg_data['StateCode'] = avg_data['State'].map(state_abbr)

    # Crear el mapa de calor de la media de muertes
    fig_avg = px.choropleth(
        avg_data,
        locations='StateCode',
        locationmode='USA-states',
        color='DeathRate',
        scope='usa',
        color_continuous_scale='Blues',
        title="Promedio de tasa de muertes por drogas en EE.UU. (1999-2015)",
        hover_name='State',
        labels={'DeathRate': 'Muertes por cada 100,000 habitantes'}
    )

    # Ajustar el diseño del gráfico
    fig_avg.update_layout(
        margin=dict(l=0, r=0, t=40, b=0),
        coloraxis_colorbar=dict(
            title=dict(text='  ', font=dict(color='black')),
            tickfont=dict(color='black'),
            thickness=20,
            len=0.75
        ),
        geo=dict(
            lakecolor='rgb(255, 255, 255)',
            landcolor='rgb(217, 217, 217)',
            subunitcolor='black'
        ),
        title=dict(
            text="Promedio de tasa de muertes por drogas en EE.UU. (1999-2015)",
            font=dict(color='black', size=20)
        ),
        font=dict(color='black', size=14),
        paper_bgcolor='#f5f5f7',
        plot_bgcolor='#f5f5f7'
    )

    st.plotly_chart(fig_avg, use_container_width=True)

    st.markdown("""
    <div style='line-height: 1.6; font-size: 20px; margin-top: 20px;'>
        <strong>Hallazgos clave:</strong>
        <ul>
          <li><strong>Altas tasas en el oeste montañoso:</strong> Estados como Nuevo México y Utah destacan por sus elevadas tasas, lo que sugiere desafíos en salud pública regional.</li>
          <li><strong>Contrastes entre estados vecinos:</strong> Hay diferencias marcadas en la tasa de muertes entre estados contiguos, lo que indica desigualdades en políticas o acceso a tratamiento.</li>
          <li><strong>Baja incidencia en el centro-norte:</strong> Estados como Dakota del Norte e Iowa presentan tasas bajas, posiblemente por menor exposición a factores de riesgo.</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# ================================
# 📌 GRÁFICO 5: Mapa de Calor por Año (con selector y descripción mejorada)
# ================================
with st.container():
    st.markdown("""
    <div class="graph-card zoom-effect">
        <div class="graph-title">📅 Evolución anual: Muertes por sobredosis por estado</div>
        <div style='line-height: 1.6; font-size: 20px; margin-bottom: 20px;'>
            Seleccione un año para visualizar cómo variaron las tasas de mortalidad entre estados.
        </div>
    """, unsafe_allow_html=True)

    # Crear un selector de año
    selected_year = st.selectbox("Selecciona un año", sorted(data['Year'].unique()))

    # Filtrar los datos para el año seleccionado
    filtered_data = data[data['Year'] == selected_year]
    state_deaths = filtered_data.groupby('State')['Deaths'].sum().reset_index()
    pop_data = filtered_data.groupby('State')['Population'].mean().reset_index()
    state_deaths = state_deaths.merge(pop_data, on='State', how='left')
    state_deaths['DeathRate'] = (state_deaths['Deaths'] / state_deaths['Population']) * 100000
    state_deaths['DeathRate'] = state_deaths['DeathRate'].round().astype(int)
    state_deaths = state_deaths[state_deaths['State'] != 'United States']
    max_value = state_deaths['DeathRate'].max()
    state_deaths['StateCode'] = state_deaths['State'].map(state_abbr)

    # Crear el mapa anual
    fig = px.choropleth(
        state_deaths,
        locations='StateCode',
        locationmode='USA-states',
        color='DeathRate',
        scope='usa',
        color_continuous_scale='Greens',
        range_color=[0, max_value],
        title=f"Tasa anual de muertes por drogas en EE.UU. ({selected_year})",
        hover_name='State',
        labels={'DeathRate': 'Muertes por cada 100,000 habitantes'}
    )

    # Ajustar el diseño del gráfico
    fig.update_layout(
        margin=dict(l=0, r=0, t=40, b=0),
        coloraxis_colorbar=dict(
            title=dict(text='  ', font=dict(color='black')),
            tickfont=dict(color='black'),
            thickness=20,
            len=0.75
        ),
        geo=dict(
            lakecolor='rgb(255, 255, 255)',
            landcolor='rgb(217, 217, 217)',
            subunitcolor='black'
        ),
        title=dict(
            text=f'Tasa de muertes por drogas en EE.UU. ({selected_year})',
            font=dict(color='black', size=20)
        ),
        font=dict(color='black', size=14),
        paper_bgcolor='#f5f5f7',
        plot_bgcolor='#f5f5f7'
    )

    st.plotly_chart(fig, use_container_width=True)

    
# CONCLUSIONES
with st.container():
    st.markdown("""
    <div class="section">
        <h2 style='color: #1d1d1f; margin-bottom: 20px;'>📌 Conclusiones validadas</h2>
        <div style='line-height: 1.6; font-size: 20px'>
            <ul>
                  <li><strong>Las políticas punitivas en EE.UU. han demostrado ser ineficaces,</strong> especialmente en estados como Nuevo México, donde las tasas de muertes por drogas siguen siendo elevadas.</li>
                  <li><strong>El enfoque de reducción de daños, aplicado en Suiza y Dakota del Norte, ha mostrado mejores resultados,</strong> priorizando la salud pública sobre la criminalización del consumo.</li>
                <li><strong>El estudio promueve la necesidad de reformar las políticas antidrogas,</strong> adoptando estrategias basadas en evidencia y centradas en la minimización de daños, con supervisión adecuada.</li>
            </ul>

            <blockquote>"La evidencia es clara: tras 30 años de datos, la reducción de daños salva vidas, ahorra recursos y protege derechos humanos" (Conclusión, Capítulo 8)</blockquote>
        </div>
    </div>
    """, unsafe_allow_html=True)

# BIBLIOGRAFÍA
with st.container():
    st.markdown("""
    <div class="section">
        <h2 style='color: #1d1d1f; margin-bottom: 20px;'>📚 Bibliografía y recursos</h2>
        <div style='line-height: 1.6;'>
            <ul style='list-style-type: none; padding-left: 0;'>
                <li style='margin-bottom: 15px;'><a href="https://catalog.data.gov/dataset/" target="_blank" style='color: #0066cc; text-decoration: none;'>Gobierno de EE.UU. - Datos oficiales</a></li>
                <li style='margin-bottom: 15px;'><a href="https://www.bfs.admin.ch/bfs/en/home.html" target="_blank" style='color: #0066cc; text-decoration: none;'>Confederación Suiza - Oficina Federal de Estadística</a></li>
                <li style='margin-bottom: 15px;'><a href="https://www.bag.admin.ch/bag/en/home/strategie-und-politik/politische-auftraege-und-aktionsplaene/drogenpolitik/vier-saeulen-politik.html" target="_blank" style='color: #0066cc; text-decoration: none;'>Política de los Cuatro Pilares de Suiza</a></li>
                <li style='margin-bottom: 15px;'><a href="https://hri.global/what-is-harm-reduction/spanish" target="_blank" style='color: #0066cc; text-decoration: none;'>Harm Reduction International</a></li>
                <li style='margin-bottom: 15px;'><a href="https://www.infobae.com/wapo/2024/05/15/las-muertes-por-sobredosis-en-estados-unidos-superaron-las-100000-por-tercer-ano-consecutivo/" target="_blank" style='color: #0066cc; text-decoration: none;'>CDC WONDER – Estadísticas de sobredosis</a></li>
                <li style='margin-bottom: 15px;'><a href="https://www.swissinfo.ch/spa/economia/principio-de-los-cuatro-pilares-_suiza-pionera-en-pol%C3%ADtica-humana-en-materia-de-drogas/42102234" target="_blank" style='color: #0066cc; text-decoration: none;'>SwissInfo - Suiza pionera en política humana en drogas</a></li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div style='text-align: center; color: #86868b; font-size: 0.9rem; padding: 30px 0 20px 0;'>
    © 2025 NarcoImpact | Proyecto académico UPV | Grado en Ciencia de Datos | Todos los derechos reservados
</div>
""", unsafe_allow_html=True)
  
            
  
   
