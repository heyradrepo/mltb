from ..telegram_helper.bot_commands import BotCommands
from ...core.mltb_client import TgClient

mirror = """<b>Kirim link bersama dengan perintah</b>:

/cmd link

<b>Dengan reply ke link/file</b>:

/cmd -n nama baru -e -up tujuan upload

<b>CATATAN:</b>
1. Perintah yang diawali dengan <b>qb</b> HANYA untuk torrent."""

yt = """<b>Kirim link bersama dengan perintah</b>:

/cmd link

<b>Dengan reply ke link</b>:
/cmd -n nama baru -z password -opt x:y|x1:y1

Cek semua situs yang didukung di sini <a href='https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md'>SITES</a>
Cek semua opsi yt-dlp api dari <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L212'>FILE</a> 
atau gunakan <a href='https://t.me/mltb_official_channel/177'>script</a> ini untuk mengubah argumen CLI ke opsi API."""

clone = """Kirim link Gdrive|Gdot|Filepress|Filebee|Appdrive|Gdflix atau path rclone bersama dengan perintah, 
atau dengan reply ke link/rc_path menggunakan perintah.

Gunakan -sync untuk memakai metode sync di rclone. 
Contoh: /cmd rcl/rclone_path -up rcl/rclone_path/rc -sync"""

new_name = """<b>Nama Baru</b>: -n

/cmd link -n nama_baru
Catatan: Tidak berfungsi dengan torrent"""

multi_link = """<b>Multi link hanya dengan reply ke link/file pertama</b>: -i

/cmd -i 10(jumlah link/file)"""

same_dir = """<b>Pindahkan file/folder ke folder baru</b>: -m

Argumen ini juga bisa dipakai untuk memindahkan isi dari beberapa link/torrent ke direktori yang sama, 
jadi semua link akan diupload bersama sebagai satu task.

/cmd link -m folder_baru (hanya satu link di dalam folder baru)
/cmd -i 10(jumlah link/file) -m nama_folder (semua isi link dalam satu folder)
/cmd -b -m nama_folder (reply ke batch pesan/file (setiap link di baris baru))

Saat menggunakan bulk, kamu juga bisa pakai argumen ini dengan nama folder berbeda 
bersamaan dengan link di pesan atau batch file.
Contoh:
link1 -m folder1
link2 -m folder1
link3 -m folder2
link4 -m folder2
link5 -m folder3
link6

Maka:
- link1 dan link2 akan diupload ke folder1
- link3 dan link4 akan diupload ke folder2
- link5 akan diupload sendiri ke folder3
- link6 akan diupload normal sendiri
"""

thumb = """<b>Thumbnail untuk task saat ini</b>: -t

/cmd link -t tg-message-link (dokumen atau foto) atau none (file tanpa thumbnail)"""

split_size = """<b>Ukuran split untuk task saat ini</b>: -sp

/cmd link -sp (500mb atau 2gb atau 4000000000)
Catatan: Hanya mb dan gb yang didukung atau tulis dalam byte tanpa satuan!"""

