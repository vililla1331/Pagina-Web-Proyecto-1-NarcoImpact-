import streamlit as st
from PIL import Image
import base64
import os
import pandas as pd
import plotly.express as px
# Para lanzar la pagina web --->  python -m streamlit run prueba.py
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
        <strong>NarcoImpact</strong> es un proyecto que analiza el efecto de las políticas antidroga aplicadas por Estados Unidos (modelo de prohibición) y Suiza (modelo de reducción de daños).<br>
        El objetivo es demostrar, mediante datos reales, cuál estrategia resulta más efectiva en términos de salud pública, mortalidad y gestión del consumo.
        </p>
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
            <p style=font-size: 20px;> La drogodependencia no es solo un problema de salud pública según la OMS, sino que genera una cadena de problemas que afectan múltiples aspectos sociales, desde la violencia hasta el sistema judicial.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class="motivation-item">
            <h3 style='color: #1d1d1f;'>El fracaso del prohibicionismo</h3>
            <p style= font-size: 20px;> EE.UU. implementó políticas de prohibición categórica en los 90s, resultando en miles de arrestos pero con un aumento constante de adictos y sobredosis, demostrando la inefectividad de este enfoque.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class="motivation-item">
            <h3 style='color: #1d1d1f;'>La alternativa suiza</h3>
            <p style= font-size: 20px;> Suiza adoptó la estrategia de Reducción de Daños (parte de los Cuatro Pilares), obteniendo resultados notablemente mejores en salud pública y reinserción social.</p>
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
    
    pdf_url = 'https://drive.google.com/file/d/1miOLYEMw7HF9c5ndxefcZa7f0cq211ga/view?usp=sharing'
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
        <p>Este gráfico muestra una tendencia alarmante: en <strong>EE.UU.</strong> las muertes por sobredosis han aumentado significativamente desde 2000, alcanzando más de 30 muertes por cada 100,000 habitantes en 2022.</p>
        <p>En contraste, <strong>Suiza</strong> ha logrado mantener cifras estables y bajas gracias a la adopción de políticas de reducción de daños como salas de consumo supervisado y programas de tratamiento integral.</p>
        <p>Esto evidencia que la estrategia suiza ha sido más efectiva en reducir la mortalidad asociada al consumo de drogas.</p>
    </div>
