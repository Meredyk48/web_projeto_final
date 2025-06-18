# Instruções para o GitHub Copilot

## 1. Visão Geral do Projeto

Este projeto consiste em uma aplicação web para construtoras imobiliárias, projetada para conectar clientes e corretores. O objetivo principal é permitir que clientes visualizem imóveis e acompanhem o andamento das obras, enquanto corretores gerenciam os imóveis e os dados dos clientes. A aplicação possui dois tipos de usuários principais: Clientes e Corretores, cada um com funcionalidades específicas para atender às suas necessidades.


## 2. Funcionalidades

### 2.1. Funcionalidades para o Cliente

*   **Tela de Cadastro e Autenticação:**
    *   **Cadastro de Cliente:** Realizado pelo corretor.
    *   **Login:** Acesso à conta do cliente.
    *   **Recuperação de Senha:** Opção para redefinir a senha (opcional).

*   **Tela de Visualização de Imóveis:**
    *   **Lista de Imóveis:** Visualização de imóveis disponíveis para investimento.
    *   **Filtros de Busca:** Filtragem por localização, tipo, preço, número de quartos, etc.
    *   **Detalhes do Imóvel:** Página detalhada com foto, descrição, preço, cômodos, condições de pagamento, etc.

*   **Acompanhamento de Obras:**
    *   **Status da Obra:** Acompanhamento da fase da obra (fundação, estrutura, acabamento) por porcentagem ou status.
    *   **Cronograma de Obra:** Linha do tempo com previsão de entrega.
    *   **Notificações:** Recebimento de notificações sobre mudanças no andamento da obra.

*   **Anúncio de Imóveis:**
    *   **Novos Imóveis:** Inscrição para receber notificações de novos imóveis que atendam aos critérios do cliente.
    *   **Anunciar Imóvel:** Possibilidade de anunciar imóvel para venda no marketplace da aplicação.

### 2.2. Funcionalidades para o Corretor

*   **Tela de Cadastro e Autenticação:**
    *   **Cadastro de Corretor:** Realizado pelo administrador da aplicação.
    *   **Login:** Acesso à área personalizada do corretor.
    *   **Recuperação de Senha:** Opção para redefinir a senha (opcional).

*   **Tela de Gerenciamento de Imóveis:**
    *   **Cadastro de Imóveis:** Inclusão de novos imóveis com informações detalhadas (localização, preço, descrição, fotos, status da obra, parcelamento).
    *   **Edição de Imóveis:** Atualização de dados de imóveis já cadastrados.
    *   **Exclusão de Imóveis:** Remoção de imóveis do sistema.

*   **Tela de Acompanhamento de Clientes:**
    *   **Cadastro de Clientes:** Registro de novos clientes interessados nos imóveis.

*   **Relatórios e Notificações:**
    *   **Relatórios de Vendas:** Visualização de relatórios detalhados sobre imóveis e clientes.
    *   **Notificações de Novos Imóveis:** Notificação sobre novos imóveis anunciados para venda por clientes.

## 2.3. Fluxo de Interação

1.  **Login:** O usuário faz login para acessar a plataforma.
2.  **Exploração de Imóveis:** O cliente pesquisa imóveis e visualiza as informações detalhadas.
3.  **Cadastro de Imóveis:** O corretor adiciona novos imóveis ao sistema, incluindo informações detalhadas.
4.  **Gestão de Obras:** O cliente acompanha o progresso das obras dos imóveis que está interessado.
5.  **Acompanhamento de Clientes:** O corretor acompanha o status das interações com seus clientes e o progresso das vendas.
6.  **Compra:** A aplicação conecta as partes interessadas para negociação, sem necessidade de método de pagamento na aplicação.


## 3. Tecnologias e Linguagens Utilizadas

Com base na estrutura do projeto, as seguintes tecnologias e linguagens são utilizadas:

*   **Backend:**
    *   **Python:** Linguagem de programação principal.
    *   **Django:** Framework web para o desenvolvimento do backend, gerenciamento de banco de dados (ORM), autenticação e rotas.

