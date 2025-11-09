# Toon Lab

Proyecto de prueba de concepto para comparar el rendimiento de LLMs utilizando JSON vs TOON format.

## Instalación

### Requisitos previos

- Python >= 3.13
- [uv](https://github.com/astral-sh/uv) (recomendado para gestión de dependencias)

### Instalación de uv

Si aún no tienes `uv` instalado, puedes instalarlo con:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Instalación de dependencias

Clona el repositorio e instala las dependencias:

```bash
git clone <repository-url>
cd toon_lab

# Instalar dependencias con uv (recomendado)
uv sync
```

### Configuración de variables de entorno

Copia el archivo `.env.example` a `.env` y configura tus credenciales:

```bash
cp .env.example .env
```

Edita el archivo `.env` y añade tu API key de OpenAI:

```env
OPENAI_API_KEY=sk-...
```

#### Configuración de LangSmith (Opcional pero recomendado)

Para una experiencia más visual y analizar mejor la trazabilidad de las ejecuciones del grafo, se recomienda configurar LangSmith:

1. Crea una cuenta en [LangSmith](https://smith.langchain.com/)
2. Obtén tu API key desde el panel de LangSmith
3. Añade las siguientes variables en tu archivo `.env`:

```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=ls__...
LANGSMITH_PROJECT=toon-lab
```

Con LangSmith podrás:
- Visualizar el flujo completo del grafo
- Analizar las llamadas a LLM
- Comparar rendimientos entre JSON y TOON
- Debuggear errores más fácilmente

## Ejecución

Para ejecutar el proyecto:

```bash
uv run python -m main
```

Este comando:
1. Procesa un JSON de entrada con un agente LLM
2. Convierte el JSON a formato TOON
3. Procesa el TOON con el mismo agente LLM
4. Guarda los resultados en `json_result.md` y `toon_result.md`

## Estructura del proyecto

```
toon_lab/
├── graph/
│   ├── agent.py      # Configuración del agente LLM
│   ├── graph.py      # Definición del grafo LangGraph
│   ├── nodes.py      # Nodos del grafo (procesamiento)
│   └── state.py      # Estado del grafo
├── main.py           # Punto de entrada
├── .env              # Variables de entorno (no versionado)
├── .env.example      # Ejemplo de variables de entorno
└── README.md         # Este archivo
```

## Resultados

Después de ejecutar el proyecto, encontrarás:
- `json_result.md`: Análisis del agente sobre el JSON original
- `toon_result.md`: Análisis del agente sobre el formato TOON

## Más información

- [TOON Format](https://github.com/toon-format/toon-python)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangSmith Documentation](https://docs.smith.langchain.com/)

Join CLAi Academy! https://discord.gg/vXJZyxSSpu