# Projeto 1 - Deti Shop - Vulnerabilities in software products
 
## Contexto 
Este projeto e respetivo relatório foram efetuados no âmbito da disciplina de Segurança Informática e nas Organizações.
O objetivo deste projeto é criar uma loja relacionada com o Departamento de Telecomunicações e Informática da Universidade de Aveiro implementando algumas funcionalidades.
As principais tecnologias usadas foram Flask e SQLite 3.
Existem duas versões desta loja, uma versão segura e uma versão insegura, na versão insegura existem algumas vulnerabilidades que podem ser exploradas de modo a comprometer o sistema. Na versão segura, estas vulnerabilidades foram corrigidas tornando o sistema completamente segur0.
Em seguida apresentamos uma lista das vulnerabilidades apresentadas:

-	[CWE 79 - Cross Site Scripting](https://cwe.mitre.org/data/definitions/79.html)
-	[CWE 89 – SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
-	[CWE 256 – Plaintext storage of a password](https://cwe.mitre.org/data/definitions/256.html)
-	[CWE 620 – Unverified Password Change](https://cwe.mitre.org/data/definitions/620.html)
-	[CWE 311 – Missing Encryptation of sensitive data](https://cwe.mitre.org/data/definitions/311.html)
-	[CWE 549 - Missing Password Field Masking](https://cwe.mitre.org/data/definitions/549.html) 
-	[CWE 756 - Missing custom error page](https://cwe.mitre.org/data/definitions/756.html)
-	[CWE 284 - Improper acess control](https://cwe.mitre.org/data/definitions/284.html)

  ## Autores

  - Alexandre Martins, 103552
  - Diogo Pires, 97889
  - Diogo Silva, 104341
  - Tomás Rodrigues, 104090

## Como correr: 

Para correr a aplicação

1. Clonar o  repositório:

   ```bash
   git clone https://github.com/detiuaveiro/1st-project-group_03.git
   cd 1st-project-group_03/app/website   # vulnerável
   ````
    ```bash
   git clone https://github.com/detiuaveiro/1st-project-group_03.git
   cd 1st-project-group_03/app_sec/website   # seguro
   ````
2. Criar um ambiente virtual
    ```` bash
   python -m venv venv
   source venv/bin/activate  # Em windows, usar 'venv\Scripts\activate'
   ````
3. Instalar os pacotes necessários
    ```` bash
   pip install -r requirements.txt
   ````

4. Por fim executar o comando
    ```` bash
    python main.py
   ````
## Contas pré-criadas:
1. Admin:
- Email: admin@gmail.com
- Password: admin
2. Usuário normal:
- Email: alex@gmail.com
- Password: 1
3. Usuário normal:
- Email: eve@gmail.com
- Password: 1
