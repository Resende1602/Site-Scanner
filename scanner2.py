import requests

def verificar_headers(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        print(f"\n🔒 Analisando headers de segurança do site: {url}\n")

        # Cabeçalhos de segurança que vamos checar
        headers_seguranca = {
            "Content-Security-Policy": "Protege contra ataques XSS e injeção de código.",
            "X-Frame-Options": "Previne clickjacking.",
            "Strict-Transport-Security": "Força HTTPS para comunicação segura.",
            "X-Content-Type-Options": "Evita sniffing de MIME types.",
            "Referrer-Policy": "Controla informações do Referer enviadas para outros sites."
        }

        for header, descricao in headers_seguranca.items():
            if header in headers:
                print(f"[✔] {header}: {headers[header]}")
            else:
                print(f"[✘] {header} NÃO encontrado. {descricao}")

    except requests.exceptions.RequestException as e:
        print(f"[!] Erro ao acessar {url}: {e}")

if __name__ == "__main__":
    site = input("Digite a URL do site (ex: https://example.com): ").strip()
    if not site.startswith(("http://", "https://")):
        site = "http://" + site  # adiciona protocolo se o usuário não forneceu
    verificar_headers(site)
    input("\nPressione Enter para encerrar...")
