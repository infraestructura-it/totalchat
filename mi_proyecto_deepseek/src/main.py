from api.deepseek_client import DeepSeekClient

client = DeepSeekClient()
response = client.generate_text("Explica la teoría de la relatividad en una frase.")

if response and "choices" in response:
    print(response["choices"][0]["message"]["content"])
else:
    print("No se pudo obtener una respuesta válida de la API.")
