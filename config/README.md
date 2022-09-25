## Konfigurasi Bot Musik Yukki

Config vars pada dasarnya adalah variabel yang mengonfigurasi atau memodifikasi bot agar berfungsi, yang merupakan kebutuhan dasar plugin atau kode agar berfungsi. Anda harus mengatur vars wajib yang tepat untuk membuatnya berfungsi dan untuk memulai fitur dasar bot.

### Kenali semua vars ini secara mendalam dari Dokumen kami. [Baca Sekarang dari Sini](https://notreallyshikhar.gitbook.io/yukkimusicbot/config-vars/available-vars)

## Vars Wajib

- Ini adalah vars minimum yang diperlukan untuk membuat Yukki Music Bot berfungsi.
1. `API_ID` : Dapatkan dari my.telegram.org
2. `API_HASH` : Dapatkan dari my.telegram.org
3. `BOT_TOKEN` : Dapatkan dari [@Botfather](http://t.me/BotFather) di Telegram
4. `MONGO_DB_URI` : Dapatkan mongo db [dari sini.](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb)
5. `LOG_GROUP_ID` : Anda memerlukan ID Grup Pribadi untuk ini. Supergroup Dibutuhkan dengan id mulai dari -100
6. `MUSIC_BOT_NAME` : Nama untuk bot Musik Anda.
7. `OWNER_ID` : ID Pemilik Anda untuk mengelola bot Anda.
8. `STRING_SESSION` : Diperlukan Sesi Pyrogram, Hasilkan string dari [@YukkiStringBot](http://t.me/YukkiStringBot) di Telegram.

## Vars Tidak Wajib

- Ini adalah vars tambahan untuk fitur tambahan di dalam Bot Musik. Anda dapat meninggalkan vars yang tidak wajib untuk saat ini dan dapat menambahkannya nanti.
1. `DURATION_LIMIT` : Durasi audio (musik) maksimum khusus untuk obrolan suara. Default untuk 60 menit.
2. `SONG_DOWNLOAD_DURATION_LIMIT` : Batas Durasi untuk mengunduh Lagu dalam format MP3 atau MP4 dari bot. Default ke 180 menit.
3. `VIDEO_STREAM_LIMIT` : Jumlah maksimum panggilan video yang diizinkan di bot. Nanti bisa diatur lewat /set_video_limit di telegram. Default untuk 3 obrolan.
4. `SERVER_PLAYLIST_LIMIT` : Batas Maksimum Diizinkan bagi pengguna untuk menyimpan daftar putar di server bot. Standar ke 30
5. `PLAYLIST_FETCH_LIMIT` : Batas maksimum pengambilan track playlist dari link youtube, spotify, apple. Default ke 25
6. `CLEANMODE_MINS` : Waktu Cleanmode setelah bot akan menghapus pesan lama dari obrolan. Default ke 5 Menit.
7. `SUPPORT_CHANNEL` : Jika Anda memiliki saluran untuk bot musik Anda, isi dengan tautan saluran Anda
8. `SUPPORT_GROUP` : Jika Anda memiliki dukungan grup untuk bot musik Anda, isi dengan tautan grup Anda.


## Play FileSize Limit Vars
## Play FileSize Limit Vars


## Spotify Vars

- You can play tracks or playlists from spotify from Yukki Music bot
- You'll need these two vars to make spotify play working. This is not essential , you can leave them blank if you want.

### How to get these? [Read from here](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/spotify)


1. `SPOTIFY_CLIENT_ID` : Get it from https://developer.spotify.com/dashboard 
2. `SPOTIFY_CLIENT_SECRET` : Get it from https://developer.spotify.com/dashboard 


## Heroku Vars

- To work some Heroku compatible modules, this var value required to Access your account to use `get_log`, `usage`, `update` etc etc commands.
- You can fill this var using your API key or Authorization token.

### How to get these? [Read from here](https://notreallyshikhar.gitbook.io/yukkimusicbot/config-vars/heroku-vars)

1. `HEROKU_API_KEY` : Get it from http://dashboard.heroku.com/account 
2. `HEROKU_APP_NAME` : You have to Enter the app name which you gave to identify your Music Bot in Heroku. 


## Custom Repo Vars

- If you plan to use Yukki Music Bot with your own customized or modified code.

1. `UPSTREAM_REPO` : Your Upstream Repo URL or Forked Repo.
2. `UPSTREAM_BRANCH` : Default Branch of your Upstream Repo URL or Forked Repo. 
3. `GIT_TOKEN` : Your GIT TOKEN if your upstream repo is private
4. `GITHUB_REPO` : Your Github Repo url, that will be shown on /start command



## Images/Thumbnail Vars

- You can change images which are used in Yukki Music Bot.
- You can generate telegaph links from [@YukkiTelegraphBot](http://t.me/YukkiTelegraphBot) and use it here.

1. `START_IMG_URL` : Image which comes on /start command in private messages of bot.
2. `PING_IMG_URL` : Image which comes on /ping command of bot.
3. `PLAYLIST_IMG_URL` : Image which comes on /play command of bot. 
4. `GLOBAL_IMG_URL` : Image which comes on /stats command of bot. 
5. `STATS_IMG_URL` : Image which comes on /stats command of bot. 
6. `TELEGRAM_AUDIO_URL` : This image comes when someone plays audios from telegram. 
7. `TELEGRAM_VIDEO_URL` : This image comes when someone plays videos from telegram. 
8. `STREAM_IMG_URL` : his image comes when someone plays m3u8 or index links.
9. `SOUNCLOUD_IMG_URL` : This image comes when someone plays music from soundcloud. 
10. `YOUTUBE_IMG_URL` : This image comes if thumbnail generator fails to gen thumb anyhow.
11. `SPOTIFY_ARTIST_IMG_URL` : This image comes when someone plays Spotify artist via link in inline mode. 
12. `SPOTIFY_ALBUM_IMG_URL` : This image comes when someone plays Spotify album via link in inline mode. 
13. `SPOTIFY_PLAYLIST_IMG_URL` : This image comes when someone plays Spotify album via link in inline mode. 

## Multi Assistant Mode

- You can use upto 5 Assistant Clients ( allowing your bot to atleast work in 2000-2500 chats at a time )

1. `STRING_SESSION2` : Pyrogram Session Needed, Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram.
2. `STRING_SESSION3` : Pyrogram Session Needed, Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram.
3. `STRING_SESSION4` : Pyrogram Session Needed, Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram.
4. `STRING_SESSION5` : Pyrogram Session Needed, Generate string from [@YukkiStringBot](http://t.me/YukkiStringBot) in Telegram.