upload = """<b>Tujuan Upload</b>: -up

/cmd link -up rcl/gdl 
(rcl: untuk memilih config rclone, remote & path | gdl: untuk memilih token.pickle, id gdrive) dengan tombol.
Kamu bisa langsung menambahkan path upload: 
-up remote:dir/subdir atau -up Gdrive_id atau -up id/username (telegram) atau -up id/username|topic_id (telegram)

Jika DEFAULT_UPLOAD adalah `rc` maka bisa tambahkan up: `gd` untuk upload menggunakan gdrive tools ke GDRIVE_ID.  
Jika DEFAULT_UPLOAD adalah `gd` maka bisa tambahkan up: `rc` untuk upload ke RCLONE_PATH.

Kalau mau menambahkan path atau gdrive manual dari config/token (UPLOAD DARI USETTING) gunakan `mrcc:` untuk rclone dan `mtp:` sebelum path/gdrive_id tanpa spasi.  
Contoh:  
/cmd link -up mrcc:main:dump  
/cmd link -up mtp:gdrive_id  
<strong>atau cukup edit upload menggunakan owner/user token/config dari usetting tanpa perlu menambahkan mtp: atau mrcc: di depan path/id</strong>

Untuk menambahkan tujuan leech:  
-up id/@username/pm  
-up b:id/@username/pm (b: berarti leech oleh bot) (id atau username chat, atau tulis pm berarti private message sehingga bot mengirim file ke private)  
Kapan gunakan b: (leech by bot)? Saat default setting kamu leech by user tapi ingin leech by bot di task tertentu.  

-up u:id/@username (u: berarti leech oleh user) — berlaku jika OWNER menambahkan USER_STRING_SESSION.  
-up h:id/@username (hybrid leech) — h: upload file oleh bot dan user berdasarkan ukuran file.  
-up id/@username|topic_id (leech di chat & topik tertentu) tambahkan | tanpa spasi dan tuliskan topic id setelah chat id/username.

Kalau mau tentukan penggunaan token.pickle atau service accounts:  
- tp:gdrive_id (pakai token.pickle)  
- sa:gdrive_id (pakai service accounts)  
- mtp:gdrive_id (pakai token.pickle dari usetting)  

DEFAULT_UPLOAD tidak berpengaruh pada perintah leech.
"""

user_download = """<b>User Download</b>: link

/cmd tp:link untuk download menggunakan owner token.pickle jika service account aktif.
/cmd sa:link untuk download menggunakan service account jika service account nonaktif.
/cmd tp:gdrive_id untuk download menggunakan token.pickle dan file_id jika service account aktif.
/cmd sa:gdrive_id untuk download menggunakan service account dan file_id jika service account nonaktif.
/cmd mtp:gdrive_id atau mtp:link untuk download menggunakan user token.pickle dari usetting.
/cmd mrcc:remote:path untuk download menggunakan user rclone config dari usetting.
Kamu juga bisa langsung edit upload menggunakan owner/user token/config dari usetting tanpa menambahkan mtp: atau mrcc: di depan path/id."""

rcf = """<b>Rclone Flags</b>: -rcf

/cmd link|path|rcl -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
Argumen ini akan menimpa semua flag lain kecuali --exclude.
Cek semua flag di sini <a href='https://rclone.org/flags/'>RcloneFlags</a>."""

bulk = """<b>Bulk Download</b>: -b

Bulk hanya bisa dipakai dengan reply ke pesan teks atau file teks yang berisi daftar link (dipisah baris baru).
Contoh:
link1 -n nama_baru -up remote1:path1 -rcf |key:value|key:value
link2 -z -n nama_baru -up remote2:path2
link3 -e -n nama_baru -up remote2:path2

Reply contoh di atas dengan perintah -> /cmd -b (bulk)

Catatan: Semua argumen yang ditambahkan bersama cmd akan diterapkan ke semua link.
/cmd -b -up remote: -z -m nama_folder 
(semua isi link akan di-zip dalam satu folder lalu diupload ke satu tujuan)

Jadi kamu tidak bisa set tujuan upload berbeda bersamaan dengan link jika sudah menambahkan -m pada cmd.

Kamu bisa tentukan start dan end dari link di bulk seperti seed, dengan:  
- -b start:end  
- -b :end (hanya end)  
- -b start (hanya start)  

Default start adalah dari nol (link pertama) sampai tak terbatas."""

rlone_dl = """<b>Rclone Download</b>:

Perlakukan path rclone sama seperti link
/cmd main:dump/ubuntu.iso atau rcl (untuk memilih config, remote dan path)
User bisa menambahkan rclone sendiri dari user settings.
Kalau mau menambahkan path manual dari config, tambahkan mrcc: di depan path tanpa spasi.
/cmd mrcc:main:dump/ubuntu.iso
Kamu juga bisa langsung edit pakai config owner/user dari usetting tanpa menambahkan mrcc: di depan path."""

