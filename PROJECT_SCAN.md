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

*   **$.NET devblog**: No description found.
*   **$8ball**: Checks your question against the fortune-telling 8-ball.
*   **$9gag**: Fetches a random featured post from the front page of 9GAG.
*   **$about**: Posts a summary of what Supibot does, and what it is. Also, mentions how long it's been in a channel, if applicable.
*   **$accountage**: Fetches the Twitch account age of a given account. If none is given, checks yours.
*   **$addbetween**: Fills the message provided with the word (usually an emote) provided as the first argument.
*   **$afk**: Flags you as AFK. Supports a custom AFK message.
*   **$alias**: This command lets you create your own aliases (shorthands) for any other combination of commands and arguments. Check the extended help for step-by-step info.
*   **$aliasbuildingblock**: A collection of smaller commands, only usable within aliases - and not as standalone commands. Consider these "building blocks" for more complex aliases, without needing to make them yourself.
*   **$Apple Newsroom article**: No description found.
*   **$Arch Linux article**: No description found.
*   **$Asahi Linux blog**: No description found.
*   **$badapplerendition**: Aggregate command for anything regarding the Bad Apple!! rendition list on the website.
*   **$ban**: Bans/unbans any combination of channel, user, and command from being executed. Only usable by channel owners and Supibot ambassadors.
*   **$bancheck**: Checks if a given message would be banphrased in a given channel. Only works for channels that I am in, plus the result isn't 100% guaranteed!
*   **$beefact**: Posts a random fact about bees.
*   **$block**: Blocks, or unblocks a specified user from using a specified command with you as the target. You can also set a channel, or platform for the block to be active on.
*   **$bot**: Allows channel owners and Supibot ambassadors to set various parameters for the bot, for their managed channel.
*   **$botsubs**: Posts the channels Supibot is currently subscribed to on Twitch, along with a sample sub emote to each.
*   **$BS update**: No description found.
*   **$Bun blogpost**: No description found.
*   **$chan**: Pulls a random post from a random 4Chan board, or a specified one if you provide it.
*   **$channelfounderlist**: Shows the list of founders for the specified (or current) channel. Does not "ping" the users in chat.
*   **$chatneighbour**: Finds your chat neighbour(s). When you take the chatter list in a channel and sort by the alphabet, your chat neighbours are users that come before and after you in the list. Use this to find new friends! 😃
*   **$chatsummary**: Summarizes the last couple of messages in the current (or provided) channel via GPT. This command applies a 30s cooldown to all users in the channel it is used in.
*   **$check**: Checks certain user or system variables. For a list of types, check the command's extended help.
*   **$checkem**: Similar to 4chan, posts the ID of your message as a number. Then, it checks it for dubs and higher.
*   **$Cloudflare Developer products update**: No description found.
*   **$code**: Posts a link to a specific command's code definition on GitHub.
*   **$coinflip**: Flips a coin, and shows you the result of it.
*   **$comment**: Fetches a random comment from a set of 10 thousand randomly generated YouTube videos.
*   **$commitcount**: For a given GitHub user, this command gives you the number of push events they have done in the last 24 hours. If nothing is provided, your username is used instead.
*   **$cookie**: Open a random fortune cookie wisdom. Only one allowed per day, no refunds! Subscribers to @Supinic get an extra golden cookie daily! Daily reset occurs at midnight UTC.
*   **$copypasta**: Fetches a random Twitch-related copypasta.
*   **$corona**: Checks the current number of infected/deceased people from the Coronavirus spread that started in October-December 2019.
*   **$countline**: Fetches the number of chat lines a specified user (or you, if nothing is provided) has sent in the current channel.
*   **$countlinechannel**: Fetches the number of chat lines in the current channel.
*   **$countlinetotal**: Fetches the number of data lines from ALL the log tables Supibot uses, including the total size and a prediction of when the storage will run out.
*   **$crypto**: Fetches the latest price of a cryptocurrency. If none is provided, defaults to BTC.
*   **$cryptogame**: Crypto game command! Receive the equivalent of €1000 on your "portfolio" and invest them into various currencies and assets to see how well you can increase your worth. Who shall become the best investor Supibot-land has ever known?
*   **$currency**: Attempts to convert a specified amount of one currency to another. Only supports 3-letter ISO codes. Example: 100 USD to EUR.
*   **$current**: Fetches the current song playing on stream.
*   **$dalle**: Fetches a random premade DALL-E image, either randomly or based on your search query.
*   **$dankdebug**: Debug command for public use, which means it's quite limited because of security.
*   **$dayoftheyear**: Checks what kind of international day (or month) it is today (or this month). Also accepts specific dates.
*   **$debug**: supiniHack
*   **$define**: Combines multiple ways of fetching a definition of a word or a phrase, and picks the best result.
*   **$Deno article**: No description found.
*   **$devnull**: Discards all output. Only usable in pipes.
*   **$dictionary**: Fetches the dictionary definition of a word in English. If there are multiple definitions, you can add "index:#" with a number to access specific definition indexes.
*   **$discord**: Posts the link to the current channel's Discord. Can be set up with the $set command.
*   **$doesnotexist**: Posts a random picture from the site thispersondoesnotexist.com, and its variants (check extended help for a list). These pictures are not real, they have been generated by an AI.
*   **$downloadclip**: Takes a Twitch clip name or link, and sends a download link to it into private messages.
*   **$Emojipedia blogpost**: No description found.
*   **$epal**: Fetches a random person from epal.gg - posts their description. If used on configured channels with TTS on, and if they have an audio introduction, it will be played on stream.
*   **$espn**: Shows info related to the matches played in a variety of North American sports leagues.
*   **$externalbot**: Makes Supibot execute a command of a different bot, and then the result will be that bot's command response. As such, this command can only be used in a pipe.
*   **$faceit**: Command for everything related to CS:GO within FACEIT
*   **$Factorio blogpost**: No description found.
*   **$fakenews**: Randomly creates fake news headlines from existing presets. These are not real, and are supposed to be light-hearted and just a joke. Don't take them seriously.
*   **$faq**: Posts the link to Supibot's FAQ on the supinic.com website.
*   **$fill**: Takes the input and scrambles it around randomly, filling the message. In live streams, there is less text and the cooldown is increased to reduce spam.
*   **$findraidstreams**: Iterates over eligible Twitch channels, finds online streams and posts a summary to Hastebin. Used to find a good raid after a stream is finished.
*   **$firstchannelfollower**: Fetches the first user that follows you or someone else on Twitch.
*   **$firstfollowedchannel**: Fetches the first channel you or someone else have ever followed on Twitch.
*   **$firstline**: Posts the target user's first chat line in the context of the current or a specified channel, and the date they sent it.
*   **$firstseen**: For a given user, this command tells you when they were first seen in chat - based on chat logs, so it might not be 100% accurate.
*   **$fish**: Go fishing! Supports multiple subcommands - check those out in the full command description.
*   **$followage**: Fetches the followage for a given user and a channel. If no channel is provided, checks the current one. If no user is provided either, checks yourself.
*   **$formula1**: Aggregate command about anything regarding Formula 1.
*   **$forsenCD**: A random quote from the two time! 1993, 1994 back to back blockbuster video game champion, Guy "DrDisrespect" Beahm.
*   **$forsenE**: Posts a random forsenE tweet.
*   **$funfact**: Fetches a random fun fact. Absolutely not guaranteed to be fun or fact.
*   **$gachicheck**: Checks if a given gachi link exists in the database, if not, adds it to the to-do list to be processed later.
*   **$gachisearch**: Searches for a given track in the gachi list, and attempts to post a link.
*   **$getprofilepicture**: For a given Twitch user, this command will fetch their profile picture.
*   **$gift**: This command is deprecated! Use `$cookie gift` instead.
*   **$Gitea**: No description found.
*   **$github**: Posts GitHub repository links for Supibot and the website. If you add anything afterwards, a search will be executed for your query on the bot repository.
*   **$GitHub**: No description found.
*   **$GitHub blogpost**: No description found.
*   **$GitLab**: No description found.
*   **$gpt**: Queries ChatGPT for a text response. Supports multiple models and parameter settings. Limited by tokens usage!
*   **$haHAA**: Posts a random, hilarious joke. A 100% guarantee it's going to be a knee-slapper.
*   **$help**: Posts either: a short list of all commands, or a description of a specific command if you specify it.
*   **$horoscope**: Checks a specific zodiac sign's horoscope. Can also check your horoscope, if you have set your birthday (day/month, not year) within Supibot.
*   **$howlongtobeat**: For a provided game, shows how long it takes to beat based on the https://howlongtobeat.com website's data.
*   **$id**: Checks your (or someone else's) ID in the database of users - the lower the number, the earlier the user was first spotted.
*   **$inspireme**: Inspires you. Randomly.
*   **$isdown**: Checks if a website is currently down or if it's just you.
*   **$kiss**: Kisses target user.
*   **$knowyourmeme**: Gets a brief description of a meme from Know Your Meme, just the summary.
*   **$lastline**: Posts the target user's last chat line in the context of the current channel, and the date they sent it.
*   **$lastseen**: For a given user, this command tells you when they were last seen - based on their chat activity.
*   **$link**: Verifies your account linking challenge across platforms. You should only ever use this command if you are prompted to.
*   **$liveuamap**: Fetches a recent event from the Russia-Ukraine War.
*   **$markov**: Creates a random sequence of words based on a Markov-chain module from Twitch chat.
*   **$math**: Does math. For more info, check the documentation for math.js.
*   **$me**: Turns the output into a "/me" message. E.g.: [Supibot] slaps someone around a bit with a large trout
*   **$metrics**: Shows off various metrics related to Supibot - e.g. current commands per minute.
*   **$moba**: This command lets you check many things related to several MOBA games - League of Legends ($league).
*   **$MSVC++ devblog**: No description found.
*   **$necrodancer**: Download, beatmap and assign any (supported by youtube-dl) song link into Crypt of the Necrodancer directly. Use (link) and then (zone) - for more info, check extended help.
*   **$news**: Fetches short articles. You can use a 2 uppercase letter code to get country specific news, or any other word as a search query.
*   **$Node.js version**: No description found.
*   **$nutrients**: Posts basic nutrients for a specified food query
*   **$ocr**: Takes your image link and attempts to find the text in it by using OCR.
*   **$optout**: Makes it so you cannot be the target of a command - the command will not be executed at all. For detailed usage, please check the extended help.
*   **$origin**: Fetches the origin of a given emote.
*   **$osrs**: Aggregate command for anything regarding Old School Runescape.
*   **$OSRS article**: No description found.
*   **$pastebin**: Returns the contents of a Pastebin/Hastebin paste, or from a GitHub gist; or posts your input into a new paste.
*   **$percent**: Rolls a random percentage between 0 and 100%.
*   **$pick**: Picks a single word from the provided list of words in a message.
*   **$ping**: Ping!
*   **$pingme**: Sets a self-notification in the current channel when the target user is spotted in a different channel.
*   **$pipe**: Pipes the result of one command to another, and so forth. Each command will be used as if used separately, so each will be checked for cooldowns and banphrases. Use the character "|" or ">" to separate each command.
*   **$playsound**: Plays a sound on Supinic's stream, if enabled. Use "list" as an argument to see the list of available playsounds.
*   **$poe**: A collection of various Path of Exile-related commands. Check the extended help on the website for more info.
*   **$pyramid**: Creates a pyramid in chat. Only usable in chats where Supibot is a VIP or a Moderator.
*   **$Python version**: No description found.
*   **$query**: Wolfram Alpha query for any kind of information, or computation.
*   **$randomalbum**: Posts a random music album.
*   **$randomanimalfact**: Posts a random fact about a selected animal type.
*   **$randomanimalpicture**: Posts a random picture for a given animal type.
*   **$randomclip**: Posts a random clip from either the current channel or the specified channel.
*   **$randomcocktail**: Searches for a cocktail recipe by its name, or fetches a random one, if no search query was provided.
*   **$randomcommandalias**: Posts a random Supibot command alias. Can be configured to create a somewhat precise search query.
*   **$randomdonger**: Raise your dongers.
*   **$randomemoji**: Fetches a random emoji. If a number is provided, rolls that many emojis.
*   **$randomemote**: Fetches a random emote from the scope of the current channel. Configurable with parameters.
*   **$randomfilm**: Fetches a random movie.
*   **$randomgachi**: Fetches a random gachi track from the gachi list, excluding Bilibili and Nicovideo videos with no YouTube reuploads.
*   **$randomhistoricevent**: For a given day, posts a random historic event that happened on that day. If not provided, uses today's date.
*   **$randominstagram**: Fetches a random Instagram user's post, from their most recently posted ones.
*   **$randomline**: Fetches a random line from the current channel. If a user is specified, fetches a random line from that user only. "rq" only chooses from your own lines.
*   **$randommeal**: Searches for a meal recipe by its name, or fetches a random one, if no search query was provided.
*   **$randommeme**: If no parameters are provided, posts a random Reddit meme. If you provide a subreddit, a post will be chosen randomly.
*   **$randompastebin**: Fetches a random recently posted Pastebin paste.
*   **$randomsadcat**: Posts a random sad cat image SadCat
*   **$randomscp**: Fetches a description of a random SCP from the SCP Foundation Wiki.
*   **$randomword**: Fetches a random word. If a number is provided, rolls that many words.
*   **$record**: Checks for various max/min records of various sources.
*   **$reload**: Reloads a database definition or hotloads an updated script
*   **$remind**: Sets a notification for a given user. Can also set a time to ping that user (or yourself) in a given amount of time, but in that case you must use the word "in" and then a number specifying the amount days, hours, minutes, etc.
*   **$restart**: Restarts the bot. Optionally, also pulls git changes and/or upgrades packages via yarn.
*   **$resumeafk**: Resumes your AFK status, if used shortly after coming back from an AFK. The time period is global, not just in the channel you came back from AFK in.
*   **$roll**: Rolls a random number. If nothing is specified, rolls 1-100. You can specify min and max values, or some expression using standard dice notation.
*   **$Runelite version**: No description found.
*   **$russianarmylosses**: Fetches the latest losses of the Russian Army in Ukraine, as provided by the General Staff of Ukraine.
*   **$russianroulette**: Play the roulette. If you win, nothing happens; if you lose, you get timed out. You can add a number 1-600 (default: 1) which says how long you will be timed out, should you lose. You can use the command anywhere, but you can only get timed out in a channel where Supibot is a moderator.
*   **$Rust article**: No description found.
*   **$schedule**: Posts the channel's stream schedule.
*   **$set**: Sets/unsets certain variables within Supibot. Check the extended help for full info.
*   **$shoutout**: Shouts out a given streamer (Twitch only), and posts the last game they played as well.
*   **$shuffle**: Shuffles the provided message, word by word.
*   **$simplesql**: Executes a quick SQL query, and returns its (simple) result.
*   **$slots**: Once at least three unique emotes (or words) have been provided, rolls a pseudo slot machine to see if you get a flush.
*   **$songrequest**: Requests a song to play on Supinic's stream. You can use "start:" and "end:" to request parts of a song using seconds or a time syntax. "start:100" or "end:05:30", for example.
*   **$songrequestqueue**: Posts the summary of the song request queue.
*   **$sort**: Alphabetically sorts the message provided to this command.
*   **$speedrun**: Fetches the current world record speedrun of a given name in the default category. Check extended help for more info.
*   **$stalk**: For a given user, attempts to find the message they last sent in chat, plus the channel and time when they posted it.
*   **$statistics**: Posts various statistics regarding you or other users, e.g. total AFK time.
*   **$Steam giveaway**: No description found.
*   **$steamgameplayers**: Searches for a Steam game, and attempts to find its current player amount.
*   **$stock**: Fetches the latest price and daily change for a stock.
*   **$stream**: Multiple configurations regarding the stream. Mostly used for #supinic, and nobody else.
*   **$streaminfo**: Posts information about a Twitch channel's stream, or the current channel if none is provided.
*   **$subage**: Fetches the subscription data for a given user on a given channel on Twitch.
*   **$subscribe**: Subscribe or unsubscribe to a plethora of events, such as a channel going live, or a suggestion you made being updated. Check the extended help for detailed info on each event.
*   **$suggest**: Suggest something for Supinic. When you post your first suggestion, you will automatically receive reminders when your suggestions get updated. Posts links to a suggestion list if you don't provide any text. To remove, check the $unset command.
*   **$test**: Test.
*   **$texttospeech**: Plays TTS on Supinic's stream, if enabled. You can specify the language by using "language:<language>" anywhere in your message.
*   **$texttransform**: Transforms provided text into one of the provided types, such as "vaporwave", for example.
*   **$tf2**: Aggregate command for everything related to Team Fortress 2.
*   **$thesaurus**: Attempts to re-creates your sentence using random synonyms for each word.
*   **$time**: Fetches the current time and timezone for a given location, or a user, if they have set their location.
*   **$top**: Posts the top X (implicitly 10) users by chat lines sent in the context of the current channel.
*   **$topgames**: Fetches the top 10 most popular games on Twitch, based on current viewer count.
*   **$topstreams**: Checks the top 10 streams on Twitch - if you add a game, will look for the top 10 streams playing that game. The game must be provided verbatim.
*   **$totalcountline**: Fetches the total amount of a user's (or yours, if nobody was specified) chat lines in all tracked channels summed together.
*   **$trackreupload**: Sets a track ID in the list already to have the next track as a reupload. The next track can be an existing ID (if it's not a reupload already) or a new link, in which case it gets added to the list.
*   **$translate**: Implicitly translates from auto-recognized language to English. Supports parameters 'from' and 'to'. Example: from:german to:french Guten Tag"
*   **$transliterate**: Transliterates non-Latin text into Latin. Should support most of the languages not using Latin (like Japanese, Chinese, Russian, ...)
*   **$tuck**: Tucks target user to bed.
*   **$twitchlotto**: Fetches a random Imgur image from a Twitch channel (based off Twitchlotto) and checks it for NSFW stuff via an AI. The "NSFW score" is posted along with the link.
*   **$twitchlottoexplain**: For a given processed TwitchLotto link from $tl, creates a version where the detections are marked with boxes.
*   **$twitter**: Fetches the last tweet from a given user. No retweets or replies, just plain standalone tweets.
*   **$Typescript devblog**: No description found.
*   **$unmention**: Makes a specific command (or, in advanced mode, a combination of command/channel/platform, or global) not mention you by removing the "username," part at the beginning.
*   **$unping**: Sets/unsets a command pinging you when it's being invoked.
*   **$urban**: Fetches the top definition of a given term from Urban Dictionary. You can append "index:#" at the end to access definitions that aren't first in the search.
*   **$V8 version**: No description found.
*   **$vanish**: Twitch only: times the user out for 1 second. Only works if Supibot is a Twitch moderator.
*   **$weather**: Fetches the current weather in a given location. You can specify parameters to check the forecast, or mention a user to get their location, if they set it up. Check all possibilities in extended help.
*   **$whatanimeisit**: What anime is it? For a given screenshot of an anime show, this command will attempt to recognize the show's name, episode and timestamp.
*   **$whatemoteisit**: What emote is it? Posts specifics about a given Twitch subscriber emote.
*   **$when**: Tells you when your command is going to be played next, approximately.
*   **$whisper**: Instead of replying in the given channel, this command will make the bot whisper you the response. Only usable in pipes.
*   **$wiki**: Fetches the headline of the first article found according to the user query. Watch out, articles might be case-sensitive.
*   **$wrongsong**: If you have at least one song playing or in the queue, this command will skip the first one. You can also add an ID to skip a specific song.
*   **$youtubesearch**: Searches YouTube for video(s) with your query. Only a certain number of uses are available daily.

---

## 3. Módulos de Chat (Chat Modules)

Estes módulos funcionam em segundo plano, reagindo a eventos do chat sem a necessidade de um comando direto:

*   **async-markov-experiment**: Super experimental automatic async markov tester thing
*   **automatic-unscramble**: Attempts to auto-unscramble thepositivebot's unscramble minigame.
*   **chat-suggestion-linker**: If a Supibot suggestion ID format is detected, posts a link to it - plus a github link, if the suggestion has one.
*   **imgur-link-gatherer**: Gathers Imgur links across channels, and reuploads them if possible.
*   **live-detection**: Sends out PMs to all users subbed to the live event, whenever a channel set up there goes live.
*   **message-react**: According to arguments, reacts to a specific message(s) with a determined response.
*   **offline-only-mirror**: This module manages channel mirrors so that they are only in effect when the channel is offline.
*   **offline-only-mode**: Makes Supibot go into Read-only mode when the channel is online. Reverts back when the channel goes offline.
*   **ping-supi**: This module notifies Supinic whenever he is mentioned (in any channel, across platforms) via Twitch whispers.
*   **pyramid-detection**: Detects \"pyramids\" in chat. Congratulates the persons who finishes one and demeans the persons who break one.
*   **raid-react**: According to arguments, reacts to a Twitch channel being raided.
*   **stream-points-redemptions**: Reacts to redemptions
*   **streamer-health-notification**: Sets up a periodic \"health notification\" when the channel goes live, and removes it when going offline.
*   **subscription-react**: According to arguments, reacts to a subscription in a Twitch channel.
*   **supinic-silence-prevention-trigger**: Toggles the silence-prevention cron on/off on Supinic's stream going on/off.
*   **supinic-stream-db**: Creates and updates database rows of Streams on Supinic's channel as he goes on/offline.
*   **suspicious-user-auto-check**: For each user who types (a part of) the \"suspicious user\" message, this module will automatically try the $suscheck alias.
*   **twitch-bot-scope-reminder**: Notifies users that used to have Supibot but didn't permit it within the crossover window.
*   **wanna-become-famous**: Bans various spam or follow bots.

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
*   `searchYoutube`
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
