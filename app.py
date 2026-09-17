from flask import Flask, jsonify, request
from base_conhecimento import BASE_CONHECIMENTO
import os
import datetime
import difflib
import time

app = Flask(__name__)

# Banco de dados simulado em memória (Segregação lógica Multitenant)
pedidos_armazenados = []

def buscar_contexto_relevante(prompt, top_k=2):
    """Simula uma busca vetorial: calcula similaridade textual contra a base de conhecimento."""
    similaridades = []
    for documento in BASE_CONHECIMENTO:
        # Simula custo computacional de comparação semântica (ex: cálculo de embeddings)
        score = difflib.SequenceMatcher(None, prompt.lower(), documento.lower()).ratio()
        similaridades.append((score, documento))
    similaridades.sort(reverse=True, key=lambda x: x[0])
    return [doc for _, doc in similaridades[:top_k]]


@app.route('/', methods=['GET'])
def healthcheck():
    return jsonify({
        "status": "Online",
        "timestamp": datetime.datetime.now().isoformat(),
        "ambiente": "Container Linux (Docker)",
        "disciplina": "Computacao em Nuvem e SOA - IFPA",
        "api_endpoint": "/predict [POST]"
    }), 200


@app.route('/predict', methods=['POST'])
def predict_rag_simplificado():
    try:
        data = request.get_json(silent=True) or {}
        user_prompt = data.get("prompt")
        tenant_id = data.get("tenant_id", "default_tenant")

        if not user_prompt:
            return jsonify({"erro": "Bad Request", "mensagem": "Prompt ausente"}), 400

        inicio = time.time()
        contexto = buscar_contexto_relevante(user_prompt)
        resposta_simulada = (
            f"[AGENTE RAG] Com base no contexto recuperado, aqui está uma resposta para: '{user_prompt}'. "
            f"Contexto utilizado: {' | '.join(contexto)}"
        )
        tempo_processamento_ms = round((time.time() - inicio) * 1000, 2)

        nova_transacao = {
            "id": len(pedidos_armazenados) + 1,
            "tenant_id": tenant_id,
            "prompt": user_prompt,
            "contexto_recuperado": contexto,
            "resposta_agente": resposta_simulada,
            "tempo_busca_ms": tempo_processamento_ms,
            "status_execucao": "Sucesso",
            "data_registro": datetime.datetime.now().isoformat()
        }
        pedidos_armazenados.append(nova_transacao)

        return jsonify({
            "sucesso": True,
            "trilha": "Integrada - Inteligencia Artificial (RAG simplificado)",
            "dados": nova_transacao
        }), 201

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)