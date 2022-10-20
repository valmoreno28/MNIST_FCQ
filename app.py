import streamlit as st
from img_classification import teachable_machine_classification
import keras
from PIL import Image, ImageOps
import numpy as np


st.title("Aplicación de reconocimiento de flores")
st.subheader("Por: Valeria Moreno")

uploaded_file = st.file_uploader("Carga una imagen ...", type=["jpg","jpeg"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  label = teachable_machine_classification(image, 'keras_model.h5') 
  if label == 0:
    st.write("Esta planta es Damask Rose")
    st.write(label)
  if label == 1:
    st.write("Esta planta es Echeveria Flower")
  if label == 2:
    st.write("Esta planta es Mirabilis Jalapa")
  if label == 3:
    st.write("Esta planta es Rain Lily")
  if label == 4:
     st.write("Zinnia Elegans")
      
st.image(uploaded_file)
  #st.write(label)