extract_zip = """<b>Extract/Zip</b>: -e -z

/cmd link -e password (ekstrak file dengan password)
/cmd link -z password (zip file dengan password)
/cmd link -z password -e (ekstrak lalu zip dengan password)
Catatan: Jika keduanya (extract dan zip) ditambahkan dalam satu cmd, proses ekstrak dilakukan lebih dulu lalu di-zip. Jadi selalu ekstrak lebih dulu."""

join = """<b>Gabung File Terpisah</b>: -j

Opsi ini hanya bekerja sebelum extract dan zip, jadi umumnya dipakai bersama argumen -m (samedir).
Dengan Reply:
/cmd -i 3 -j -m nama_folder
/cmd -b -j -m nama_folder

Jika kamu punya link (folder) berisi file terpisah:
/cmd link -j"""

tg_links = """<b>Link Telegram (TG Links)</b>:

Perlakukan link Telegram sama seperti direct link.
Beberapa link butuh akses user, jadi kamu harus menambahkan USER_SESSION_STRING untuk menggunakannya.

Tiga tipe link:
Publik: https://t.me/channel_name/message_id
Private: tg://openmessage?user_id=xxxxxx&message_id=xxxxx
Super: https://t.me/c/channel_id/message_id
Range: https://t.me/channel_name/first_message_id-last_message_id

Contoh Range: 
tg://openmessage?user_id=xxxxxx&message_id=555-560  
atau  
https://t.me/channel_name/100-150  

Catatan: Link Range hanya bisa dipakai dengan reply cmd ke link tersebut."""

sample_video = """<b>Sample Video</b>: -sv

Buat video sampel dari satu video atau folder berisi video.
/cmd -sv (akan memakai nilai default: durasi sampel 60 detik dan durasi per bagian 4 detik).
Kamu bisa atur nilainya. Contoh:
/cmd -sv 70:5 (sample-duration:part-duration)
/cmd -sv :5
/cmd -sv 70"""

screenshot = """<b>Screenshot</b>: -ss

Buat screenshot dari satu video atau folder berisi video.
/cmd -ss (akan memakai nilai default: 10 foto).
Kamu bisa ubah nilainya. Contoh:
/cmd -ss 6"""

seed = """<b>Bittorrent Seed</b>: -d

/cmd link -d ratio:seed_time atau dengan reply ke file/link.
Untuk menentukan ratio dan waktu seeding tambahkan -d ratio:time.
Contoh:
-d 0.7:10 (ratio dan waktu)
/cmd link -d 0.7 (hanya ratio)
/cmd link -d :10 (hanya waktu, dalam menit)"""

zip_arg = """<b>Zip</b>: -z password

/cmd link -z (zip)
/cmd link -z password (zip dengan password)"""

qual = """<b>Tombol Kualitas</b>: -s

Jika default quality ditentukan dari opsi yt-dlp menggunakan format option, 
dan kamu ingin memilih kualitas untuk link tertentu atau untuk link dengan fitur multi-link.
/cmd link -s"""

yt_opt = """<b>Opsi</b>: -opt

/cmd link -opt {"format": "bv*+mergeall[vcodec=none]", "nocheckcertificate": True, "playliststart": 10, "fragment_retries": float("inf"), "matchtitle": "S13", "writesubtitles": True, "live_from_start": True, "postprocessor_args": {"ffmpeg": ["-threads", "4"]}, "wait_for_video": (5, 100), "download_ranges": [{"start_time": 0, "end_time": 10}]}

Cek semua opsi yt-dlp API di <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>FILE</a> 
atau gunakan <a href='https://t.me/mltb_official_channel/177'>script ini</a> untuk mengubah argumen CLI ke opsi API."""

