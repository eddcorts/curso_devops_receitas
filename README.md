# Curso DevOps

Criação de API de ingredientes e receitas para aprendizagem de ferramentas de DevOps.

Haverão três linguagens sendo empregadas, implementando a mesma API e seguindo arquiteturas semelhantes e inspiradas na _clean architecture_, visando haver facilidade para agregar novos componentes à lógica como um serviço de banco de dados.

As linguagens são: .NET, Python e Rust. A proposta inicial é de trabalhar com as três independentemente e replicar os feitos das aulas e tarefas para aprender detalhes específicos das linguagens de interesse.

## Configurações gerais

### Python
Para Python, é feito o uso do [Poetry](https://python-poetry.org/) (2.1.2) para gerenciamento de dependências, respectivo ao NPM para JavaScript.
Também se faz o uso do [pre-commit](https://pre-commit.com/) para manter qualidade geral de código.

Após instalar instalar o `poetry`, instale as dependências com o comando `poetry install`. É necessário estar na pasta `python/` para executar esse e os comandos a seguir.

Para iniciar a API, utilize o comando `poe start`. É possível acessar o `swagger` da API neste [link](0.0.0.0:8888/docs).

## Escolhas de design

Conforme mencionado, as APIs implementarão a _clean architecture_.

Os **dados** são armazenados em memória. Com a arquitetura, será fácil transitar para um armazenamento em um banco de dados ou ainda uma versão mais rústica com gerenciamento de um arquivo local.

## Estrutura de pastas

As aplicações de cada linguagem ficam isoladas dentro de suas respectivas pastas.

    python/
    ├── src/                                    # Código da aplicação
    │   ├── app/                                # Entidades, contratos e definições abstratas
    │   └── infra/                              # Implementações e infraestrutura para contato externo da aplicação
    ├── config/                                 # Configurações específicas das bibliotecas de apoio que não suportam o `pyproject.toml`
    ├── .pre-commit-config.yaml                 # Configurações do pre-commit
    ├── poetry.toml                             # Configurações locais do poetry
    └── pyproject.toml                          # Gerenciamento de dependências (utilizando Poetry)


...
