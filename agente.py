import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """Eres un agente inteligente de organización académica. 
Tu rol es ayudar a estudiantes con:
- Organizar horarios de estudio
- Recordar tareas y exámenes
- Recomendar técnicas de estudio
- Mejorar la productividad
- Resolver dudas académicas básicas

Responde siempre en español, de forma clara, amigable y motivadora.
Cuando el estudiante mencione un examen próximo, ofrece un plan de estudio.
Cuando mencione que olvida tareas, sugiere un sistema de recordatorios.
Cuando no tenga tiempo, recomienda técnicas de organización."""

historial = [{"role": "system", "content": SYSTEM_PROMPT}]

print("Agente Académico Inteligente")
print("=" * 40)
print("Hola! Soy tu asistente académico. ¿En qué te puedo ayudar hoy?")
print("(escribe 'salir' para terminar)\n")

while True:
    entrada = input("Tú: ").strip()
    
    if entrada.lower() == "salir":
        print("¡Hasta luego! Sigue estudiando con disciplina ")
        break
    
    if not entrada:
        continue

    historial.append({"role": "user", "content": entrada})

    respuesta = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=historial
    )

    mensaje = respuesta.choices[0].message.content
    historial.append({"role": "assistant", "content": mensaje})
    
    print(f"\nAgente: {mensaje}\n")