convert_media = """<b>Konversi Media</b>: -ca -cv

/cmd link -ca mp3 -cv mp4 (konversi semua audio ke mp3 dan semua video ke mp4)
/cmd link -ca mp3 (konversi semua audio ke mp3)
/cmd link -cv mp4 (konversi semua video ke mp4)
/cmd link -ca mp3 + flac ogg (hanya konversi audio flac dan ogg ke mp3)
/cmd link -cv mkv - webm flv (konversi semua video ke mp4 kecuali webm dan flv)"""

force_start = """<b>Force Start</b>: -f -fd -fu
/cmd link -f (paksa download dan upload)
/cmd link -fd (paksa download saja)
/cmd link -fu (paksa upload langsung setelah download selesai)"""

gdrive = """<b>Gdrive</b>: link
Jika DEFAULT_UPLOAD adalah `rc`, maka bisa pakai up: `gd` untuk upload menggunakan gdrive tools ke GDRIVE_ID.
/cmd gdriveLink atau gdl atau gdriveId -up gdl atau gdriveId atau gd
/cmd tp:gdriveLink atau tp:gdriveId -up tp:gdriveId atau gdl atau gd (pakai token.pickle jika service account aktif)
/cmd sa:gdriveLink atau sa:gdriveId -p sa:gdriveId atau gdl atau gd (pakai service account jika service account nonaktif)
/cmd mtp:gdriveLink atau mtp:gdriveId -up mtp:gdriveId atau gdl atau gd (jika sudah menambahkan upload gdriveId dari usetting) (pakai user token.pickle dari usetting)
Kamu juga bisa langsung edit pakai owner/user token dari usetting tanpa menambahkan mtp: di depan id"""

rclone_cl = """<b>Rclone</b>: path
Jika DEFAULT_UPLOAD adalah `gd`, maka bisa pakai up: `rc` untuk upload ke RCLONE_PATH.
/cmd rcl/rclone_path -up rcl/rclone_path/rc -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue
/cmd rcl atau rclone_path -up rclone_path atau rc atau rcl
/cmd mrcc:rclone_path -up rcl atau rc (jika sudah menambahkan rclone path dari usetting) (pakai user config)
Kamu juga bisa langsung edit pakai owner/user config dari usetting tanpa menambahkan mrcc: di depan path"""

name_sub = r"""<b>Penggantian Nama (Name Substitution)</b>: -ns
/cmd link -ns script/code/s | mirror/leech | tea/ /s | clone | cpu/ | \[mltb\]/mltb | \\text\\/text/s
Ini akan berpengaruh ke semua file. Format: kataDiganti/kataPengganti/sensitiveCase
Penggantian kata bisa juga dengan pola (pattern) bukan teks biasa. Timeout: 60 detik
CATATAN: Kamu harus menambahkan \ sebelum karakter spesial berikut: \^$.|?*+()[]{}
1. script akan diganti dengan code (case sensitive)
2. mirror akan diganti dengan leech
3. tea akan diganti dengan spasi (case sensitive)
4. clone akan dihapus
5. cpu akan diganti dengan spasi
6. [mltb] akan diganti dengan mltb
7. \text\ akan diganti dengan text (case sensitive)
"""

transmission = """<b>Tg Transmission</b>: -hl -ut -bt
/cmd link -hl (leech oleh user dan bot session sesuai ukuran) (Hybrid Leech)
/cmd link -bt (leech dengan bot session)
/cmd link -ut (leech dengan user)"""

thumbnail_layout = """<b>Thumbnail Layout</b>: -tl
/cmd link -tl 3x3 (widthxheight) → 3 foto per baris dan 3 foto per kolom"""

leech_as = """<b>Leech sebagai</b>: -doc -med
/cmd link -doc (Leech sebagai dokumen)
/cmd link -med (Leech sebagai media)"""

