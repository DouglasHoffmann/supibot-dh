# Scanner Geral do Projeto Supibot

Este documento fornece uma visão geral detalhada das funcionalidades, módulos e arquitetura técnica do Supibot.

## 1. Resumo das Funcionalidades por Categoria

O Supibot possui mais de 200 comandos. Abaixo estão as principais categorias:

*   **🔧 Utilitários e Ferramentas:** Tradução (`translate`), clima (`weather`), dicionário (`dictionary`), cálculos matemáticos (`math`), conversão de moeda (`currency`), e encurtamento de links.
*   **🌐 Redes Sociais e Integrações:** Busca no YouTube (`youtubesearch`), ChatGPT (`gpt`), GitHub (`github`), Steam (`steamgameplayers`), e informações de canais Twitch.
*   **🎮 Diversão e Entretenimento:** 8ball, 9gag, cara ou coroa (`coinflip`), roleta russa (`russianroulette`), fatos curiosos (`funfact`), e geração de imagens por IA (`dalle`).
*   **👤 Gestão de Usuários:** Status AFK (`afk`), tempo de conta (`accountage`), histórico de mensagens (`stalk`), e vinculação de contas entre plataformas (`link`).
*   **🤖 Sistema e Administração:** Ajuda (`help`), informações do bot (`about`), recarregamento de módulos (`reload`), e gerenciamento de permissões/banimentos (`ban`, `block`).
*   **💬 Meta-Comandos:** Piping de comandos (`pipe`), criação de apelidos (`alias`), e desativação de menções (`unmention`).

---

## 2. Lista Individual de Comandos

Abaixo estão todos os comandos detectados e suas descrições resumidas:

