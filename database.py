import sqlite3

DB_PATH = "anime.db"

GENRES = [
    "Action", "Adventure", "Comedy", "Drama", "Ecchi", "Fantasy",
    "Horror", "Isekai", "Josei", "Magic", "Mecha", "Mystery",
    "Psychological", "Romance", "School", "Sci-Fi", "Seinen",
    "Shounen", "Slice of Life", "Sports", "Super Power",
    "Supernatural", "Thriller", "Harem", "Parody", "Game",
    "Music", "Historical", "Military", "Martial Arts", "Shoujo"
]

ANIME_LIST = [
    {
        "title": "Nisekoi",
        "synopsis": "Raku Ichijou adalah putra dari pemimpin keluarga yakuza Shuei-gumi. Suatu hari, ia terpaksa berpura-pura berpacaran dengan Chitoge Kirisaki, putri bos geng rival Bee Hive, demi menjaga perdamaian antara kedua kelompok tersebut. Meski awalnya saling membenci, keduanya harus memainkan peran sebagai sepasang kekasih di depan umum setiap harinya. Di sisi lain, hati Raku sebenarnya tertambat pada Kosaki Onodera, teman sekelasnya yang lembut dan manis. Semakin dalam cerita berjalan, semakin banyak gadis yang terlibat dalam kehidupan Raku — termasuk gadis-gadis yang masing-masing mengklaim memiliki hubungan masa lalu dengannya lewat sebuah liontin kunci misterius yang ia selalu bawa. Siapakah sebenarnya gadis yang dijanjikan dalam kenangan masa kecilnya?",
        "rating": 7.6,
        "genres": ["Romance", "Comedy", "School", "Harem", "Shounen"]
    },
    {
        "title": "Yamada-kun to 7-nin no Majo",
        "synopsis": "Ryu Yamada adalah siswa nakal yang selalu terlibat masalah di sekolahnya. Suatu hari, ia tidak sengaja jatuh menimpa Urara Shiraishi, siswi paling pintar di sekolah, dan menyadari bahwa mereka telah bertukar tubuh lewat ciuman. Kejadian aneh ini membuka jalan ke sebuah rahasia besar: terdapat tujuh penyihir di sekolah mereka, masing-masing memiliki kekuatan unik yang diaktifkan lewat ciuman. Bersama anggota Supernatural Studies Club, Ryu mulai menemukan dan mengidentifikasi para penyihir satu per satu. Setiap penyihir menyimpan kemampuan berbeda — dari membaca pikiran, meniru wajah orang lain, hingga melihat masa depan. Di balik pencarian ini, tersimpan sebuah misteri besar tentang legenda tujuh penyihir yang lebih dalam dari yang mereka bayangkan.",
        "rating": 7.5,
        "genres": ["Romance", "Comedy", "School", "Magic", "Supernatural", "Harem", "Shounen"]
    },
    {
        "title": "Isekai wa Smartphone to Tomo ni",
        "synopsis": "Touya Mochizuki tewas secara tidak sengaja akibat kelalaian Tuhan saat disambar petir. Sebagai permintaan maaf, Tuhan mengizinkannya bereinkarnasi di dunia fantasi dengan satu permintaan — ia memilih membawa smartphone-nya. Di dunia baru ini, Touya memiliki bakat sihir yang luar biasa, mampu mempelajari hampir semua elemen sihir dengan mudah. Smartphonenya pun dimodifikasi agar bisa berfungsi di dunia tersebut, memungkinkannya mengakses informasi, peta, dan berbagai kemampuan canggih. Perjalanannya membawa ia bertemu berbagai gadis cantik yang perlahan jatuh cinta padanya. Kehidupan santai, penuh petualangan ringan, dan dikelilingi harem pun menjadi keseharian Touya di dunia yang baru ini.",
        "rating": 6.7,
        "genres": ["Adventure", "Fantasy", "Romance", "Harem", "Isekai", "Magic", "Comedy"]
    },
    {
        "title": "Kono Subarashii Sekai ni Shukufuku wo!",
        "synopsis": "Kazuma Satou, seorang hikikomori remaja, meninggal dengan cara yang sangat memalukan. Di alam barzah, ia dihadapkan pada dewi sombong bernama Aqua yang menawarkan dua pilihan: masuk surga atau bereinkarnasi di dunia fantasi untuk mengalahkan Raja Iblis. Kazuma memilih yang kedua, dan dengan jahil memilih Aqua sebagai 'satu item istimewa' yang dibawanya — yang ternyata berarti Aqua ikut bersamanya ke dunia itu. Di dunia fantasi, mereka membentuk partai bersama Megumin, penyihir yang hanya bisa menggunakan satu mantra ledakan sehari, dan Darkness, kesatria yang sebenarnya masokis. Petualangan mereka jauh dari heroik — penuh kegagalan, kemiskinan, dan kekacauan yang mengocok perut — namun justru itulah yang membuat mereka istimewa.",
        "rating": 8.1,
        "genres": ["Comedy", "Fantasy", "Adventure", "Magic", "Isekai", "Parody", "Supernatural", "Shounen"]
    },
    {
        "title": "Trinity Seven",
        "synopsis": "Arata Kasuga menjalani hari-hari normal bersama sepupunya Hijiri di sebuah kota kecil — sampai suatu hari matahari hitam muncul dan menghancurkan seluruh kota tersebut. Ternyata selama ini Arata hidup dalam ilusi sihir. Hijiri menghilang dan Arata terpaksa masuk ke Royal Biblia Academy, sekolah khusus sihir, untuk menguasai Thema sihirnya dan menyelamatkan Hijiri. Di sana ia bertemu Trinity Seven — tujuh penyihir wanita paling kuat yang masing-masing menguasai salah satu dari tujuh dosa mematikan. Untuk menyelamatkan Hijiri dan memahami kekuatannya sendiri sebagai Demon Lord Candidate, Arata harus belajar dari dan bersama mereka semua. Penuh aksi sihir yang seru dan momen komedi yang terselip di antara pertempuran.",
        "rating": 7.3,
        "genres": ["Action", "Comedy", "Fantasy", "Magic", "Romance", "Harem", "School", "Ecchi", "Shounen"]
    },
    {
        "title": "Beelzebub",
        "synopsis": "Tatsumi Oga adalah siswa paling berandal dan ditakuti di SMA Ishiyama, sekolah khusus anak-anak bermasalah. Suatu hari, ia menemukan seorang pria terapung di sungai yang terbelah dua, dan dari dalam perut pria itu keluarlah bayi — yang ternyata adalah Beelzebub IV, putra dan pewaris tahta Raja Iblis. Secara tidak sengaja, Oga menjadi 'ayah asuh' sang bayi iblis yang makin hari makin menempel padanya. Jika mereka dipisahkan terlalu jauh, Oga akan disetrum. Bersama Hildegard, iblis pelayan yang cantik tapi galak, Oga harus membesarkan sang Bayi Raja Iblis sambil tetap mempertahankan statusnya sebagai preman terkuat di sekolah.",
        "rating": 7.9,
        "genres": ["Action", "Comedy", "Fantasy", "School", "Supernatural", "Shounen"]
    },
    {
        "title": "Saenai Heroine no Sodatekata",
        "synopsis": "Tomoya Aki adalah otaku berat yang bercita-cita membuat doujin game sendiri. Sumber inspirasinya datang saat ia bertemu gadis cantik di bukit yang dipenuhi bunga sakura pada suatu pagi musim semi. Gadis itu ternyata adalah Megumi Katou, teman sekelasnya yang nyaris tidak punya kehadiran. Ia lalu merekrut Eriri Spencer Sawamura, sahabat masa kecilnya yang juga seorang illustrator doujin terkenal, dan Utaha Kasumigaoka, seniornya yang merupakan penulis light novel bestseller. Ketiganya bersama Megumi membentuk circle untuk membuat visual novel. Di balik proses pembuatan game yang penuh perdebatan dan drama, hubungan antar karakter berkembang dengan cara yang tidak terduga dan menyentuh.",
        "rating": 7.5,
        "genres": ["Romance", "Comedy", "School", "Harem", "Ecchi", "Seinen"]
    },
    {
        "title": "Blend S",
        "synopsis": "Maika Sakuranomiya adalah gadis baik hati yang bermimpi pergi ke luar negeri. Untuk mengumpulkan uang, ia mencari pekerjaan paruh waktu — namun tatapan matanya yang tajam dan ekspresinya yang seakan sadis saat gugup selalu membuat pewawancara ketakutan. Hingga suatu hari ia bertemu Dino, pemilik kafe Stile yang unik, yang justru terpesona dengan ekspresi tersebut. Kafe Stile memiliki konsep di mana setiap pelayan memainkan peran kepribadian berbeda — tsundere, kuudere, imouto, dan lainnya. Maika ditugaskan sebagai karakter sadis. Meski aslinya ramah dan pemalu, interaksinya dengan pelanggan dan rekan kerja yang sama-sama unik menghasilkan momen-momen lucu yang menggemaskan setiap episodenya.",
        "rating": 7.2,
        "genres": ["Comedy", "Slice of Life", "Romance", "School"]
    },
    {
        "title": "Eromanga-sensei",
        "synopsis": "Masamune Izumi adalah penulis light novel SMA yang cukup sukses. Illustrator karyanya dikenal dengan nama samaran 'Eromanga-sensei' yang terkenal dengan gambar-gambar ecchi berkualitas tinggi. Selama setahun, adik tirinya Sagiri mengurung diri di kamarnya dan tidak mau keluar sama sekali setelah ibu mereka meninggal. Suatu hari Masamune tidak sengaja menyaksikan siaran langsung streaming Sagiri dan terkejut menyadari bahwa Sagiri adalah Eromanga-sensei yang selama ini bekerja sama dengannya. Momen ini menjadi awal dari hubungan baru antara keduanya — Masamune berusaha membuat Sagiri mau membuka pintu kamarnya, sementara keduanya terus berkolaborasi dalam karya mereka di tengah perasaan yang semakin rumit.",
        "rating": 6.8,
        "genres": ["Comedy", "Drama", "Romance", "Ecchi", "Slice of Life", "Shounen"]
    },
    {
        "title": "Kimi no Na wa",
        "synopsis": "Mitsuha Miyamizu, gadis remaja dari desa pegunungan terpencil, bosan dengan kehidupannya dan berharap bisa menjadi pemuda tampan di Tokyo. Taki Tachibana, pemuda Tokyo yang sibuk, tiba-tiba suatu pagi terbangun di tubuh seorang gadis di desa yang tidak ia kenal. Keduanya mulai bertukar tubuh secara acak setiap kali tidur. Mereka meninggalkan catatan satu sama lain di buku harian dan ponsel, perlahan mengenal satu sama lain meski tidak pernah bertemu. Namun suatu hari, pertukaran itu tiba-tiba berhenti. Taki memutuskan mencari Mitsuha, dan menemukan kebenaran yang jauh lebih mengejutkan dari yang bisa dibayangkan — kebenaran yang berkaitan dengan waktu, ruang, dan takdir yang menghubungkan mereka.",
        "rating": 9.0,
        "genres": ["Drama", "Romance", "Supernatural", "Mystery"]
    },
    {
        "title": "Sakamoto Desu ga?",
        "synopsis": "Sakamoto adalah siswa baru yang sempurna dalam segala hal — tampan, cerdas, atletis, dan selalu tenang dalam situasi apapun. Setiap hal yang ia lakukan tampak begitu elegan dan keren, bahkan saat melakukan hal-hal paling biasa sekalipun seperti menyapu kelas atau berjalan di koridor. Para siswa laki-laki yang merasa tersaingi terus berusaha mempermalukannya atau menjahilinya, namun setiap rencana selalu berbalik menjadikan Sakamoto semakin keren di mata semua orang. Para siswi perempuan kagum padanya tanpa bisa berbuat apa-apa. Kisah episodik yang penuh humor absurd ini mengeksplorasi berbagai situasi sekolah yang dihadapi Sakamoto dengan gaya yang selalu mengejutkan dan menghibur.",
        "rating": 7.8,
        "genres": ["Comedy", "School", "Slice of Life", "Seinen"]
    },
    {
        "title": "Aho Girl",
        "synopsis": "Yoshiko Hanabatake adalah gadis SMA yang luar biasa bodoh — bukan hanya soal pelajaran, tapi juga dalam hal logika dan akal sehat sehari-hari. Satu-satunya hal yang ia sukai adalah pisang, dan ia akan melakukan segalanya demi buah tersebut. A-kun, sahabat masa kecilnya sejak TK, adalah siswa serius berotak encer yang selalu kelelahan dan frustasi menghadapi kelakuan Yoshiko yang tidak masuk akal setiap harinya. Meski terus direpotkan, A-kun tidak bisa benar-benar meninggalkan Yoshiko. Serial komedi pendek ini penuh dengan humor absurd, teriakan frustrasi A-kun, dan kebodohan Yoshiko yang entah mengapa selalu berhasil membuat orang di sekitarnya tertawa — kecuali A-kun sendiri.",
        "rating": 7.0,
        "genres": ["Comedy", "School", "Ecchi", "Shounen"]
    },
    {
        "title": "Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu",
        "synopsis": "Kaede Honjo, seorang pemain baru di game VRMMO NewWorld Online, mendapat saran dari temannya untuk memfokuskan semua stat ke VIT (vitality/pertahanan) karena tidak suka kesakitan. Hasilnya, karakternya Maple menjadi hampir tidak bisa diserang — peluru mental, racun, bahkan serangan fisik tidak berpengaruh padanya. Tapi kemampuan unik Maple tidak berhenti di situ; ia terus menemukan skill-skill aneh dan broken yang bahkan tidak terpikir oleh para developer game. Dengan innocent dan polosnya, Maple menjadi pemain yang ditakuti seluruh server tanpa benar-benar berusaha menjadi kuat. Bersama temannya Sally yang gesit, petualangan konyol dan menggemaskan mereka di dunia game pun terus berlanjut.",
        "rating": 7.3,
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Game"]
    },
    {
        "title": "Prison School",
        "synopsis": "Akademi Hachimitsu adalah sekolah putri bergengsi yang baru saja memutuskan untuk menerima siswa laki-laki. Lima siswa laki-laki pertama — Kiyoshi, Gakuto, Shingo, Andre, dan Joe — adalah satu-satunya pria di antara ratusan siswi. Sayangnya, pada malam pertama mereka mencoba mengintip ke pemandian wanita dan ketahuan oleh Underground Student Council yang dipimpin Mari dan diisi anggota-anggota kejam. Hukumannya: satu bulan di penjara sekolah dengan kondisi kerja keras dan perlakuan yang tidak manusiawi. Serial ini adalah komedi gelap yang penuh strategi, plot twist mengejutkan, dan situasi memalukan yang terus mengalami eskalasi secara tidak terduga.",
        "rating": 7.8,
        "genres": ["Comedy", "Ecchi", "Romance", "School", "Seinen"]
    },
    {
        "title": "Himouto! Umaru-chan",
        "synopsis": "Umaru Doma adalah siswi SMA yang sempurna di mata semua orang — cantik, cerdas, atletis, sopan, dan disukai semua orang di sekolah. Namun begitu ia tiba di rumah dan menutup pintu, ia langsung berubah menjadi gadis kecil mungil berkerudung hamster yang malas, manja, dan hanya mau bermain game, membaca manga, menonton anime, dan menghabiskan waktu dengan camilan. Kakaknya, Taihei, yang harus menanggung semua kelakuan Umaru di rumah sering merasa kewalahan namun tetap menyayanginya. Serial slice of life yang hangat ini juga mengikuti pertemanan Umaru dengan teman-teman sekolahnya yang tidak mengetahui sisi lain gadis sempurna itu.",
        "rating": 7.2,
        "genres": ["Comedy", "Slice of Life", "School", "Seinen"]
    },
    {
        "title": "Go-Toubun no Hanayome",
        "synopsis": "Fuutarou Uesugi, siswa miskin berotak cerdas, mendapat tawaran pekerjaan sebagai tutor dengan bayaran luar biasa besar. Namun ia langsung menyesal saat mengetahui murid-muridnya adalah lima bersaudara kembar identik — Ichika, Nino, Miku, Yotsuba, dan Itsuki Nakano — yang semuanya cantik namun memiliki nilai buruk dan sama sekali tidak mau belajar. Masing-masing quintuplet punya kepribadian yang bertolak belakang dan awalnya menolak kehadiran Fuutarou. Flashforward ke masa depan, salah satu dari mereka akan menikah dengannya. Anime romantis ini menjadi teka-teki menarik bagi penonton: siapakah di antara kelima bersaudara itu yang menjadi pengantin dalam foto pernikahan di awal cerita?",
        "rating": 7.9,
        "genres": ["Romance", "Comedy", "School", "Harem", "Shounen"]
    },
    {
        "title": "Ryuuou no Oshigoto!",
        "synopsis": "Yaichi Kuzuryuu baru saja meraih gelar Ryuuou — gelar shogi tertinggi — di usia 16 tahun, menjadikannya Ryuuou termuda dalam sejarah. Namun ia sedang berada dalam kemerosotan dan tidak tahu cara keluar dari slumpnya. Suatu hari, seorang anak perempuan berusia 9 tahun bernama Ai Hinatsuru tiba-tiba muncul di depan pintunya dan menagih janji Yaichi untuk menjadikan dirinya murid. Meski ragu, Yaichi akhirnya menerimanya — dan terkejut dengan bakat luar biasa yang tersembunyi dalam diri Ai. Kisah ini mengikuti perjalanan Yaichi sebagai guru shogi yang tidak berpengalaman dan Ai sebagai murid yang penuh semangat, dibalut dengan komedi dan drama dunia shogi yang kompetitif.",
        "rating": 7.2,
        "genres": ["Comedy", "Ecchi", "Game", "Romance", "Slice of Life"]
    },
    {
        "title": "Chuunibyou demo Koi ga Shitai!",
        "synopsis": "Yuuta Togashi sangat ingin melupakan fase chuunibyou-nya di SMP — masa di mana ia berpura-pura menjadi 'Dark Flame Master' yang memiliki kekuatan tersembunyi. Kini sebagai siswa SMA baru, ia bertekad memulai hidup normal. Sayangnya, tetangga barunya adalah Rikka Takanashi — siswi yang masih sepenuhnya hidup dalam delusi chuunibyou-nya, meyakini bahwa matanya menyimpan 'Wicked Eye' dengan kekuatan tersembunyi. Rikka terus menyeret Yuuta kembali ke dunia fantasi yang ingin ia tinggalkan. Di balik cerita komedi yang menggemaskan ini, tersimpan kisah yang jauh lebih menyentuh tentang Rikka yang menggunakan dunia fantasinya sebagai cara untuk melarikan diri dari kesedihan dan kenyataan pahit yang tidak bisa ia terima.",
        "rating": 7.9,
        "genres": ["Romance", "Comedy", "Drama", "School", "Slice of Life", "Fantasy"]
    },
    {
        "title": "Dumbbell Nan Kilo Moteru?",
        "synopsis": "Hibiki Sakura adalah siswi SMA yang hobi makan dan mulai sadar berat badannya bertambah. Bertekad menurunkan berat badan, ia mendaftar ke gym Silverman — dan terkejut bertemu Akemi Souryuuin, teman sekelasnya yang cantik dan populer, ternyata juga anggota gym tersebut dengan kecintaan terhadap otot yang mengejutkan. Dipandu oleh trainer tampan Machio yang memiliki tubuh sangat berotot, Hibiki mulai belajar berbagai latihan dasar gym. Serial ini unik karena di balik ceritanya yang lucu dan penuh momen ecchi ringan, setiap episode memberikan informasi edukatif yang akurat tentang teknik olahraga, nutrisi, dan kesehatan yang benar-benar bisa dipraktikkan.",
        "rating": 7.3,
        "genres": ["Comedy", "Ecchi", "School", "Slice of Life", "Sports", "Seinen"]
    },
    {
        "title": "Kanojo, Okarishimasu",
        "synopsis": "Kazuya Kinoshita, mahasiswa yang baru saja diputus pacarnya, menggunakan layanan sewa pacar dalam kondisi depresi dan memesan Chizuru Mizuhara — gadis cantik yang berambisi menjadi aktris. Setelah foto mereka tersebar ke keluarga, Kazuya terpaksa mempertahankan kebohongan bahwa Chizuru adalah pacar sungguhnya. Situasi semakin rumit ketika mantan pacar Kazuya muncul kembali, dan ketika Chizuru ternyata tinggal tepat di sebelah apartemennya. Serial ini mengikuti dilema Kazuya yang terjebak antara perasaannya yang sesungguhnya, komitmen kontraknya dengan Chizuru, dan kemunculan karakter-karakter lain yang memperumit situasi sewa-menyewa yang sudah kacau ini.",
        "rating": 7.1,
        "genres": ["Romance", "Comedy", "School", "Shounen"]
    },
    {
        "title": "Kaguya-sama wa Kokurasetai",
        "synopsis": "Miyuki Shirogane dan Kaguya Shinomiya adalah dua siswa terbaik di SMA Shuchiin yang bergengsi — Shirogane sebagai Ketua OSIS dan Kaguya sebagai Wakil Ketua. Keduanya saling menyukai, namun bagi mereka yang terbiasa menjadi yang terdepan dalam segalanya, mengakui perasaan duluan adalah tanda kelemahan yang tidak bisa diterima. Maka dimulailah perang psikologi sehari-hari — setiap interaksi menjadi medan pertempuran di mana masing-masing berusaha memanipulasi situasi agar pihak lawanlah yang menyatakan cinta lebih dulu. Komedi cerdas ini penuh strategi rumit, narasi internal yang lucu, dan momen-momen romantis yang menggemaskan di tengah pertarungan ego dua orang jenius yang sama-sama keras kepala.",
        "rating": 8.4,
        "genres": ["Romance", "Comedy", "School", "Psychological", "Seinen"]
    },
    {
        "title": "Danshi Koukousei no Nichijou",
        "synopsis": "Keseharian tiga sahabat siswa SMA laki-laki — Tadakuni, Hidenori, dan Yoshitake — bersama teman-teman mereka yang sama-sama unik dan tidak kalah anehnya. Tidak ada plot besar, tidak ada petualangan heroik — hanya sekumpulan momen sehari-hari yang sekilas biasa namun selalu berakhir dengan cara yang tidak terduga dan menggelikan. Dari percobaan memakai pakaian perempuan milik adik Tadakuni, hingga imajinasi liar mereka tentang berbagai skenario, hingga interaksi konyol dengan siswi-siswi dari sekolah lain. Serial ini menangkap dengan sempurna absurditas kehidupan remaja laki-laki yang penuh energi, kebodohan yang menggemaskan, dan persahabatan yang tulus di balik semua kekonyolan tersebut.",
        "rating": 8.2,
        "genres": ["Comedy", "School", "Slice of Life", "Shounen"]
    },
    {
        "title": "Re:Zero kara Hajimeru Isekai Seikatsu",
        "synopsis": "Subaru Natsuki, seorang hikikomori, tiba-tiba dipindahkan ke dunia fantasi saat keluar dari minimarket. Tanpa kekuatan sihir atau keahlian khusus, ia tampak tidak memiliki apa-apa — sampai ia menyadari kemampuan tersembunyinya: Return by Death. Setiap kali ia mati, ia kembali ke 'checkpoint' tertentu, seolah mengulang waktu. Kemampuan yang tampak menguntungkan ini ternyata adalah kutukan yang menyiksa — ia harus mengalami kematian berulang kali, menyaksikan orang-orang yang dicintainya mati, dan menanggung semua trauma itu sendirian karena tidak ada yang bisa ingat apa yang terjadi kecuali dirinya. Kisah ini mengeksplorasi tema ketahanan mental, cinta, dan pengorbanan dengan cara yang sangat emosional dan menegangkan.",
        "rating": 8.3,
        "genres": ["Drama", "Fantasy", "Psychological", "Mystery", "Thriller", "Isekai", "Supernatural"]
    },
    {
        "title": "Shigatsu wa Kimi no Uso",
        "synopsis": "Kousei Arima adalah pianis anak ajaib yang mendominasi setiap kompetisi. Namun setelah ibunya meninggal — ibu yang sekaligus guru kerasnya — ia mengalami trauma dan tidak bisa lagi mendengar suara pianonya sendiri saat memainkannya, seolah dunia menjadi hitam putih. Dua tahun kemudian, kehidupannya yang abu-abu berubah saat teman baiknya memperkenalkan Kaori Miyazono, pemain biola bebas spirited yang memainkan musik dengan penuh ekspresi dan emosi tanpa terikat partitur. Kaori memaksa Kousei untuk menjadi pengiringnya dan perlahan mendorongnya kembali ke panggung. Kisah cinta yang indah namun menyakitkan ini menyentuh tema trauma, penyembuhan, dan arti musik sebagai bahasa jiwa yang melampaui kata-kata.",
        "rating": 8.7,
        "genres": ["Drama", "Music", "Romance", "School", "Slice of Life", "Shounen"]
    },
    {
        "title": "High School DxD",
        "synopsis": "Issei Hyoudou adalah siswa SMA lecher yang hanya punya satu mimpi: memiliki harem. Impian itu tampak mulai terwujud saat ia berkencan pertama kali — namun kencan itu berakhir dengan ia dibunuh oleh pacarnya yang ternyata adalah Fallen Angel. Ia dibangkitkan dari kematian oleh Rias Gremory, siswi cantik yang merupakan iblis dari keluarga bangsawan, dan kini menjadi anggota keluarga iblis milik Rias dengan Sacred Gear bernama Boosted Gear yang memiliki kemampuan untuk melipatgandakan kekuatan tanpa batas. Issei harus belajar cara bertarung di dunia yang dipenuhi iblis, malaikat, dan fallen angel, sambil tetap bermimpi menjadi Harem King — impian yang kini tidak lagi hanya angan-angan.",
        "rating": 7.6,
        "genres": ["Action", "Comedy", "Ecchi", "Fantasy", "Harem", "Romance", "School", "Supernatural", "Shounen"]
    },
    {
        "title": "Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai",
        "synopsis": "Sakuta Azusagawa adalah siswa SMA yang tidak peduli dengan opini orang lain setelah mengalami insiden aneh yang meninggalkan luka di tubuhnya. Suatu hari di perpustakaan, ia melihat Mai Sakurajima — aktris terkenal yang sedang hiatus — berjalan dengan kostum kelinci tanpa ada seorangpun yang memperhatikannya. Fenomena ini disebut Puberty Syndrome, anomali berbasis kuantum yang menyerang remaja dengan masalah emosional. Sakuta memutuskan untuk membantu Mai dan berbagai orang yang mengalami fenomena serupa. Setiap arc mengikuti gadis yang berbeda dengan manifestasi Puberty Syndrome yang unik — dari kehilangan keberadaan hingga berulangnya waktu — sambil hubungan Sakuta dan Mai berkembang dengan cara yang natural dan menyentuh.",
        "rating": 8.4,
        "genres": ["Drama", "Mystery", "Romance", "School", "Supernatural", "Sci-Fi"]
    },
    {
        "title": "Uzaki-chan wa Asobitai!",
        "synopsis": "Shinichi Sakurai adalah mahasiswa year dua yang menikmati waktu sendirian dan hidupnya yang tenang. Hana Uzaki, adik kelas yang pernah satu SMA dengannya, tiba-tiba muncul di kehidupan kampusnya dan bersikeras bahwa Sakurai terlalu kesepian dan membosankan. Uzaki yang cerewet, energetik, dan selalu bersemangat terus memaksa Sakurai untuk menghabiskan waktu bersama — pergi ke kafe game, menonton film, berkunjung ke rumahnya, dan berbagai aktivitas lain yang Sakurai hadiri dengan setengah hati namun diam-diam menikmati. Di sekitar mereka, teman-teman dan staf kafe mulai bertaruh kapan kedua orang yang jelas-jelas cocok ini akhirnya akan mengakui perasaan satu sama lain.",
        "rating": 7.2,
        "genres": ["Comedy", "Romance", "Ecchi", "Slice of Life", "School", "Seinen"]
    },
    {
        "title": "Enen no Shouboutai",
        "synopsis": "Di dunia masa depan, fenomena misterius bernama Spontaneous Human Combustion membuat manusia tiba-tiba terbakar dan berubah menjadi makhluk api yang disebut Infernal. Special Fire Force, brigade pemadam khusus yang terdiri dari individu-individu dengan kemampuan pyrokinesis, bertugas menghentikan Infernal dan mendoakan arwah mereka. Shinra Kusakabe, pemuda yang dijuluki 'Iblis' karena tersenyum saat gugup dan memiliki kemampuan membakar kakinya sendiri untuk terbang, bergabung dengan Company 8 dengan tekad menemukan kebenaran di balik kematian ibunya dan adiknya 12 tahun lalu. Semakin dalam ia menyelidiki, semakin besar konspirasi yang ia temukan di balik fenomena pembakaran ini.",
        "rating": 7.5,
        "genres": ["Action", "Fantasy", "Mystery", "Supernatural", "Shounen"]
    },
    {
        "title": "Boku wa Tomodachi ga Sukunai",
        "synopsis": "Kodaka Hasegawa pindah ke sekolah baru dan tidak bisa berteman karena rambut pirangnya yang membuatnya terlihat seperti delinkuen meski sebenarnya ia anak yang baik. Suatu hari ia menemukan Yozora Mikazuki berbicara dengan 'teman khayalannya' sendirian di kelas. Dari pertemuan itu, mereka mendirikan Neighbor's Club — klub untuk orang-orang yang tidak punya teman dan ingin belajar cara berteman. Anggota yang bergabung termasuk Sena Kashiwazaki yang cantik namun arogan dan lebih suka game dari orang nyata, hingga berbagai karakter lain yang sama-sama canggung dalam bersosialisasi. Ironi terbesar klub ini: meskipun semua anggotanya tidak punya teman, mereka justru sudah menjadi teman satu sama lain tanpa menyadarinya.",
        "rating": 7.4,
        "genres": ["Comedy", "Ecchi", "Harem", "Romance", "School", "Seinen"]
    },
    {
        "title": "Kakegurui",
        "synopsis": "Di Akademi Hyakkaou yang eksklusif untuk anak-anak orang kaya dan berpengaruh, hierarki sosial tidak ditentukan oleh nilai akademis melainkan oleh kemampuan berjudi. Siswa yang kalah berjudi menjadi 'housepet' — budak yang melayani siswa yang lebih tinggi. Tiba-tiba Yumeko Jabami, gadis cantik berwajah innocent, masuk sebagai murid baru. Namun di balik penampilannya tersimpan jiwa penjudi yang sesungguhnya — bukan seseorang yang bermain untuk menang, melainkan seseorang yang merasakan euforia terbesar justru saat berada di tepi antara menang dan kalah. Kehadirannya mengacaukan seluruh sistem yang sudah lama berdiri di sekolah tersebut dengan cara yang sama sekali tidak terduga.",
        "rating": 7.9,
        "genres": ["Drama", "Game", "Mystery", "Psychological", "School", "Thriller", "Seinen"]
    },
    {
        "title": "Girls und Panzer",
        "synopsis": "Di dunia alternatif ini, Tankery — olahraga menggunakan tank perang sesungguhnya — adalah seni bela diri feminin yang bergengsi dan diwariskan turun-temurun. Miho Nishizumi berasal dari keluarga Tankery terpandang namun pindah sekolah justru untuk menghindari olahraga tersebut setelah insiden traumatis. Di sekolah barunya yang berupa kapal induk raksasa, Oarai Girls Academy, ia dibujuk bergabung dengan tim Tankery yang baru dibentuk untuk menyelamatkan sekolah dari ancaman penutupan. Dengan tim yang hampir tidak berpengalaman dan tank-tank tua yang diperbaiki dari berbagai tempat, mereka menghadapi turnamen nasional melawan sekolah-sekolah dengan tradisi Tankery yang jauh lebih kuat. Kisah tentang persahabatan, kepemimpinan, dan menemukan kembali passion yang sempat ditinggalkan.",
        "rating": 7.9,
        "genres": ["Action", "Comedy", "Military", "School", "Sports"]
    },
    {
        "title": "Youjo Senki",
        "synopsis": "Seorang eksekutif perusahaan Jepang yang kejam dan tidak berempati dibunuh oleh bawahannya yang dendam. Di alam kematian, ia berhadapan dengan Being X yang mengklaim sebagai Tuhan dan menghukumnya dengan cara bereinkarnasi di era perang yang mirip Eropa Perang Dunia Satu, dalam tubuh seorang anak perempuan kecil bernama Tanya Degurechaff. Tanya yang tetap mempertahankan semua memori dan kepribadian aslinya bertekad bertahan hidup dan naik jabatan militer secepat mungkin untuk keluar dari zona perang. Dengan kecerdasan orang dewasa dalam tubuh anak kecil, ia menjadi perwira yang paling berbahaya, dingin, dan ditakuti dalam seluruh angkatan bersenjata — sambil diam-diam menentang Being X.",
        "rating": 8.0,
        "genres": ["Action", "Fantasy", "Historical", "Military", "Isekai"]
    },
    {
        "title": "Great Pretender",
        "synopsis": "Makoto Edamura mengklaim sebagai penipu terhebat di Jepang, namun satu-satunya orang yang berhasil ia tipu ternyata adalah Laurent Thierry, penipu kelas dunia asal Prancis yang jauh lebih berpengalaman. Merasa tertantang, Laurent merekrut Edamura untuk bergabung dalam misi penipuan berskala internasional yang menargetkan individu-individu paling jahat dan berbahaya di dunia — mulai dari bandar narkoba Hollywood, mafia Singapura, hingga arms dealer internasional. Setiap arc membawa Edamura ke lokasi eksotis yang berbeda dengan rencana penipuan yang semakin kompleks dan berlapis. Visual yang memukau dengan palet warna cerah khas Studio Wit, twist yang mengejutkan, dan dinamika karakter yang kaya membuat serial ini menonjol dari anime thriller lainnya.",
        "rating": 8.2,
        "genres": ["Action", "Adventure", "Comedy", "Mystery", "Thriller", "Seinen"]
    },
    {
        "title": "Overlord",
        "synopsis": "Momonga adalah pemain hardcore MMORPG Yggdrasil yang memutuskan untuk tetap login hingga server ditutup sebagai perpisahan dengan game yang telah menemaninya bertahun-tahun. Namun saat waktu shutdown tiba, ia tidak terputus — malah terjebak di dalam dunia game yang kini menjadi nyata. Semua NPC mulai menunjukkan kesadaran dan emosi, dan ia yang sekarang terkurung dalam avatar tulang belulangnya sebagai Overlord Ainz Ooal Gown harus beradaptasi dengan dunia baru ini. Sambil mencari cara pulang dan kemungkinan pemain lain yang senasib, ia memimpin Nazarick — guild dungeon terkuatnya — dan secara perlahan mulai memperluas pengaruhnya atas dunia yang baru ini dengan kekuatan yang jauh melampaui semua makhluk hidup di dalamnya.",
        "rating": 7.9,
        "genres": ["Action", "Adventure", "Fantasy", "Magic", "Isekai", "Game", "Supernatural"]
    },
    {
        "title": "Date A Live",
        "synopsis": "Shido Itsuka menjalani hari-hari biasa sampai sebuah gempa spasial menghancurkan kota dan memunculkan Spirit — makhluk misterius dari dimensi lain yang kemunculannya selalu disertai bencana. Organisasi rahasia Ratatoskr mengungkapkan cara untuk menaklukkan Spirit tanpa pertumpahan darah: membuat mereka jatuh cinta pada Shido, yang kemudian bisa menyegel kekuatan mereka. Shido yang awalnya ragu tidak punya pilihan selain menjalani 'kencan' dengan berbagai Spirit yang masing-masing memiliki kepribadian unik dan trauma mendalam. Di sisi lain, organisasi militer AST dipimpin oleh gadis yang juga mengincar Shido. Pertarungan antara dua pendekatan berbeda dalam menghadapi Spirit menjadi latar konflik yang terus berkembang.",
        "rating": 7.2,
        "genres": ["Action", "Comedy", "Fantasy", "Harem", "Romance", "School", "Sci-Fi", "Shounen", "Ecchi"]
    },
    {
        "title": "Wotaku ni Koi wa Muzukashii",
        "synopsis": "Narumi Momose adalah wanita karir yang mati-matian menyembunyikan identitasnya sebagai fujoshi dan otaku dari rekan kerja barunya. Namun di hari pertama kerja, ia langsung bertemu Hirotaka Nifuji, teman masa kecilnya yang merupakan gamer berat — dan Hirotaka langsung membocorkan rahasia otakunya di depan semua orang. Hirotaka kemudian mengusulkan dengan santai agar mereka berpacaran karena 'sesama otaku lebih mudah satu frekuensi'. Anime slice of life dewasa ini mengikuti hubungan pasangan otaku yang realistis — penuh gaming bersama, jalan ke Comiket, dan momen-momen canggung tapi tulus. Juga mengikuti pasangan sahabat mereka yang sama-sama otaku dengan dinamika hubungan yang berbeda.",
        "rating": 7.7,
        "genres": ["Comedy", "Romance", "Slice of Life", "Josei"]
    },
    {
        "title": "Goblin Slayer",
        "synopsis": "Di dunia petualangan fantasi ini, goblin dianggap musuh paling rendah dan tidak berbahaya — quest melawan mereka hanya diberikan kepada adventurer pemula. Tapi bagi mereka yang pernah menjadi korban serangan goblin, kebenaran jauh lebih gelap dan mengerikan. Seorang Pendeta muda yang baru memulai petualangannya hampir kehilangan segalanya dalam quest pertamanya melawan goblin. Ia diselamatkan oleh Goblin Slayer — pria bersenjata lengkap dan berpengalaman yang mengkhususkan hidupnya hanya untuk satu tujuan: memusnahkan seluruh goblin. Kisah gelap ini tidak meromantiskan petualangan, menggambarkan bahaya nyata di dunia fantasi, dan mengikuti perjalanan Goblin Slayer yang perlahan-lahan membuka diri pada orang-orang di sekitarnya.",
        "rating": 7.5,
        "genres": ["Action", "Adventure", "Fantasy", "Horror", "Mystery", "Seinen"]
    },
    {
        "title": "JoJo no Kimyou na Bouken",
        "synopsis": "Saga epik keluarga Joestar yang membentang lintas generasi dan berbagai era waktu. Dimulai dari Jonathan Joestar di abad ke-19 yang berhadapan dengan Dio Brando, rival yang meresapi seluruh hidupnya. Dilanjutkan dengan Joseph Joestar melawan kaum Pillar Men di Perang Dunia II, Jotaro Kujo yang mengembangkan kekuatan Stand untuk menghadapi Dio yang telah abadi, Josuke Higashikata di kota damai Morioh, hingga Giorno Giovanna yang bercita-cita menguasai mafia Italia. Setiap bagian memperkenalkan sistem kekuatan baru yang kreatif, villain ikonik, dan pose-pose dramatis khas JoJo. Serial yang mendefinisikan ulang batas kreativitas dalam manga dan anime dengan referensi musik dan fashion yang kaya.",
        "rating": 8.8,
        "genres": ["Action", "Adventure", "Fantasy", "Horror", "Mystery", "Supernatural", "Shounen"]
    },
    {
        "title": "Violet Evergarden",
        "synopsis": "Violet Evergarden adalah mantan prajurit yang hanya mengenal perang dan pertempuran sepanjang hidupnya. Setelah kehilangan kedua lengannya dalam pertempuran terakhir dan kehilangan pula satu-satunya orang yang ia cintai, ia mulai bekerja sebagai Auto Memory Doll — jasa pengetik surat yang menerjemahkan perasaan klien menjadi kata-kata. Violet yang tidak mengerti arti kata 'cinta' — kata terakhir yang diucapkan oleh Mayor Gilbert padanya sebelum mereka terpisah — memulai perjalanan menemukan makna di balik kata itu melalui setiap surat yang ia tulis. Setiap episode membawa kisah klien berbeda yang menyentuh hati: seorang ibu yang sekarat menulis surat untuk putrinya, seorang dramawan yang mencari inspirasi, seorang pria yang sulit mengungkapkan perasaan. Visual yang memukau dan musik yang indah melengkapi cerita yang luar biasa emosional ini.",
        "rating": 8.7,
        "genres": ["Drama", "Fantasy", "Slice of Life", "Mystery"]
    },
    {
        "title": "One Punch Man",
        "synopsis": "Saitama memulai hobi menjadi pahlawan karena iseng. Selama tiga tahun ia berlatih dengan sangat keras — lari 10km, 100 push-up, 100 sit-up, 100 squat setiap hari — hingga rambutnya rontok semua. Hasilnya: ia menjadi pahlawan yang bisa mengalahkan musuh siapapun, sekuat apapun, hanya dengan satu pukulan. Masalahnya, kekuatan mutlak ini membuatnya tidak merasakan kepuasan dalam bertarung — tidak ada tantangan, tidak ada tegangan, tidak ada kegembiraan. Ia menjalani hidupnya yang monoton sebagai pahlawan amatir tak terdaftar sambil berburu diskon di supermarket. Kisah satiris jenius ini membalik trope pahlawan dengan memberikan karakter utama kekuatan maksimal sejak awal, lalu mengeksplorasi kekosongan emosional yang hadir bersamanya.",
        "rating": 8.7,
        "genres": ["Action", "Comedy", "Parody", "Super Power", "Supernatural", "Seinen"]
    },
    {
        "title": "Dr. Stone",
        "synopsis": "Suatu hari seluruh umat manusia di bumi secara serentak membatu, terperangkap dalam batu selama ribuan tahun. Senku Ishigami, remaja jenius dengan kecintaan luar biasa terhadap ilmu pengetahuan, berhasil keluar dari petrifikasinya setelah 3.700 tahun. Ia menemukan dunia yang telah kembali ke alam liar — peradaban manusia musnah total. Senku bertekad membangun kembali ilmu pengetahuan dari nol, memulai dari membuat api, kemudian alkohol, obat-obatan, baja, dan perlahan merekonstruksi peradaban modern menggunakan otak dan sains semata. Namun ia tidak sendirian — ada yang ingin membangun dunia baru tanpa ilmu pengetahuan. Anime yang secara mengejutkan sangat edukatif tentang kimia, fisika, dan biologi sambil tetap seru dan menghibur.",
        "rating": 8.3,
        "genres": ["Action", "Adventure", "Comedy", "Sci-Fi", "Shounen"]
    },
    {
        "title": "Shingeki no Kyojin",
        "synopsis": "Selama ratusan tahun, umat manusia berlindung di balik tiga tembok konsentris raksasa untuk bertahan dari Titan — makhluk humanoid raksasa yang memakan manusia tanpa alasan yang jelas. Eren Yeager hidup di balik tembok terluar bersama ibunya Carla dan sahabatnya Mikasa dan Armin. Ketenangan itu hancur saat Colossal Titan dan Armored Titan menghancurkan tembok terluar, dan Eren menyaksikan sendiri ibunya dimakan. Ia bersumpah akan membasmi seluruh Titan. Bergabung dengan Survey Corps, Eren menemukan bahwa dirinya menyimpan kemampuan transformasi Titan, dan bahwa kebenaran di balik Titan, tembok, dan sejarah dunia jauh lebih gelap dan kompleks dari yang bisa dibayangkan siapapun.",
        "rating": 9.0,
        "genres": ["Action", "Drama", "Fantasy", "Horror", "Military", "Mystery", "Shounen", "Thriller"]
    },
    {
        "title": "Hataraku Saibou!!",
        "synopsis": "Bayangkan tubuh manusia sebagai sebuah kota yang sangat ramai dan sibuk, di mana triliunan 'pekerja' menjalankan fungsinya masing-masing setiap saat. Sel Darah Merah (RBC) mengantarkan oksigen ke seluruh tubuh dengan seragam merahnya sambil sering tersesat di kapiler yang membingungkan. Sel Darah Putih (WBC) adalah tentara yang siap siaga membunuh bakteri dan virus yang masuk. Trombosit adalah barisan anak-anak kecil menggemaskan yang memperbaiki luka. Setiap episode mengikuti satu atau beberapa situasi medis — dari luka gores biasa, serangan bakteri, alergi, hingga kondisi yang lebih serius — yang divisualisasikan sebagai pertempuran dan krisis yang harus diselesaikan oleh para 'pekerja' tubuh. Edukatif, lucu, dan menggemaskan sekaligus.",
        "rating": 7.7,
        "genres": ["Action", "Comedy", "Shounen"]
    },
    {
        "title": "Josee to Tora to Sakana-tachi",
        "synopsis": "Tsuneo Nakamura adalah mahasiswa muda yang bermimpi menyelam di Meksiko bersama ribuan ikan laut dalam yang bercahaya. Untuk mewujudkan mimpinya, ia bekerja keras sambil kuliah. Suatu hari ia menyelamatkan kursi roda yang meluncur di jalan miring — dan bertemu Josee, gadis yang lahir dengan kondisi tak bisa berjalan dan telah lama mengurung dirinya di rumah neneknya, hidup dalam dunia buku dan imajinasi. Nenek Josee menawarkan Tsuneo pekerjaan menemani Josee. Perlahan, Tsuneo dengan sabar membuka dunia luar untuk Josee — membawanya ke pantai, ke kafe, ke kehidupan yang belum pernah ia rasakan. Film anime ini adalah kisah cinta yang hangat tentang dua orang yang saling membantu meraih mimpi masing-masing.",
        "rating": 8.4,
        "genres": ["Drama", "Romance", "Slice of Life"]
    },
    {
        "title": "Shuumatsu no Walküre",
        "synopsis": "Para dewa dari semua mitologi — Zeus, Odin, Thor, Poseidon, Shiva, Budha, dan lainnya — mengadakan pertemuan setiap 1000 tahun untuk mengevaluasi nasib umat manusia. Kali ini, keputusan bulat: manusia layak dimusnahkan. Namun Brunhild, salah satu Valkyrie, mengajukan usulan Ragnarok — turnamen di mana 13 manusia terkuat sepanjang sejarah melawan 13 dewa dalam pertarungan satu lawan satu. Jika manusia memenangkan 7 pertarungan, mereka boleh hidup 1000 tahun lagi. Para Valkyrie sendiri berubah menjadi senjata untuk para pejuang manusia. Dari Adam melawan Zeus hingga pertarungan bersejarah lainnya, setiap laga adalah epik yang penuh emosi, backstory mendalam, dan aksi yang memompa adrenalin.",
        "rating": 7.9,
        "genres": ["Action", "Drama", "Fantasy", "Historical", "Martial Arts", "Supernatural", "Seinen"]
    },
    {
        "title": "Gokushufudou",
        "synopsis": "Tatsu, yakuza legendaris yang dijuluki 'Naga Tidak Terkalahkan', adalah salah satu pria paling berbahaya dan ditakuti di dunia kriminal Jepang. Namun ia memutuskan pensiun total dari dunia tersebut demi menikah dengan Miku, wanita yang ia cintai dan yang bekerja sebagai desainer. Sekarang Tatsu adalah ibu rumah tangga sepenuh waktu — memasak, membersihkan rumah, berbelanja di supermarket, dan bersaing sengit dengan ibu-ibu kompleks lainnya dalam urusan rumah tangga. Manga dan anime ini menangkap kontras lucu antara reputasi kerasnya sebagai yakuza dengan kesungguhannya menjalani kehidupan domestik, sambil sesekali berhadapan dengan musuh-musuh lama yang terus mencarinya.",
        "rating": 8.0,
        "genres": ["Action", "Comedy", "Slice of Life", "Seinen"]
    },
    {
        "title": "Baki",
        "synopsis": "Baki Hanma adalah pemuda yang menghabiskan seluruh hidupnya untuk satu tujuan: mengalahkan Yuujirou Hanma, ayahnya sendiri yang dijuluki Ogre — manusia terkuat yang pernah hidup di bumi. Yuujirou adalah makhluk yang bahkan tentara dan senjata modern tidak mampu menghadapinya. Untuk mencapai level itu, Baki bertarung melawan petarung-petarung terkuat dari seluruh dunia. Di arc ini, lima narapidana paling berbahaya di dunia — yang dipenjara bukan karena kejahatan biasa, melainkan karena kemampuan tempur yang melampaui batas normal — melarikan diri dan datang ke Jepang mencari kekalahan, karena mereka belum pernah merasakan kalah. Pertarungan brutal tanpa aturan yang mengeksplorasi filosofi kekuatan, kemenangan, dan kekalahan.",
        "rating": 7.5,
        "genres": ["Action", "Adventure", "Martial Arts", "Seinen", "Sports"]
    },
    {
        "title": "Kengan Ashura",
        "synopsis": "Sejak zaman kuno, pengusaha-pengusaha Jepang menyelesaikan sengketa bisnis mereka dengan cara yang tidak biasa: menyewa petarung bayaran untuk bertarung satu lawan satu, dan pemenangnya mendapatkan semua. Sistem ini dikenal sebagai Kengan Match. Yamashita Kazuo, seorang salaryman biasa, tidak sengaja terlibat dalam dunia ini saat Tokita Ohma — petarung misterius dengan kemampuan luar biasa yang muncul entah dari mana — memilihnya sebagai pemilik. Ohma berpartisipasi dalam turnamen Kengan Annihilation untuk alasan yang tersembunyi. Setiap petarung memiliki teknik dan filosofi bertarung yang unik, dan setiap pertandingan mengungkap lebih banyak tentang latar belakang misterius Ohma.",
        "rating": 7.9,
        "genres": ["Action", "Drama", "Martial Arts", "Seinen", "Sports"]
    },
    {
        "title": "No Game No Life",
        "synopsis": "Sora dan Shiro, kakak-adik yang tidak pernah keluar rumah, adalah legenda dunia game online yang tidak pernah kalah dengan nama samaran Blank. Suatu hari mereka menerima tantangan catur dari entitas misterius yang mengundang mereka ke Disboard — dunia di mana segala konflik diselesaikan melalui permainan dengan aturan ketat yang tidak boleh dilanggar. Di dunia ini, umat manusia (Imanity) adalah ras paling lemah di antara 16 ras yang ada, tidak memiliki sihir atau kemampuan istimewa. Sora dan Shiro harus menggunakan kecerdasan murni, psikologi, dan kreativitas luar biasa untuk mengalahkan ras-ras yang jauh lebih kuat dan akhirnya menantang Tet, Dewa Permainan, demi menguasai Disboard.",
        "rating": 8.2,
        "genres": ["Adventure", "Comedy", "Fantasy", "Game", "Isekai", "Ecchi", "Shounen"]
    },
    {
        "title": "Ansatsu Kyoushitsu",
        "synopsis": "Sebuah makhluk misterius dengan tubuh seperti gurita, wajah bulan sabit, dan kemampuan bergerak dengan kecepatan Mach 20 menghancurkan sebagian besar bulan dan mengancam akan melakukan hal yang sama pada bumi dalam satu tahun. Namun ia mengajukan satu permintaan aneh: izinkan dirinya mengajar kelas 3-E di SMA Kunugigaoka — kelas paling tidak dianggap yang berisi siswa-siswa yang dianggap gagal. Siswa-siswa ini diberi tugas membunuhnya sebelum batas waktu berakhir dengan reward 10 miliar yen. Tapi Korosensei, sebutan yang diberikan murid-muridnya, ternyata adalah guru terbaik yang pernah ada — peduli, pintar mengajar, dan selalu mendorong setiap murid untuk berkembang. Ironi terbesar: semakin mereka ingin membunuhnya, semakin mereka sayang padanya.",
        "rating": 8.1,
        "genres": ["Action", "Comedy", "Fantasy", "School", "Shounen"]
    },
    {
        "title": "Mushoku Tensei: Isekai Ittara Honki Dasu",
        "synopsis": "Seorang pria Jepang berusia 34 tahun yang telah membuang seluruh hidupnya sebagai hikikomori — tidak bekerja, tidak bermasyarakat, menyia-nyiakan semua kesempatan — mati dalam kecelakaan saat melakukan satu-satunya tindakan heroik dalam hidupnya. Ia bereinkarnasi sebagai Rudeus Greyrat, bayi di dunia sihir dan fantasi, dengan mempertahankan semua memori dari kehidupan sebelumnya. Kali ini, ia bertekad untuk tidak menyia-nyiakan hidupnya. Dengan memulai belajar sihir sejak bayi dan memanfaatkan semua pengetahuan dan penyesalan dari kehidupan sebelumnya, Rudeus tumbuh menjadi penyihir luar biasa. Anime ini dikenal dengan world-building yang kaya, karakter yang kompleks, dan penggambaran pertumbuhan personal yang jujur — termasuk kelemahan dan masa lalu gelap sang protagonis.",
        "rating": 8.3,
        "genres": ["Adventure", "Drama", "Fantasy", "Magic", "Romance", "Isekai", "Seinen"]
    },
    {
        "title": "Jujutsu Kaisen",
        "synopsis": "Yuji Itadori adalah siswa SMA dengan fisik luar biasa yang tergabung dalam klub okultisme untuk mengisi waktu luang. Saat temannya membuka kotak segel berisi jari kutukan Ryoumen Sukuna — Raja Kutukan terkuat dalam sejarah — Yuji menelan jari tersebut untuk melindungi orang lain, dan menjadi wadah Sukuna. Alih-alih dieksekusi seketika, Jujutsu Society memutuskan memanfaatkan Yuji sebagai 'wadah' untuk mengumpulkan semua 20 jari Sukuna sebelum kemudian mengeksekusinya. Bersama gurunya Gojo Satoru yang eksentrik namun sangat kuat, dan rekan-rekan sorgotannya, Yuji terjun ke dunia kutukan, dukun jujutsu, dan konspirasi yang melibatkan hidup dan mati jutaan jiwa.",
        "rating": 8.7,
        "genres": ["Action", "Fantasy", "Horror", "School", "Supernatural", "Shounen"]
    },
    {
        "title": "Tensei Shitara Slime Datta Ken",
        "synopsis": "Satoru Mikami, salaryman Jepang berusia 37 tahun yang biasa-biasa saja, ditikam secara acak di jalanan dan mati. Ia bereinkarnasi di dunia fantasi sebagai — slime. Makhluk paling lemah dalam hierarki monster fantasi. Namun slime ini memiliki kemampuan istimewa Predator yang memungkinkannya menyerap kekuatan, pengetahuan, dan bentuk makhluk yang ia telan. Setelah menyerap naga kuno Veldora yang terjebak dalam barrier, ia mendapat nama Rimuru Tempest. Dengan kepribadian santai, kebijaksanaan orang dewasa, dan kekuatan yang terus berkembang, Rimuru membangun komunitas monster yang damai — menerima goblin, serigala, ogre, dan berbagai ras — perlahan membangun bangsa yang berprinsip kesetaraan dan perdamaian di dunia yang penuh konflik.",
        "rating": 8.1,
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Isekai", "Magic", "Shounen"]
    },
    {
        "title": "Mob Psycho 100",
        "synopsis": "Shigeo Kageyama, dipanggil Mob, adalah siswa SMP yang tampak biasa namun menyimpan kekuatan psikis yang luar biasa — mungkin yang terkuat yang pernah ada. Untuk menghindari merusak lingkungan sekitarnya, ia secara konstan menekan seluruh emosinya, beroperasi pada persentase yang selalu dipantau. Saat emosi mencapai 100%, ledakan kekuatan yang tidak terkontrol terjadi. Ia bekerja magang pada Reigen Arataka, penipu yang mengklaim sebagai psikis namun sebenarnya tidak punya kemampuan apapun, untuk belajar mengendalikan kekuatannya. Di balik komedi dan aksi yang memukau, Mob Psycho adalah eksplorasi mendalam tentang pertumbuhan pribadi — bahwa kekuatan sejati bukan dari kemampuan supranatural, melainkan dari mengenal diri sendiri dan membangun hubungan yang tulus.",
        "rating": 8.9,
        "genres": ["Action", "Comedy", "Drama", "Mystery", "Psychological", "School", "Slice of Life", "Super Power", "Supernatural", "Shounen"]
    },
    {
        "title": "Mahou Shoujo Madoka Magica",
        "synopsis": "Madoka Kaname adalah siswi SMP yang menjalani kehidupan normal dengan keluarga yang hangat dan sahabat-sahabat yang menyayanginya. Suatu malam ia bermimpi melihat seorang gadis berjuang sendirian melawan monster di tempat yang aneh. Keesokan harinya, gadis itu — Homura Akemi — muncul sebagai murid baru di kelasnya dan memperingatkan Madoka untuk tidak mengubah apa pun dalam hidupnya. Kemudian muncul Kyubey, makhluk imut yang menawarkan kontrak: jadilah Magical Girl, dapatkan satu keinginan apapun terkabulkan, dan bertarung melawan Witch sebagai imbalannya. Tawaran yang tampak sempurna ini menyimpan kebenaran yang jauh lebih gelap dan tragis dari yang bisa dibayangkan Madoka. Anime ini merevolusi genre Magical Girl dengan mempertanyakan fondasi-fondasi moralnya.",
        "rating": 8.4,
        "genres": ["Drama", "Horror", "Magic", "Mystery", "Psychological", "Thriller", "Sci-Fi", "Supernatural", "Shoujo"]
    },
    {
        "title": "Koe no Katachi",
        "synopsis": "Shouya Ishida di SD pernah menjadi pembully utama Shouko Nishimiya, siswi tuli yang baru pindah ke kelasnya. Ia dan teman-temannya mengejek, mengambil alat bantu dengar Shouko, dan membuatnya menderita setiap hari — sampai Shouko akhirnya pindah sekolah dan Shouya sendiri menjadi sasaran bully dari teman-temannya yang kemudian menyangkal semua yang mereka lakukan. Bertahun-tahun Shouya hidup dalam rasa bersalah yang mendalam, menjauhi semua orang dan berencana mengakhiri hidupnya setelah melunasi semua hutang budi pada ibunya. Sebelum itu, ia ingin meminta maaf pada Shouko. Pertemuan kembali mereka membuka luka lama sekaligus kemungkinan penyembuhan — bagi keduanya dan semua yang pernah terlibat dalam kejadian masa kecil itu.",
        "rating": 9.0,
        "genres": ["Drama", "Romance", "School", "Slice of Life", "Shounen"]
    },
    {
        "title": "Sousou no Frieren",
        "synopsis": "Frieren adalah penyihir elf yang telah hidup selama lebih dari seribu tahun. Sepuluh tahun lalu, ia bersama partai pahlawan — Himmel sang pahlawan, Heiter sang pendeta, dan Eisen sang pejuang — mengalahkan Raja Iblis dan menyelamatkan dunia. Bagi Frieren yang berumur panjang, sepuluh tahun bersama mereka hanyalah sekejap. Tapi saat Himmel meninggal karena usia, Frieren menangis dan menyesal tidak pernah benar-benar mengenal sahabat yang telah bersamanya selama petualangan itu. Ia memulai perjalanan baru — mengunjungi tempat-tempat yang pernah mereka kunjungi bersama, menemui orang-orang yang pernah mereka bantu, dan belajar untuk memahami makna dari hubungan singkat dengan manusia yang berumur jauh lebih pendek dari dirinya. Sebuah refleksi puitis tentang waktu, kehilangan, dan arti dari kebersamaan.",
        "rating": 9.0,
        "genres": ["Adventure", "Drama", "Fantasy", "Mystery", "Shounen"]
    },
    {
        "title": "Summertime Render",
        "synopsis": "Shinpei Ajiro kembali ke Pulau Hitogashima — pulau terpencil tempat ia dibesarkan — untuk menghadiri pemakaman Ushio Kofune, sahabat masa kecilnya yang mati tenggelam secara misterius. Kecurigaan muncul saat ada tanda-tanda Ushio sebenarnya dibunuh. Sebelum Shinpei bisa menyelidiki lebih jauh, ia sendiri dibunuh — dan terbangun kembali di hari kedatangannya di pulau itu. Ia menyadari kemampuannya untuk kembali ke saat kematiannya. Di balik keindahan musim panas pulau kecil itu, tersembunyi makhluk supernatural bernama Shadow yang mampu menyalin bentuk manusia sempurna dan membunuh dengan brutal. Shinpei harus menggunakan kemampuan loop-nya untuk menemukan cara menyelamatkan semua orang yang ia cintai dari ancaman yang semakin besar dan kompleks.",
        "rating": 8.9,
        "genres": ["Action", "Drama", "Horror", "Mystery", "Psychological", "Romance", "Supernatural", "Thriller", "Shounen"]
    },
    {
        "title": "Chainsaw Man",
        "synopsis": "Denji adalah pemuda miskin yang hidup dengan hutang warisan ayahnya kepada yakuza. Untuk bertahan hidup, ia bekerja sebagai pemburu iblis bersama Pochita, anjingnya yang sebenarnya adalah Chainsaw Devil. Saat dibunuh oleh yakuza yang berkhianat, Pochita menyatu dengan hati Denji dan menghidupkannya kembali sebagai Chainsaw Man — manusia yang bisa mengubah bagian tubuhnya menjadi gergaji mesin. Ia direkrut oleh Public Safety Devil Hunter Division di bawah kendali Makima yang misterius dan menawan. Chainsaw Man adalah manga/anime yang berani mendobrak konvensi dengan narasi yang tidak bisa diprediksi, karakter-karakter yang sangat manusiawi dalam cara yang mengejutkan, dan eksplorasi trauma, kesenangan sederhana, dan kematian dengan cara yang tidak lazim.",
        "rating": 8.6,
        "genres": ["Action", "Adventure", "Fantasy", "Horror", "Supernatural", "Seinen"]
    },
    {
        "title": "Dan Da Dan",
        "synopsis": "Momo Ayase adalah gadis SMA yang percaya pada hantu karena neneknya adalah medium spiritual, namun tidak percaya alien. Ken Takakura alias Okarun percaya pada alien namun tidak percaya hantu. Keduanya bertaruh — Momo pergi ke gedung yang diyakini berhantu, Okarun pergi ke lokasi penampakan alien. Keduanya mengalami hal supernatural secara bersamaan: Okarun dirasuki oleh kekuatan roh purba dan Momo hampir diculik alien. Kekacauan itu menjadi awal petualangan supranatural yang tidak ada habisnya — alien Serpo, Turbo Granny, dan berbagai entitas aneh lainnya — sambil di antara keduanya tumbuh perasaan yang tidak mereka duga. Anime yang menggabungkan aksi energik, komedi absurd, momen romantis menggemaskan, dan horror yang genuine dalam satu paket yang unik.",
        "rating": 8.6,
        "genres": ["Action", "Comedy", "Horror", "Mystery", "Romance", "Sci-Fi", "Supernatural", "Shounen"]
    },
    {
        "title": "Kage no Jitsuryokusha ni Naritakute!",
        "synopsis": "Minoru Kagenou adalah anak laki-laki yang terobsesi menjadi 'penguasa bayangan' — figur misterius di balik layar yang mengendalikan segalanya tanpa diketahui siapapun. Setelah bereinkarnasi di dunia fantasi sebagai Cid Kagenou, ia mendirikan Shadow Garden — organisasi yang ia kira hanya permainannya sendiri, namun tanpa sadar ia terus mengarang organisasi jahat bernama Diabolos Cult yang ternyata benar-benar ada di dunia itu. Setiap kali Cid berlagak dramatis sebagai 'Shadow' dalam apa yang ia kira skenario karangan, ternyata semua itu nyata dan konsekuensinya sangat serius bagi dunia. Komedi meta jenius tentang seseorang yang terlalu asyik bermain peran sampai tidak sadar bahwa ia benar-benar menjadi karakter yang ia mainkan.",
        "rating": 8.3,
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Mystery", "Isekai", "Harem", "Seinen"]
    },
    {
        "title": "Kobayashi-san Chi no Maid Dragon",
        "synopsis": "Kobayashi, programmer wanita yang hidup sendirian di apartemen kecilnya, suatu malam saat mabuk menemukan Tohru — naga betina dari dunia lain yang terluka — dan mengundangnya tinggal bersamanya sebagai pembantu. Keesokan paginya Tohru benar-benar muncul di depan pintunya dalam wujud manusia dengan seragam pembantu. Tohru yang berasal dari fraksi iblis dan memiliki kekuatan luar biasa kini mengurus rumah Kobayashi dengan sepenuh hati — meski beberapa metodenya sangat tidak konvensional. Perlahan naga-naga lain mulai berdatangan ke dunia manusia. Anime slice of life yang hangat ini adalah tentang keluarga non-konvensional yang terbentuk antara manusia dan naga, tentang perbedaan yang melampaui ras dan dunia, dan tentang apa artinya benar-benar menjadi bagian dari kehidupan seseorang.",
        "rating": 8.0,
        "genres": ["Comedy", "Fantasy", "Slice of Life", "Supernatural", "Seinen"]
    },
    {
        "title": "One Piece",
        "synopsis": "Di era bajak laut, Gol D. Roger sang Raja Bajak Laut mengungkapkan sebelum dieksekusi bahwa ia meninggalkan semua hartanya di satu titik di dunia — One Piece — dan siapapun yang menemukannya berhak menjadi Raja Bajak Laut berikutnya. Monkey D. Luffy, bocah yang memakan Buah Iblis Gomu-gomu dan tubuhnya menjadi karet, bercita-cita menjadi Raja Bajak Laut. Ia berlayar sendirian dan perlahan mengumpulkan nakama-nakama yang setia: Zoro sang pendekar pedang, Nami sang navigator, Usopp sang penembak jitu, Sanji sang koki, Chopper sang dokter, Robin sang arkeolog, Franky sang tukang kapal, Brook sang musisi, dan Jinbei sang helmsman. Petualangan epik yang sudah berjalan lebih dari 25 tahun ini adalah tentang persahabatan, kebebasan, dan mimpi yang tidak pernah mati.",
        "rating": 8.7,
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Supernatural", "Shounen"]
    },
    {
        "title": "Tokyo Ghoul",
        "synopsis": "Tokyo hidup dalam bayangan teror ghoul — makhluk yang menyerupai manusia namun hanya bisa bertahan dengan memakan daging manusia. Ken Kaneki, mahasiswa pemalu yang gemar membaca, berkencan dengan gadis impiannya Rize yang ternyata adalah ghoul. Setelah diserang, ia selamat melalui transplantasi organ Rize yang menjadikannya half-ghoul pertama yang pernah ada. Kini ia harus menghadapi kebutuhan akan daging manusia yang bertentangan dengan moralnya, sambil berusaha diterima di komunitas ghoul. Terjepit antara dua dunia yang saling membenci dan menghancurkan satu sama lain, Ken harus menemukan jalannya sendiri. Serial ini mengeksplorasi pertanyaan tentang kemanusiaan, identitas, dan siapa sebenarnya yang menjadi monster dalam konflik ini.",
        "rating": 7.8,
        "genres": ["Action", "Drama", "Fantasy", "Horror", "Mystery", "Psychological", "Supernatural", "Seinen"]
    },
    {
        "title": "Ouran Koukou Host Club",
        "synopsis": "Haruhi Fujioka adalah siswi baru berbeasiswa di SMA Ouran yang sangat elit, diisi anak-anak dari keluarga super kaya. Saat mencari tempat tenang untuk belajar, ia masuk ke ruangan yang ternyata adalah markas Host Club — grup enam siswa tampan yang menghibur siswi-siswi dengan pesona mereka. Tidak sengaja Haruhi memecahkan vas antik seharga 8 juta yen dan terpaksa bekerja sebagai host untuk melunasinya — dengan identitas gender perempuannya yang tidak diketahui para anggota awalnya. Shoujo klasik ini adalah romcom yang cerdas dengan kritik sosial tentang kesenjangan kelas, sambil menghadirkan ensemble karakter yang lovable dengan dinamika kelompok yang menggemaskan dan momen-momen romantis yang organik.",
        "rating": 8.2,
        "genres": ["Comedy", "Drama", "Romance", "School", "Shoujo", "Slice of Life"]
    },
        {
        "title": "Azur Lane",
        "synopsis": "Di dunia di mana lautan dikuasai oleh ancaman alien misterius bernama Siren, armada kapal perang dari berbagai negara dipersonifikasikan sebagai gadis-gadis cantik dengan kemampuan tempur luar biasa. Empat faksi besar — Eagle Union, Royal Navy, Sakura Empire, dan Iron Blood — awalnya bersatu dalam Azur Lane untuk melawan Siren. Namun setelah ancaman itu berkurang, perpecahan muncul di antara mereka. Sakura Empire dan Iron Blood memisahkan diri membentuk Crimson Axis karena perbedaan ideologi tentang cara memanfaatkan teknologi Siren. Perang saudara di antara para shipgirl pun tidak bisa dihindari. Di tengah konflik ini, Enterprise — shipgirl paling kuat dari Eagle Union — menyimpan rahasia misterius yang berkaitan dengan visi-visi gelap tentang masa depan.",
        "rating": 6.8,
        "genres": ["Action", "Military", "Sci-Fi", "Game"]
    },
    {
        "title": "Valkyrie no Shokutaku",
        "synopsis": "Valkyrie, sang pejuang legendaris dari mitologi Norse yang seharusnya memimpin para pahlawan di medan perang Valhalla, tiba-tiba mendapati dirinya bekerja sebagai pelayan di sebuah restoran keluarga biasa di Jepang modern. Bersama berbagai dewa dan makhluk mitologi lainnya yang juga bekerja di sana, Valkyrie harus menghadapi tantangan terbesar dalam hidupnya: melayani pelanggan, mengambil pesanan, dan berurusan dengan jam sibuk tanpa menggunakan kekuatan perangnya. Serial komedi pendek ini mengambil ide sederhana tentang tokoh-tokoh mitologi yang terperangkap dalam situasi duniawi yang paling biasa dan memeras habis humor dari kontras tersebut.",
        "rating": 6.5,
        "genres": ["Comedy", "Fantasy", "Slice of Life", "Seinen"]
    },
    {
        "title": "Mujaki no Rakuen",
        "synopsis": "Shouta Tanaka adalah pria dewasa yang merasa hidupnya gagal total — karir tidak sukses, tidak punya pacar, dan terus-terusan kalah bersaing dengan teman-teman SMA-nya yang kini sukses. Di reuni SMA, ia jatuh dan terbentur kepala, lalu terbangun kembali di masa ketika ia masih kelas 5 SD. Di sana ia bertemu kembali dengan teman-teman masa kecilnya yang kini masih anak-anak — termasuk gadis-gadis yang di masa depan tumbuh menjadi wanita cantik. Dengan memori orang dewasa, Shouta berusaha memperbaiki berbagai hubungan dan keputusan yang dulu ia sesalkan, sambil mencoba tidak berlaku tidak pantas dengan pengetahuan yang ia miliki tentang masa depan mereka masing-masing.",
        "rating": 6.5,
        "genres": ["Comedy", "Ecchi", "Romance", "Seinen"]
    },
    {
        "title": "Ore no Kanojo to Osananajimi ga Shuraba Sugiru",
        "synopsis": "Eita Kidou adalah siswa serius yang bersumpah tidak akan terlibat cinta karena trauma akibat perceraian orang tuanya dan ingin fokus mendapat beasiswa kedokteran. Hidupnya berubah saat Masuzu Natsukawa — gadis paling cantik di sekolah yang tidak tertarik dengan romansa — memeras Eita dengan buku harian chuunibyou-nya yang memalukan dan memaksanya berpacaran palsu untuk menghindari perhatian pria. Masalah bertambah pelik saat Chiwa Harusaki, teman masa kecil Eita yang menyukainya sejak lama, mendeklarasikan persaingan. Kemudian muncul lagi Ai Fuyuumi dan Himari Jougasaki yang masing-masing punya klaim atas Eita. Percekcokan empat gadis ini menjadi 'shuraba' (medan pertempuran) yang tidak ada habisnya dalam kehidupan Eita.",
        "rating": 7.1,
        "genres": ["Comedy", "Harem", "Romance", "School", "Shounen"]
    },
    {
        "title": "Fugou Keiji: Balance:Unlimited",
        "synopsis": "Daisuke Kanbe adalah detektif baru yang dipindahkan ke divisi kasus tak terpecahkan setelah insiden kontroversial. Yang membuatnya berbeda dari detektif lain bukan kemampuan investigasinya — melainkan kekayaannya yang tidak terbatas. Ia menyelesaikan masalah dengan cara paling sederhana: membayar. Menabrak mobil polisi? Dibayar. Merusak properti saat mengejar tersangka? Dibayar. Dipasangkan dengannya adalah Haru Kato, detektif idealis yang sangat menjunjung etika dan keadilan serta tidak bisa mentolerir cara Kanbe yang menggunakan uang untuk mengatasi segalanya. Dinamika antara dua karakter yang bertolak belakang ini menciptakan komedi dan drama yang menarik, sambil secara perlahan mengungkap motivasi tersembunyi Kanbe di balik semua kekayaannya.",
        "rating": 7.4,
        "genres": ["Action", "Comedy", "Mystery", "Seinen"]
    },
    {
        "title": "Kore wa Zombie Desu ka?",
        "synopsis": "Ayumu Aikawa adalah siswa SMA biasa yang dibunuh oleh serial killer misterius. Ia kemudian dibangkitkan sebagai zombie oleh Eucliwood Hellscythe, necromancer cantik yang tidak pernah berbicara karena kekuatan suaranya terlalu berbahaya. Kini Ayumu hidup sebagai zombie — tidak bisa mati lagi namun sangat lemah terhadap sinar matahari. Saat pertemuan tidak sengaja dengan Haruna, Magical Garment Girl, berakhir dengan Ayumu menyerap kemampuan sihirnya secara tidak sengaja, ia terpaksa mengambil alih peran Magical Girl — dalam kostum yang sangat tidak pantas untuk tubuh laki-lakinya. Kini ia harus menjalani kehidupan double sebagai zombie Magical Girl sambil mencari pembunuhnya dan menghadapi ancaman dari dunia lain.",
        "rating": 7.4,
        "genres": ["Action", "Comedy", "Ecchi", "Fantasy", "Harem", "Magic", "Supernatural", "Seinen"]
    },
    {
        "title": "Uchi no Maid ga Uzasugiru!",
        "synopsis": "Tsubame Kamoi adalah mantan anggota Japan Self-Defense Force dengan fisik dan kemampuan bertarung luar biasa. Ia melamar pekerjaan sebagai pembantu rumah tangga di rumah Yasuhiro Takanashi — seorang ayah yang membesarkan putri kecilnya Misha seorang diri setelah istrinya meninggal. Misha adalah anak campuran Jepang-Rusia berambut pirang yang sangat mirip dengan idol idola Tsubame di masa lalu. Tsubame langsung jatuh cinta pada kecantikan Misha dan menjadi pembantu dengan obsesi yang jauh melampaui batas profesional — selalu berusaha memeluk, mencium, dan bermanjaan dengan Misha. Misha yang cerdas dan waspada selalu menggagalkan setiap usaha Tsubame dengan cara yang semakin kreatif dan lucu.",
        "rating": 7.4,
        "genres": ["Comedy", "Slice of Life", "Seinen"]
    },
    {
        "title": "Hinamatsuri",
        "synopsis": "Yoshifumi Nitta adalah anggota yakuza muda yang hidup rapi dan menyukai keramik antik. Hidupnya berubah total saat sebuah kapsul misterius jatuh dari langit dan menimpa kepalanya, dan dari dalamnya keluar anak perempuan bernama Hina yang memiliki kekuatan telekinesis luar biasa namun sikap manja dan tidak bisa apa-apa dalam kehidupan sehari-hari. Jika kekuatannya tidak disalurkan secara rutin, ia akan meledak — sehingga Nitta terpaksa merawatnya. Kisah ini tidak hanya mengikuti hubungan ayah-anak yang tidak biasa antara Nitta dan Hina, tapi juga kisah mengharukan Anzu — anak psikis lain — yang belajar keras hidup mandiri, dan Hitomi — teman sekolah Hina yang tidak sengaja terseret menjadi bartender profesional.",
        "rating": 8.2,
        "genres": ["Comedy", "Drama", "Sci-Fi", "Seinen", "Slice of Life", "Supernatural"]
    },
    {
        "title": "Mairimashita! Iruma-kun",
        "synopsis": "Iruma Suzuki adalah anak 14 tahun yang sejak kecil selalu dieksploitasi oleh orang tuanya yang tidak bertanggung jawab. Suatu hari orang tuanya menjualnya kepada iblis Sullivan, salah satu iblis paling kuat di dunia iblis, yang sudah lama menginginkan cucu. Sullivan mengadopsi Iruma dengan penuh kasih sayang dan mendaftarkannya ke Babyls — sekolah iblis bergengsi. Di sana Iruma harus bertahan tanpa ketahuan bahwa ia manusia biasa tanpa sihir apapun di tengah para iblis, karena manusia yang ketahuan akan dimakan. Beruntung Iruma memiliki 'keberuntungan setan' yang selalu menyelamatkannya dari situasi berbahaya. Kisah heartwarming tentang anak yang akhirnya mendapatkan keluarga dan teman-teman sejati untuk pertama kalinya.",
        "rating": 7.9,
        "genres": ["Comedy", "Fantasy", "School", "Supernatural", "Shounen"]
    },
    {
        "title": "The God of High School",
        "synopsis": "Jin Mori adalah remaja 17 tahun yang sangat mencintai taekwondo dan selalu mencari lawan yang kuat. Ia diundang untuk berpartisipasi dalam God of High School — turnamen martial arts nasional bergengsi yang pesertanya adalah pelajar SMA terkuat dari seluruh Korea. Pemenang akan mendapat satu keinginan apapun terkabulkan. Bersama Yoo Mira yang menguasai seni pedang kuno dan Han Daewi yang bertarung demi biaya pengobatan sahabatnya, Mori melewati berbagai pertarungan sengit. Namun di balik turnamen ini tersimpan agenda yang jauh lebih besar dan gelap — berkaitan dengan kekuatan dewa-dewa kuno yang pernah menguasai dunia dan kini perlahan bangkit kembali melalui para petarung manusia.",
        "rating": 7.4,
        "genres": ["Action", "Adventure", "Fantasy", "Martial Arts", "Supernatural", "Shounen"]
    },
    {
        "title": "Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru",
        "synopsis": "Seiya Ryuuguin dipanggil ke dunia fantasi oleh dewi Ristarte untuk menjadi pahlawan yang menyelamatkan dunia Gaeabrande yang terancam oleh kekuatan gelap. Masalahnya, Seiya adalah orang yang paling berhati-hati yang pernah ada — ia tidak akan menyerang musuh sebelum memastikan ia sudah siap sepenuhnya, bahkan untuk goblin level 1 sekalipun ia akan menggunakan kemampuan penuh. Ia berlatih selama berhari-hari sebelum keluar dari kota pertama, membeli persediaan dalam jumlah absurd untuk berjaga-jaga, dan selalu meragukan kemenangan meski sudah sangat dominan. Ristarte yang frustrasi terus-terusan terseret dalam ritme overpreparation Seiya yang ekstrem — namun cara hati-hati itulah yang ternyata paling efektif menghadapi dunia yang jauh lebih berbahaya dari perkiraan.",
        "rating": 7.5,
        "genres": ["Adventure", "Comedy", "Fantasy", "Parody", "Isekai"]
    },
    {
        "title": "Uchi no Ko no Tame naraba, Ore wa Moshikashitara Maou mo Taoseru kamo Shirenai",
        "synopsis": "Dale Reki adalah adventurer muda yang sudah cukup terkenal dan berbakat. Suatu hari saat menyelesaikan quest di hutan berbahaya, ia menemukan seorang anak iblis kecil bernama Latina yang sendirian, lemah, dan salah satu tanduknya patah — tanda bahwa ia adalah anak buangan dari kaumnya. Dale yang seharusnya tidak peduli dengan urusan orang lain spontan memutuskan untuk membawa Latina pulang dan merawatnya. Tidak punya pengalaman mengurus anak sama sekali, Dale belajar sambil jalan bagaimana menjadi figur ayah yang baik. Latina tumbuh menjadi anak yang lembut dan penyayang, meskipun masa lalunya menyimpan rahasia yang akan mengguncang kehidupan tenang yang telah mereka bangun bersama.",
        "rating": 7.3,
        "genres": ["Adventure", "Fantasy", "Slice of Life", "Seinen"]
    },
    {
        "title": "Ijiranaide, Nagatoro-san",
        "synopsis": "Senpai — nama aslinya tidak pernah disebutkan — adalah siswa SMA kelas dua yang penyendiri, pemalu, dan gemar menggambar manga di ruang klub yang selalu ia gunakan sendirian. Hidupnya yang tenang berubah saat Nagatoro Hayase, siswi kelas satu yang aktif dan jail, menemukan manga buatannya dan mulai sering datang ke ruang klub hanya untuk menggoda dan menjahilinya. Nagatoro memanggil senpai dengan sebutan merendahkan, mengomentari karyanya, dan menciptakan berbagai situasi memalukan — namun anehnya, ia juga yang paling sering membantu senpai dan melindunginya dari orang lain. Di balik kenakalan Nagatoro tersimpan perasaan yang perlahan-lahan ia sendiri tidak bisa menyangkali.",
        "rating": 7.6,
        "genres": ["Comedy", "Romance", "School", "Slice of Life", "Ecchi", "Seinen"]
    },
    {
        "title": "Maou Gakuin no Futekigousha",
        "synopsis": "Anos Voldigoad adalah Raja Iblis legendaris yang 2000 tahun lalu bersepakat untuk mati demi mengakhiri perang antara iblis, manusia, dan dewa — dengan keyakinan ia akan bereinkarnasi suatu hari. Ia bereinkarnasi sesuai rencana, namun terkejut menemukan bahwa sejarah tentang dirinya telah diputarbalikkan secara sistematis. Nama aslinya telah diganti dengan 'Avos Dilhevia', dan keturunannya tidak mengenalinya sama sekali. Anos mendaftar ke Maou Gakuin — akademi yang didirikan untuk menunggu reinkarnasi sang Raja Iblis — hanya untuk dicap sebagai 'yang tidak sesuai' karena kekuatannya yang benar-benar melampaui semua standar. Ia harus membuktikan identitas aslinya sambil mengungkap konspirasi di balik pemalsuan sejarah.",
        "rating": 7.4,
        "genres": ["Action", "Adventure", "Fantasy", "Magic", "School", "Harem", "Supernatural", "Shounen"]
    },
    {
        "title": "Rokudenashi Majutsu Koushi to Akashic Records",
        "synopsis": "Akademi Alzano Imperial Magic Academy adalah sekolah sihir bergengsi yang mencetak penyihir-penyihir terbaik. Sistine Fibel dan Rumia Tingel terkejut saat guru sihir favorit mereka tiba-tiba mengundurkan diri dan digantikan oleh Glenn Radars — pria muda acak-acakan yang di hari pertama mengajar langsung tidur di kelas dan menyuruh muridnya belajar mandiri. Glenn tampak tidak kompeten dan malas total. Namun saat sekelompok teroris menyerang sekolah, semua orang menyaksikan sisi lain Glenn yang sama sekali berbeda — kemampuan bertarung luar biasa dan taktik jenius yang tidak sesuai dengan penampilannya. Di balik sikap malasnya tersimpan masa lalu gelap sebagai agen rahasia kekaisaran yang meninggalkan trauma mendalam.",
        "rating": 7.3,
        "genres": ["Action", "Comedy", "Fantasy", "Magic", "School", "Ecchi"]
    },
    {
        "title": "Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta",
        "synopsis": "Seorang gadis otaku tersadar dan menyadari bahwa ia telah bereinkarnasi sebagai Katarina Claes — villain utama dari game otome favoritnya Fortune Lover. Masalahnya, semua ending dalam game tersebut berakhir buruk bagi Katarina: diasingkan dari negeri atau dibunuh oleh karakter-karakter lainnya. Dengan memori penuh tentang alur game, Katarina bertekad mengubah takdirnya dengan cara mengubah kepribadiannya dari villain menjadi orang baik — agar tidak ada yang mau mengasingkan atau membunuhnya. Namun upaya polosnya untuk berteman dengan semua orang justru membuat semua karakter — baik target romansa laki-laki maupun perempuan — jatuh cinta padanya tanpa ia sadari, menciptakan harem yang tidak pernah ia rencanakan.",
        "rating": 7.7,
        "genres": ["Comedy", "Fantasy", "Romance", "Harem", "Magic", "School", "Isekai", "Shoujo"]
    },
    {
        "title": "Back Street Girls: Gokudolls",
        "synopsis": "Kentarou, Ryou, dan Kazuhiko adalah tiga anggota yakuza yang melakukan kesalahan fatal yang mengecewakan bos mereka. Diberikan pilihan antara kematian atau operasi perubahan kelamin di Thailand diikuti karir sebagai idol perempuan, mereka terpaksa memilih yang kedua. Kini mereka tampil sebagai Gokudolls — trio idol cantik yang sangat populer di Jepang. Di balik panggung, mereka masih berbicara kasar seperti yakuza, tidak bisa bergerak luwes, dan terus menderita dalam kostum idol yang tidak nyaman. Bos mereka yang sadis terus mengawasi dan memaksa mereka tampil sempurna. Komedi gelap yang mengeksplorasi absurditas industri idol Jepang dari perspektif paling tidak terduga.",
        "rating": 6.9,
        "genres": ["Comedy", "Music", "Seinen"]
    },
    {
        "title": "Asobi Asobase",
        "synopsis": "Hanako Honda, Olivia, dan Kasumi Nomura adalah tiga siswi SMP yang tampaknya biasa namun sama sekali tidak biasa. Hanako yang energetik dan ekspresif berlebihan, Olivia yang sebenarnya lahir dan besar di Jepang namun pura-pura tidak bisa bahasa Jepang demi terlihat keren, dan Kasumi yang serius namun mudah terseret kekacauan. Ketiganya mendirikan Pastimers Club untuk bermain berbagai permainan setelah sekolah. Yang membuat anime ini menonjol adalah ekspresi wajah karakter yang ekstrem dan sangat overreacted — dari momen paling biasa sekalipun bisa menghasilkan ekspresi yang terlihat seperti adegan horror. Humor gelap yang tidak terduga dan timing komedi yang presisi menjadikannya salah satu anime komedi terbaik.",
        "rating": 7.9,
        "genres": ["Comedy", "School", "Slice of Life", "Seinen"]
    },
    {
        "title": "Xian Wang de Richang Shenghuo",
        "synopsis": "Wang Ling adalah siswa SMA yang tampak biasa namun sebenarnya memiliki kekuatan yang melampaui semua dewa, iblis, dan makhluk legendaris yang pernah ada. Ia hanya ingin menjalani kehidupan normal — makan mi instan, tidur siang, dan tidak menarik perhatian. Masalahnya, kekuatannya terus bocor secara tidak sengaja: napas biasanya bisa melubangi tembok, bersin bisa menghancurkan bangunan, dan saat ia berjalan, makhluk-makhluk kuat otomatis menyingkir ketakutan. Gurunya yang tahu kemampuan aslinya berusaha keras merahasiakannya dari dunia. Donghua (anime China) ini adalah parodi isekai/xuanxuan yang lucu tentang seseorang yang terlalu overpowered hingga hal paling sederhana pun menjadi masalah besar.",
        "rating": 7.3,
        "genres": ["Action", "Comedy", "Fantasy", "School", "Super Power"]
    },
    {
        "title": "Tenkuu Shinpan",
        "synopsis": "Yuri Honjo adalah siswi SMA yang tiba-tiba terbangun sendirian di gedung pencakar langit yang tampak ditinggalkan sepenuhnya. Kota di bawahnya kosong melompong. Sebelum bisa memahami situasinya, ia langsung diserang oleh seseorang yang mengenakan topeng tersenyum menyeramkan dan bersenjata kapak — disebut Masker. Hanya insting bertahan hidup yang kuat membuatnya lolos. Ia mencari kakaknya yang ternyata juga terjebak di gedung lain. Bertahan hidup sambil mencari jalan turun dan menemukan kebenaran tentang apa tempat aneh ini. Thriller survival yang intens dengan berbagai jenis Masker yang memiliki kepribadian dan senjata berbeda, serta misteri besar tentang siapa yang menciptakan dan mengoperasikan arena kematian berbentuk kota ini.",
        "rating": 6.7,
        "genres": ["Action", "Horror", "Mystery", "Psychological", "Thriller", "Seinen"]
    },
    {
        "title": "Grand Blue",
        "synopsis": "Iori Kitahara pindah ke kota tepi pantai untuk berkuliah dan tinggal di toko selam milik pamannya, Grand Blue. Dengan semangat tinggi ia membayangkan kehidupan kampus yang ideal — berteman dengan mahasiswa keren, berkencan dengan gadis cantik, dan menikmati masa muda. Kenyataannya, ia langsung terseret ke dalam dunia anggota Diving Club Peek-a-Boo yang tradisi utamanya adalah minum alkohol dalam jumlah absurd sambil telanjang. Meski awalnya menolak, Iori perlahan menjadi bagian dari kekacauan itu. Di luar kegilaan club, ada juga romance yang berkembang perlahan antara Iori dan Chisa, sepupunya yang serius dan berdedikasi pada menyelam sungguhan. Komedi yang sangat dewasa dengan situasi memalukan yang terus bereskalasi.",
        "rating": 8.4,
        "genres": ["Comedy", "Ecchi", "Romance", "Seinen", "Slice of Life", "Sports"]
    },
    {
        "title": "Kyou kara Ore wa!!",
        "synopsis": "Takashi Mitsuhashi dan Shinji Itou adalah dua siswa yang kebetulan pindah ke sekolah yang sama pada hari yang sama. Keduanya memutuskan bahwa ini adalah kesempatan emas untuk memulai kehidupan baru sebagai delinquent tangguh. Mitsuhashi yang licik dan oportunistik mengubah rambutnya menjadi pirang mencolok, sementara Itou yang sebenarnya lebih serius memilih gaya delinquent klasik. Mereka tidak punya background bertarung yang kuat tapi terus-menerus terlibat dalam konflik dengan geng-geng sekolah lain. Mitsuhashi yang pengecut namun sangat cerdik selalu menemukan cara curang namun efektif untuk menang, sementara Itou lebih mengandalkan keberanian. Live action klasik tahun 90an yang diadaptasi jadi anime — penuh nostalgia dan humor yang timeless.",
        "rating": 8.1,
        "genres": ["Action", "Comedy", "Romance", "School", "Seinen"]
    },
    {
        "title": "Ao no Exorcist",
        "synopsis": "Rin Okumura dan saudara kembarnya Yukio dibesarkan oleh Pastor Fujimoto, exorcist handal, tanpa pernah mengetahui siapa ayah biologis mereka sebenarnya. Saat Rin berusia 15 tahun, kekuatan iblis dalam dirinya tiba-tiba bangkit dan terungkaplah kebenaran yang selama ini disembunyikan: ia adalah putra Iblis Raja Lucifer sendiri. Setelah kematian tragis sang Pastor, Rin bertekad menjadi Paladin — exorcist terkuat — untuk mengalahkan Lucifer dengan kekuatannya sendiri. Ia masuk ke True Cross Academy, sekolah khusus exorcist, dan harus menyembunyikan identitasnya sebagai anak iblis dari teman-temannya sambil belajar mengendalikan api biru yang diwarisinya dari sang ayah.",
        "rating": 7.6,
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "School", "Supernatural", "Shounen"]
    },
    {
        "title": "Saiki Kusuo no Ψ-nan",
        "synopsis": "Kusuo Saiki lahir dengan hampir semua kekuatan psikis yang bisa dibayangkan — telepati, telekinesis, clairvoyance, time travel, transformation, dan masih banyak lagi. Masalahnya, kekuatan ini bukan berkah melainkan kutukan. Sejak lahir ia bisa membaca semua pikiran orang di sekitarnya, melihat semua hal yang tidak ingin ia lihat, dan tidak bisa menyentuh apapun tanpa menghancurkannya tanpa sarung tangan khusus. Yang ia inginkan hanya satu hal yang mustahil: hidup normal yang tenang. Tapi orang-orang dengan kepribadian paling aneh terus-terusan tertarik kepadanya. Komedi yang brilian dengan Saiki sebagai narator yang selalu frustasi sambil diam-diam menggunakan kemampuannya untuk mengelola kekacauan yang selalu muncul dalam hidupnya.",
        "rating": 8.4,
        "genres": ["Comedy", "School", "Slice of Life", "Super Power", "Supernatural", "Shounen"]
    },
    {
        "title": "Noragami",
        "synopsis": "Yato adalah dewa kecil yang tidak punya kuil, tidak punya pengikut, dan menawarkan jasanya seharga 5 yen — berdoa untuk segala macam permintaan mulai dari menemukan kucing hilang hingga balas dendam. Impiannya adalah memiliki kuil megah dengan jutaan pengikut. Regalia-nya yang setia baru saja meninggalkannya, sehingga ia harus mencari Regalia baru. Hiyori Iki, siswi SMA yang menyelamatkan Yato dari kecelakaan, kondisi jiwanya menjadi tidak stabil — jiwanya sering lepas dari tubuhnya. Ia meminta Yato memperbaikinya, dan jadilah ia terlibat dalam urusan dunia roh yang penuh bahaya. Di balik cerita ringan di awal, Noragami berkembang menjadi kisah yang lebih gelap dan emosional tentang trauma dewa-dewa dan masa lalu yang tidak bisa dilupakan.",
        "rating": 8.0,
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Supernatural", "Shounen"]
    },
    {
        "title": "Gabriel DropOut",
        "synopsis": "Gabriel White Tenma lulus sebagai malaikat terbaik dari surga dan dikirim ke bumi untuk belajar tentang manusia sebagai bagian dari tradisi malaikat muda. Namun tidak lama setelah tiba, ia menemukan game online dan langsung kecanduan parah. Malaikat sempurna itu berubah menjadi hikikomori yang malas, apatis, dan hanya bangun dari tempat tidur untuk bermain game dan makan. Di sisi lain, Vignette, setan yang juga tinggal di bumi untuk tujuan serupa, justru sangat rajin, perhatian, memasak untuk orang lain, dan bertingkah seperti malaikat sejati. Satania, setan lainnya, mengklaim dirinya 'Demon Lord' namun tidak bisa berbuat apa-apa. Komedi tentang inversion ekspektasi — malaikat yang menjadi setan dan setan yang menjadi malaikat.",
        "rating": 7.5,
        "genres": ["Comedy", "Fantasy", "School", "Slice of Life", "Seinen"]
    },
    {
        "title": "Senpai ga Uzai Kouhai no Hanashi",
        "synopsis": "Futaba Igarashi adalah wanita muda pekerja keras di sebuah perusahaan penjualan. Senpai-nya, Harumi Takeda, adalah pria besar dan berisik yang sering membuat komentar-komentar yang tidak diminta, mengelus kepala Futaba yang mungil layaknya anak kecil, dan terus-terusan mengundang tapi tidak memahami batas pribadi. Futaba yang awalnya selalu kesal dan menganggap Takeda menyebalkan perlahan menyadari bahwa di balik semua keusilannya, Takeda selalu ada saat ia membutuhkan bantuan dan genuinely peduli dengan kesejahteraannya. Anime romance dewasa yang hangat dengan setting kantor — mengikuti dua pasang karakter, termasuk sahabat mereka yang sedang dalam fase awal hubungan yang juga manis.",
        "rating": 7.7,
        "genres": ["Comedy", "Romance", "Slice of Life", "Seinen"]
    },
    {
        "title": "Busou Shoujo Machiavellianism",
        "synopsis": "Private Aichi Symbiosis Academy awalnya adalah sekolah putri yang kemudian menerima siswa laki-laki. Namun untuk menjaga keamanan, lima siswi petarung terkuat — dijuluki Supreme Five Swords — berkuasa penuh dan mewajibkan semua siswa laki-laki untuk bersikap feminin atau menghadapi konsekuensi. Fudou Nomura masuk sebagai siswa baru laki-laki yang menolak tunduk pada sistem ini. Ia harus mengalahkan kelima Supreme Five Swords satu per satu untuk mendapatkan kebebasannya. Setiap anggota Supreme Five Swords memiliki latar belakang dan gaya bertarung yang berbeda — dari kenjutsu hingga berbagai seni bela diri — dan masing-masing menyimpan alasan tersendiri mengapa mereka mempertahankan sistem yang ada.",
        "rating": 7.1,
        "genres": ["Action", "Comedy", "Romance", "School", "Ecchi", "Shounen"]
    },
    {
        "title": "Satsuriku no Tenshi",
        "synopsis": "Rachel Gardner adalah gadis berusia 13 tahun yang terbangun di lantai paling bawah dari sebuah gedung bawah tanah tanpa ingatan apapun. Gedung itu ternyata adalah fasilitas yang setiap lantainya dijaga oleh seorang pembunuh dengan obsesi uniknya masing-masing. Zack, pembunuh berantai berpembalut perban dan bersenjata sabit besar, ditemui Rachel di lantai B6. Keduanya membuat perjanjian: Zack akan membunuh Rachel — yang entah mengapa tidak bisa mati dan sangat ingin mati — jika Rachel membantu Zack kabur. Mereka harus bekerja sama melewati setiap lantai dengan pembunuh dan teka-teki yang semakin berbahaya, sambil perlahan mengungkap kebenaran tentang gedung misterius ini dan masa lalu gelap yang terhubung antara mereka berdua.",
        "rating": 7.2,
        "genres": ["Action", "Drama", "Horror", "Mystery", "Psychological", "Thriller", "Supernatural"]
    },
    {
        "title": "Platinum End",
        "synopsis": "Mirai Kakehashi, setelah bertahun-tahun menderita di bawah perlakuan brutal keluarga angkatnya, memutuskan untuk mengakhiri hidupnya dengan melompat dari atap gedung. Ia diselamatkan oleh Nasse, malaikat pelindungnya, yang mengungkapkan sistem kontroversial Tuhan: Tuhan akan pensiun dan 13 manusia yang dipilih oleh malaikat masing-masing akan bersaing untuk menjadi pengganti Tuhan. Setiap kandidat dibekali dengan berbagai panah dan sayap supernatural. Mirai yang awalnya tidak punya ambisi apapun harus bertahan hidup dalam kompetisi berbahaya ini. Serial ini mengangkat pertanyaan filosofis berat tentang apakah manusia layak menjadi Tuhan, apa definisi kebahagiaan, dan harga yang harus dibayar untuk kekuasaan absolut.",
        "rating": 6.4,
        "genres": ["Drama", "Mystery", "Psychological", "Supernatural", "Thriller", "Shounen"]
    },
    {
        "title": "Level E",
        "synopsis": "Yukiteru Tsukinomiya pindah ke apartemen baru untuk pertama kali hidup mandiri sambil bersekolah. Tapi ia menemukan pria asing sudah duduk santai di apartemennya — pria yang mengklaim sebagai alien dari planet Dogura yang pesawatnya jatuh di bumi dan kehilangan ingatannya. Pria itu ternyata adalah Pangeran Baka, putra mahkota Planet Dogura yang dikenal sebagai jenius paling eksentrik dan jahil dalam sejarah galaksi. Meski mengaku kehilangan ingatan, Baka terus menciptakan skema-skema rumit yang mengorbankan orang-orang di sekitarnya hanya untuk kesenangannya sendiri. Setiap arc menghadirkan petualangan alien baru yang berbeda, dengan Baka selalu menjadi biang kerok di balik semua kekacauan yang terjadi.",
        "rating": 7.9,
        "genres": ["Comedy", "Mystery", "Sci-Fi", "Seinen", "Supernatural"]
    },
    {
        "title": "Fantasy Bishoujo Juniku Ojisan to",
        "synopsis": "Hinata Tachibana dan Jinguji Tsukasa adalah dua sahabat pria berusia 32 tahun. Saat tertidur setelah minum bersama, keduanya dipanggil ke dunia fantasi oleh dewi yang iseng. Sebagai 'bonus', dewi itu mengubah Tachibana menjadi gadis cantik yang sangat mencolok. Lebih parahnya, kutukan Tachibana akan semakin kuat seiring dengan semakin banyak orang yang jatuh cinta padanya — termasuk Jinguji, sahabatnya sendiri. Untuk kembali ke dunia asal, mereka harus mengalahkan Demon Lord. Komedi meta yang mengolok-olok trope isekai secara cerdas, dengan dua karakter dewasa yang merespons situasi fantasi dengan perspektif orang dewasa yang lelah, sambil hubungan mereka berkembang ke arah yang tidak terduga.",
        "rating": 7.9,
        "genres": ["Adventure", "Comedy", "Fantasy", "Romance", "Magic", "Isekai", "Shounen"]
    },
    {
        "title": "Sewayaki Kitsune no Senko-san",
        "synopsis": "Kuroto Nakano adalah salaryman yang hidupnya hampir seluruhnya diisi kerja lembur — pulang larut malam, kelelahan, dan stres kronis yang sudah menumpuk selama bertahun-tahun. Suatu malam ia pulang ke apartemennya dan menemukan Senko-san sudah ada di sana — rubah setengah dewa berusia 800 tahun yang mengklaim sebagai 'penjaga' Nakano berdasarkan hubungan karmik dengan nenek moyangnya. Senko-san bertekad memanjakan dan merawat Nakano dengan sepenuh hati: memasak, membersihkan rumah, memperbolehkan Nakano mengelus telinganya yang lembut untuk menghilangkan stres. Anime yang terasa seperti terapi — tempo lambat, atmosfer sangat hangat, dan desain karakter yang memaksimalkan fluffiness untuk efek maksimal.",
        "rating": 7.4,
        "genres": ["Comedy", "Fantasy", "Romance", "Seinen", "Slice of Life", "Supernatural"]
    },
    {
        "title": "Yuru Yuri",
        "synopsis": "Akari Akaza akhirnya masuk ke SMP yang sama dengan kakak dan teman-teman lamanya. Ia bersama Yui Funami, Kyouko Toshinou, dan Chinatsu Yoshikawa merebut kembali ruang bekas klub teh yang sudah tidak aktif dan mendirikan Amusement Club — klub tanpa tujuan jelas selain bersenang-senang bersama. Akari yang selalu memperkenalkan dirinya sebagai protagonist namun selalu dilupakan oleh semua orang, Kyouko yang energetik dan tidak bisa diam, Yui yang bijak dan sabar, dan Chinatsu yang tampak manis namun menyimpan obsesi mencuri ciuman. Juga mengikuti Dewan Siswa yang berusaha membubarkan mereka. Anime moe slice of life yang hangat dengan humor yang mengalir natural dari dinamika karakter yang lovable.",
        "rating": 7.6,
        "genres": ["Comedy", "School", "Slice of Life", "Seinen"]
    },
    {
        "title": "Sentouin, Hakenshimasu!",
        "synopsis": "Kibou adalah agen elit dari organisasi jahat Kisaragi Corporation — organisasi yang bermimpi menguasai dunia menggunakan robot raksasa dan senjata super canggih. Ia dikirim ke dunia fantasi sebagai agen penyusup dengan misi membantu Kisaragi memperluas dominasinya. Bersama Rose — pahlawan wanita dunia itu yang penuh semangat namun sering salah perhitungan — Kibou harus bertarung melawan ancaman Demon Lord. Masalahnya, Kibou yang sebenarnya adalah agen sangat berbahaya terus berhadapan dengan ironi: ia yang seharusnya jahat justru harus berperilaku lebih heroik dari pahlawan sungguhan, sementara organisasi 'jahat' Kisaragi justru melakukan hal-hal yang lebih bermanfaat dari pemerintah setempat. Parodi isekai yang sangat lucu dengan kritik cerdas terhadap genre.",
        "rating": 7.0,
        "genres": ["Action", "Comedy", "Fantasy", "Ecchi", "Isekai", "Seinen"]
    },
    {
        "title": "Nanbaka",
        "synopsis": "Penjara Nanba adalah penjara dengan keamanan paling ketat di dunia — tidak ada yang pernah berhasil kabur. Namun empat penghuni sel 13 adalah kumpulan orang yang tidak biasa: Juugo yang ahli membobol segala jenis kunci, Uno yang jenius dalam segala jenis permainan dan perjudian, Rock yang kuat secara fisik dengan ketahanan tubuh luar biasa, dan Nico yang pecandu anime dengan kemampuan meniru teknik apapun yang pernah ia lihat. Keempat orang ini sudah kabur dari semua penjara di dunia sebelumnya. Kini mereka dipenjara di Nanba — dan anehnya, meski bisa kabur kapanpun, mereka justru mulai nyaman di sana karena hubungan yang terbentuk dengan para sipir. Serial komedi penuh warna dengan visual yang sangat stylish.",
        "rating": 7.3,
        "genres": ["Action", "Comedy", "Mystery", "Seinen"]
    },
    {
        "title": "Mirai Nikki",
        "synopsis": "Yukiteru Amano adalah siswa penyendiri yang menghabiskan waktu menulis diary di ponselnya dan berbicara dengan teman khayalannya — Deus Ex Machina, dewa ruang dan waktu. Suatu hari ia terbangun dan menemukan diary-nya terisi tulisan tentang masa depan — setiap entri menggambarkan kejadian yang akan terjadi 90 hari ke depan dengan akurasi sempurna. Ia kemudian mengetahui bahwa Deus ternyata benar-benar ada dan sedang sekarat, dan ia memilih 12 pemegang Future Diary untuk bertarung satu sama lain dalam death game. Pemenang terakhir akan menjadi pengganti Deus sebagai Tuhan. Yuno Gasai, gadis dari sekolah yang sama, memiliki diary yang isinya hanya tentang Yukiteru — dan obsesinya yang gelap terhadap Yukiteru jauh melampaui batas normal.",
        "rating": 7.5,
        "genres": ["Action", "Drama", "Horror", "Mystery", "Psychological", "Romance", "Shounen", "Supernatural", "Thriller"]
    },
    {
        "title": "Kill la Kill",
        "synopsis": "Ryuuko Matoi tiba di Honnouji Academy membawa setengah gunting raksasa yang merupakan satu-satunya petunjuk tentang pembunuh ayahnya. Sekolah ini dikuasai dengan tangan besi oleh Satsuki Kiryuuin dan pasukan Elite Four-nya. Para siswa mengenakan Goku Uniforms — seragam yang ditenun dengan serat Life Fibers yang memberikan kekuatan supranatural sesuai peringkat bintangnya. Ryuuko menemukan Senketsu, Kamui (pakaian hidup) yang hanya bisa dipakai olehnya, yang memberikan kekuatan luar biasa dengan menghisap darahnya. Petarungan Ryuuko melawan hierarki sekolah mengungkap konspirasi yang jauh lebih besar tentang Life Fibers dan rencana untuk menguasai seluruh umat manusia. Anime Trigger yang penuh energi, fanservice, dan aksi yang tidak pernah membosankan.",
        "rating": 8.1,
        "genres": ["Action", "Comedy", "Ecchi", "Fantasy", "School", "Super Power", "Seinen"]
    },
    {
        "title": "Masamune-kun no Revenge",
        "synopsis": "Masamune Makabe di masa kecilnya adalah anak gemuk yang pernah ditolak dengan sangat kejam oleh Aki Adagaki, gadis cantik dari keluarga kaya yang memberinya julukan merendahkan 'Buta'. Trauma itu membuatnya berubah total — ia berlatih keras, diet ketat, dan mengubah dirinya menjadi pemuda tampan berprestasi. Kini ia pindah ke sekolah yang sama dengan Aki, bertekad membuat Aki jatuh cinta padanya dan kemudian menolaknya sebagai balas dendam. Rencananya berjalan dengan baik — Aki mulai tertarik. Tapi semakin dekat ia dengan Aki, semakin ia menemukan sisi lain gadis itu yang tidak ia ketahui sebelumnya. Dan kemudian muncul seseorang yang mengklaim mengetahui identitas asli Masamune dan mengancam seluruh rencananya.",
        "rating": 7.0,
        "genres": ["Comedy", "Romance", "School", "Shounen"]
    },
    {
        "title": "Oniichan wa Oshimai!",
        "synopsis": "Mahiro Oyama adalah gamer dewasa yang menghabiskan seluruh waktunya di rumah bermain game. Adiknya Mihari yang brilian di bidang teknologi secara diam-diam mengembangkan obat yang mengubah jenis kelamin seseorang. Suatu pagi Mahiro terbangun sebagai perempuan. Mihari yang excited mengumumkan bahwa ia ingin mengamati kehidupan Mahiro sebagai perempuan untuk penelitiannya — dan obat pembaliknya belum ada. Mahiro yang awalnya sangat keberatan harus mulai menjalani kehidupan sehari-hari sebagai perempuan: bersekolah dengan seragam perempuan, berteman dengan siswi-siswi lucu, dan perlahan-lahan menemukan bahwa ia menikmati aspek-aspek tertentu dari kehidupan barunya lebih dari yang ia akui.",
        "rating": 7.5,
        "genres": ["Comedy", "Slice of Life", "School", "Seinen"]
    },
    {
        "title": "Maoujou de Oyasumi",
        "synopsis": "Putri Syalis dari kerajaan manusia diculik oleh pasukan Demon Lord dan dipenjara di kastil iblis. Para pahlawan bersiap menyelamatkannya. Sementara itu, Syalis sendiri sama sekali tidak terlihat tertekan — ia jauh lebih khawatir soal satu hal: bagaimana caranya mendapatkan tidur yang enak dan nyaman. Tempat tidurnya terlalu keras, bantalnya tidak cukup fluffy. Untuk mendapatkan bahan-bahan yang sempurna untuk tempat tidur idealnya, Syalis tidak segan mencuri bulu dari monster-monster kastil, meminta benang dari laba-laba raksasa, hingga meminjam benda-benda dari Demon Lord sendiri. Para iblis kastil yang seharusnya menakutkan ini justru bingung menghadapi putri yang lebih fokus pada kenyamanan tidur daripada merencanakan kabur. Komedi yang sangat cozy dan menggemaskan.",
        "rating": 7.9,
        "genres": ["Comedy", "Fantasy", "Romance", "Slice of Life", "Shounen"]
    },
    {
        "title": "Akame ga Kill!",
        "synopsis": "Tatsumi adalah pemuda dari desa terpencil yang pergi ke ibu kota kekaisaran bermimpi bergabung dengan tentara dan membantu desanya yang miskin. Namun ia menemukan bahwa ibu kota dikuasai oleh korupsi yang membusuk dari dalam — perdana menteri yang bengis mengendalikan kaisar muda yang naif, sementara rakyat jelata menderita. Night Raid, kelompok pembunuh bayaran yang bekerja untuk pasukan revolusi, merekrut Tatsumi. Mereka menggunakan Teigu — senjata dan baju besi super kuat yang dibuat dari binatang legendaris — untuk melawan kekaisaran. Serial ini dikenal dengan satu hal yang tidak biasa untuk shounen: tidak ada karakter yang benar-benar aman. Kematian mengintai setiap anggota Night Raid, membuat setiap pertarungan terasa nyata dan penuh taruhan.",
        "rating": 7.5,
        "genres": ["Action", "Adventure", "Drama", "Fantasy", "Horror", "Mystery", "Shounen"]
    },
    {
        "title": "Happy Sugar Life",
        "synopsis": "Satou Matsuzaka adalah gadis SMA cantik dan populer yang dikenal suka berganti-ganti pacar. Tapi semua itu berubah saat ia menemukan Shio Koube — anak kecil yang tersesat dan sendirian — dan merasakannya sebagai cinta pertamanya yang sesungguhnya. Satou menyembunyikan Shio di apartemennya dan bertekad melindungi 'kehidupan manis' mereka bersama dengan cara apapun yang diperlukan — dan ia benar-benar tidak keberatan melakukan cara apapun itu. Semakin banyak yang mengancam keberadaan Shio, semakin gelap tindakan yang Satou lakukan. Psychological thriller yang mengeksplorasi obsesi, trauma, dan distorsi definisi cinta dengan cara yang disturbing namun tidak bisa dilepaskan mata — setiap karakter menyimpan luka dan versi terdistorsi mereka sendiri tentang kasih sayang.",
        "rating": 7.2,
        "genres": ["Drama", "Horror", "Mystery", "Psychological", "Romance", "Thriller", "Seinen"]
    },
    {
        "title": "Baka to Test to Shoukanjuu",
        "synopsis": "Di SMA Fumizuki, kelas siswa ditentukan oleh hasil ujian masuk — Kelas A mendapat fasilitas mewah, Kelas F mendapat kursi rusak dan meja kayu lapuk. Yoshii Akihisa masuk Kelas F bersama teman-temannya yang tidak kalah unik. Sekolah ini memiliki sistem Summoner Test War: setiap siswa bisa memanggil avatar fantasi yang kekuatannya setara dengan nilai ujian mereka. Kelas F yang difasilitasi paling buruk memutuskan untuk menantang kelas-kelas di atasnya dalam perang avatar untuk merebut fasilitas yang lebih baik. Komedi sekolah yang kreatif dengan premis unik, dipenuhi humor tentang perbedaan kemampuan, persahabatan yang solid, dan romance yang perlahan berkembang antara karakter-karakternya.",
        "rating": 7.7,
        "genres": ["Comedy", "Fantasy", "Romance", "School", "Shounen"]
    },
    {
        "title": "D-Frag!",
        "synopsis": "Kenji Kazama adalah ketua geng sekolah yang ingin sekali terlihat keren dan ditakuti. Semua rencana itu hancur saat ia tidak sengaja menyelamatkan Game Creation Club dari kebakaran dan langsung 'direkrut' paksa oleh keempat anggotanya yang perempuan semua: Roka yang pendiam dan menggunakan karung untuk menangkap orang, Chitose yang kuat dan agresif, Sakura yang feminin namun tidak bisa dibaca, dan Minami yang lebih normal dari yang terlihat. Kazama yang berusaha keras mempertahankan image delinquent-nya terus-terusan terseret dalam kekacauan club yang tidak ada hubungannya dengan pembuatan game. Komedi timing yang sangat baik dengan karakter-karakter yang punya quirk unik namun tidak terasa memaksakan.",
        "rating": 7.8,
        "genres": ["Comedy", "Game", "School", "Seinen"]
    },
    {
        "title": "Seto no Hanayome",
        "synopsis": "Nagasumi Michishio berlibur ke laut dan hampir tenggelam sebelum diselamatkan oleh Sun Seto — yang ternyata adalah putri duyung. Menurut hukum klan duyung, manusia yang mengetahui keberadaan mereka harus dibunuh — kecuali jika mereka menikah dengan anggota klan. Untuk menyelamatkan nyawa Nagasumi, Sun melamarnya. Kini Nagasumi harus menjalani kehidupan sebagai suami Sun sambil menyembunyikan identitas Sun dari dunia manusia, berhadapan dengan ayah Sun yang yakuza duyung super protektif, dan menghadapi berbagai anggota klan duyung lainnya yang tidak setuju dengan pernikahan ini. Komedi gila dengan karakter-karakter yakuza duyung yang absurd namun sangat menghibur, dan romance yang genuine di balik semua kekacauan.",
        "rating": 7.8,
        "genres": ["Action", "Comedy", "Fantasy", "Romance", "School", "Shounen"]
    },
    {
        "title": "Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka",
        "synopsis": "Di kota Orario yang unik, sebuah dungeon raksasa menjadi pusat kehidupan — para adventurer menyelami kedalamannya mencari monster, pengalaman, dan kekayaan. Sistem Familia menghubungkan adventurer dengan dewa-dewa yang turun ke dunia manusia. Bell Cranel, pemula 14 tahun yang bergabung dengan Familia terkecil dan paling tidak dianggap — Hestia Familia yang hanya beranggotakan dua orang termasuk dewi Hestia sendiri — bermimpi menjadi pahlawan terbesar. Takdir berubah saat ia diselamatkan dari monster oleh Ais Wallenstein, sword princess terkuat yang langsung membuat Bell jatuh cinta. Perasaan itu membangkitkan Skill langka Realis Phrase yang membuat pertumbuhannya berlipat ganda saat ia berjuang mengejar seseorang yang jauh di atasnya.",
        "rating": 7.9,
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Romance", "Shounen"]
    },
    {
        "title": "Gakkougurashi!",
        "synopsis": "Yuki Takeya adalah siswi SMA yang bersemangat dan ceria, anggota School Living Club — klub yang tinggal dan hidup di sekolah. Sekilas tampak seperti anime sekolah yang manis dan slice of life biasa. Tapi kamera perlahan-lahan mengungkap kebenaran yang kontras tajam dengan keceriaan Yuki: di luar jendela sekolah yang aman, dunia sudah dipenuhi zombie. Sekolah adalah benteng terakhir mereka. Yuki mengalami disosiasi — pikirannya menciptakan realitas yang lebih nyaman untuk melindunginya dari trauma. Sementara anggota lain bertahan dengan penuh ketegangan dan kesedihan, Yuki melihat sekolah yang masih normal dan teman-teman yang belum hilang. Perpaduan genre yang mengejutkan dan sangat efektif, dengan momen-momen heartbreaking yang tidak terduga.",
        "rating": 7.6,
        "genres": ["Drama", "Horror", "Mystery", "Psychological", "School", "Slice of Life", "Seinen"]
    },
    {
        "title": "High School of the Dead",
        "synopsis": "Takashi Komuro menyaksikan dari balik jendela kelasnya saat seorang pria mati dibalik gerbang sekolah, kemudian bangkit sebagai zombie dan mulai menyerang. Dalam hitungan jam, seluruh sekolah kacau. Takashi bersama Rei Miyamoto — teman lama yang punya sejarah rumit dengannya — dan sekelompok survivor lainnya berjuang keluar dari sekolah yang sudah dipenuhi undead. Kelompok yang terbentuk mencakup Saya Takagi yang jenius, Kohta Hirano yang ahli senjata api, Saeko Busujima yang master kendo, dan Shizuka Marikawa sang guru UKS. Di luar ancaman zombie, mereka juga harus menghadapi bahaya dari sesama manusia yang sudah kehilangan moralnya di tengah kekacauan. Survival horror dengan aksi intens yang tidak pernah memberi waktu istirahat.",
        "rating": 7.1,
        "genres": ["Action", "Drama", "Ecchi", "Horror", "Supernatural", "Seinen", "School"]
    },
    {
        "title": "Kamisama ni Natta Hi",
        "synopsis": "Di hari-hari terakhir musim panas menjelang akhir SMA, Youta Narukami didatangi gadis misterius bernama Hina yang mengklaim bahwa ia adalah Dewa Yang Maha Tahu dan bahwa kiamat akan terjadi dalam 30 hari. Youta tentu saja tidak percaya sampai Hina mulai membuktikan kemampuannya yang luar biasa — ia mengetahui segalanya tentang masa lalu dan rahasia setiap orang. Youta memutuskan menghabiskan 30 hari itu bersama Hina, membantu mewujudkan berbagai keinginannya. Seiring waktu berlalu, kebenaran tentang Hina — siapa dia sebenarnya, dari mana kemampuannya, dan apa yang sebenarnya akan terjadi — terungkap dengan cara yang jauh lebih menyentuh dan menyakitkan dari yang Youta duga.",
        "rating": 7.3,
        "genres": ["Comedy", "Drama", "Fantasy", "Romance", "Sci-Fi", "Supernatural"]
    },
    {
        "title": "Binbougami ga!",
        "synopsis": "Ichiko Sakura adalah gadis SMA yang tampaknya dianugerahi segalanya — kecantikan luar biasa, kepintaran, atletis, tubuh sempurna, dan keberuntungan yang tak ada habisnya. Alasannya ternyata karena ia secara tidak sadar menyerap keberuntungan orang-orang di sekitarnya, membuat mereka sial. Momiji Binbougami, Dewa Kemiskinan, dikirim untuk menyeimbangkan kembali Fortune Energy yang sudah terlalu banyak terserap Ichiko. Masalahnya Ichiko tidak mau menyerah begitu saja dan terus menggagalkan usaha Momiji. Pertarungan absurd antara keduanya menjadi inti komedi serial ini, namun di balik konflik lucu mereka tersimpan eksplorasi mendalam tentang kesepian Ichiko yang sebenarnya — gadis yang memiliki segalanya namun tidak punya siapapun.",
        "rating": 7.9,
        "genres": ["Action", "Comedy", "Parody", "Romance", "Supernatural", "Shounen"]
    },
    {
        "title": "Kotoura-san",
        "synopsis": "Haruka Kotoura lahir dengan kemampuan membaca pikiran yang tidak bisa ia matikan. Sejak kecil ia tidak sengaja mengungkapkan pikiran tersembunyi orang-orang di sekitarnya — rahasia orang tua, kebohongan teman, pikiran tidak pantas guru — yang satu per satu menghancurkan semua hubungan yang ia miliki sampai akhirnya ia sendirian. Setelah dibuang oleh orang tuanya dan tumbuh tanpa kasih sayang, Haruka memasuki SMA baru dengan harapan bisa hidup tanpa menyakiti siapapun dengan cara tidak berteman sama sekali. Namun Manabe Yoshihisa, siswa yang pemikirannya transparan dan tidak malu-malu, justru tidak keberatan pikirannya terbaca dan terus-terusan berusaha mendekati Haruka. Kisah yang dimulai dengan sedih namun berkembang menjadi hangat tentang menerima dan diterima apa adanya.",
        "rating": 7.5,
        "genres": ["Comedy", "Drama", "Romance", "School", "Supernatural", "Seinen"]
    },
    {
        "title": "Rewrite",
        "synopsis": "Kotarou Tennouji adalah siswa SMA yang memiliki kemampuan Rewrite — ia bisa menulis ulang tubuhnya sendiri, meningkatkan kecepatan atau kekuatan dengan mengorbankan sebagian umurnya. Di kotanya yang tampak biasa, ia secara tidak sengaja terlibat dengan dua organisasi yang berlawanan: Guardian yang bertugas melindungi umat manusia dan Gaia yang percaya bahwa manusia harus memberi jalan pada evolusi bumi. Ia mendirikan Occult Research Club dengan lima gadis yang masing-masing memiliki koneksi tersembunyi dengan kedua organisasi ini. Seiring cerita berkembang, sebuah kebenaran tentang kota mereka dan masa depan bumi terungkap. Adaptasi visual novel Key yang kompleks dengan multiple route, mengeksplorasi tema hubungan manusia dengan alam dan harga dari kelangsungan hidup.",
        "rating": 7.0,
        "genres": ["Action", "Comedy", "Drama", "Fantasy", "Mystery", "Romance", "School", "Supernatural", "Seinen"]
    },
    {
        "title": "Hoshizora e Kakaru Hashi",
        "synopsis": "Kazuma Hoshi pindah bersama adiknya ke sebuah desa pegunungan kecil yang tenang karena alasan kesehatan adiknya. Di hari pertama, saat berjalan melalui hutan, ia tersesat dan tidak sengaja mencium seorang gadis desa bernama Ui Nakatsugawa yang menjadi teman pertamanya di tempat baru. Ciuman tidak sengaja itu ternyata adalah ritual adat setempat yang maknanya cukup serius, sehingga langsung menciptakan drama. Di desa yang damai itu, Kazuma bertemu berbagai gadis dengan kepribadian berbeda — dari Ui yang lembut dan sabar, Ibuki yang tomboi dan terus terang, hingga Senka yang merupakan teman masa kecil yang tidak ia ingat. Slice of life romance yang tenang dengan latar desa yang indah.",
        "rating": 6.9,
        "genres": ["Comedy", "Harem", "Romance", "School", "Seinen", "Slice of Life"]
    },
    {
        "title": "Toaru Series",
        "synopsis": "Academy City adalah kota futuristik yang didedikasikan untuk mengembangkan esper — manusia dengan kemampuan supranatural. 80% dari tiga juta penduduknya adalah pelajar yang mengikuti program pengembangan kemampuan. Touma Kamijou adalah siswa Level 0 — dianggap tidak punya kemampuan esper sama sekali. Namun tangan kanannya menyimpan Imagine Breaker — kemampuan yang bisa membatalkan sihir, ESP, bahkan keberuntungan apapun yang menyentuhnya. Hidupnya berubah saat ia menemukan Index, biarawati muda yang memiliki 103.000 kitab sihir tersimpan dalam ingatannya, tergantung di balkon apartemennya. Pertemuan itu menariknya ke dalam konflik antara dunia sains Academy City dan dunia sihir Gereja yang telah lama bersitegang.",
        "rating": 7.8,
        "genres": ["Action", "Adventure", "Fantasy", "Magic", "Romance", "Sci-Fi", "Supernatural", "Shounen"]
    },
    {
        "title": "Zom 100: Zombie ni Naru made ni Shitai 100 no Koto",
        "synopsis": "Akira Tendou baru lulus kuliah dengan penuh semangat dan bergabung dengan perusahaan impiannya di industri hiburan. Tiga tahun kemudian ia adalah zombie — bukan zombie sungguhan, tapi zombie karena kerja lembur ekstrem, atasan yang menindas, dan tidak ada kehidupan di luar kantor. Suatu pagi ia bangun dan melihat tetangganya telah berubah menjadi zombie sungguhan. Alih-alih panik, reaksi pertamanya adalah kelegaan yang luar biasa — akhirnya ia tidak perlu pergi kerja! Dengan energi yang sudah lama tertidur, Akira membuat bucket list 100 hal ingin ia lakukan sebelum menjadi zombie. Serial ini adalah komentar tajam tentang budaya kerja Jepang yang membunuh jiwa, dibungkus dalam petualangan zombie apocalypse yang penuh warna dan semangat.",
        "rating": 7.9,
        "genres": ["Action", "Adventure", "Comedy", "Horror", "Shounen"]
    },
    {
        "title": "Isekai Quartet",
        "synopsis": "Suatu hari, sebuah tombol misterius muncul di hadapan karakter-karakter dari empat isekai berbeda — Ainz dari Overlord, Subaru dari Re:Zero, Kazuma dan kelompoknya dari KonoSuba, dan Tanya dari Youjo Senki. Siapapun yang menekan tombol akan langsung dipindahkan ke... sekolah biasa. Keempat kelompok dari dunia yang berbeda-beda ini harus bersekolah bersama di kelas yang sama, menghadiri pelajaran, mengikuti kegiatan sekolah, dan berinteraksi satu sama lain. Crossover komedi yang mengeksplorasi bagaimana karakter-karakter dengan kepribadian dan latar belakang sangat berbeda berinteraksi — dengan banyak momen meta yang menyindir trope isekai dan karakter masing-masing seri.",
        "rating": 7.7,
        "genres": ["Comedy", "Fantasy", "Isekai", "Parody", "School", "Seinen"]
    },
    {
        "title": "Isekai Ojisan",
        "synopsis": "Takafumi terkejut saat pamannya, Yousuke Shibazaki, bangun dari koma 17 tahun. Lebih mengejutkan lagi, selama koma itu sang paman ternyata hidup di dunia fantasi Granbahamal dan baru saja kembali ke dunia nyata. Paman yang tadinya otaku gamer ini kini kembali dengan kemampuan sihir yang kuat — namun kepribadiannya masih sama seperti orang Jepang era 90an yang nostalgia Sega dan tidak update dengan perkembangan zaman. Takafumi membantu pamannya menyesuaikan diri dengan dunia modern sambil mereka berdua membuat konten YouTube tentang petualangan di dunia fantasi yang bisa divisualisasikan dengan sihir sang paman. Humor yang mengolok-olok trope isekai dari perspektif orang yang sudah kembali, dipenuhi referensi game klasik.",
        "rating": 8.0,
        "genres": ["Comedy", "Fantasy", "Isekai", "Seinen"]
    },
    {
        "title": "Tokyo Ravens",
        "synopsis": "Harutora Tsuchimikado lahir dalam cabang keluarga onmyoji yang turun-temurun kuat, namun ia sendiri sama sekali tidak memiliki kekuatan spiritual apapun. Suatu hari, Natsume — gadis yang merupakan kepala dari cabang utama keluarga Tsuchimikado dan diduga sebagai reinkarnasi leluhur legendaris mereka — datang meminta Harutora memenuhi janji masa kecil: menjadi shikigami-nya. Setelah tragedi yang menewaskan orang yang ia sayangi, Harutora bergabung dengan Onmyo Prep School bersama Natsume. Di sana mereka menghadapi berbagai ancaman dari berbagai pihak yang mengincar kekuatan Natsume, sementara Harutora perlahan-lahan menyadari kebenaran tentang dirinya yang jauh lebih kompleks dari yang ia kira.",
        "rating": 7.5,
        "genres": ["Action", "Fantasy", "Magic", "Romance", "School", "Supernatural", "Shounen"]
    },
    {
        "title": "Musaigen no Phantom World",
        "synopsis": "Suatu virus menyebar ke seluruh dunia dan mengaktifkan bagian otak yang sebelumnya tidak aktif, membuat manusia bisa melihat dan berinteraksi dengan Phantom — makhluk yang sebelumnya hanya ada dalam imajinasi dan cerita rakyat. Kebanyakan Phantom tidak berbahaya, tapi beberapa menjadi ancaman. Haruhiko Ichijo dan Mai Kawakami bergabung dengan Phantom-Hunting Club di sekolah mereka, bekerja sama dengan beberapa anggota lain masing-masing dengan kemampuan unik, untuk menyegel Phantom-Phantom yang bermasalah. Haruhiko yang bookworm memiliki kemampuan memanggil karakter dari buku dan lukisan, sementara Mai menggunakan kekuatan elemental melalui gerakan tubuh. Visual yang indah khas KyoAni dengan dunia yang kreatif dan beragam, meski plot lebih ringan.",
        "rating": 6.9,
        "genres": ["Action", "Comedy", "Fantasy", "Magic", "School", "Ecchi"]
    },
    {
        "title": "To LOVE-Ru",
        "synopsis": "Rito Yuuki adalah siswa SMA pemalu yang tidak bisa mengungkapkan perasaannya pada gadis yang ia suka, Haruna Sairenji. Suatu malam saat mandi, seorang gadis telanjang tiba-tiba muncul di bak mandinya — Lala Satalin Deviluke, putri pertama dari Raja seluruh galaksi yang kabur dari rumah untuk menghindari perjodohan. Lala yang spontan langsung memutuskan bahwa Rito adalah calon suaminya dan mengumumkannya ke seluruh galaksi. Kini berbagai alien berdatangan — sebagian ingin membunuh Rito untuk merebut Lala, sebagian melamar Lala. Sementara Rito yang malang masih mencoba menyatakan perasaannya pada Haruna, rumahnya menjadi tempat tinggal para alien yang semakin bertambah.",
        "rating": 7.1,
        "genres": ["Comedy", "Ecchi", "Fantasy", "Harem", "Romance", "School", "Sci-Fi", "Shounen"]
    },
    {
        "title": "Yofukashi no Uta",
        "synopsis": "Kou Yamori adalah siswa SMA yang tiba-tiba tidak bisa tidur di malam hari tanpa alasan yang jelas. Ia memutuskan untuk berhenti mencoba tidur dan mulai menjelajahi kota di malam hari. Di sanalah ia bertemu Nazuna Nanakusa — gadis yang tinggal di bawah jembatan dan ternyata adalah vampir. Nazuna menawarkan untuk menghisap darah Kou agar ia bisa tidur. Kou justru memutuskan ingin menjadi vampir, namun syaratnya untuk berubah menjadi vampir adalah sang calon harus jatuh cinta pada vampir yang menggigitnya. Kou mulai berusaha jatuh cinta pada Nazuna yang tidak terbiasa dengan perasaan tersebut. Eksplorasi malam kota yang indah dengan atmosfer misterius dan hubungan yang berkembang perlahan antara dua orang yang sama-sama tidak terbiasa dengan keintiman.",
        "rating": 7.7,
        "genres": ["Action", "Mystery", "Romance", "Supernatural", "Seinen"]
    },
    {
        "title": "Monogatari Series",
        "synopsis": "Koyomi Araragi, siswa SMA yang hampir menjadi vampir namun berhasil kembali menjadi manusia (hampir), memiliki kemampuan regenerasi sisa yang membuatnya hampir tidak bisa mati. Ia bertemu berbagai gadis yang mengalami Aberration — kelainan supernatural yang merupakan manifestasi fisik dari tekanan emosional dan psikologis yang tidak terselesaikan. Hitagi yang hampir tidak berbobot karena bertemu kepiting roh, Suruga yang lengannya dikuasai jiwa setan karena keinginan yang terlalu kuat, Nadeko yang menderita karena kutukan ular, dan banyak lagi. Setiap arc adalah kombinasi unik dari dialog yang sangat cerdas dan filosofis, visual yang eksperimental, dan eksplorasi mendalam tentang psikologi dan emosi manusia yang terbungkus dalam cerita supernatural.",
        "rating": 8.4,
        "genres": ["Action", "Comedy", "Drama", "Mystery", "Psychological", "Romance", "Supernatural", "Seinen"]
    },
    {
        "title": "Blood Lad",
        "synopsis": "Staz Charlie Blood adalah vampir berkuasa yang menguasai wilayah di dunia iblis, namun lebih suka menghabiskan waktu bermain game dan menonton anime karena ia terobsesi dengan budaya pop Jepang. Suatu hari seorang gadis Jepang sungguhan bernama Yanagi Fuyumi menyasar ke wilayahnya secara tidak sengaja — dan langsung dimakan monster dan mati, berubah menjadi hantu. Staz yang sudah lama bermimpi bertemu manusia Jepang asli sangat kecewa dengan kejadian ini dan berjanji untuk menghidupkan Fuyumi kembali. Petualangan mereka membawa Staz ke berbagai penjuru dunia iblis, menghadapi berbagai faksi kuat, dan menemukan bahwa kemampuan menghidupkan orang mati berkaitan langsung dengan rahasia asal-usulnya sendiri.",
        "rating": 7.3,
        "genres": ["Action", "Comedy", "Fantasy", "Romance", "Supernatural", "Seinen"]
    },
    {
        "title": "Nu Wushen de Canzhuo",
        "synopsis": "Di perbatasan antara dunia manusia dan dunia dewa, terdapat sebuah restoran kecil yang hanya buka pada malam tertentu. Restoran yang dikelola oleh seorang wanita muda bernama Wei Wei ini menjadi tempat pertemuan berbagai pelanggan dari dunia dewa, dunia iblis, dunia roh, dan dunia manusia. Setiap tamu membawa ceritanya masing-masing — kisah cinta yang gagal, dendam yang belum terselesaikan, kerinduan akan masa lalu — dan Wei Wei menyajikan masakan yang entah bagaimana selalu tepat dengan apa yang dibutuhkan tamu tersebut, bukan hanya mengisi perut tapi juga menyentuh hati. Donghua yang hangat dan puitis dengan visual yang memukau, mengangkat tema tentang penyembuhan, penerimaan, dan hubungan yang melampaui batas dunia.",
        "rating": 8.1,
        "genres": ["Fantasy", "Slice of Life", "Mystery", "Supernatural"]
    },
    {
        "title": "Endro~!",
        "synopsis": "Yusha dan kelompok pahlawannya berhasil mengalahkan Demon Lord dengan mantra yang hampir sempurna — namun mantra tersebut mengirim Demon Lord kembali ke masa lalu, tepat saat Yusha baru memulai petualangannya sebagai pahlawan muda. Demon Lord yang kini terjebak dalam tubuh anak kecil imut memutuskan untuk menjadi guru di Hero School agar bisa memastikan Yusha tidak pernah tumbuh menjadi pahlawan yang cukup kuat untuk mengalahkannya. Masalahnya, Yusha dan teman-temannya sangat menggemaskan dan menyenangkan untuk ditonton, dan rencana sang Demon Lord terus gagal karena ia sendiri mulai menikmati waktu bersama mereka. Fantasy slice of life yang sangat cozy dan hangat tentang pahlawan-pahlawan muda yang petualangannya jauh lebih santai dari yang seharusnya.",
        "rating": 7.1,
        "genres": ["Adventure", "Comedy", "Fantasy", "Magic", "School", "Slice of Life", "Seinen"]
    },
    {
        "title": "Seitokai no Ichizon",
        "synopsis": "Dewan Siswa SMA Hekiyou dipilih berdasarkan popularitas — sehingga semua kursinya diisi oleh siswi-siswi cantik dari berbagai tipe: Minatsu yang atlet tomboi, Chizuru yang feminin dan manipulatif, Mafuyu yang kutu buku pemalu, dan Kurimu si ketua yang imut namun sering tidak kompeten. Satu-satunya anggota laki-laki adalah Ken Sugisaki yang masuk bukan karena popularitas melainkan karena meraih nilai ujian sempurna. Ken secara terbuka mengumumkan mimpinya untuk menjadikan Dewan Siswa sebagai harem-nya seperti di eroge favoritnya. Setiap rapat Dewan Siswa berubah menjadi sesi obrolan penuh referensi anime/manga/game, candaan meta, dan interaksi jenaka antara lima karakter yang punya chemistry yang sangat solid.",
        "rating": 7.2,
        "genres": ["Comedy", "Parody", "Romance", "School", "Seinen", "Harem"]
    },
    {
        "title": "Bokura wa Minna Kawai-sou",
        "synopsis": "Kazunari Usa pindah ke kos-kosan agar bisa hidup mandiri dan bebas dari orang tua yang terlalu protektif. Ia langsung terkejut dengan penghuni kos lainnya yang semuanya eksentrik: penyewa senior Shirosaki yang masokis berat, Mayumi yang sinis tentang hubungan karena terus diputus pacar, dan Sayaka yang menulis novel dewasa dari siang sampai malam. Di antara semua keanehan itu, ada Ritsu Kawai — siswi yang cantik namun lebih memilih menghabiskan waktu membaca buku daripada bergaul. Usa yang tertarik pada Ritsu harus menembus dinding buku yang ia bangun di sekelilingnya. Slice of life romance yang sangat charming dengan art style yang sangat detail dan hangat, dan humor yang mengalir natural.",
        "rating": 7.9,
        "genres": ["Comedy", "Romance", "School", "Seinen", "Slice of Life"]
    },
    {
        "title": "Arakawa Under the Bridge",
        "synopsis": "Kou Ichinomiya dibesarkan dengan satu prinsip keluarga yang paling penting: tidak pernah berhutang budi pada siapapun. Saat ia hampir tenggelam di sungai Arakawa dan diselamatkan oleh Nino — gadis aneh yang tinggal di bawah jembatan dan mengklaim berasal dari Venus — ia terpaksa mengakui ia berhutang nyawa. Nino hanya meminta satu hal: jadilah kekasihnya. Kou yang tidak mau berhutang setuju dan tinggal di bawah jembatan Arakawa. Di sana ia menemukan komunitas orang-orang tidak biasa yang tinggal di bawah jembatan — pemimpin berpakaian kappa, bintang musik berpenampilan bintang laut, mantan tentara yang tinggal di bungker. Komedi absurd dari SHAFT yang mengocok perut sekaligus mengajukan pertanyaan tentang apa yang membuat hidup bermakna.",
        "rating": 7.8,
        "genres": ["Comedy", "Romance", "Seinen", "Slice of Life"]
    },
    {
        "title": "Ore no Nounai Sentakushi ga, Gakuen Love Comedy wo Zenryoku de Jama Shiteiru",
        "synopsis": "Kanade Amakusa menderita kutukan yang ia sebut Absolute Choice — secara tiba-tiba dan tanpa peringatan apapun, di manapun ia berada, ia dipaksa memilih antara dua pilihan yang keduanya sama-sama memalukan atau tidak masuk akal, dan harus segera melakukannya. Akibatnya, seluruh sekolah menganggapnya orang paling aneh dan pervert yang pernah ada, meski sebenarnya ia adalah korban. Suatu hari Absolute Choice memunculkan pilihan yang berujung pada kemunculan gadis berambut pirang cantik bernama Chocolat dari langit. Chocolat mengungkap bahwa kutukan itu berasal dari dewa-dewa iseng dan bisa dihilangkan dengan cara menyelesaikan berbagai quest aneh — yang tentu saja semuanya harus melibatkan situasi memalukan bagi Kanade.",
        "rating": 7.1,
        "genres": ["Comedy", "Romance", "School", "Supernatural", "Harem", "Shounen"]
    },
    {
        "title": "Hataraku Maou-sama!",
        "synopsis": "Iblis Raja Maou Sadao hampir berhasil menaklukkan seluruh Ente Isla ketika Pahlawan Emilia memaksanya mundur dan membuka portal ke dimensi lain dalam keadaan terjepit. Ia dan jenderal setianya Alsiel tiba di Tokyo modern Jepang — tanpa kekuatan, tanpa uang, tanpa kemampuan berbahasa Jepang. Dalam situasi putus asa, Maou beradaptasi dengan cepat: ia belajar bahasa Jepang, mendapat pekerjaan paruh waktu di restoran cepat saji MgRonalds, dan hidup hemat di apartemen murah. Pahlawan Emilia juga terjebak di Tokyo dan kini bekerja sebagai pegawai call center. Komedi slice of life yang sangat menghibur tentang si 'jahat' yang ternyata adalah karyawan paling pekerja keras dan dapat diandalkan, sementara 'pahlawan' kewalahan menghadapi kehidupan modern.",
        "rating": 8.0,
        "genres": ["Comedy", "Fantasy", "Romance", "Supernatural", "Seinen"]
    },
    {
        "title": "Hentai Ouji to Warawanai Neko",
        "synopsis": "Youto Yokodera adalah siswa SMA yang dipenuhi pikiran tidak pantas namun memiliki filter yang kuat sehingga apa yang terucap selalu kebalikan dari yang ia pikirkan. Ia membuat permohonan pada patung kucing supernatural yang konon bisa mengambil sifat yang tidak diinginkan seseorang. Youto meminta agar filter-nya diambil — ia ingin bisa bicara jujur. Tsukiko Tsutsukakushi memohon hal sebaliknya — ia ingin wajahnya tidak pernah menunjukkan ekspresi emosi agar ia bisa menyembunyikan perasaannya. Permintaan terkabul: Youto sekarang tidak punya filter sama sekali dan bicara hal-hal yang tidak pantas, sementara Tsukiko tidak bisa menunjukkan ekspresi apapun. Keduanya harus bekerja sama menemukan cara mendapatkan kembali sifat mereka yang hilang.",
        "rating": 7.4,
        "genres": ["Comedy", "Romance", "School", "Supernatural", "Seinen"]
    },
    {
        "title": "Isekai Maou to Shoukan Shoujo no Dorei Majutsu",
        "synopsis": "Takuma Sakamoto adalah gamer hikikomori yang mendominasi MMORPG Cross Reverie sebagai karakter Iblis Raja Diablo — makhluk paling kuat di server dengan berbagai item langka yang tidak bisa diduplikasi. Suatu hari ia di-summon ke dunia yang persis seperti game tersebut oleh dua gadis: Rem Galeu, gadis kucing yang berencana mentransfer kutukan berbahaya dari dalam tubuhnya ke Diablo, dan Shera L. Greenwood, putri elf yang melarikan diri dari kerajaannya. Ritual summon mereka berbalik dan Diablo malah menjadi 'tuan' mereka. Kini Takuma yang tidak punya kemampuan sosial harus berinteraksi dengan orang lain — namun ia memutuskan untuk tetap memainkan peran Iblis Raja yang dominan dan angkuh karena tidak tahu cara lain berinteraksi.",
        "rating": 7.2,
        "genres": ["Adventure", "Comedy", "Ecchi", "Fantasy", "Harem", "Magic", "Romance", "Isekai", "Seinen"]
    },
    {
        "title": "Boku no Kanojo ga Majimesugiru Sho-bitch na Ken",
        "synopsis": "Haruka Shinozaki akhirnya memberanikan diri mengungkapkan perasaannya kepada Akiho Kousaka — siswi yang paling serius, sopan, dan berprestasi di sekolahnya. Mengejutkannya, Akiho menerima. Namun Akiho menginterpretasikan 'menjadi kekasih yang baik' dengan cara yang sangat ekstrem dan literal — ia membaca berbagai artikel dan buku tentang hubungan, dan mencoba menerapkan semuanya sekaligus dengan keseriusan total, menghasilkan situasi yang sangat tidak nyaman dan melampaui batas kesopanan yang bisa Haruka toleransi. Komedi yang bermain dengan konsep gadis yang terlalu serius dan naif namun memiliki pikiran yang sangat tidak terduga saat ia berusaha menjadi kekasih ideal.",
        "rating": 6.8,
        "genres": ["Comedy", "Ecchi", "Romance", "School", "Seinen"]
    },
    {
        "title": "Kishuku Gakkou no Juliet",
        "synopsis": "Di sekolah asrama Dahlia, dua asrama besar saling bermusuhan sengit sejak bertahun-tahun: Westia yang mewakili negara barat dan Touwa yang mewakili negara timur. Romio Inuzuka adalah pemimpin asrama Touwa, sementara Juliet Percia adalah pemimpin Westia. Di tengah permusuhan abadi ini, keduanya menyimpan rahasia yang jika ketahuan akan mengacaukan segalanya: mereka saling mencintai. Hubungan rahasia mereka harus dijaga dari ratusan pasang mata di sekolah yang selalu mencari-cari konflik. Serial ini adalah Romeo and Juliet versi sekolah asrama dengan banyak komedi dari berbagai usaha menyembunyikan hubungan mereka yang selalu hampir ketahuan, diselingi momen-momen romantis yang tulus.",
        "rating": 7.3,
        "genres": ["Comedy", "Romance", "School", "Shounen"]
    },
    {
        "title": "Dagashi Kashi",
        "synopsis": "Kokonotsu Shikada bermimpi menjadi mangaka, namun ayahnya yang pemilik toko dagashi (snack tradisional) ingin ia mewarisi toko tersebut. Situasi rumit saat Hotaru Shidare — gadis eksentrik dari keluarga produsen dagashi terbesar Jepang — datang dengan misi merekrut sang ayah untuk perusahaan keluarganya. Ayah setuju dengan satu syarat: Hotaru harus membuat Kokonotsu mencintai dagashi dan mau mewarisi toko. Hotaru yang fanatik berat dengan dagashi kemudian menghabiskan setiap hari memperkenalkan berbagai snack tradisional kepada Kokonotsu dengan penuh semangat yang sering berlebihan. Setiap episode adalah petualangan mengenal satu atau dua dagashi tertentu dengan sejarah dan cara makannya yang unik — edukasi snack yang dikemas dengan komedi dan romansa ringan.",
        "rating": 7.1,
        "genres": ["Comedy", "Romance", "School", "Seinen", "Slice of Life"]
    },
    {
        "title": "Denki-gai no Honya-san",
        "synopsis": "Umanohone adalah toko buku dan manga yang terletak di distrik serupa Akihabara. Para karyawannya adalah kumpulan orang-orang dengan kepribadian yang sangat unik: Hio-tan yang polos dan canggung, Sensei yang mangaka doujin yang selalu melewati deadline, Kantoku yang sangat pemalu namun membaca buku dewasa, Sommelier yang bisa merekomendasikan buku apapun hanya dari melihat pelanggan, dan lainnya. Keseharian mereka di toko — menghadapi pelanggan aneh, mengejar deadline, acara special sale yang chaos, hingga hubungan-hubungan romantis yang berkembang perlahan — menjadi bahan komedi slice of life yang hangat. Anime untuk pecinta manga dan budaya akiba yang menangkap atmosfer toko buku manga dengan affectionate dan akurat.",
        "rating": 7.1,
        "genres": ["Comedy", "Romance", "Seinen", "Slice of Life"]
    },
    {
        "title": "Maou no Ore ga Dorei Elf wo Yome ni Shitanda ga, Dou Medereba Ii?",
        "synopsis": "Zagan adalah penyihir muda yang sangat ditakuti — kemampuan sihirnya luar biasa namun kepribadiannya antisosial ekstrem karena sejak kecil tidak pernah punya teman. Di lelang gelap para penyihir hitam, ia melihat seorang budak elf silver-haired bernama Nephy yang memiliki kecantikan luar biasa dan spontan menghabiskan semua tabungannya untuk membelinya. Sekarang ia punya 'istri' elf yang ia tidak tahu cara berinteraksi dengannya. Sementara Nephy yang sudah lama diperlakukan buruk tidak bisa mempercayai niat baik siapapun. Keduanya sama-sama tidak punya pengalaman dengan hubungan manusia yang normal — Zagan terus mencoba mengungkapkan perasaannya dengan cara yang canggung, dan Nephy terus salah menginterpretasikan semuanya sebagai ancaman.",
        "rating": 7.1,
        "genres": ["Comedy", "Fantasy", "Magic", "Romance", "Seinen"]
    },
    {
        "title": "Princess Connect! Re:Dive",
        "synopsis": "Yuuki adalah pemuda yang jatuh dari langit ke dunia Astraea tanpa ingatan apapun — bahkan cara berbicara dan berjalan pun harus dipelajari ulang. Kokkoro, gadis elf putih kecil, sudah menunggunya karena ia adalah 'tuan' yang harus ia layani dan pandu. Bersama mereka bergabung Pecorine — gadis dengan nafsu makan luar biasa dan kekuatan memukul yang dahsyat namun berhati paling tulus — dan Karyl si kucing yang misterius dan memiliki agenda tersembunyi. Keempat orang ini membentuk guild Gourmet Guild yang lebih sering mencari makanan enak daripada quest berbahaya. Di balik kisah ringan dan penuh makan-makan, tersimpan misteri besar tentang identitas asli Pecorine dan konspirasi yang mengancam seluruh kerajaan.",
        "rating": 7.6,
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Game", "Harem", "Slice of Life"]
    },
    {
        "title": "Henjin no Salad Bowl",
        "synopsis": "Lulutia adalah putri dari dunia sihir yang jatuh ke dunia modern Jepang saat melarikan diri dari pengejaran. Ia bertemu Sousuke Kaburagi, detektif swasta yang mengkhususkan diri membantu orang-orang yang berada di titik paling rendah dalam hidup mereka. Sousuke memutuskan membantu Lulutia beradaptasi dengan kehidupan modern sambil mencari cara mengembalikannya ke dunianya — atau mencari cara agar ia bisa hidup di sini. Sementara itu berbagai karakter dari dunia fantasi lain juga mulai berdatangan ke kota yang sama karena alasan masing-masing. Slice of life komedi yang hangat tentang orang-orang dari latar belakang sangat berbeda yang menemukan cara untuk saling membantu dan membentuk komunitas kecil yang unik di kota biasa.",
        "rating": 7.2,
        "genres": ["Comedy", "Fantasy", "Slice of Life", "Seinen"]
    },
    {
        "title": "Oroka na Tenshi wa Akuma to Odoru",
        "synopsis": "Akutsu Lily, iblis muda yang ambisius, berencana merasuki malaikat agar bisa menguasai surga dari dalam. Rencananya berjalan tidak sesuai harapan — alih-alih berhasil merasuki, ia malah terjebak dalam situasi di mana malaikat Ainosuke Nikaido mengetahui eksistensinya. Ainosuke yang polos dan tulus justru tidak ingin mengusir Lily — ia malah ingin berteman dan berusaha keras memenangkan hati si iblis dengan cara yang tulus. Lily yang terbiasa dengan pengkhianatan dan kelicikan dunia iblis sama sekali tidak tahu cara menghadapi ketulusan yang tidak ada agenda tersembunyi. Komedi romantis tentang iblis yang dikalahkan bukan dengan pertarungan melainkan dengan kebaikan, dan malaikat yang tidak mengerti kenapa usahanya terus ditolak.",
        "rating": 7.4,
        "genres": ["Comedy", "Romance", "Supernatural", "Shounen"]
    },
    {
        "title": "Himegoto",
        "synopsis": "Hime Arikawa adalah siswa SMA laki-laki yang mewarisi hutang luar biasa besar dari orang tuanya yang kabur. Saat hampir ditagih paksa oleh penagih hutang, ia diselamatkan oleh tiga anggota dewan siswa perempuan. Harga penyelamatannya: ia harus menjadi pelayan dewan siswa selama tiga tahun SMA-nya, dan yang lebih mengejutkan, ia harus mengenakan seragam perempuan setiap harinya. Hime yang sebenarnya memiliki wajah dan penampilan yang sangat feminin ternyata cocok sekali dengan pakaian perempuan sehingga hampir tidak ada yang menyadari ia sebenarnya laki-laki. Serial komedi pendek yang mengeksplor situasi crossdressing dengan humor ringan dan interaksi yang menggemaskan antara Hime dan para anggota dewan siswa.",
        "rating": 6.8,
        "genres": ["Comedy", "School", "Seinen", "Slice of Life"]
    },
    {
        "title": "Astarotte no Omocha!",
        "synopsis": "Astarotte Ygvar adalah putri kecil Succubus berusia 10 tahun yang sangat membenci laki-laki — yang ironisnya sangat bermasalah karena Succubus membutuhkan esensi laki-laki untuk bertahan hidup. Atas desakan sang ibu dan tradisi kerajaan, ia terpaksa mulai membangun harem — syaratnya, satu-satunya laki-laki yang ia mau adalah yang datang dari Yggdrasil (pohon dunia). Naoya Touhara, pria muda dari dunia manusia, dipanggil ke dunia iblis bersama putrinya Asuha yang sebaya dengan Lotte. Meski Lotte awalnya sangat menolak dan membenci Naoya, interaksi sehari-hari perlahan mengikis prasangkanya. Slice of life fantasi yang hangat dengan hubungan keluarga non-konvensional sebagai inti ceritanya.",
        "rating": 6.8,
        "genres": ["Comedy", "Fantasy", "Romance", "Seinen", "Slice of Life"]
    },
    {
        "title": "Bokusatsu Tenshi Dokuro-chan",
        "synopsis": "Kusakabe Sakura adalah siswa SMA biasa yang tiba-tiba kedatangan tamu dari masa depan: Dokuro Mitsukai, malaikat muda berambut pirang bersenjata gada berduri bernama Excalibolg. Ternyata di masa depan, Sakura akan menciptakan teknologi yang membuat semua perempuan berhenti menua setelah usia 12 tahun — sesuatu yang melanggar aturan surga. Dokuro dikirim untuk membunuhnya, namun ia memutuskan tinggal bersama Sakura dan melindunginya dari malaikat pembunuh lainnya. Masalahnya, Dokuro sendiri terus membunuh Sakura secara tidak sengaja dengan gada Excalibolg-nya setiap hari, lalu menghidupkannya kembali dengan mantra pemulihan. Komedi gelap ultra-violent yang sangat absurd dan tidak serius sama sekali.",
        "rating": 6.7,
        "genres": ["Comedy", "Ecchi", "Fantasy", "Romance", "School", "Seinen", "Supernatural"]
    },
    {
        "title": "Mangaka-san to Assistant-san to The Animation",
        "synopsis": "Aito Yuuki adalah mangaka manga ecchi yang sangat berbakat namun punya kebiasaan yang sangat merepotkan: ia selalu meminta asisten wanitanya, Ashisu Sahoto, untuk menjadi model langsung bagi pose-pose yang ingin ia gambar — tidak peduli betapa tidak nyaman atau memalukan posenya. Ashisu yang profesional dan sabar selalu menuruti dengan wajah merah padam. Serial komedi pendek ini mengikuti dinamika lucu antara mangaka yang terobsesi akurasi gambar dengan cara paling tidak profesional dan asisten yang entah mengapa masih bertahan. Juga menampilkan berbagai karakter pendukung dengan kepribadian unik yang menambah kekacauan.",
        "rating": 6.7,
        "genres": ["Comedy", "Ecchi", "Romance", "Seinen", "Slice of Life"]
    },
    {
        "title": "Super Crooks",
        "synopsis": "Johnny Bolt adalah penjahat super dengan kemampuan mengendalikan listrik yang sudah masuk penjara berkali-kali karena selalu ketahuan. Saat pacarnya terjebak hutang kepada kriminal berbahaya, Johnny berkumpul kembali dengan tim lama mentor-nya dan merekrut beberapa penjahat super baru untuk melakukan satu heist besar terakhir: merampok Salamander, kriminal paling berbahaya dan dilindungi sihir di Las Vegas. Untuk mencuri dari seseorang yang ditetapkan tidak bisa dirampok, mereka harus menyusun rencana yang berlapis dan mempertaruhkan segalanya. Adaptasi komik Mark Millar ini menampilkan ensemble karakter penjahat yang lovable, aksi yang stylish, dan twist-twist yang mengejutkan dalam cerita heist yang solid.",
        "rating": 7.3,
        "genres": ["Action", "Adventure", "Comedy", "Sci-Fi", "Super Power", "Seinen"]
    },
    {
        "title": "Koisuru One Piece",
        "synopsis": "Spin-off romantis dari dunia One Piece yang mengikuti kisah-kisah cinta para karakter ikonik di seluruh Grand Line. Dengan gaya chibi yang menggemaskan, serial pendek ini mengeksplorasi momen-momen manis dan canggung yang tidak sempat ditampilkan dalam seri utama — dari perasaan-perasaan yang tersembunyi, momen kebersamaan yang tidak terduga, hingga interaksi-interaksi yang mengundang senyum. Untuk penggemar One Piece, ini adalah bonus melihat karakter favorit mereka dalam konteks yang lebih ringan dan penuh kehangatan, dengan twist komedi yang tetap setia pada kepribadian unik masing-masing karakter dari Straw Hat Pirates dan sekitarnya.",
        "rating": 7.0,
        "genres": ["Comedy", "Fantasy", "Romance", "Adventure", "Shounen"]
    },
    {
        "title": "Ple Ple Pleiades x Kagejitsu!",
        "synopsis": "Crossover parodi antara dua anime populer — Overlord dan The Eminence in Shadow — yang mempertemukan karakter-karakter dari kedua seri dalam situasi sehari-hari yang konyol dan tidak serius sama sekali. Ainz Ooal Gown dan Cid Kagenou, dua karakter yang sama-sama suka berpose dramatis dan bicara tentang rencana besar mereka, dipaksa berinteraksi dalam berbagai skenario absurd. Serial pendek ini adalah murni fanservice komedi untuk penggemar kedua seri — penuh referensi internal, lelucon tentang trope isekai dan over-powered protagonist, serta chemistry menggelikan antara karakter-karakter yang sebenarnya sangat mirip satu sama lain.",
        "rating": 7.0,
        "genres": ["Comedy", "Fantasy", "Parody", "Seinen"]
    },
        {
        "title": "Arifureta Shokugyou de Sekai Saikyou",
        "synopsis": "Hajime Nagumo adalah siswa lemah di antara sekelompok siswa SMA yang dipindahkan ke dunia fantasi. Saat eksplorasi dungeon, ia dikhianati oleh rekan satu timnya dan jatuh ke jurang terdalam — Great Orcus Labyrinth — yang dipenuhi monster paling berbahaya. Ditinggal sendirian, hampir mati, dan tanpa kemampuan bertarung yang berarti, Hajime terpaksa memakan daging monster untuk bertahan hidup. Proses itu secara perlahan mengubahnya — fisik maupun mentalnya — menjadi sesuatu yang jauh berbeda dari sebelumnya. Dengan kombinasi kemampuan transmutation yang dianggap remeh dan keberanian putus asa, ia mulai membangun kekuatan dari nol dengan cara yang brutal dan tidak konvensional. Perjalanannya menembus dungeon mematikan itu juga mempertemukannya dengan Yue, vampir kuno yang terjebak di dasar labyrinth.",
        "rating": 6.9,
        "genres": ["Action", "Adventure", "Fantasy", "Harem", "Romance", "Isekai", "Shounen"]
    },
    {
        "title": "Mahou Shoujo Ore",
        "synopsis": "Saki Uno adalah gadis SMA yang ingin mengikuti jejak ibunya menjadi idol top. Suatu hari ia bertemu makhluk berbadan besar yang mengaku sebagai manajer iblis bernama Kokoro-chan, yang mengungkapkan bahwa ibu Saki dulunya adalah Magical Girl. Saat orang yang ia suka — Mohiro, kakak dari sahabatnya — diculik oleh monster, Saki menerima tawaran menjadi Magical Girl. Kejutannya: transformasi Magical Girl mengubahnya menjadi... pria berotot besar dengan kostum rumbai-rumbai mungil. Meski terkejut, Saki tetap berjuang sebagai Magical Girl dalam wujud tersebut. Semakin kacau saat sahabatnya Sakuyo juga ikut menjadi Magical Girl dengan kondisi yang sama. Parodi cerdas genre Magical Girl yang bermain dengan ekspektasi penonton dengan cara yang absurd dan sangat menghibur.",
        "rating": 6.6,
        "genres": ["Comedy", "Magic", "Parody", "Romance", "Seinen"]
    },
    {
        "title": "Maria Holic",
        "synopsis": "Kanako Miyamae mendaftar ke SMA Ame no Kisaki — sekolah Katolik campuran yang sama di mana orang tua almarhum-nya bertemu dan jatuh cinta — dengan harapan menemukan jodohnya di sana. Ia juga menyimpan rahasia: ia alergi terhadap laki-laki hingga kulitnya melepuh saat menyentuh mereka, dan sebenarnya ia lebih tertarik pada perempuan. Di hari pertama, ia terpesona pada Mariya Shidou, siswa tampan berpenampilan sempurna yang tampak seperti putri dari surga. Namun Kanako menangkap sebuah petunjuk — dan Mariya mengakui bahwa ia adalah laki-laki yang menyamar sebagai perempuan untuk memenangkan taruhan dengan mendiang neneknya. Mariya mengancam akan membongkar perasaan Kanako jika ia membocorkan rahasianya, sehingga Kanako terpaksa merahasiakan identitas asli Mariya sambil terus menjadi korban kenakalan dan manipulasi Mariya setiap harinya.",
        "rating": 7.0,
        "genres": ["Comedy", "Romance", "School", "Seinen"]
    },
]

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS anime_genres")
    c.execute("DROP TABLE IF EXISTS anime")
    c.execute("DROP TABLE IF EXISTS genres")

    c.execute("""
        CREATE TABLE genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)

    c.execute("""
        CREATE TABLE anime (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            synopsis TEXT,
            rating REAL,
            image_url TEXT DEFAULT NULL
        )
    """)

    c.execute("""
        CREATE TABLE anime_genres (
            anime_id INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (anime_id) REFERENCES anime(id),
            FOREIGN KEY (genre_id) REFERENCES genres(id),
            PRIMARY KEY (anime_id, genre_id)
        )
    """)

    for genre in GENRES:
        c.execute("INSERT OR IGNORE INTO genres (name) VALUES (?)", (genre,))

    for anime in ANIME_LIST:
        c.execute(
            "INSERT INTO anime (title, synopsis, rating) VALUES (?, ?, ?)",
            (anime["title"], anime["synopsis"], anime["rating"])
        )
        anime_id = c.lastrowid
        for genre_name in anime["genres"]:
            genre_row = c.execute("SELECT id FROM genres WHERE name = ?", (genre_name,)).fetchone()
            if genre_row:
                c.execute("INSERT OR IGNORE INTO anime_genres (anime_id, genre_id) VALUES (?, ?)",
                          (anime_id, genre_row[0]))

    conn.commit()
    conn.close()
    print(f"✅ Database berhasil dibuat dengan {len(ANIME_LIST)} anime!")

if __name__ == "__main__":
    init_db()