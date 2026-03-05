📖 Como Usar
Uso Básico
1. Preparar seu arquivo CSV
Seu arquivo CSV deve conter uma coluna com CEPs. Exemplo:

id,nome,cep,endereco
1,Empresa A,01310100,Avenida Paulista
2,Empresa B,01412100,Rua A
3,Empresa C,01415100,Avenida B

2. Executar o Script Principal
Para coletar dados:
python BCK2.py

Ou para operações específicas:
python insetjunho.py

3. Resultado
O script gerará um arquivo CSV com as coordenadas adicionadas:
id,nome,cep,endereco,latitude,longitude
1,Empresa A,01310100,Avenida Paulista,-23.5505,−46.6333
2,Empresa B,01412100,Rua A,-23.5615,−46.6560
3,Empresa C,01415100,Avenida B,-23.5725,−46.6670

Estrutura de Arquivos
Coletor-de-dados-long_lati/

🎯 Coletor-de-dados-long_lati/

│
├── 📄 BCK2.py                      ⚙️ Script principal de coleta

├── 📄 insetjunho.py                ⚙️ Script alternativo

├── 📊 base_sp_junho.csv            📈 Dados de entrada (exemplo)

├── 📊 teste de lat-log.csv         🧪 Arquivo de teste

├── 📋 pip-install.txt              📦 Dependências

├── 📋 requirements.txt             📦 (Recomendado)

├── 📖 README.md                    📘 Este arquivo

│
└── 📁 Dados/
    ├── 📝 Resultado da tabela.txt  ✅ Processamento concluído
    └── 📝 OBS e anotações.txt      💭 Observações importantes

💡 Exemplos de Uso
Exemplo 1: Processar arquivo simples
python BCK2.py

Exemplo 2: Usar um arquivo específico
Edite o script Python e altere a linha:
arquivo_entrada = "seu_arquivo.csv"
arquivo_saida = "seu_arquivo_com_coordenadas.csv"

Exemplo 3: Processar múltiplos arquivos
python insetjunho.py

⚙️ Configuração Avançada
Customizar o Script
Abra BCK2.py e ajuste os parâmetros:
# Arquivo de entrada
arquivo_csv = "base_sp_junho.csv"

# Coluna que contém o CEP
coluna_cep = "cep"

# Arquivo de saída
arquivo_saida = "resultado_final.csv"

# Timeout para requisições (em segundos)
timeout = 10

Usar Fonte de Dados Customizada
Se estiver usando uma API específica de geolocalização, configure:
URL_API = "https://sua-api-geocoding.com/search"
API_KEY = "sua_chave_api"

🛠️ Troubleshooting
❌ Erro: "ModuleNotFoundError: No module named 'pandas'"
Solução:
pip install pandas

❌ Erro: "Arquivo CSV não encontrado"


Solução:

Verifique se o arquivo está na mesma pasta do script
Use o caminho completo: /caminho/para/arquivo.csv
❌ CEPs não encontrados
Possíveis causas:

CEP inválido ou inexistente
Problema de conexão com a API
Limite de requisições atingido
Solução:

Verifique o formato do CEP (deve ser 8 dígitos)
Verifique sua conexão com a internet
Aguarde alguns minutos antes de tentar novamente
❌ Arquivo Excel não pode ser lido
Solução:
pip install openpyxl

🔗 Dependências Externas
API de Geocoding: O script utiliza uma API pública para converter CEP em coordenadas
Verificar limite de requisições
Pode exigir chave de API (verifique a documentação)

📝 Observações Importantes
⚠️ Antes de usar:

Faça backup de seus dados originais
Teste com um arquivo pequeno primeiro
Verifique os CEPs antes de executar
Considere o limite de requisições das APIs utilizadas

🤝 Como Contribuir
Faça um Fork do projeto
Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)
Commit suas mudanças (git commit -m 'Add some AmazingFeature')
Push para a branch (git push origin feature/AmazingFeature)
Abra um Pull Request

📄 Licença
Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.

📞 Suporte e Contato

Autor: @yungGenos

GitHub: github.com/yungGenos

linkdin: https://www.linkedin.com/in/kaique-genonadio-451102203/ 

🎓 Dicas de Otimização
Para grandes volumes de dados:
Use processamento em lotes
Implemente cache de CEPs já consultados
Considere usar threading para requisições paralelas
Para melhor performance:

# Use CHUNKSIZE para arquivos grandes
chunksize = 1000
for chunk in pd.read_csv('arquivo.csv', chunksize=chunksize):
    # processar chunk
    # Use CHUNKSIZE para arquivos grandes
chunksize = 1000
for chunk in pd.read_csv('arquivo.csv', chunksize=chunksize):
    # processar chunk

    ⭐ Se este projeto foi útil para você, considere deixar uma estrela! 🌟

Code

---

## 📌 Próximos Passos

Esse README cobre:
- ✅ Instalação completa passo a passo
- ✅ Como usar o código
- ✅ Estrutura de arquivos
- ✅ Exemplos práticos
- ✅ Troubleshooting
- ✅ Dicas de otimização

