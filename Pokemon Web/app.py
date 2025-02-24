import streamlit as st
import random
import requests

st.set_page_config(
    page_title='Pokémon Explorer',
    page_icon='',
    layout='centered'
)

#Función para obtener datos de un pokemon
def get_pokemon_data(pokemon_name):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}')
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except:
        return None
    
#Funcion para obtener un Pokemon aleatorio
def get_random_pokemon():
    random_id = random.randint(1,1010)
    return get_pokemon_data(str(random_id))

#Titulo y descrición
st.title('Pokedex')
st.markdown('Descubre información sobre tus Pokemon favoritos o encuentra nuevos Pokemon al azar!')

#Crear dos columnas para la busqueda y el botón aleatorio
col1, col2 = st.columns([2,1])

#Columna de busqueda
with col1:
    pokemon_name = st.text_input('Ingresa el nombre de un Pokémon: ', '')

#Columna del botón aleatorio
with col2:
    random_btn = st.button('¡Pokemon Aleatorio!')

get_pokemon_data = None

#Manejar la busqueda o el botón aleatorio
if pokemon_name:
    pokemon_data = get_pokemon_data(pokemon_name)
elif random_btn:
    pokemon_data = get_random_pokemon()

#Mostrar información del Pokemon
if pokemon_data:
    #Crear dos columnas para la imagen y la información
    img_col, info_col = st.columns([2,1])

    with img_col:
        #Mostrar imagen del Pokemon
        st.image(
            pokemon_data['sprites']['other']['official-artwork']['front_default'],
            caption=f'#{pokemon_data['id']}{pokemon_data['name'].title()}',
            use_container_width=True
        )

    with info_col:
        #Información básica
        st.subheader('Información básica')
        st.write(f'**ALTURA:**{pokemon_data['height']/10} m')
        st.write(f'**PESO:**{pokemon_data['weight']/10} kg')

        #Tipos
        st.subheader('TIPOS')
        tipos = [tipo['type']['name'] for tipo in pokemon_data['types']]
        for tipo in tipos:
            st.write(f'- {tipo.title()}')
    
    #Stats
    st.subheader('ESTADISTICAS')
    stats_cols = st.columns(3)
    stats = pokemon_data['stats']

    for idx, stat in enumerate(stats):
        col_idx = idx%3
        with stats_cols[col_idx]:
            st.metric(
                label=stats['stat']['name'].replace('-',' ').title(),
                value=stat['base_stat']
            )

    #Habilidades
    st.subheader('HABILIDADES')
    abilities = [ability['ability']['name'].replace('-',' ').title()
                 for ability in pokemon_data['abilities']]
    
    for ability in abilities:
        st.write(f'- {ability}')

elif pokemon_name:
    st.error('¡Pokémon no encontrado! Verifica el nombre e intenta nuevamente')
else:
    st.info('Ingresa el nombre de un Pokemon o prueba con uno aleatorio!')