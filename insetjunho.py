import pandas as pd
import pymysql as sql
import mysql.connector
from mysql import connector


csv_file = r'C:\Users\thiago.oliveira\Desktop\inset slq\base_sp_junho.csv'

# Conectar ao MySQL
try:
    conn = sql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        database='uono'
    )
    cursor = conn.cursor()
    print("✅ Conectado ao MySQL com sucesso!")
except sql.connector.Error as err:
    print(f"❌ Erro de conexão: {err}")
    exit()

# Carregar o CSV
try:
    df = pd.read_csv(csv_file)
    print(f"📄 CSV carregado: {len(df)} registros encontrados.")
except Exception as e:
    print(f"❌ Erro ao ler CSV: {e}")
    conn.close()
    exit()

# Inserir dados
try:
    for _, row in df.iterrows():
        sql = """
            INSERT INTO cadastro_imovel_junho (
                numero_cadastro,
                nome_logradouro,
                numero,
                complemento,
                bairro,
                referencia,
                cep,
                natureza_transacao,
                valor_transacao,
                data_transacao,
                valor_venal_referencia,
                proporcao_transmitida,
                valor_venal_proporcional,
                base_calculo,
                tipo_financiamento,
                valor_financiado,
                cartorio_registro,
                matricula_imovel,
                situacao_sql,
                area_terreno_m2,
                testada_m,
                fracao_ideal,
                area_construida_m2,
                uso_iptu,
                descricao_uso_iptu,
                padrao_iptu,
                descricao_padrao_iptu,
                acc_iptu
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, tuple(row))
    
    conn.commit()
    print("✅ Dados inseridos com sucesso na tabela cadastro_imovel_junho!")

except Exception as e:
    print(f"❌ Erro ao inserir dados: {e}")
    conn.rollback()

# Fechar conexão
cursor.close()
conn.close()