*   **Frontend:**
    *   **HTML:** Para a estrutura das páginas web (arquivos `.html` nos diretórios `templates`).
    *   **CSS:** Para estilização (presumivelmente, embora não haja arquivos `.css` explícitos na estrutura listada, é padrão em projetos web).
    *   **JavaScript:** Para interatividade no lado do cliente (presumivelmente, embora não haja arquivos `.js` explícitos na estrutura listada, é padrão em projetos web).

*   **Banco de Dados:**
    *   O Django suporta diversos bancos de dados (SQLite, PostgreSQL, MySQL, Oracle). A configuração específica estaria no arquivo `core/settings.py`.

## 4. Estrutura do Projeto

O projeto segue a estrutura padrão de um projeto Django, com aplicações (`apps`) separadas para diferentes funcionalidades:

*   `web_projeto_final-master/` (diretório raiz do projeto)
    *   `.gitignore`: Arquivo para controle de versão.
    *   `cliente/`: Aplicação Django para funcionalidades relacionadas aos clientes.
        *   `models.py`: Definição dos modelos de dados para clientes.
        *   `views.py`: Lógica de negócio e renderização de templates para clientes.
        *   `urls.py`: Definição das rotas específicas para a aplicação de clientes.
    *   `contas/`: Aplicação Django para gerenciamento de contas de usuário (login, registro).
        *   `models.py`: Modelos de dados para usuários e autenticação.
        *   `views.py`: Lógica para autenticação e gerenciamento de contas.
        *   `urls.py`: Rotas para as funcionalidades de contas.
        *   `templates/`: Contém os templates HTML para login e registro (`login.html`, `register.html`).
    *   `core/`: Configurações principais do projeto Django.
        *   `settings.py`: Configurações globais do projeto (banco de dados, aplicações instaladas, etc.).
        *   `urls.py`: Rotas principais do projeto, que incluem as rotas das aplicações.
    *   `corretor/`: Aplicação Django para funcionalidades relacionadas aos corretores.
        *   `models.py`: Modelos de dados para corretores e imóveis.
        *   `views.py`: Lógica de negócio para gerenciamento de imóveis e corretores.
        *   `urls.py`: Rotas específicas para a aplicação de corretores.
    *   `manage.py`: Utilitário de linha de comando do Django para tarefas administrativas.
    *   `requirements.txt`: Lista de dependências Python do projeto.
    *   `templates/`: Contém templates HTML globais (`base.html`, `footer.html`).




## 5. Como o GitHub Copilot pode ajudar

O GitHub Copilot pode ser uma ferramenta extremamente útil para trabalhar neste projeto, auxiliando em diversas tarefas:

*   **Geração de Código:** Com base na estrutura do projeto e nas funcionalidades descritas, o Copilot pode sugerir trechos de código para:
    *   Modelos Django (`models.py`): Geração de campos e métodos para novos modelos ou expansão de existentes.
    *   Views Django (`views.py`): Implementação de lógica para visualização, criação, edição e exclusão de dados, bem como a manipulação de formulários.
    *   URLs Django (`urls.py`): Definição de padrões de URL e mapeamento para as views correspondentes.
    *   Templates HTML: Criação de estruturas HTML, formulários, loops e condicionais com base no contexto do Django.
    *   Testes (`tests.py`): Geração de testes unitários e de integração para as funcionalidades implementadas.

*   **Autocompletar e Sugestões:** O Copilot pode oferecer sugestões inteligentes enquanto você digita, acelerando o desenvolvimento em Python (Django) e HTML.

*   **Refatoração de Código:** Ao identificar padrões ou trechos de código que podem ser melhorados, o Copilot pode sugerir refatorações para tornar o código mais limpo e eficiente.

*   **Documentação:** Auxiliar na escrita de docstrings para funções e classes Python, explicando seu propósito, parâmetros e retornos.

*   **Depuração:** Embora não depure diretamente, o Copilot pode ajudar a identificar possíveis erros ou a sugerir correções com base no contexto do código.

*   **Entendimento do Código:** Ao navegar por arquivos existentes, o Copilot pode fornecer explicações sobre trechos de código complexos ou desconhecidos, facilitando o entendimento do projeto.