ffmpeg_cmds = """<b>Perintah FFmpeg</b>: -ff
List berisi kumpulan perintah ffmpeg. Kamu bisa set banyak perintah ffmpeg untuk semua file sebelum upload. Jangan tulis ffmpeg di awal, langsung mulai dengan argumennya.
Catatan:
1. Tambahkan <code>-del</code> pada list yang ingin kamu hapus file aslinya setelah perintah selesai dijalankan!
2. Untuk menjalankan salah satu list yang sudah ditambahkan di bot, misalnya: ({"subtitle": ["-i mltb.mkv -c copy -c:s srt mltb.mkv"]}), gunakan -ff subtitle (key list).

Contoh:
["-i mltb.mkv -c copy -c:s srt mltb.mkv",
 "-i mltb.video -c copy -c:s srt mltb",
 "-i mltb.m4a -c:a libmp3lame -q:a 2 mltb.mp3",
 "-i mltb.audio -c:a libmp3lame -q:a 2 mltb.mp3",
 "-i mltb -map 0:a -c copy mltb.mka -map 0:s -c copy mltb.srt",
 "-i mltb -i tg://openmessage?user_id=5272663208&message_id=322801 -filter_complex 'overlay=W-w-10:H-h-10' -c:a copy mltb"]

Penjelasan penggunaan mltb.* (referensi file yang diproses):
1. Cmd pertama: input mltb.mkv → hanya jalan untuk video mkv, output juga mltb.mkv, jadi semua output tetap mkv. Tambahkan -del untuk hapus file asli setelah selesai.
2. Cmd kedua: input mltb.video → jalan untuk semua video, output hanya mltb → ekstensi ikut input aslinya.
3. Cmd ketiga: input mltb.m4a → hanya untuk audio m4a, output mltb.mp3 → hasilnya mp3.
4. Cmd keempat: input mltb.audio → untuk semua audio, output mltb.mp3 → hasil mp3.
5. Cmd kelima: kamu bisa pakai link Telegram untuk input kecil seperti foto agar bisa ditambahkan watermark.
"""

YT_HELP_DICT = {
    "main": yt,
    "New-Name": f"{new_name}\nCatatan: Jangan tambahkan ekstensi file",
    "Zip": zip_arg,
    "Quality": qual,
    "Options": yt_opt,
    "Multi-Link": multi_link,
    "Same-Directory": same_dir,
    "Thumb": thumb,
    "Split-Size": split_size,
    "Upload-Destination": upload,
    "Rclone-Flags": rcf,
    "Bulk": bulk,
    "Sample-Video": sample_video,
    "Screenshot": screenshot,
    "Convert-Media": convert_media,
    "Force-Start": force_start,
    "Name-Substitute": name_sub,
    "TG-Transmission": transmission,
    "Thumb-Layout": thumbnail_layout,
    "Leech-Type": leech_as,
    "FFmpeg-Cmds": ffmpeg_cmds,
}

MIRROR_HELP_DICT = {
    "main": mirror,
    "New-Name": new_name,
    "DL-Auth": "<b>Otorisasi direct link</b>: -au -ap\n\n/cmd link -au username -ap password",
    "Headers": "<b>Header custom direct link</b>: -h\n\n/cmd link -h key:value|key1:value1",
    "Extract/Zip": extract_zip,
    "Select-Files": "<b>Pemilihan file Bittorrent/JDownloader/Sabnzbd</b>: -s\n\n/cmd link -s atau dengan reply ke file/link",
    "Torrent-Seed": seed,
    "Multi-Link": multi_link,
    "Same-Directory": same_dir,
    "Thumb": thumb,
    "Split-Size": split_size,
    "Upload-Destination": upload,
    "Rclone-Flags": rcf,
    "Bulk": bulk,
    "Join": join,
    "Rclone-DL": rlone_dl,
    "Tg-Links": tg_links,
    "Sample-Video": sample_video,
    "Screenshot": screenshot,
    "Convert-Media": convert_media,
    "Force-Start": force_start,
    "User-Download": user_download,
    "Name-Substitute": name_sub,
    "TG-Transmission": transmission,
    "Thumb-Layout": thumbnail_layout,
    "Leech-Type": leech_as,
    "FFmpeg-Cmds": ffmpeg_cmds,
}