""", unsafe_allow_html=True)


# GRÁFICO 2 - EVOLUCIÓN DE TASA DE DROGADICCIÓN EN SUIZA (CORREGIDO)
with st.container():
    st.markdown("""
    <div class="graph-card zoom-effect">
        <div class="graph-title">📉 Evolución de la tasa de drogadicción en Suiza (1990-2023)</div>
    """, unsafe_allow_html=True)
    
    # Asegúrate de tener esta imagen en tu directorio
    img_suiza = Image.open("evolucion_droga_suiza.png")  
    st.image(img_suiza, width=900)
    
    st.markdown("""
        <div style='line-height: 1.6; font-size: 20px;'>
            <p>Este gráfico muestra la evolución de las tasas de drogadicción en Suiza tras la implementación de su política de <strong>Reducción de Daños</strong> (1994):</p>
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
# GRÁFICO 3
with st.container():
    st.markdown("""
    <div class="graph-card zoom-effect">
        <div class="graph-title">⚖️ Muertes por drogadicción según género en Suiza (1995-2023)</div>
    """, unsafe_allow_html=True)
    img3 = Image.open("grafico donut.png")
    st.image(img3, width=1100)
    st.markdown("""
        <div style='line-height: 1.6; font-size: 20px;'>
            <h4 style='color: #1d1d1f; margin-top: 15px;'>Hallazgos clave:</h4>
            <ol>
                <li><strong>Diferencias de género en las muertes relacionadas con drogas:</strong><br>
                    - Hombres: 74.1%<br>
                    - Mujeres: 25.9%<br>
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


# GRÁFICO 4 - MAPA DE CALOR
import streamlit as st
import pandas as pd
import plotly.express as px

# GRÁFICO 4 - MAPA DE CALOR
with st.container():
    st.markdown("""
    <div class="graph-card zoom-effect">
        <div class="graph-title">🌡️ Distribución geográfica de muertes relacionadas con drogas en EE.UU. (1999-2015) </div>
    """, unsafe_allow_html=True)
# Cargar los datos
data = pd.read_csv('datos EEUU.csv', sep=';', encoding='latin1')

# Crear un slider para seleccionar el año
selected_year = st.selectbox("Selecciona un año", tuple(range(1999,2016,1)))

# Filtrar los datos para el año seleccionado
filtered_data = data[data['Year'] == selected_year]

# Agrupar muertes por estado en el año seleccionado
state_deaths = filtered_data.groupby('State')['Deaths'].sum().reset_index()

# Obtener población por estado en el año seleccionado
pop_data = filtered_data.groupby('State')['Population'].mean().reset_index()

# Unir datos de muertes y población
state_deaths = state_deaths.merge(pop_data, on='State', how='left')

# Calcular la tasa de muertes ajustada por población
state_deaths['DeathRate'] = (state_deaths['Deaths'] / state_deaths['Population']) * 100000
state_deaths['DeathRate'] = state_deaths['DeathRate'].round().astype(int)  # Redondear valores

# Limitar los valores entre 5 y 20
state_deaths['DeathRate'] = state_deaths['DeathRate'].clip(5, 20)

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

# Agregar código de estado
state_deaths['StateCode'] = state_deaths['State'].map(state_abbr)

# Crear el mapa interactivo con la escala ajustada
fig = px.choropleth(
    state_deaths,
    locations='StateCode',
    locationmode='USA-states',
    color='DeathRate',
    scope='usa',
    color_continuous_scale='Greens',  # Se mantiene el verde oscuro para valores altos
    range_color=[5, 20],  # Ajustamos el rango de la escala de colores
    title=f"Tasa anual de muertes por drogas en EE.UU. ({selected_year})",
    hover_name='State',
    labels={'DeathRate': 'Muertes por cada 100,000 habitantes'}
)

# Ajustar el diseño del gráfico con fuente en negro
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

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig, use_container_width=True)
# Información adicional fuera del contenedor
st.markdown("""
    <div style='line-height: 1.6; font-size: 20px;'>
        <p>Este mapa de calor interactivo permite visualizar la distribución geográfica de las tasas de mortalidad relacionadas con drogas en los diferentes estados de EE.UU. a lo largo del periodo 1999-2015. Usa el deslizador para explorar cómo han cambiado las tasas en cada estado con el tiempo.</p>
        <h4 style='color: #1d1d1f; margin-top: 15px;'>Observaciones clave:</h4>
        <ul>
            <li><strong>Concentración en el noreste:</strong> Estados como West Virginia, Ohio y Pennsylvania muestran tasas más altas en varios años.</li>
            <li><strong>Patrón regional:</strong> Se observa un "corredor de alta mortalidad" desde los Apalaches hasta Nueva Inglaterra, aunque los valores pueden cambiar según el año seleccionado.</li>
            <li><strong>Variabilidad estatal:</strong> Las diferencias entre estados pueden alcanzar hasta 5 veces en tasas de mortalidad, con fluctuaciones anuales.</li>
        </ul>
        <p><strong>Interpretación:</strong> Este análisis refuerza la necesidad de abordar el problema desde una perspectiva de salud pública adaptada a la evolución de la crisis en el tiempo.</p>
    </div>
""", unsafe_allow_html=True)

# CONCLUSIONES
with st.container():
    st.markdown("""
    <div class="section">
        <h2 style='color: #1d1d1f; margin-bottom: 20px;'>📌 Conclusiones</h2>
        <div style='line-height: 1.6; font-size: 20px'>
            <ul>
                <li>Las políticas de <strong>reducción de daños</strong> aplicadas en Suiza han demostrado una eficacia notable en términos de salud pública.</li>
                <li>El modelo <strong>prohibicionista estadounidense</strong>, pese a sus altos costos económicos y humanos, no ha logrado frenar el aumento de muertes por sobredosis.</li>
                <li>Es crucial cambiar la perspectiva: de la represión al tratamiento, de la criminalización a la prevención.</li>
                <li><strong>NarcoImpact</strong> busca contribuir a este cambio, difundiendo datos y promoviendo un debate basado en evidencia.</li>
            </ul>
            <blockquote>"El objetivo último de este proyecto es la mejora de la sociedad. Las drogas destruyen vidas, y la información puede salvarlas."</blockquote>
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