*   **$.NET devblog**: Notícias sobre o blog de desenvolvimento .NET.
*   **$8ball**: Verifica sua pergunta contra a bola 8 de previsão do futuro.
*   **$9gag**: Busca uma postagem em destaque aleatória da página inicial do 9GAG.
*   **$about**: Posta um resumo do que o Supibot faz e o que ele é. Também menciona há quanto tempo ele está em um canal, se aplicável.
*   **$accountage**: Busca a idade da conta Twitch de uma conta informada. Se nenhuma for informada, verifica a sua.
*   **$addbetween**: Preenche a mensagem fornecida com a palavra (geralmente um emote) fornecida como primeiro argumento.
*   **$afk**: Sinaliza você como AFK (ausente). Suporta uma mensagem personalizada.
*   **$alias**: Este comando permite criar seus próprios apelidos (atalhos) para qualquer combinação de comandos e argumentos. Verifique a ajuda estendida para informações passo a passo.
*   **$aliasbuildingblock**: Uma coleção de comandos menores, usáveis apenas dentro de apelidos - e não como comandos autônomos. Considere estes como 'blocos de construção' para apelidos mais complexos.
*   **$Apple Newsroom article**: Notícias da sala de imprensa da Apple.
*   **$Arch Linux article**: Artigos sobre o Arch Linux.
*   **$Asahi Linux blog**: Notícias do blog do Asahi Linux.
*   **$badapplerendition**: Comando agregado para qualquer coisa relacionada à lista de interpretações de 'Bad Apple!!' no site.
*   **$ban**: Bane/desbane qualquer combinação de canal, usuário e comando. Usável apenas por donos de canais e embaixadores do Supibot.
*   **$bancheck**: Verifica se uma mensagem seria banida pelo sistema de banphrases em um determinado canal. Funciona apenas para canais onde estou presente.
*   **$beefact**: Posta um fato aleatório sobre abelhas.
*   **$block**: Bloqueia ou desbloqueia um usuário específico de usar um comando com você como alvo.
*   **$bot**: Permite que donos de canais e embaixadores configurem diversos parâmetros do bot para o canal gerenciado.
*   **$botsubs**: Lista os canais aos quais o Supibot está inscrito na Twitch, junto com um emote de exemplo de cada.
*   **$BS update**: Atualizações sobre Beat Saber.
*   **$Bun blogpost**: Postagens do blog do Bun.
*   **$chan**: Puxa uma postagem aleatória de um fórum do 4Chan (ou um específico se fornecido).
*   **$channelfounderlist**: Mostra a lista de fundadores do canal especificado (ou atual). Não marca os usuários no chat.
*   **$chatneighbour**: Encontra seus 'vizinhos' de chat. Quando a lista de usuários é ordenada alfabeticamente, são os usuários que vêm antes e depois de você.
*   **$chatsummary**: Resume as últimas mensagens no canal atual (ou fornecido) via GPT. Aplica um cooldown de 30s para todos no canal.
*   **$check**: Verifica certas variáveis do sistema ou usuário. Verifique a ajuda estendida para a lista de tipos.
*   **$checkem**: Similar ao 4chan, posta o ID da sua mensagem e verifica se possui dígitos repetidos (dubs e superiores).
*   **$Cloudflare Developer products update**: Atualizações de produtos para desenvolvedores da Cloudflare.
*   **$code**: Posta um link para a definição do código de um comando específico no GitHub.
*   **$coinflip**: Joga uma moeda e mostra o resultado.
*   **$comment**: Busca um comentário aleatório de um conjunto de 10 mil vídeos do YouTube gerados aleatoriamente.
*   **$commitcount**: Para um usuário do GitHub, informa o número de eventos de push nas últimas 24 horas.
*   **$cookie**: Abre um biscoito da sorte aleatório. Apenas um por dia! Reset ocorre à meia-noite UTC.
*   **$copypasta**: Busca uma copypasta aleatória relacionada à Twitch.
*   **$corona**: Verifica o número atual de infectados/falecidos pela propagação do Coronavírus.
*   **$countline**: Busca o número de linhas de chat que um usuário específico (ou você) enviou no canal atual.
*   **$countlinechannel**: Busca o número total de linhas de chat no canal atual.
*   **$countlinetotal**: Busca o número de linhas de dados de TODAS as tabelas de log que o Supibot usa.
*   **$crypto**: Busca o preço mais recente de uma criptomoeda. Padrão: BTC.
*   **$cryptogame**: Comando do jogo de cripto! Receba o equivalente a €1000 em seu portfólio e invista em várias moedas.
*   **$currency**: Tenta converter uma quantia especificada de uma moeda para outra. Suporta códigos ISO de 3 letras.
*   **$current**: Busca a música que está tocando atualmente na stream.
*   **$dalle**: Busca uma imagem DALL-E pré-fabricada aleatória, ou baseada em sua busca.
*   **$dankdebug**: Comando de depuração para uso público (limitado por segurança).
*   **$dayoftheyear**: Verifica que tipo de dia internacional (ou mês) é hoje. Também aceita datas específicas.
*   **$debug**: Comando de depuração (supiniHack).
*   **$define**: Combina várias formas de buscar a definição de uma palavra ou frase e escolhe o melhor resultado.
*   **$Deno article**: Artigos sobre o Deno.
*   **$devnull**: Descarta toda a saída. Usável apenas em pipes.
*   **$dictionary**: Busca a definição de dicionário de uma palavra em inglês.
*   **$discord**: Posta o link para o Discord do canal atual.
*   **$doesnotexist**: Posta uma imagem aleatória do site 'thispersondoesnotexist.com' (gerada por IA).
*   **$downloadclip**: Recebe um nome ou link de clipe da Twitch e envia um link de download por mensagem privada.
*   **$Emojipedia blogpost**: Postagens do blog da Emojipedia.
*   **$epal**: Busca uma pessoa aleatória do epal.gg e posta sua descrição.
*   **$espn**: Mostra informações relacionadas a partidas em diversas ligas esportivas da América do Norte.
*   **$externalbot**: Faz o Supibot executar um comando de outro bot e retorna a resposta desse bot. Usável apenas em pipes.
*   **$faceit**: Comando para tudo relacionado ao CS:GO dentro do FACEIT.
*   **$Factorio blogpost**: Postagens do blog do Factorio.
*   **$fakenews**: Cria aleatoriamente manchetes de notícias falsas para fins humorísticos. Não leve a sério.
*   **$faq**: Posta o link para o FAQ do Supibot no site supinic.com.
*   **$fill**: Embaralha a entrada aleatoriamente, preenchendo a mensagem.
*   **$findraidstreams**: Itera sobre canais da Twitch qualificados para encontrar streams online para um raid.
*   **$firstchannelfollower**: Busca o primeiro usuário que segue você ou outra pessoa na Twitch.
*   **$firstfollowedchannel**: Busca o primeiro canal que você ou outra pessoa seguiu na Twitch.
*   **$firstline**: Posta a primeira linha de chat do usuário alvo no canal atual ou especificado.
*   **$firstseen**: Informa quando um usuário foi visto pela primeira vez no chat (baseado nos logs).
*   **$fish**: Vá pescar! Suporta vários subcomandos.
*   **$followage**: Busca o tempo de seguimento (followage) para um usuário e canal.
*   **$formula1**: Comando agregado sobre qualquer coisa relacionada à Fórmula 1.
*   **$forsenCD**: Uma citação aleatória do 'DrDisrespect'.
*   **$forsenE**: Posta um tweet aleatório do 'forsenE'.
*   **$funfact**: Busca um fato curioso aleatório. Não garantido ser divertido ou fato.
*   **$gachicheck**: Verifica se um link de gachi existe no banco de dados.
*   **$gachisearch**: Busca por uma faixa na lista de gachi e tenta postar um link.
*   **$getprofilepicture**: Busca a foto de perfil de um usuário da Twitch.
*   **$gift**: Comando depreciado! Use `$cookie gift`.
*   **$Gitea**: Atualizações do Gitea.
*   **$github**: Posta links dos repositórios do Supibot e do site no GitHub.
*   **$GitHub**: Atualizações do GitHub.
*   **$GitHub blogpost**: Postagens do blog do GitHub.
*   **$GitLab**: Atualizações do GitLab.
*   **$gpt**: Consulta o ChatGPT para uma resposta de texto. Suporta múltiplos modelos.
*   **$haHAA**: Posta uma piada aleatória e hilária.
*   **$help**: Posta uma lista curta de comandos ou a descrição de um comando específico.
*   **$horoscope**: Verifica o horóscopo de um signo do zodíaco.
*   **$howlongtobeat**: Mostra quanto tempo leva para zerar um jogo, baseado no site howlongtobeat.com.
*   **$id**: Verifica seu ID (ou de outro) no banco de dados de usuários.
*   **$inspireme**: Inspira você. Aleatoriamente.
*   **$isdown**: Verifica se um site está fora do ar ou se é apenas com você.
*   **$kiss**: Beija o usuário alvo.
*   **$knowyourmeme**: Obtém uma breve descrição de um meme do site Know Your Meme.
*   **$lastline**: Posta a última linha de chat do usuário alvo no canal atual.
*   **$lastseen**: Informa quando um usuário foi visto pela última vez, baseado em sua atividade no chat.
*   **$link**: Verifica o desafio de vinculação de conta entre plataformas.
*   **$liveuamap**: Busca um evento recente da guerra Rússia-Ucrânia.
*   **$markov**: Cria uma sequência aleatória de palavras baseada em uma cadeia de Markov do chat da Twitch.
*   **$math**: Faz cálculos matemáticos usando math.js.
*   **$me**: Transforma a saída em uma mensagem '/me'.
*   **$metrics**: Mostra várias métricas relacionadas ao Supibot.
*   **$moba**: Permite verificar várias coisas relacionadas a jogos MOBA como League of Legends.
*   **$MSVC++ devblog**: Blog de desenvolvimento do MSVC++.
*   **$necrodancer**: Comando relacionado ao jogo Crypt of the Necrodancer.
*   **$news**: Busca notícias curtas. Suporta códigos de países de 2 letras ou busca por termos.
*   **$Node.js version**: Atualizações de versão do Node.js.
*   **$nutrients**: Posta nutrientes básicos para uma consulta de alimento específica.
*   **$ocr**: Tenta encontrar texto em um link de imagem usando OCR.
*   **$optout**: Faz com que você não possa ser alvo de um comando.
*   **$origin**: Busca a origem de um determinado emote.
*   **$osrs**: Comando agregado para qualquer coisa relacionada ao Old School Runescape.
*   **$OSRS article**: Artigos sobre o Old School Runescape.
*   **$pastebin**: Retorna o conteúdo de um paste do Pastebin/Hastebin ou posta sua entrada em um novo paste.
*   **$percent**: Gera uma porcentagem aleatória entre 0 e 100%.
*   **$pick**: Escolhe uma palavra aleatória de uma lista fornecida.
*   **$ping**: Ping! Mostra tempo de atividade, temperatura e latência.
*   **$pingme**: Define uma autonotificação quando o usuário alvo é visto em outro canal.
*   **$pipe**: Passa o resultado de um comando para outro. Use os caracteres '|' ou '>' para separar.
*   **$playsound**: Toca um som na stream do Supinic, se habilitado.
*   **$poe**: Uma coleção de comandos relacionados ao Path of Exile.
*   **$pyramid**: Cria uma pirâmide no chat (requer VIP ou Moderador).
*   **$Python version**: Atualizações de versão do Python.
*   **$query**: Consulta ao Wolfram Alpha para informações ou cálculos.
*   **$randomalbum**: Posta um álbum de música aleatório.
*   **$randomanimalfact**: Posta um fato aleatório sobre um tipo de animal selecionado.
*   **$randomanimalpicture**: Posta uma imagem aleatória de um tipo de animal.
*   **$randomclip**: Posta um clipe aleatório do canal atual ou especificado.
*   **$randomcocktail**: Busca uma receita de coquetel.
*   **$randomcommandalias**: Posta um apelido de comando aleatório do Supibot.
*   **$randomdonger**: Levante seus dongers (͡° ͜ʖ ͡°).
*   **$randomemoji**: Busca um emoji aleatório.
*   **$randomemote**: Busca um emote aleatório do escopo do canal atual.
*   **$randomfilm**: Busca um filme aleatório.
*   **$randomgachi**: Busca uma faixa de gachi aleatória da lista.
*   **$randomhistoricevent**: Posta um evento histórico aleatório que aconteceu no dia atual.
*   **$randominstagram**: Busca uma postagem aleatória de um usuário do Instagram.
*   **$randomline**: Busca uma linha aleatória do canal atual.
*   **$randommeal**: Busca uma receita de refeição.
*   **$randommeme**: Posta um meme aleatório do Reddit.
*   **$randompastebin**: Busca um paste aleatório postado recentemente no Pastebin.
*   **$randomsadcat**: Posta uma imagem aleatória de um gato triste SadCat.
*   **$randomscp**: Busca a descrição de um SCP aleatório da Wiki da Fundação SCP.
*   **$randomword**: Busca uma palavra aleatória.
*   **$record**: Verifica recordes de várias fontes.
*   **$reload**: Recarrega uma definição de banco de dados ou um script atualizado.
*   **$remind**: Define um lembrete para um usuário ou para si mesmo.
*   **$restart**: Reinicia o bot e opcionalmente puxa mudanças do git.
*   **$resumeafk**: Retoma seu status AFK se usado logo após voltar.
*   **$roll**: Gera um número aleatório (padrão 1-100) ou rola dados.
*   **$Runelite version**: Atualizações de versão do Runelite.
*   **$russianarmylosses**: Busca as perdas mais recentes do exército russo na Ucrânia.
*   **$russianroulette**: Joga roleta russa. Se perder, você é silenciado (timeout).
*   **$Rust article**: Artigos sobre Rust.
*   **$schedule**: Posta a programação de streams do canal.
*   **$set**: Define ou remove certas variáveis dentro do Supibot.
*   **$shoutout**: Dá um 'shoutout' a um streamer e mostra o último jogo jogado.
*   **$shuffle**: Embaralha a mensagem fornecida, palavra por palavra.
*   **$simplesql**: Executa uma consulta SQL rápida e retorna o resultado.
*   **$slots**: Gira uma pseudo máquina caça-níqueis com emotes.
*   **$songrequest**: Solicita uma música para tocar na stream do Supinic.
*   **$songrequestqueue**: Posta o resumo da fila de pedidos de música.
*   **$sort**: Ordena alfabeticamente a mensagem fornecida.
*   **$speedrun**: Busca o recorde mundial atual (WR) de um jogo.
*   **$stalk**: Tenta encontrar a última mensagem enviada por um usuário, o canal e o horário.
*   **$statistics**: Posta várias estatísticas sobre você ou outros usuários.
*   **$Steam giveaway**: Informações sobre sorteios (giveaways) na Steam.
*   **$steamgameplayers**: Busca um jogo da Steam e informa a quantidade atual de jogadores.
*   **$stock**: Busca o preço mais recente e a variação diária de uma ação.
*   **$stream**: Múltiplas configurações sobre a stream do Supinic.
*   **$streaminfo**: Posta informações sobre uma stream da Twitch.
*   **$subage**: Busca dados de inscrição de um usuário em um canal da Twitch.
*   **$subscribe**: Inscreve-se ou cancela inscrição em diversos eventos (ex: canal entrando ao vivo).
*   **$suggest**: Sugere algo para o Supinic.
*   **$test**: Teste.
*   **$texttospeech**: Toca TTS na stream do Supinic, se habilitado.
*   **$texttransform**: Transforma o texto fornecido em um dos tipos disponíveis (ex: vaporwave).
*   **$tf2**: Comando agregado para tudo relacionado ao Team Fortress 2.
*   **$thesaurus**: Tenta recriar sua frase usando sinônimos aleatórios para cada palavra.
*   **$time**: Busca a hora atual e fuso horário para um local ou usuário.
*   **$top**: Posta os top X usuários por linhas de chat enviadas no canal atual.
*   **$topgames**: Busca os 10 jogos mais populares na Twitch no momento.
*   **$topstreams**: Verifica as 10 principais streams na Twitch.
*   **$totalcountline**: Busca o total de linhas de chat de um usuário em todos os canais rastreados.
*   **$trackreupload**: Gerencia reuploads de faixas na lista.
*   **$translate**: Traduz implicitamente de um idioma reconhecido para o inglês (ou conforme parâmetros).
*   **$transliterate**: Transliterator de texto não-latino para latino.
*   **$tuck**: Coloca o usuário alvo na cama.
*   **$twitchlotto**: Busca uma imagem aleatória do Imgur de um canal da Twitch e verifica conteúdo NSFW.
*   **$twitchlottoexplain**: Cria uma versão explicativa de um link do TwitchLotto.
*   **$twitter**: Busca o último tweet de um usuário.
*   **$Typescript devblog**: Blog de desenvolvimento do TypeScript.
*   **$unmention**: Faz com que um comando específico não mencione você.
*   **$unping**: Define/remove se um comando deve mencionar você ao ser invocado.
*   **$urban**: Busca a definição de um termo no Urban Dictionary.
*   **$V8 version**: Atualizações de versão do motor V8.
*   **$vanish**: Aplica um timeout de 1 segundo em si mesmo (apenas Twitch).
*   **$weather**: Busca o clima atual em um determinado local.
*   **$whatanimeisit**: Tenta identificar um anime a partir de uma captura de tela.
*   **$whatemoteisit**: Posta detalhes sobre um determinado emote de inscrito da Twitch.
*   **$when**: Informa aproximadamente quando seu comando será executado.
*   **$whisper**: Faz com que o bot responda por mensagem privada (apenas em pipes).
*   **$wiki**: Busca o cabeçalho do primeiro artigo encontrado na Wikipedia.
*   **$wrongsong**: Pula a primeira música ou uma específica na fila de pedidos.
*   **$youtubesearch**: Busca vídeos no YouTube.