CLONE_HELP_DICT = {
    "main": clone,
    "Multi-Link": multi_link,
    "Bulk": bulk,
    "Gdrive": gdrive,
    "Rclone": rclone_cl,
}

RSS_HELP_MESSAGE = """
Gunakan format ini untuk menambahkan feed url:
Judul1 link (wajib)
Judul2 link -c cmd -inf xx -exf xx
Judul3 link -c cmd -d ratio:time -z password

-c command -up mrcc:remote:path/subdir -rcf --buffer-size:8M|key|key:value
-inf Filter untuk kata yang harus ada.
-exf Filter untuk kata yang harus tidak ada.
-stv true atau false (filter sensitif)

Contoh:
Judul https://www.rss-url.com -inf 1080 or 720 or 144p|mkv or mp4|hevc -exf flv or web|xxx
Filter ini akan memproses link yang judulnya berisi (1080 atau 720 atau 144p) dan (mkv atau mp4) dan hevc
serta tidak mengandung (flv atau web) dan kata xxx.

Contoh lain:
-inf  1080  or 720p|.web. or .webrip.|hvec or x264
Ini akan memproses judul yang mengandung (1080 atau 720p) dan (.web. atau .webrip.) dan (hvec atau x264).
Tambahkan spasi sebelum dan sesudah 1080 untuk menghindari salah pencocokan.
Kalau di judul ada angka 10805695, itu bisa cocok ke 1080 jika tidak menambahkan spasi.

Catatan Filter:
1. | berarti dan
2. Gunakan or di antara kunci yang mirip (kualitas/ekstensi). 
   Jangan buat seperti: 1080|mp4 or 720|web
   Karena itu akan diproses sebagai 1080 dan (mp4 atau 720) dan web,
   bukan (1080 dan mp4) atau (720 dan web).
3. Kamu bisa menambahkan or dan | sebanyak yang kamu mau.
4. Perhatikan judul. Jika ada karakter khusus (titik, strip, dll.)
   sebelum/ sesudah kualitas atau ekstensi, tambahkan juga di filter.

Batas waktu: 60 detik.
"""

PASSWORD_ERROR_MESSAGE = """
<b>Link ini membutuhkan password!</b>
- Tambahkan <b>::</b> setelah link lalu tuliskan password setelah tanda tersebut.

<b>Contoh:</b> link::passwordku
"""

