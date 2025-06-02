# Site-Scanner
 🔍 Scanner de Headers de Segurança HTTP

Este projeto é um scanner simples desenvolvido em Python que analisa os headers de segurança de um site. Ele verifica se certos cabeçalhos HTTP importantes estão presentes na resposta da aplicação web.

## 🚀 Funcionalidades

- Verifica presença de:
  - `Content-Security-Policy`
  - `X-Frame-Options`
  - `Strict-Transport-Security`
  - `X-Content-Type-Options`
  - `Referrer-Policy`
- Mostra mensagens visuais de acordo com a presença ou ausência dos headers.
- Ajuda a identificar vulnerabilidades básicas de configuração em sites.

## 🛠 Requisitos

- Python 3.x
- Módulo `requests` (instale com `pip install requests`)

## ▶️ Como executar

```bash
python3 scanner2.py

Digite a URL do site (ex: https://example.com): https://exemplo.com

📌 Exemplo de saída
Analisando headers de segurança do site: https://exemplo.com

[✘] Content-Security-Policy NÃO encontrado. Protege contra ataques XSS e injeção de código.
[✔] X-Frame-Options encontrado: SAMEORIGIN
[✘] Strict-Transport-Security NÃO encontrado. Força HTTPS para comunicação segura.
[✔] X-Content-Type-Options encontrado: nosniff
[✔] Referrer-Policy encontrado: same-origin

🧑‍💻 Autor

Desenvolvido por lkz (Resende1602)
📄 Licença

Este projeto está licenciado sob a MIT License


---

### ✅ Próximos passos:

1. **Crie o arquivo:**

```bash
nano README.md