---

## 3. Módulos de Chat (Chat Modules)

Estes módulos funcionam em segundo plano, reagindo a eventos do chat sem a necessidade de um comando direto:

*   **async-markov-experiment**: Experimento super experimental de markov automático assíncrono.
*   **automatic-unscramble**: Tenta resolver automaticamente o minijogo de desembaralhar do thepositivebot.
*   **chat-suggestion-linker**: Detecta IDs de sugestões do Supibot e posta o link correspondente.
*   **imgur-link-gatherer**: Coleta links do Imgur nos canais e faz o reupload se possível.
*   **live-detection**: Envia mensagens privadas para usuários inscritos em eventos de início de stream.
*   **message-react**: Reage a mensagens específicas com uma resposta determinada.
*   **offline-only-mirror**: Gerencia espelhamento de canais para que funcionem apenas quando o canal está offline.
*   **offline-only-mode**: Faz o Supibot entrar em modo apenas leitura quando o canal está online.
*   **ping-supi**: Notifica o Supinic via sussurros na Twitch sempre que ele é mencionado.
*   **pyramid-detection**: Detecta 'pirâmides' no chat. Parabeniza quem termina uma e critica quem quebra uma.
*   **raid-react**: Reage a um canal da Twitch sendo alvo de um raid.
*   **stream-points-redemptions**: Reage a resgates de pontos de canal.
*   **streamer-health-notification**: Configura notificações periódicas de 'saúde' quando o canal entra ao vivo.
*   **subscription-react**: Reage a inscrições em canais da Twitch.
*   **supinic-silence-prevention-trigger**: Alterna o gatilho de prevenção de silêncio na stream do Supinic.
*   **supinic-stream-db**: Cria e atualiza linhas no banco de dados sobre streams no canal do Supinic.
*   **suspicious-user-auto-check**: Verifica automaticamente usuários suspeitos baseados em mensagens enviadas.
*   **twitch-bot-scope-reminder**: Notifica usuários sobre permissões do bot durante janelas de transição.
*   **wanna-become-famous**: Bane vários bots de spam ou de seguidores.

