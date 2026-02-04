import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Descuentos 3º ESO", page_icon="🏥")

# Título y Descripción
st.title("💯 Calculadora de Descuentos")
st.markdown("Bienvenido. Introduce tus datos para calcular tu descuento.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio_original = st.sidebar.number_input("Original_price ($)", min_value=0, max_value=200, value=60)
porcentaje = st.sidebar.slider("porcentaje ($)", 0, 100, 50)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular Descuento"):
    
    # Fórmula Matemática: Peso entre altura al cuadrado
    rebaja = precio_original*porcentaje/100
    precio_final = precio_original - rebaja
    
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu :", value=f"{precio_final:.2f}")
        
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if porcentaje < 5:
            st.warning("⚠️ ")
            st.write(" Descuento bajo.")
        elif 18.5 <= porcentaje < 15:
            st.success("✅ descuento normal")
            st.balloons() # ¡Premio!
        elif 25 <= porcentaje < 30:
            st.warning("💰")
            st.write("muy buen descuento.")
        else:
            st.error("")
            st.write(".")
            
    # Extra: Mostrar la fórmula usada (LaTeX)
    st.write("---")
    st.info("Fórmula matemática utilizada:")
    st.latex(r''' IMC = \frac{peso}{altura^2} ''')
