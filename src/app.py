import streamlit as st
from services.blob_service import upload_blob
from services.card_service import analize_card

def configure_interface():
    st.title("POC - Azure Intelligence Docs")
    upload_file = st.file_uploader("Escolher arquivo", type=["png", "jpg", "jpeg"])
    
    if upload_file is not None:
        file_name = upload_file.name
        blob_url = upload_blob(upload_file, file_name)
        if blob_url:
            st.write(f"Arquivo {file_name} enviado com sucesso para o Azure Blob Storage.")
            credit_card_info = analize_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {file_name} para o Azure Blob Storage.")
            
            
def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada.", use_container_width=True)
    st.write("Resultado da validação: ")
    if credit_card_info and credit_card_info["card_holder_name"]:
        st.markdown(f"<h1 style='color: green';>Cartão válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do titular: {credit_card_info['card_holder_name']}")
        st.write(f"Banco emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de validade: {credit_card_info['expiration_date']}")
        st.write(f"Número: {credit_card_info['card_number']}")
    else:
        st.markdown(f"<h1 style='color: red';>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write(f"O cartão não atende aos critérios de validação.")
    
if __name__ == "__main__":
    configure_interface()