---

## 4. Plataformas Suportadas

O Supibot é multi-plataforma e possui integrações específicas para cada uma:

*   **Twitch:** Plataforma principal, com suporte a emotes (BTTV/FFZ/7TV), subs, raids, e moderação.
*   **Discord:** Integração via bot de Discord, suportando embeds e mirrors de canais.
*   **Cytube:** Suporte a salas do Cytube.
*   **IRC:** Integração com servidores IRC (atualmente ativo na Libera).

---

## 5. Arquitetura Técnica

### Principais Classes (`classes/`)
*   **`Command`**: Define a estrutura de um comando (Nome, Descrição, Cooldown, Flags) e gerencia sua execução.
*   **`User`**: Gerencia dados de usuários, permissões globais e vínculos entre plataformas.
*   **`Channel`**: Representa um canal em qualquer plataforma, gerenciando modos (Read-only, etc.) e configurações locais.
*   **`Platform`**: Classe base abstrata para todas as plataformas, definindo como enviar mensagens, sussurros e tratar eventos.
*   **`Banphrase`**: Sistema de filtragem de mensagens por palavras proibidas ou regras complexas.

### Utilitários e Funções Internas (`utils/`)

#### `command-utils.ts`
*   `TWITCH_ANTIPING_CHARACTER`
*   `VIDEO_TYPE_REPLACE_PREFIX`
*   `fetchGeoLocationData`
*   `fetchTimeData`
*   `fetchYoutubePlaylist`
*   `getPathFromURL`
*   `getTwitchGameID`
*   `handleGenericFilter`
*   `parseChrono`
*   `parseGenericFilterOptions`
*   `parseRSS`
*   `postToHastebin`
*   `postToPastebin`
*   `randomInt`
*   `searchYoutube`
*   `uploadFile`
*   `uploadToImgur`
*   `uploadToKappaLol`
*   `uploadToNuuls`

