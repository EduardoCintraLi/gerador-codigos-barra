import streamlit as st

# Função para gerar o novo código
def gerar_novo_codigo(codigo_atual):
    # Validação do código
    if len(codigo_atual) < 3:
        raise ValueError("Código muito curto.")
    
    inicio = codigo_atual[0]
    corpo = codigo_atual[1:-1]
    try:
        dv = int(codigo_atual[-1])
    except:
        raise ValueError("Dígito verificador deve ser um número.")

    # Trata o primeiro caractere
    if inicio.isdigit():
        novo_inicio = str((int(inicio) + 1) % 10)
    elif inicio.isalpha():
        novo_inicio = chr((ord(inicio.upper()) - 65 + 1) % 26 + 65)
    else:
        raise ValueError("Caractere inicial inválido")

    # Ajusta o DV
    novo_dv = (dv - 3) % 10

    return novo_inicio + corpo + str(novo_dv)

# Interface Streamlit
st.title("🔢 Gerador de Novo Código de Barras")

codigo_input = st.text_input("Digite o código de barras atual:", max_chars=20)

if st.button("Gerar novo código"):
    if not codigo_input:
        st.warning("Por favor, digite um código.")
    else:
        try:
            resultado = gerar_novo_codigo(codigo_input.strip())
            st.success(f"✅ Novo código: `{resultado}`")
        except Exception as e:
            st.error(f"Erro: {e}")
