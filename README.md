# Curso DevOps

Criação de API de ingredientes e receitas para aprendizagem de ferramentas de DevOps.

Haverão três linguagens sendo empregadas, implementando a mesma API e seguindo arquiteturas semelhantes inspiradas na _clean architecture_.
As linguagens são: .NET, Python e Rust. A proposta inicial é de trabalhar com as três independentemente e replicar os feitos das aulas e tarefas para aprender detalhes específicos das linguagens de interesse.

## Configurações gerais

Para Python, é feito o uso do Poetry (2.1.2) para gerenciamento de dependências, respectivo ao NPM para JavaScript.

## Estrutura de pastas

As aplicações de cada linguagem ficam isoladas dentro de suas respectivas pastas.

    python/
    ├── src/                                    # Código da aplicação
    │   ├── app/                                # Contratos e definições abstratas
    │   └── infra/                              # Implementações e infraestrutura para contato externo da aplicação
    ├── config/                                 # Configurações específicas das bibliotecas de apoio que não suportam o `pyproject.toml`
    ├── .pre-commit-config.yaml                 # Configurações do pre-commit
    ├── poetry.toml                             # Configurações locais do poetry
    └── pyproject.toml                          # Gerenciamento de dependências (utilizando Poetry)


...