#### `config-validation-schema.ts`
*   `ConfigSchema`

#### `languages.ts`
*   `get`
*   `getCode`
*   `getLanguage`
*   `getName`
*   `languages`
*   `search`

#### `regexes.ts`
*   `asciiArtRegex`
*   `brailleRegex`
*   `emojiRegex`
*   `linkRegex`
*   `whitespaceRegex`

#### `schemas.ts`
*   `ivrClipSchema`
*   `ivrEmoteSchema`
*   `ivrErrorSchema`
*   `ivrFoundersSchema`
*   `ivrSubAgeSchema`
*   `ivrUserDataSchema`
*   `twitchChannelSchema`
*   `twitchIdentitySchema`
*   `twitchScheduleSchema`
*   `twitchStreamSchema`
*   `twitchSubscriberSchema`

#### `ts-helpers.ts`
*   `filterNonNullable`
*   `hasKey`
*   `typeRegexGroups`
*   `typedEntries`
*   `typedKeys`

### Singletons e Infraestrutura
*   **`Logger`**: Central de logs de execução e erros.
*   **`Query` (supi-core)**: Abstração para consultas ao banco de dados SQL.
*   **`Got` (supi-core)**: Cliente HTTP para chamadas de API externas.

### Fluxo de Execução de um Comando
1.  **Recebimento:** A plataforma (ex: Twitch) recebe a mensagem.
2.  **Identificação:** `Command.checkAndExecute` verifica se a mensagem começa com o prefixo (`$`) e se o comando existe.
3.  **Filtros:** Verifica permissões do usuário, se o canal permite o comando e se há cooldown ativo.
4.  **Execução:** O código definido em `index.ts` do comando é executado.
5.  **Banphrase:** O resultado é verificado contra o sistema de banphrases.
6.  **Resposta:** O bot envia a resposta final para a plataforma de origem.