user_settings_text = {
"LEECH_SPLIT_SIZE": f"Kirim ukuran split Leech dalam bytes atau gunakan gb/mb. Contoh: 40000000 atau 2.5gb atau 1000mb. IS_PREMIUM_USER: {TgClient.IS_PREMIUM_USER}. Batas waktu: 60 detik",
"LEECH_DUMP_CHAT": """"Kirim ID/USERNAME/PM tujuan leech. 
* b:id/@username/pm (b: artinya leech oleh bot) (id atau username chat atau tulis pm artinya pesan pribadi sehingga bot akan mengirim file ke private chat denganmu). Kapan pakai b: (leech oleh bot)? Saat pengaturan default kamu leech by user tapi ingin leech by bot untuk task tertentu.
* u:id/@username (u: artinya leech oleh user) Ini jika OWNER menambahkan USER_STRING_SESSION.
* h:id/@username (hybrid leech) h: untuk upload file dengan bot dan user berdasarkan ukuran file.
* id/@username|topic_id (leech di chat dan topik tertentu) tambahkan | tanpa spasi lalu tulis topic id setelah chat id atau username. Batas waktu: 60 detik""",
"LEECH_FILENAME_PREFIX": r"Kirim Prefix Nama File Leech. Bisa menambahkan HTML tags. Contoh: <code>@mychannel</code>. Batas waktu: 60 detik",
"THUMBNAIL_LAYOUT": "Kirim layout thumbnail (widthxheight, 2x2, 3x3, 2x4, 4x4, ...). Contoh: 3x3. Batas waktu: 60 detik",
"RCLONE_PATH": "Kirim Rclone Path. Jika ingin menggunakan config rclone edit pakai owner/user config dari usetting atau tambahkan mrcc: sebelum rclone path. Contoh mrcc:remote:folder. Batas waktu: 60 detik",
"RCLONE_FLAGS": "key:value|key|key|key:value . Cek semua di <a href='https://rclone.org/flags/'>RcloneFlags</a>\nContoh: --buffer-size:8M|--drive-starred-only",
"GDRIVE_ID": "Kirim Gdrive ID. Jika ingin pakai token.pickle edit dengan owner/user token dari usetting atau tambahkan mtp: sebelum id. Contoh: mtp:F435RGGRDXXXXXX . Batas waktu: 60 detik",
"INDEX_URL": "Kirim Index URL. Batas waktu: 60 detik",
"UPLOAD_PATHS": "Kirim Dict dari key yang punya nilai path. Contoh: {'path 1': 'remote:rclonefolder', 'path 2': 'gdrive1 id', 'path 3': 'tg chat id', 'path 4': 'mrcc:remote:', 'path 5': b:@username} . Batas waktu: 60 detik",
"EXCLUDED_EXTENSIONS": "Kirim ekstensi yang dikecualikan, dipisahkan dengan spasi tanpa titik di awal. Batas waktu: 60 detik",
"NAME_SUBSTITUTE": r"""Substitusi Kata. Bisa menambahkan pola (pattern) bukan hanya teks normal. Batas waktu: 60 detik
CATATAN: Harus tambahkan \ sebelum karakter spesial berikut: \^$.|?*+()[]{}-
Contoh: script/code/s | mirror/leech | tea/ /s | clone | cpu/ | \[mltb\]/mltb | \\text\\/text/s
1. script akan diganti dengan code (case sensitif)
2. mirror akan diganti dengan leech
4. tea akan diganti dengan spasi (case sensitif)
5. clone akan dihapus
6. cpu akan diganti dengan spasi
7. [mltb] akan diganti dengan mltb
8. \text\ akan diganti dengan text (case sensitif)
""",
"YT_DLP_OPTIONS": """Kirim dict opsi YT-DLP. Batas waktu: 60 detik
Format: {key: value, key: value, key: value}.
Contoh: {"format": "bv*+mergeall[vcodec=none]", "nocheckcertificate": True, "playliststart": 10, "fragment_retries": float("inf"), "matchtitle": "S13", "writesubtitles": True, "live_from_start": True, "postprocessor_args": {"ffmpeg": ["-threads", "4"]}, "wait_for_video": (5, 100), "download_ranges": [{"start_time": 0, "end_time": 10}]}
Cek semua opsi api yt-dlp di <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>FILE</a> atau gunakan <a href='https://t.me/mltb_official_channel/177'>script ini</a> untuk mengubah argumen CLI jadi opsi API.""",
"FFMPEG_CMDS": """Dict berisi list command ffmpeg. Bisa atur banyak command ffmpeg untuk semua file sebelum upload. Jangan tulis ffmpeg di awal, langsung tulis argumennya.
Contoh: {"subtitle": ["-i mltb.mkv -c copy -c:s srt mltb.mkv", "-i mltb.video -c copy -c:s srt mltb"], "convert": ["-i mltb.m4a -c:a libmp3lame -q:a 2 mltb.mp3", "-i mltb.audio -c:a libmp3lame -q:a 2 mltb.mp3"], "extract": ["-i mltb -map 0:a -c copy mltb.mka -map 0:s -c copy mltb.srt"], "metadata": ["-i mltb.mkv -map 0 -map -0:v:1 -map -0:s -map 0:s:0 -map -0:v:m:attachment -c copy -metadata:s:v:0 title={title} -metadata:s:a:0 title={title} -metadata:s:a:1 title={title2} -metadata:s:a:2 title={title2} -c:s srt -metadata:s:s:0 title={title3} mltb -y -del"], "watermark": ["-i mltb -i tg://openmessage?user_id=5272663208&message_id=322801 -filter_complex 'overlay=W-w-10:H-h-10' -c:a copy mltb"]}
Catatan:
- Tambahkan `-del` di list jika ingin bot menghapus file asli setelah command selesai!
- Untuk menjalankan salah satu list di bot, misalnya: pakai -ff subtitle (nama list key) atau -ff convert (nama list key)
Penjelasan mltb.* adalah referensi file yang akan diproses:
1. Cmd pertama: input mltb.mkv → hanya jalan di video mkv, output juga mkv. -del akan hapus file asli setelah selesai.
2. Cmd kedua: input mltb.video → jalan di semua video, output mltb (ekstensi sama dengan input).
3. Cmd ketiga: input mltb.m4a → hanya jalan di audio m4a, output mltb.mp3.
4. Cmd keempat: input mltb.audio → jalan di semua audio, output mltb.mp3.
5. Variabel FFmpeg di cmd metadata ({title}, {title2}, dst...), bisa diubah di usetting.
6. Link Telegram bisa dipakai untuk input kecil seperti foto untuk watermark.""",
}


