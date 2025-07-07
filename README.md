# Construtora Imobiliária - Projeto Web Final

Este projeto é uma aplicação web desenvolvida com Django e HTML para gestão de imóveis para uma construtora imobiliária. O sistema oferece funcionalidades completas para corretores e clientes, incluindo cadastro de imóveis, acompanhamento de status de obras, notificações, interesses e vendas.

---

## Sumário
- [Funcionalidades Principais](#funcionalidades-principais)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Instalar e Executar](#como-instalar-e-executar)
- [Modelos Principais](#modelos-principais)
- [Fluxo do Usuário](#fluxo-do-usuário)
- [Testes](#testes)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Funcionalidades Principais

### Para Clientes
- Cadastro e autenticação de usuários (realizado pelo corretor)
- Dashboard personalizado para acompanhar imóveis de interesse
- Visualização detalhada de imóveis (descrição, preço, área, status da obra, condições, etc.)
- Cadastro de interesse em imóveis com notificações automáticas
- Acompanhamento do status da obra com barra de progresso e cronograma
- Anúncio de imóveis próprios para venda no marketplace da aplicação
- Recebimento de notificações sobre imóveis de interesse e atualizações de obras

### Para Corretores
- Cadastro e autenticação de usuários (realizado pelo administrador)
- Dashboard personalizado para gerenciar imóveis, clientes e vendas
- Cadastro de imóveis com foto, dados completos, status e condições de pagamento
- Edição e atualização de dados de imóveis já cadastrados
- Gestão de status de obras (fundação, estrutura, acabamento, entregue)
- Visualização e gerenciamento de clientes interessados em imóveis
- Adição de imóveis à lista de interesse de clientes específicos
- Gestão de vendas de imóveis
- Administração dos dados via Django Admin

### Funcionalidades Gerais
- Sistema de notificações automáticas
- Interface responsiva com Bootstrap 5
- Autenticação baseada em perfis (Cliente/Corretor)
- Upload e gerenciamento de imagens de imóveis
- Relatórios de vendas e atividades

---

## Tecnologias Utilizadas

- **Backend:** Python 3, Django 5.2
- **Frontend:** HTML5, Bootstrap 5, Bootstrap Icons
- **Banco de Dados:** SQLite (padrão do Django, pode ser alterado para PostgreSQL, MySQL, etc.)
- **Upload de Arquivos:** Pillow para processamento de imagens
- **Outros:** Django Admin, autenticação padrão do Django, sistema de sinais Django

---

## Estrutura do Projeto

```
web_projeto_final/
├── cliente/                    # App para funcionalidades do cliente
│   ├── admin.py               # Configuração do admin Django
│   ├── models.py              # Modelos: Notificacao, InteresseImovel, AnuncioImovelCliente
│   ├── views.py               # Views para dashboard e funcionalidades do cliente
│   ├── urls.py                # URLs específicas do cliente
│   ├── tests.py               # Testes unitários
│   └── migrations/            # Migrações do banco de dados
├── corretor/                   # App para funcionalidades do corretor
│   ├── admin.py               # Configuração do admin Django
│   ├── models.py              # Modelos: Imovel, StatusObra, Venda, RelatorioVenda
│   ├── views.py               # Views para dashboard e gestão de imóveis
│   ├── urls.py                # URLs específicas do corretor
│   ├── forms.py               # Formulários Django
│   ├── tests.py               # Testes unitários
│   └── migrations/            # Migrações do banco de dados
├── contas/                     # App para autenticação e perfis de usuário
│   ├── models.py              # Modelo: Profile (perfis de usuário)
│   ├── views.py               # Views para login, registro e perfis
│   ├── urls.py                # URLs para autenticação
│   ├── signals.py             # Sinais Django para criação automática de perfis
│   ├── templates/             # Templates específicos de autenticação
│   │   ├── login.html
│   │   └── register.html
│   └── migrations/            # Migrações do banco de dados
├── core/                       # Configurações principais do Django
│   ├── settings.py            # Configurações globais do projeto
│   ├── urls.py                # URLs principais do projeto
│   ├── wsgi.py                # Configuração WSGI para produção
│   └── asgi.py                # Configuração ASGI para aplicações assíncronas
├── templates/                  # Templates globais
│   ├── base.html              # Template base com navegação
│   ├── footer.html            # Rodapé comum
│   └── pages/                 # Templates de páginas específicas
│       ├── dashboard_cliente.html
│       ├── dashboard_corretor.html
│       ├── cadastrar_imovel.html
│       ├── editar_imovel.html
│       ├── detalhe_imovel.html
│       ├── clientes_interessados.html
│       ├── editar_status_obra.html
│       ├── perfil.html
│       └── editar_perfil.html
├── imoveis/                    # Diretório para upload de imagens
├── static/                     # Arquivos estáticos (CSS, JS, imagens)
├── manage.py                   # Utilitário de linha de comando do Django
├── requirements.txt            # Dependências Python do projeto
├── ATUALIZAR_MODELS_STATUS.txt # Instruções para migração de modelos
└── README.md                   # Esta documentação
```

### Principais Apps Django:
- **cliente:** Funcionalidades direcionadas ao cliente (interesses, notificações, anúncios)
- **corretor:** Funcionalidades para o corretor (gestão de imóveis, vendas, relatórios)
- **contas:** Autenticação, registro e perfis de usuário com roles diferenciados

---

## Como Instalar e Executar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Meredyk48/web_projeto_final.git
   cd web_projeto_final
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realize as migrações do banco de dados:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
   **Nota:** Caso altere os modelos, siga as instruções do arquivo `ATUALIZAR_MODELS_STATUS.txt`.

5. **Crie um usuário administrador:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação:**
   - **Sistema principal:** http://localhost:8000/
   - **Admin Django:** http://localhost:8000/admin/

### Configuração Adicional
- Para uso em produção, altere as configurações em `core/settings.py`
- Configure um banco de dados apropriado (PostgreSQL, MySQL) se necessário
- Defina uma `SECRET_KEY` segura para produção
- Configure o `DEBUG = False` em produção

---

## Modelos Principais

### Profile (contas/models.py)
- **Propósito:** Estender o modelo User padrão do Django com roles e informações específicas
- **Campos principais:** user, role (CLIENTE/CORRETOR), telefone, data_nascimento, creci, endereco
- **Relacionamentos:** OneToOne com User

### Imovel (corretor/models.py)
- **Propósito:** Representa os imóveis disponíveis para venda
- **Campos principais:** titulo, descricao, tipo (apartamento, casa, etc), localização, preço, quartos, banheiros, vagas, área, status, condições de pagamento, foto, ativo
- **Relacionamentos:** ForeignKey com Profile (corretor)
- **Status de obra:** ESTRUTURACAO, ACABAMENTO, FINALIZADO

### StatusObra (corretor/models.py)
- **Propósito:** Controla o progresso da construção dos imóveis
- **Campos principais:** imovel, status (FUNDACAO, ESTRUTURA, ACABAMENTO, ENTREGUE), porcentagem, cronograma
- **Relacionamentos:** OneToOne com Imovel

### InteresseImovel (cliente/models.py)
- **Propósito:** Registra o interesse de clientes em imóveis específicos
- **Campos principais:** cliente, imovel, data_interesse, receber_novos (notificações)
- **Relacionamentos:** ForeignKey com Profile (cliente) e Imovel

### Notificacao (cliente/models.py)
- **Propósito:** Sistema de notificações para clientes
- **Campos principais:** cliente, mensagem, data_envio, lida
- **Relacionamentos:** ForeignKey com Profile (cliente)

### Venda (corretor/models.py)
- **Propósito:** Registra as vendas realizadas
- **Campos principais:** imovel, cliente, corretor, data_venda, valor_venda, status
- **Relacionamentos:** ForeignKey com Imovel, Profile (cliente e corretor)

### AnuncioImovelCliente (cliente/models.py)
- **Propósito:** Permite que clientes anunciem seus próprios imóveis
- **Campos principais:** cliente, titulo, descricao, localizacao, preco, foto, data_anuncio, ativo
- **Relacionamentos:** ForeignKey com Profile (cliente)

---

## Fluxo do Usuário

### Fluxo de Registro e Login
1. **Acesso inicial:** Usuário acessa o sistema pela página de login
2. **Registro:** Escolha do perfil (Cliente ou Corretor) durante o cadastro
3. **Login:** Autenticação e redirecionamento para dashboard específico do role

### Fluxo do Cliente
1. **Dashboard:** Visualiza resumo de imóveis de interesse e notificações
2. **Exploração:** Navega pelos imóveis disponíveis com filtros
3. **Interesse:** Registra interesse em imóveis específicos
4. **Acompanhamento:** Monitora o progresso das obras dos imóveis de interesse
5. **Notificações:** Recebe atualizações automáticas sobre imóveis e obras
6. **Anúncios:** Pode anunciar imóveis próprios para venda

### Fluxo do Corretor
1. **Dashboard:** Visualiza resumo de imóveis, clientes e vendas
2. **Gestão de Imóveis:** 
   - Cadastra novos imóveis com informações completas
   - Edita dados de imóveis existentes
   - Atualiza status das obras
3. **Gestão de Clientes:**
   - Visualiza clientes interessados em cada imóvel
   - Adiciona imóveis específicos à lista de interesse de clientes
4. **Vendas:** Registra e acompanha o processo de vendas
5. **Relatórios:** Acessa relatórios de desempenho e vendas

### Fluxo de Interação
- **Conexão:** O sistema conecta clientes interessados com corretores
- **Comunicação:** Notificações automáticas mantêm todas as partes informadas
- **Transparência:** Acompanhamento em tempo real do status das obras
- **Eficiência:** Dashboards personalizados para cada tipo de usuário

---

## Testes

O projeto possui testes unitários para validar os modelos e funcionalidades principais.

### Executar Todos os Testes
```bash
python manage.py test
```

### Executar Testes Específicos
```bash
# Testes do app corretor
python manage.py test corretor

# Testes do app cliente  
python manage.py test cliente

# Testes do app contas
python manage.py test contas
```

### Testes Implementados
- **corretor.tests.ImovelModelTest:** Testa criação de imóveis com status e validações
- Testes de modelos para validar relacionamentos e campos obrigatórios
- Testes de views para funcionalidades críticas

---

### Créditos
Desenvolvido como projeto final de curso em Django/Python para demonstrar conceitos de:
- Desenvolvimento web full-stack
- Modelagem de banco de dados
- Autenticação e autorização
- Interface de usuário responsiva
- Arquitetura MVT (Model-View-Template)

---

## Desenvolvido por [Bruno Meredyk](https://github.com/Meredyk48) e [Luiz Bernardi](https://github.com/luizbernardi)
