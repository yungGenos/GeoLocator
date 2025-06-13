import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def abrir_site():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com/maps")
    print("✅ Google Maps aberto com sucesso!")
    return driver

def pesquisar_cep(driver, cep):
    try:
        wait = WebDriverWait(driver, 20)
        campo_pesquisa = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#searchboxinput")))
        campo_pesquisa.clear()
        campo_pesquisa.send_keys(cep)
        campo_pesquisa.send_keys(Keys.ENTER)
        print(f"🔍 Buscando CEP: {cep}")
        time.sleep(8)
    except Exception as e:
        print(f"❌ Erro ao buscar o CEP {cep}: {e}")

def clicar_direito_e_capturar_lat_long(driver):
    try:
        time.sleep(2)
        mapa = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "widget-scene"))
        )
        
        # Move o cursor para o centro do mapa e clica com o botão direito
        ActionChains(driver).move_to_element_with_offset(mapa, 500, 300).context_click().perform()
        time.sleep(2)

        # Captura a latitude e longitude do menu
        coordenada = driver.find_element(By.CLASS_NAME, "mLuXec").text.strip()
        print(f"📍 Coordenadas capturadas: {coordenada}")
        return coordenada
    except Exception as e:
        print(f"❌ Erro ao capturar coordenadas: {e}")
        return None

def ler_ceps_do_csv(nome_arquivo, linha_inicio=0):
    try:
        df = pd.read_csv(nome_arquivo, encoding='latin1', delimiter=';')
        df['CEP'] = df['CEP'].astype(str).str.strip().str.replace(r'\D', '', regex=True)
        return df['CEP'].dropna().iloc[linha_inicio:].tolist()
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo CSV: {e}")
        return []

def salvar_resultado_em_csv(lista_dados, nome_arquivo):
    df = pd.DataFrame(lista_dados, columns=["CEP", "LAT_LONG"])
    df.to_csv(nome_arquivo, index=False, sep=";")
    print(f"✅ Dados salvos em: {nome_arquivo}")

# ===== EXECUÇÃO PRINCIPAL =====
if __name__ == "__main__":
    lista_ceps = ler_ceps_do_csv("base_sp_junho.csv", linha_inicio=2554)
    resultados = []

    if lista_ceps:
        driver = abrir_site()
        time.sleep(5)

        for cep in lista_ceps:
            pesquisar_cep(driver, cep)
            lat_long = clicar_direito_e_capturar_lat_long(driver)
            resultados.append([cep, lat_long if lat_long else "Não encontrado"])

        salvar_resultado_em_csv(resultados, "new lag log.csv")
        print("✅ Processo concluído.")
        # driver.quit()  # Descomente para fechar o navegador no final
