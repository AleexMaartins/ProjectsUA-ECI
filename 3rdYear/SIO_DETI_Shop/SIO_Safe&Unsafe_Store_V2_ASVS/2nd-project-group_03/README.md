# Projeto 2 - Deti Shop - Application Security Verification Standard (ASVS)
 
## Contexto 
Este projeto e respetivo relatório foram efetuados no âmbito da disciplina de Segurança Informática e nas Organizações.
O objetivo deste projeto é criar uma loja relacionada com o Departamento de Telecomunicações e Informática da Universidade de Aveiro implementando algumas funcionalidades.
As principais tecnologias usadas foram Flask e SQLite 3.


  ## Autores

  - Alexandre Martins, 103552
  - Diogo Pires, 97889
  - Diogo Silva, 104341
  - Tomás Rodrigues, 104090

## Como correr: 

Para correr a aplicação

1. Clonar o  repositório:

   ```bash
   git clone https://github.com/detiuaveiro/2nd-project-group_03.git
   cd 2nd-project-group_03/app_org/website/   # vulnerável
   ````
    ```bash
   git clone https://github.com/detiuaveiro/2nd-project-group_03.git
   cd 2nd-project-group_03/app_sec/website/  # seguro
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
## Correções das vulnerabilidades
1. Software Feature No 1: Multi-factor Authentication (MFA)
- TOTP authentication login
- OAUTH 2.0
2. Software Feature No 2: Password Strength & Breach Verification.
3. CWE-352: Cross-Site Request Forgery (CSRF)
4. ASVS 2.5.4: No default Accounts 
5. ASVS 3.4.1: Session tokens have the 'Secure' attribute set.
6. ASVS 3.4.2: Session tokens have the 'HttpOnly' attribute set.
7. ASVS 3.4.3: Session tokens use 'SameSite' attribute 
8. ASVS 9.1.1: Secure TLS 
9. ASVS 3.2.2: Tokens with 64 bits of entropy 
10. ASVS 3.1.1: Protecting session tokens
