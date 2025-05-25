
import streamlit as st
import random

st.set_page_config(page_title="Gems Mines", layout="centered")

st.title("Gems Mines - 5 aciertos con 4 minas")
st.markdown("Toca las gemas, evita las minas. ¡Necesitás 5 aciertos por ronda!")

# Parámetros
filas, columnas = 5, 5
total_casillas = filas * columnas
minas = 4
aciertos_meta = 5

# Inicialización
if "estado" not in st.session_state:
st.session_state.estado = ["pendiente"] * total_casillas
st.session_state.mina_indices = random.sample(range(total_casillas), minas)
 st.session_state.aciertos = 0
 st.session_state.juego_terminado = False

# Función de reinicio
def reiniciar_juego():
 st.session_state.estado = ["pendiente"] * total_casillas
st.session_state.mina_indices = random.sample(range(total_casillas), minas)
st.session_state.aciertos = 0
 st.session_state.juego_terminado = False

# Interfaz
for i in range(filas):
 cols = st.columns(columnas)
 for j in range(columnas):
 index = i * columnas + j
 estado = st.session_state.estado[index]

if estado == "acierto":
emoji = "⭐"
 elif estado == "mina":
 emoji = "⛏️"
 else:
emoji = "⬜"
if st.session_state.juego_terminado or estado != "pendiente":
cols[j].button(emoji, key=index, disabled=True)
else:
 if cols[j].button(emoji, key=index):
 if index in st.session_state.mina_indices:  st.session_state.estado[index] = "mina"
 st.session_state.juego_terminado = True
 st.error("¡Perdiste! Tocaste una mina.")
 else:
 st.session_state.estado[index] = "acierto"
st.session_state.aciertos += 1  if st.session_state.aciertos >= aciertos_meta:
 st.session_state.juego_terminado = True      st.success("¡Ganaste! 5 aciertos logrados.")

# Botón para reiniciar
st.markdown("---")
st.button("🔄 Nueva ronda", on_click=reiniciar_juego)

4. Bajá hasta abajo del todo y tocá el botón “Commit changes”.










