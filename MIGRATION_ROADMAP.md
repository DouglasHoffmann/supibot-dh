# Cronograma de Migração: Supibot (TypeScript para Python)

Este documento descreve o roteiro sugerido para migrar o ecossistema Supibot de Node.js/TypeScript para Python.

## Objetivos
- Melhorar a integração com ferramentas de IA e Ciência de Dados.
- Reduzir o consumo de memória em certas operações.
- Facilitar a contribuição de desenvolvedores Python.

---

## Fases da Migração

### Fase 1: Infraestrutura (Porte do `supi-core`)
Antes de migrar o bot, é necessário portar as ferramentas de base que ele utiliza.
- **Duração estimada:** 3-4 semanas.
- **Tarefas:**
    - Criar `Query` wrapper usando **SQLAlchemy** ou **Tortoise-ORM**.
    - Criar `Cache` wrapper para Redis usando **redis-py** ou **aioredis**.
    - Criar `Got` (HTTP client) wrapper usando **httpx** ou **aiohttp**.
    - Implementar utilitários de data e formatação (`SupiDate`, `timeDelta`).

### Fase 2: Estrutura de Classes Core
Implementação das classes fundamentais que regem a lógica do bot.
- **Duração estimada:** 2 semanas.
- **Tarefas:**
    - `User`: Gestão de dados e permissões.
    - `Channel`: Gestão de canais e modos.
    - `Platform`: Template base para Twitch, Discord, etc.
    - `Command`: Registro e definição de comandos.

### Fase 3: Motor de Execução e Middleware
O coração do bot que processa mensagens e decide o que executar.
- **Duração estimada:** 3 semanas.
- **Tarefas:**
    - Parser de argumentos e parâmetros (equivalente ao `parseParametersFromArguments`).
    - Sistema de Cooldown (Gerenciador em Redis/Memória).
    - Sistema de Filtros e Banphrases.
    - Sistema de Transações (Rollback em caso de erro).

### Fase 4: Integração de Plataformas
- **Duração estimada:** 4 semanas.
- **Plataformas:**
    - **Twitch:** Usando `TwitchIO`.
    - **Discord:** Usando `discord.py`.
    - **IRC/Cytube:** Implementações personalizadas usando asyncio.

### Fase 5: Migração de Comandos (Em Massa)
A parte mais extensa do projeto devido ao volume (180+ comandos).
- **Estratégia:** Migrar por grupos de importância (Sistema -> Utilidades -> Diversão).
- **Duração estimada:** 3-6 meses (dependendo da equipe).

---

## Comandos Prioritários para Migração (Sprint 1)
1. `ping`: Teste básico de latência e uptime.
2. `help`: Essencial para descoberta de outros comandos.
3. `about`: Informações do bot.
4. `afk`: Um dos comandos mais utilizados.
5. `remind`: Lógica de tempo e agendamento.
6. `set`: Configurações de canal.

---

## Desafios Técnicos Identificados
1. **Segurança ($js):** O comando `$js` atual usa `vm2` no Node. No Python, a execução de código dinâmico exige ambientes isolados (ex: Docker containers efêmeros) para garantir a mesma segurança.
2. **Tipagem:** O TypeScript oferece segurança em tempo de compilação que o Python (mesmo com Pydantic/Type Hints) lida de forma diferente. Testes unitários serão cruciais.
3. **Pipes e Aliases:** A lógica de encadeamento de comandos (`$pipe`) precisa ser cuidadosamente portada para manter a compatibilidade com a sintaxe atual.

---

## Conclusão
A migração é um projeto de longo prazo. Recomenda-se uma abordagem híbrida inicial, onde o core em Python é desenvolvido enquanto o bot em Node.js continua operando, migrando os comandos gradualmente.
