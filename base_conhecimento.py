# base_conhecimento.py
# Base de conhecimento simulando um índice vetorial para o Agente RAG (Trilha Integrada)
# Organizada por tema — conteúdo das Aulas 4 e 5 e Prática 2, complementado com tópicos correlatos de Cloud/SOA/Sistemas Distribuídos

BASE_CONHECIMENTO = [

    # --- Virtualização e Containers (Aula 4 / Buyya) ---
    "O Machine Reference Model de Rajkumar Buyya define quatro camadas de interface: ISA, ABI, API e User Space, delimitando onde cada tipo de virtualização atua.",
    "A camada ISA (Instruction Set Architecture) define as instruções de máquina que a CPU física executa, sendo a fronteira entre hardware e software.",
    "A camada ABI (Application Binary Interface) define como programas compilados interagem com as chamadas de sistema (syscalls) do kernel.",
    "A camada API interliga bibliotecas de sistema, como a glibc, às aplicações em código aberto.",
    "Hypervisors Tipo 1 (como Xen e ESXi) rodam diretamente sobre o hardware físico, sem sistema operacional hospedeiro intermediário.",
    "Hypervisors Tipo 2 (como VirtualBox e Hyper-V) rodam sobre um sistema operacional hospedeiro já existente.",
    "Na virtualização de hardware, o hypervisor intercepta a camada ISA, emulando um conjunto completo de instruções e exigindo um Guest OS completo.",
    "O overhead da virtualização de hardware inclui consumo elevado de RAM, armazenamento e latência na tradução de instruções de CPU pela camada de emulação.",
    "Containers Docker interceptam a camada ABI, sem emulação de hardware e sem Guest OS, compartilhando o kernel do sistema operacional hospedeiro.",
    "Namespaces do Linux garantem isolamento lógico de visualização, dando a cada container seu próprio sistema de arquivos, pilha de rede e árvore de processos (PID).",
    "Control Groups (cgroups) limitam fisicamente quanta CPU, RAM, I/O de disco e banda de rede um processo de container pode consumir do hardware físico.",
    "Containers inicializam em milissegundos e consomem RAM mínima, sendo portáveis de forma imutável entre ambientes de nuvem.",
    "Uma imagem base Alpine Linux em um Dockerfile reduz drasticamente o tamanho da imagem final, diminuindo overhead computacional, uso de armazenamento e superfície de ataque de segurança.",
    "O comando docker build compila uma imagem em camadas (layers), permitindo cache eficiente entre builds sucessivos.",
    "O parâmetro -p no docker run mapeia uma porta física do host para a porta lógica interna do container.",
    "O Gunicorn é um servidor WSGI usado para rodar aplicações Flask em ambiente de produção dentro de containers.",

    # --- Modelos de Nuvem e Responsabilidade Compartilhada ---
    "Em uma Matriz de Responsabilidade Compartilhada de PaaS, o provedor gerencia hardware físico, rede básica, hypervisors e o sistema operacional host, enquanto o cliente gerencia as dependências de runtime e o código da aplicação.",
    "Nos modelos de serviço em nuvem, IaaS oferece infraestrutura bruta (VMs, storage, rede), PaaS abstrai o gerenciamento de servidores e SaaS entrega a aplicação pronta ao usuário final.",
    "PaaS como o Render provisiona automaticamente hardware, monta o container em produção e expõe o serviço sob uma URL pública HTTPS.",
    "Planos gratuitos de provedores PaaS costumam hibernar instâncias após período de inatividade, causando latência elevada na primeira requisição (cold start).",
    "Auto-escalonamento horizontal em plataformas PaaS cria novas instâncias de um serviço conforme a carga de requisições aumenta, buscando manter a vazão estável.",

    # --- Bancos de Dados Distribuídos (Aula 5) ---
    "Bancos de Dados Distribuídos replicam ou particionam dados entre múltiplos nós para garantir escalabilidade horizontal e tolerância a falhas.",
    "Particionamento (sharding) divide um conjunto de dados em fragmentos menores distribuídos entre diferentes servidores, reduzindo a carga individual de cada nó.",
    "Replicação de dados mantém cópias idênticas de um mesmo conjunto de dados em múltiplos nós, aumentando disponibilidade e tolerância a falhas.",
    "Sistemas distribuídos precisam lidar com particionamento de rede, atrasos de comunicação e falhas parciais de nós individuais.",
    "Provisionamento elástico em bancos distribuídos permite adicionar ou remover nós de armazenamento e processamento conforme a demanda de carga varia.",
    "Consistência eventual é um modelo em que, na ausência de novas atualizações, todas as réplicas de um dado convergem para o mesmo valor após um tempo.",

    # --- Teorema CAP e Consistência ---
    "O Teorema CAP de Eric Brewer afirma que um sistema distribuído não pode garantir simultaneamente Consistência, Disponibilidade e Tolerância a Particionamento.",
    "Sistemas CP (Consistência + Tolerância a Particionamento) sacrificam disponibilidade durante uma partição de rede para manter os dados consistentes.",
    "Sistemas AP (Disponibilidade + Tolerância a Particionamento) continuam respondendo requisições durante uma partição, mesmo que os dados fiquem temporariamente inconsistentes.",
    "O modelo BASE (Basically Available, Soft state, Eventually consistent) é uma alternativa ao modelo ACID, priorizando disponibilidade em sistemas distribuídos.",

    # --- Lei de Amdahl e Desempenho Paralelo ---
    "A Lei de Amdahl calcula o speedup teórico máximo de um sistema ao paralelizar parte do seu processamento, limitado pela fração não paralelizável do código.",
    "Segundo a Lei de Amdahl, mesmo aumentando indefinidamente o número de processadores ou nós, o ganho de desempenho é limitado pela porção sequencial do sistema.",
    "Overheads de sincronização, comunicação de rede e contenção de recursos compartilhados reduzem o speedup real previsto pela Lei de Amdahl em sistemas distribuídos.",
    "Sob concorrência massiva de usuários, gargalos de rede e limites de conexões simultâneas frequentemente dominam a fração não paralelizável de uma API.",

    # --- Complexidade Assintótica (Big-O) ---
    "Complexidade Assintótica (Big-O) descreve como o tempo ou espaço de execução de um algoritmo cresce em relação ao tamanho da entrada.",
    "Um algoritmo de complexidade O(n) tem tempo de execução proporcional ao tamanho da entrada, como uma busca linear em uma lista.",
    "Um algoritmo de complexidade O(n²) tem tempo de execução proporcional ao quadrado do tamanho da entrada, comum em comparações par a par entre todos os elementos.",
    "Buscas por similaridade textual que comparam uma consulta contra todos os documentos de uma base tendem a ter complexidade O(n) em relação ao tamanho da base de conhecimento.",
    "Em sistemas de busca vetorial reais, índices como HNSW ou IVF são usados para evitar a comparação O(n) contra toda a base, reduzindo a latência de busca em grandes volumes de dados.",

    # --- Arquitetura Orientada a Serviços (SOA) ---
    "Arquitetura Orientada a Serviços (SOA) estrutura sistemas como um conjunto de serviços fracamente acoplados, reutilizáveis e independentes.",
    "Em SOA, serviços se comunicam por meio de contratos bem definidos (como APIs REST ou SOAP), independentemente da tecnologia interna de cada serviço.",
    "Baixo acoplamento em SOA permite que serviços sejam atualizados, escalados ou substituídos individualmente, sem impactar diretamente os demais.",
    "Microsserviços são uma evolução prática dos princípios de SOA, com cada serviço implantado e escalado de forma independente, geralmente em containers.",

    # --- Testes de Carga, Estresse e Elasticidade (Prática 2) ---
    "Testes de carga simulam múltiplos usuários acessando um sistema simultaneamente para medir vazão (throughput), latência e taxa de erros sob condições realistas.",
    "Vazão (throughput), medida em requisições por segundo (RPS), indica quantas requisições um sistema consegue processar em um intervalo de tempo.",
    "Latência p95 representa o tempo de resposta abaixo do qual 95% das requisições foram atendidas, sendo mais representativa de experiência real do que a média.",
    "Latência p99 representa o tempo de resposta abaixo do qual 99% das requisições foram atendidas, evidenciando os piores casos (outliers) de desempenho.",
    "Ferramentas como o Locust permitem simular usuários concorrentes enviando requisições HTTP para medir o comportamento de uma API sob estresse.",
    "Sob estresse crescente de usuários concorrentes, uma API pode apresentar saturação, evidenciada por aumento de latência e queda na vazão de requisições.",
    "Testes de estresse ajudam a identificar o ponto de saturação de uma infraestrutura, revelando gargalos de CPU, memória, rede ou limite de conexões concorrentes.",

    # --- Redes, Escalabilidade e Infraestrutura Complementar ---
    "Balanceadores de carga distribuem requisições recebidas entre múltiplas instâncias de um serviço, evitando sobrecarga em um único nó.",
    "Cache em memória, como Redis, reduz a latência de respostas ao evitar reprocessamento ou reconsulta de dados frequentemente acessados.",
    "Filas de mensagens, como RabbitMQ ou Kafka, permitem processamento assíncrono de tarefas, desacoplando a geração de uma requisição do seu processamento efetivo.",
    "Content Delivery Networks (CDNs) distribuem conteúdo estático geograficamente próximo ao usuário final, reduzindo a latência de rede.",
    "Kubernetes orquestra a implantação, o escalonamento automático e a recuperação de containers em clusters de múltiplos nós.",
    "Arquiteturas serverless abstraem completamente o gerenciamento de servidores, escalando funções individuais sob demanda conforme o volume de requisições.",
]