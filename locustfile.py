import json
from locust import HttpUser, task, between

class APIStressTestUser(HttpUser):
    # Tempo de espera aleatório (1 a 3 segundos) entre requisições de cada usuário
    wait_time = between(1, 3)

    @task(1)
    def test_healthcheck(self):
        # Simula acesso leve à raiz da API (Sonda de disponibilidade)
        self.client.get("/")

    @task(3)
    def test_predict_endpoint(self):
        # Simula requisições simultâneas de processamento pesado no endpoint /predict (RAG)
        headers = {'Content-Type': 'application/json'}

        payload = {
            "prompt": "Explique o Teorema CAP de Eric Brewer e o modelo BASE de forma simples."
        }

        self.client.post(
            "/predict",
            data=json.dumps(payload),
            headers=headers
        )