import requests

# Endpoint local de LMStudio
LMSTUDIO_URL = "http://localhost:1234/v1/completions"  # 👈 Usa /v1/completions

def generar_texto(prompt):
    """Envía el prompt al LLM local y devuelve la respuesta generada."""
    payload = {
        "model": "deepseek-r1-distill-llama-8b",
        "prompt": prompt,  # 👈 Cambia 'messages' por 'prompt'
        "temperature": 0.7,
        "max_tokens": 300
    }

    response = requests.post(LMSTUDIO_URL, json=payload)

    try:
        response_json = response.json()
        print("🔍 Respuesta de LMStudio:", response_json)  # 👈 Imprime para depurar
        
        # Verifica si "choices" existe en la respuesta
        if "choices" in response_json and len(response_json["choices"]) > 0:
            return response_json["choices"][0]["text"]  # 👈 Cambia "message" por "text"
        else:
            return "⚠️ Error: No se encontraron respuestas válidas en LMStudio."
    
    except Exception as e:
        return f"❌ Error al procesar la respuesta: {str(e)}"

# Prueba rápida
print(generar_texto("Eres experto en crear cuentos infantiles. Vas a Crear un cuento de 100 palabras inciando con este texto: 'Érase una vez un castillo encantado...'"))

