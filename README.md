Generador de Texto con LMStudio y DeepSeek LLM

Este es un proyecto simple en Python que utiliza LMStudio y el modelo deepseek-r1-distill-llama-8b para generar texto a partir de un prompt.

🚀 Requisitos

Python 3.8+

LMStudio instalado y ejecutándose localmente

Modelo deepseek-r1-distill-llama-8b cargado en LMStudio

Dependencias Python:

pip install requests

📌 Instalación y Configuración

1️⃣ Descarga e instala LMStudio

LMStudio se puede descargar desde:
🔗 https://lmstudio.ai/

2️⃣ Carga el modelo en LMStudio

Abre LMStudio y carga el modelo deepseek-r1-distill-llama-8b.

3️⃣ Ejecuta el servidor local

Asegúrate de que LMStudio está corriendo en http://localhost:1234. Puedes verificarlo accediendo a:

http://localhost:1234/v1/models

Deberías ver el modelo cargado en la respuesta JSON.

📝 Uso

1️⃣ Clona este repositorio:

git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo

2️⃣ Ejecuta el script:

python main.py

🛠 Código Principal (main.py)

import requests

LMSTUDIO_URL = "http://localhost:1234/v1/completions"

def generar_texto(prompt):
    payload = {
        "model": "deepseek-r1-distill-llama-8b",
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 300
    }
    response = requests.post(LMSTUDIO_URL, json=payload)
    response_json = response.json()
    return response_json.get("choices", [{}])[0].get("text", "Error: Sin respuesta")

print(generar_texto("Érase una vez un castillo encantado..."))

🎯 Contribuciones

¡Las contribuciones son bienvenidas! Puedes hacer un fork, crear una branch y enviar un pull request.

📜 Licencia

Este proyecto está bajo la licencia MIT. ¡Úsalo libremente! 🚀




