# Projeto M2A

## Configuração

1. Clone o repositório:
    ```sh
    git clone git@github.com:havinercavalcante/m2a-tecnologia.git
    cd m2a-tecnologia
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Configure o banco de dados:
    ```sh
    python manage.py migrate
    ```

4. Execute os testes:
    ```sh
    python manage.py test   
    ```

5. Inicie o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

## Uso

A aplicação está pronta para uso. Navegue até `http://localhost:8000/` para acessar a API de abastecimentos.

## Funcionalidades Principais

- **Registro de Abastecimentos**: Controle dos abastecimentos feitos durante cada dia, incluindo identificação da bomba utilizada, quantidade de litros e valor abastecido, com cálculo do imposto de 13%.
- **Estrutura dos Tanques e Bombas**: Gerenciamento de dois tanques (gasolina e óleo diesel), cada um associado a duas bombas.
- **Relatórios**: Geração de relatórios em PDF com dados agrupados por dia, tanque, bomba e valor, incluindo soma total do período.

## Endpoints da API

- **Tanques**: `http://localhost:8000/api/tanques/`
- **Bombas**: `http://localhost:8000/api/bombas/`
- **Abastecimentos**: `http://localhost:8000/api/abastecimentos/`
- **Relatórios**: `http://localhost:8000/api/relatorio/`

## Relatórios em PDF

Para gerar um relatório em PDF, acesse o endpoint:

- **Relatórios**: `http://localhost:8000/api/relatorio/`
  
Requisição POST com um JSON contendo data_inicio e data_fim.

- **Exemplo**:
`{
    "data_inicio": "2024-06-01",
    "data_fim": "2024-06-19"
}`


