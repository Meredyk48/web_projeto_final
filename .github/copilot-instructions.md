# Levantamento de Requisitos - Aplicação Imobiliária para Construtoras

## Tecnologias a Utilizar
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript com **Bootstrap** para estilização responsiva.
- **Banco de Dados**: PostgreSQL (Render)

---

## Objetivo
Desenvolver uma aplicação web para construtoras imobiliárias, permitindo:
- Clientes visualizarem imóveis e acompanharem o andamento das obras.
- Corretores gerenciarem os imóveis e os dados dos clientes.

---

## Usuários
- **Cliente**: Visualiza imóveis, acompanha obras e gerencia preferências.
- **Corretor**: Gerencia portfólio de imóveis e acompanha clientes.

---

## Funcionalidades

### Funcionalidades para o Cliente

#### Tela de Cadastro e Autenticação
- [ ] Implementar tela de login para cliente.
- [ ] Implementar funcionalidade de recuperação de senha (opcional).

#### Tela de Visualização de Imóveis
- [ ] Criar página de listagem de imóveis.
- [ ] Implementar filtros de busca: localização, tipo, preço, número de quartos.
- [ ] Criar página de detalhes do imóvel com foto, descrição, preço, cômodos e condições de pagamento.

#### Acompanhamento de Obras
- [ ] Implementar visualização do status da obra (fases ou porcentagem).
- [ ] Criar cronograma de obra com linha do tempo e previsão de entrega.
- [ ] Configurar sistema de notificações sobre mudanças no andamento da obra.

#### Anúncio de Imóveis
- [ ] Implementar inscrição para notificações sobre novos imóveis conforme critérios.
- [ ] Criar funcionalidade para o cliente anunciar seu imóvel para venda no marketplace.

---

### Funcionalidades para o Corretor

#### Tela de Cadastro e Autenticação
- [ ] Implementar tela de login para corretor.
- [ ] Implementar funcionalidade de recuperação de senha (opcional).

#### Tela de Gerenciamento de Imóveis
- [ ] Criar funcionalidade de cadastro de novos imóveis (localização, preço, descrição, fotos, status da obra e parcelamento).
- [ ] Implementar funcionalidade de edição de imóveis cadastrados.
- [ ] Implementar funcionalidade de exclusão de imóveis do sistema.

#### Tela de Acompanhamento de Clientes
- [ ] Criar funcionalidade para cadastro de novos clientes interessados.

#### Relatórios e Notificações
- [ ] Criar relatório de vendas com informações detalhadas de imóveis e clientes.
- [ ] Configurar notificações para corretor sobre novos imóveis anunciados por clientes.

---

## Fluxo de Interação

1. [ ] Implementar fluxo de login para acesso à plataforma.
2. [ ] Implementar sistema de busca e visualização detalhada de imóveis pelo cliente.
3. [ ] Implementar cadastro de imóveis pelo corretor.
4. [ ] Implementar acompanhamento do progresso de obras pelo cliente.
5. [ ] Implementar acompanhamento do status das interações com clientes pelo corretor.
6. [ ] Definir que a aplicação não inclui métodos de pagamento, apenas conecta as partes interessadas.

---

# Configuração da Conexão com PostgreSQL no Django

## Dados da conexão:

- **hostname**: dpg-d0qellbe5dus739gp0f0-a
- **port**: 5432
- **database**: localdb_4qrk
- **username**: localdb
- **password**: fCdbUbcqlaM1PCHkCkVQJn04J2L96VAy
- **internal URL**:  
`postgresql://localdb:fCdbUbcqlaM1PCHkCkVQJn04J2L96VAy@dpg-d0qellbe5dus739gp0f0-a/localdb_4qrk`

- **external URL**:  
`postgresql://localdb:fCdbUbcqlaM1PCHkCkVQJn04J2L96VAy@dpg-d0qellbe5dus739gp0f0-a.oregon-postgres.render.com/localdb_4qrk`

---

## ✅ Passos para Configurar no Django

### 1. Instalar dependência do PostgreSQL:

```bash
pip install psycopg2-binary

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'localdb_4qrk',
        'USER': 'localdb',
        'PASSWORD': 'fCdbUbcqlaM1PCHkCkVQJn04J2L96VAy',
        'HOST': 'dpg-d0qellbe5dus739gp0f0-a.oregon-postgres.render.com',
        'PORT': '5432',
    