# full help untuk owner/sudo
help_string = f"""
📌 Daftar Perintah Lengkap (Owner/Sudo Only)

Mirror & Leech:
/{BotCommands.MirrorCommand[0]} | /{BotCommands.QbMirrorCommand[0]} | /{BotCommands.JdMirrorCommand[0]} | /{BotCommands.NzbMirrorCommand[0]}
/{BotCommands.LeechCommand[0]} | /{BotCommands.QbLeechCommand[0]} | /{BotCommands.JdLeechCommand[0]} | /{BotCommands.NzbLeechCommand[0]}
/{BotCommands.YtdlCommand[0]} | /{BotCommands.YtdlLeechCommand[0]}

Google Drive:
/{BotCommands.CloneCommand} | /{BotCommands.CountCommand} | /{BotCommands.DeleteCommand}

Tasks:
/{BotCommands.SelectCommand} | /{BotCommands.CancelTaskCommand[0]} | /{BotCommands.CancelAllCommand} | /{BotCommands.ForceStartCommand[0]}

Bot Control:
/{BotCommands.UsersCommand} | /{BotCommands.BotSetCommand[0]} | /{BotCommands.UserSetCommand[0]} | /{BotCommands.StatsCommand}
/{BotCommands.PingCommand} | /{BotCommands.RestartCommand} | /{BotCommands.LogCommand}

Owner Only:
/{BotCommands.ShellCommand} | /{BotCommands.ExecCommand} | /{BotCommands.AExecCommand} | /{BotCommands.ClearLocalsCommand}
"""

# versi singkat user biasa (authorized)
help_string_user = f"""
👋 Selamat datang!
perintah untuk user

Mirror & Leech:
/{BotCommands.MirrorCommand[0]} | /{BotCommands.QbMirrorCommand[0]} | /{BotCommands.YtdlCommand[0]}
/{BotCommands.LeechCommand[0]} | /{BotCommands.QbLeechCommand[0]} | /{BotCommands.YtdlLeechCommand[0]}

Google Drive:
/{BotCommands.CloneCommand} | /{BotCommands.CountCommand} | /{BotCommands.DeleteCommand}

Tools:
/{BotCommands.StatusCommand} | /{BotCommands.StatsCommand}
/{BotCommands.SearchCommand} | /{BotCommands.ListCommand} | /{BotCommands.UserSetCommand}
"""

# unauthorized
help_string_unauth = """
⚠️ 你还没有使用权限。
想用的话，请先联系机器人主人申请。
"""
