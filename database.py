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
        "synopsis": "Raku Ichijou, putra yakuza, terpaksa berpura-pura pacaran dengan Chitoge Kirisaki, putri bos geng rival, demi menjaga perdamaian antar kelompok. Namun hatinya sebenarnya menyukai Kosaki Onodera.",
        "rating": 7.6,
        "image_url": "https://cdn.myanimelist.net/images/anime/1893/93591.jpg",
        "genres": ["Romance", "Comedy", "School", "Harem", "Shounen"]
    },
    {
        "title": "Yamada-kun to 7-nin no Majo",
        "synopsis": "Ryu Yamada menemukan bahwa ia bisa bertukar tubuh dengan orang lain lewat ciuman. Ia kemudian terlibat dalam pencarian 7 penyihir di sekolahnya.",
        "rating": 7.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/72472.jpg",
        "genres": ["Romance", "Comedy", "School", "Magic", "Supernatural", "Harem", "Shounen"]
    },
    {
        "title": "Isekai wa Smartphone to Tomo ni",
        "synopsis": "Touya Mochizuki tewas karena kelalaian Tuhan dan dikirim ke dunia fantasi dengan membawa smartphone yang serba bisa. Ia menjalani kehidupan santai sambil mengumpulkan harem.",
        "rating": 6.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/1535/91203.jpg",
        "genres": ["Adventure", "Fantasy", "Romance", "Harem", "Isekai", "Magic", "Comedy"]
    },
    {
        "title": "Kono Subarashii Sekai ni Shukufuku wo!",
        "synopsis": "Kazuma Satou mati secara memalukan dan diberi pilihan untuk bereinkarnasi di dunia fantasi bersama dewi Aqua yang keras kepala. Petualangan kacau pun dimulai.",
        "rating": 8.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/8/77831.jpg",
        "genres": ["Comedy", "Fantasy", "Adventure", "Magic", "Isekai", "Parody", "Supernatural", "Shounen"]
    },
    {
        "title": "Trinity Seven",
        "synopsis": "Arata Kasuga masuk sekolah sihir dan bertemu 7 penyihir wanita yang disebut Trinity Seven. Ia harus menguasai sihir untuk menyelamatkan sepupunya.",
        "rating": 7.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/67177.jpg",
        "genres": ["Action", "Comedy", "Fantasy", "Magic", "Romance", "Harem", "School", "Ecchi", "Shounen"]
    },
    {
        "title": "Beelzebub",
        "synopsis": "Tatsumi Oga, murid paling berandal di sekolahnya, tiba-tiba harus menjadi ayah asuh bagi bayi iblis bernama Beelzebub, putra Raja Iblis.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/33830.jpg",
        "genres": ["Action", "Comedy", "Fantasy", "School", "Supernatural", "Shounen"]
    },
    {
        "title": "Saenai Heroine no Sodatekata",
        "synopsis": "Tomoya Aki, otaku berat, ingin membuat visual novel dan merekrut teman-teman wanitanya yang ternyata berbakat untuk membantunya.",
        "rating": 7.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/9/71063.jpg",
        "genres": ["Romance", "Comedy", "School", "Harem", "Ecchi", "Seinen"]
    },
    {
        "title": "Blend S",
        "synopsis": "Maika Sakuranomiya bekerja di kafe bertema kepribadian unik. Meski aslinya baik hati, tatapannya yang sadis membuatnya cocok berperan sebagai karakter tsundere.",
        "rating": 7.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/1329/92762.jpg",
        "genres": ["Comedy", "Slice of Life", "Romance", "School"]
    },
    {
        "title": "Eromanga-sensei",
        "synopsis": "Masamune Izumi adalah penulis light novel yang suatu hari menyadari bahwa illustrator anonimnya, Eromanga-sensei, ternyata adalah adik tirinya sendiri yang selalu mengurung diri.",
        "rating": 6.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/1893/85400.jpg",
        "genres": ["Comedy", "Drama", "Romance", "Ecchi", "Slice of Life", "Shounen"]
    },
    {
        "title": "Kimi no Na wa",
        "synopsis": "Dua remaja, Mitsuha dan Taki, misterius bertukar tubuh secara acak saat tidur. Mereka pun mencoba menemukan satu sama lain di kehidupan nyata.",
        "rating": 9.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/80291.jpg",
        "genres": ["Drama", "Romance", "Supernatural", "Mystery"]
    },
    {
        "title": "Sakamoto Desu ga?",
        "synopsis": "Sakamoto adalah siswa sempurna yang selalu tampil keren dalam segala situasi. Para pemuda yang mencoba menjatuhkannya justru akhirnya kagum padanya.",
        "rating": 7.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/11/77729.jpg",
        "genres": ["Comedy", "School", "Slice of Life", "Seinen"]
    },
    {
        "title": "Aho Girl",
        "synopsis": "Yoshiko Hanabatake adalah gadis yang sangat bodoh dan selalu membuat onar. Sahabatnya sejak kecil, A-kun, selalu kelelahan menghadapi kelakuannya.",
        "rating": 7.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/1905/90685.jpg",
        "genres": ["Comedy", "School", "Ecchi", "Shounen"]
    },
    {
        "title": "Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu",
        "synopsis": "Maple, pemain baru game VRMMO, memfokuskan semua statnya ke pertahanan. Hasilnya ia menjadi karakter yang hampir tak terkalahkan dengan cara yang tidak terduga.",
        "rating": 7.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/1123/105023.jpg",
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Game"]
    },
    {
        "title": "Prison School",
        "synopsis": "Lima siswa laki-laki pertama di sekolah putri yang baru membuka diri, tertangkap mengintip dan dihukum di penjara sekolah oleh Dewan Eksekutif bawah tanah yang kejam.",
        "rating": 7.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/73178.jpg",
        "genres": ["Comedy", "Ecchi", "Romance", "School", "Seinen"]
    },
    {
        "title": "Himouto! Umaru-chan",
        "synopsis": "Umaru Doma tampak sempurna di luar, tapi di rumah ia berubah menjadi gadis malas yang hanya ingin main game, nonton anime, dan makan keripik.",
        "rating": 7.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/5/73655.jpg",
        "genres": ["Comedy", "Slice of Life", "School", "Seinen"]
    },
    {
        "title": "Go-Toubun no Hanayome",
        "synopsis": "Fuutarou Uesugi menjadi tutor bagi quintuplet bersaudara yang cantik tapi malas belajar. Salah satu dari mereka akan menjadi istrinya di masa depan.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1839/97048.jpg",
        "genres": ["Romance", "Comedy", "School", "Harem", "Shounen"]
    },
    {
        "title": "Ryuuou no Oshigoto!",
        "synopsis": "Yaichi Kuzuryuu, Ryuuou (Raja Naga) termuda dalam shogi, kedatangan anak perempuan 9 tahun yang ingin menjadi muridnya dan mengubah hidupnya.",
        "rating": 7.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/89521.jpg",
        "genres": ["Comedy", "Ecchi", "Game", "Romance", "Slice of Life"]
    },
    {
        "title": "Chuunibyou demo Koi ga Shitai!",
        "synopsis": "Yuuta Togashi ingin melupakan masa chuunibyou-nya, tapi malah bertemu Rikka Takanashi yang masih hidup dalam delusinya sendiri dan menyeret Yuuta kembali.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/8/39813.jpg",
        "genres": ["Romance", "Comedy", "Drama", "School", "Slice of Life", "Fantasy"]
    },
    {
        "title": "Dumbbell Nan Kilo Moteru?",
        "synopsis": "Hibiki Sakura ingin menurunkan berat badan dan bergabung ke gym, di mana ia bertemu banyak karakter unik dan belajar tentang olahraga dan nutrisi.",
        "rating": 7.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/1942/95837.jpg",
        "genres": ["Comedy", "Ecchi", "School", "Slice of Life", "Sports", "Seinen"]
    },
    {
        "title": "Kanojo, Okarishimasu",
        "synopsis": "Kazuya Kinoshita menggunakan layanan sewa pacar setelah diputus, dan terjebak dalam hubungan rumit dengan Chizuru Mizuhara, gadis yang ia sewa.",
        "rating": 7.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/1485/107693.jpg",
        "genres": ["Romance", "Comedy", "School", "Shounen"]
    },
    {
        "title": "Kaguya-sama wa Kokurasetai",
        "synopsis": "Dua siswa paling brilian di sekolah saling menyukai tapi tidak mau mengakuinya duluan. Mereka terus bersiasat agar pihak lawanlah yang menyatakan cinta lebih dulu.",
        "rating": 8.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/1295/106551.jpg",
        "genres": ["Romance", "Comedy", "School", "Psychological", "Seinen"]
    },
    {
        "title": "Danshi Koukousei no Nichijou",
        "synopsis": "Keseharian tiga siswa SMA laki-laki dan teman-temannya yang selalu penuh dengan situasi konyol, aneh, dan menggelikan.",
        "rating": 8.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/4/39717.jpg",
        "genres": ["Comedy", "School", "Slice of Life", "Shounen"]
    },
    {
        "title": "Re:Zero kara Hajimeru Isekai Seikatsu",
        "synopsis": "Subaru Natsuki tiba-tiba dipindahkan ke dunia fantasi dan menemukan ia memiliki kemampuan untuk kembali ke titik tertentu setelah mati, sebuah anugerah sekaligus kutukan.",
        "rating": 8.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/11/79410.jpg",
        "genres": ["Drama", "Fantasy", "Psychological", "Mystery", "Thriller", "Isekai", "Supernatural"]
    },
    {
        "title": "Shigatsu wa Kimi no Uso",
        "synopsis": "Pianis berbakat Kousei Arima kehilangan kemampuan mendengar musiknya sendiri setelah ibunya meninggal. Perjumpaan dengan biolis ceria Kaori Miyazono mengubah hidupnya.",
        "rating": 8.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/67177.jpg",
        "genres": ["Drama", "Music", "Romance", "School", "Slice of Life", "Shounen"]
    },
    {
        "title": "High School DxD",
        "synopsis": "Issei Hyoudou, remaja pervert, dibunuh oleh pacar pertamanya yang ternyata setan. Ia dibangkitkan oleh Rias Gremory dan menjadi iblis kelas rendah dalam grupnya.",
        "rating": 7.6,
        "image_url": "https://cdn.myanimelist.net/images/anime/4/37883.jpg",
        "genres": ["Action", "Comedy", "Ecchi", "Fantasy", "Harem", "Romance", "School", "Supernatural", "Shounen"]
    },
    {
        "title": "Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai",
        "synopsis": "Sakuta Azusagawa bertemu Mai Sakurajima yang mengenakan kostum kelinci dan tidak terlihat oleh siapapun karena fenomena aneh 'Puberty Syndrome'.",
        "rating": 8.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/1301/93586.jpg",
        "genres": ["Drama", "Mystery", "Romance", "School", "Supernatural", "Sci-Fi"]
    },
    {
        "title": "Uzaki-chan wa Asobitai!",
        "synopsis": "Hana Uzaki terus mengganggu dan mengajak seniornya Sakurai untuk menghabiskan waktu bersama karena ia pikir Sakurai terlalu kesepian.",
        "rating": 7.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/1429/106864.jpg",
        "genres": ["Comedy", "Romance", "Ecchi", "Slice of Life", "School", "Seinen"]
    },
    {
        "title": "Enen no Shouboutai",
        "synopsis": "Di dunia di mana manusia bisa tiba-tiba terbakar menjadi 'Infernal', Shinra Kusakabe bergabung dengan pemadam kebakaran khusus untuk membasmi ancaman ini.",
        "rating": 7.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/1143/103841.jpg",
        "genres": ["Action", "Fantasy", "Mystery", "Supernatural", "Shounen"]
    },
    {
        "title": "Mujaki no Rakuen",
        "synopsis": "Shouta Tanaka, pria dewasa gagal, kembali ke masa kecilnya dan bertemu kembali dengan teman-teman lamanya yang kini masih kecil.",
        "rating": 6.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/1864/93535.jpg",
        "genres": ["Comedy", "Ecchi", "Romance", "Seinen"]
    },
    {
        "title": "Boku wa Tomodachi ga Sukunai",
        "synopsis": "Kodaka Hasegawa yang kesulitan berteman bergabung dengan klub 'Rinjinbu' yang anggotanya adalah orang-orang yang juga tidak punya teman.",
        "rating": 7.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/10/33287.jpg",
        "genres": ["Comedy", "Ecchi", "Harem", "Romance", "School", "Seinen"]
    },
    {
        "title": "Kakegurui",
        "synopsis": "Di sekolah elit Hyakkaou, hierarki ditentukan oleh kemampuan berjudi. Yumeko Jabami, gadis baru yang gemar berjudi dengan cara ekstrem, mengacaukan segalanya.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1877/93289.jpg",
        "genres": ["Drama", "Game", "Mystery", "Psychological", "School", "Thriller", "Seinen"]
    },
    {
        "title": "Girls und Panzer",
        "synopsis": "Miho Nishizumi bergabung dengan tim tankery sekolahnya meski ia punya trauma dengan olahraga tersebut. Ia pun memimpin tim yang kurang pengalaman menuju kejuaraan nasional.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1/42832.jpg",
        "genres": ["Action", "Comedy", "Military", "School", "Sports"]
    },
    {
        "title": "Youjo Senki",
        "synopsis": "Seorang eksekutif kejam terlahir kembali sebagai anak perempuan kecil di dunia yang mirip Eropa era Perang Dunia. Ia menjadi perwira militer paling berbahaya.",
        "rating": 8.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/1375/93332.jpg",
        "genres": ["Action", "Fantasy", "Historical", "Military", "Isekai"]
    },
    {
        "title": "Azur Lane",
        "synopsis": "Personifikasi kapal perang dari berbagai negara bersatu melawan ancaman alien misterius bernama Siren, namun perpecahan muncul di antara mereka.",
        "rating": 6.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/1063/104067.jpg",
        "genres": ["Action", "Military", "Sci-Fi", "Game"]
    },
    {
        "title": "Great Pretender",
        "synopsis": "Makoto Edamura, penipu kelas teri Jepang, tidak sengaja menipu Laurent Thierry, penipu kelas dunia, dan terpaksa bergabung dalam misi penipuan berskala internasional.",
        "rating": 8.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/1142/106386.jpg",
        "genres": ["Action", "Adventure", "Comedy", "Mystery", "Thriller", "Seinen"]
    },
    {
        "title": "Overlord",
        "synopsis": "Pemain game MMORPG Yggdrasil terjebak di dalam game saat server shutdown. Ia kini berperan sebagai Ainz Ooal Gown, penguasa guild undead yang paling ditakuti.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/7/88811.jpg",
        "genres": ["Action", "Adventure", "Fantasy", "Magic", "Isekai", "Game", "Supernatural"]
    },
    {
        "title": "Valkyrie no Shokutaku",
        "synopsis": "Para Valkyrie dari mitologi Norse bekerja di sebuah restoran keluarga di Jepang. Kisah slice of life penuh komedi tentang kehidupan mereka sehari-hari.",
        "rating": 6.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/1171/97543.jpg",
        "genres": ["Comedy", "Fantasy", "Slice of Life", "Seinen"]
    },
    {
        "title": "Date A Live",
        "synopsis": "Shido Itsuka bisa menyegel kekuatan Spirit berbahaya dengan cara membuat mereka jatuh cinta padanya. Ia pun menjalani 'kencan' dengan berbagai Spirit demi perdamaian.",
        "rating": 7.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/10/44650.jpg",
        "genres": ["Action", "Comedy", "Fantasy", "Harem", "Romance", "School", "Sci-Fi", "Shounen", "Ecchi"]
    },
    {
        "title": "Wotaku ni Koi wa Muzukashii",
        "synopsis": "Narumi, otaku yang menyembunyikan hobinya, mulai bekerja di kantor baru dan bertemu Hirotaka, teman masa kecil yang gamer berat. Hubungan mereka berkembang menjadi romansa.",
        "rating": 7.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/1900/91433.jpg",
        "genres": ["Comedy", "Romance", "Slice of Life", "Josei"]
    },
    {
        "title": "Goblin Slayer",
        "synopsis": "Seorang adventurer yang hanya berfokus membunuh goblin membantu seorang Pendeta yang baru memulai petualangannya. Dunia ini jauh lebih gelap dan kejam dari yang dibayangkan.",
        "rating": 7.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/1518/104666.jpg",
        "genres": ["Action", "Adventure", "Fantasy", "Horror", "Mystery", "Seinen"]
    },
    {
        "title": "JoJo no Kimyou na Bouken",
        "synopsis": "Saga epik keluarga Joestar yang bertarung melawan kejahatan lintas generasi, menggunakan kekuatan unik yang terus berkembang dari Hamon hingga Stand.",
        "rating": 8.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/40409.jpg",
        "genres": ["Action", "Adventure", "Fantasy", "Horror", "Mystery", "Supernatural", "Shounen"]
    },
    {
        "title": "Violet Evergarden",
        "synopsis": "Violet Evergarden, mantan prajurit yang kehilangan kedua tangannya, bekerja sebagai 'Auto Memory Doll' untuk menuliskan perasaan orang lain sekaligus mencari makna dari kata 'cinta'.",
        "rating": 8.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/1795/95088.jpg",
        "genres": ["Drama", "Fantasy", "Slice of Life", "Mystery"]
    },
    {
        "title": "One Punch Man",
        "synopsis": "Saitama bisa mengalahkan semua musuh hanya dengan satu pukulan. Tapi kekuatan tak tertandingi justru membuatnya merasa bosan dan hampa.",
        "rating": 8.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/12/76049.jpg",
        "genres": ["Action", "Comedy", "Parody", "Super Power", "Supernatural", "Seinen"]
    },
    {
        "title": "Dr. Stone",
        "synopsis": "Seluruh umat manusia membatu secara misterius. Ribuan tahun kemudian, Senku Ishigami bangkit dan bertekad membangun kembali peradaban menggunakan ilmu pengetahuan.",
        "rating": 8.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/1613/102576.jpg",
        "genres": ["Action", "Adventure", "Comedy", "Sci-Fi", "Shounen"]
    },
    {
        "title": "Shingeki no Kyojin",
        "synopsis": "Manusia tinggal di balik tembok raksasa untuk berlindung dari Titan pemangsa manusia. Eren Yeager bersumpah membasmi semua Titan setelah ibunya dimakan.",
        "rating": 9.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/10/47347.jpg",
        "genres": ["Action", "Drama", "Fantasy", "Horror", "Military", "Mystery", "Shounen", "Thriller"]
    },
    {
        "title": "Hataraku Saibou!!",
        "synopsis": "Kehidupan dalam tubuh manusia divisualisasikan sebagai kota ramai di mana sel-sel darah dan imun bekerja keras setiap hari melawan kuman dan penyakit.",
        "rating": 7.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/1532/104320.jpg",
        "genres": ["Action", "Comedy", "Educational", "Shounen"]
    },
    {
        "title": "Josee to Tora to Sakana-tachi",
        "synopsis": "Tsuneo, mahasiswa pecinta menyelam, bertemu Josee, gadis yang tidak bisa berjalan dan mengurung diri dalam dunianya sendiri. Persahabatan mereka perlahan berkembang menjadi cinta.",
        "rating": 8.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/1839/111291.jpg",
        "genres": ["Drama", "Romance", "Slice of Life"]
    },
    {
        "title": "Ore no Kanojo to Osananajimi ga Shuraba Sugiru",
        "synopsis": "Eita Kidou dipaksa berpacaran palsu oleh gadis cantik Masuzu Natsukawa. Namun masalah bertambah ketika masa lalunya yang memalukan dan perasaan teman lamanya ikut terlibat.",
        "rating": 7.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/50581.jpg",
        "genres": ["Comedy", "Harem", "Romance", "School", "Shounen"]
    },
    {
        "title": "Shuumatsu no Walküre",
        "synopsis": "Para dewa memutuskan untuk memusnahkan umat manusia. 13 manusia terkuat dalam sejarah ditantang bertarung melawan 13 dewa dalam turnamen penentuan nasib manusia.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1733/111514.jpg",
        "genres": ["Action", "Drama", "Fantasy", "Historical", "Martial Arts", "Supernatural", "Seinen"]
    },
    {
        "title": "Gokushufudou",
        "synopsis": "Tatsu, mantan yakuza paling ditakuti, pensiun dan menjadi ibu rumah tangga demi istrinya. Ia berusaha keras menjadi suami yang baik sambil berurusan dengan masa lalunya.",
        "rating": 8.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/1879/113144.jpg",
        "genres": ["Action", "Comedy", "Slice of Life", "Seinen"]
    },
    {
        "title": "Baki",
        "synopsis": "Baki Hanma berlatih keras untuk mengalahkan ayahnya, Yuujirou Hanma, manusia terkuat di dunia. Lima narapidana paling berbahaya kabur dan mencari petarung terkuat.",
        "rating": 7.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/1319/94663.jpg",
        "genres": ["Action", "Adventure", "Martial Arts", "Seinen", "Sports"]
    },
    {
        "title": "Kengan Ashura",
        "synopsis": "Untuk menyelesaikan sengketa bisnis, perusahaan-perusahaan Jepang menyewa petarung bayaran. Tokita Ohma, petarung misterius, bertarung di turnamen Kengan yang brutal.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1303/105338.jpg",
        "genres": ["Action", "Drama", "Martial Arts", "Seinen", "Sports"]
    },
    {
        "title": "No Game No Life",
        "synopsis": "Sora dan Shiro, duo hikikomori jenius, dipindahkan ke dunia di mana segala sesuatu diputuskan melalui permainan. Mereka bertekad menaklukkan semua ras dan menantang Tuhan.",
        "rating": 8.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/5/65187.jpg",
        "genres": ["Adventure", "Comedy", "Fantasy", "Game", "Isekai", "Ecchi", "Shounen"]
    },
    {
        "title": "Ansatsu Kyoushitsu",
        "synopsis": "Kelas 3-E yang terpinggirkan diberi tugas mustahil: membunuh guru mereka, Koro-sensei, makhluk misterius yang mengancam akan menghancurkan bumi.",
        "rating": 8.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/5/73171.jpg",
        "genres": ["Action", "Comedy", "Fantasy", "School", "Shounen"]
    },
    {
        "title": "Arifureta Shokugyou de Sekai Saikyou",
        "synopsis": "Hajime Nagumo, siswa lemah yang dipindahkan ke dunia fantasi, dikhianati dan jatuh ke jurang terdalam. Ia bertahan dan menjadi manusia paling kuat lewat cara yang brutal.",
        "rating": 6.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1711/99636.jpg",
        "genres": ["Action", "Adventure", "Fantasy", "Harem", "Romance", "Isekai", "Shounen"]
    },
    {
        "title": "Fugou Keiji: Balance:Unlimited",
        "synopsis": "Daisuke Kanbe, detektif kaya raya yang menyelesaikan semua masalah dengan uang, dipasangkan dengan Haru Kato, detektif bermoral tinggi yang anti korupsi.",
        "rating": 7.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/1637/106671.jpg",
        "genres": ["Action", "Comedy", "Mystery", "Seinen"]
    },
    {
        "title": "Kore wa Zombie Desu ka?",
        "synopsis": "Ayumu Aikawa dibunuh oleh serial killer dan dibangkitkan sebagai zombie oleh necromancer bernama Eucliwood Hellscythe. Ia pun tidak sengaja menjadi Magical Girl.",
        "rating": 7.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/1335/93373.jpg",
        "genres": ["Action", "Comedy", "Ecchi", "Fantasy", "Harem", "Magic", "Supernatural", "Seinen"]
    },
    {
        "title": "Uchi no Maid ga Uzasugiru!",
        "synopsis": "Bekas anggota JSDF Tsubame Kamoi menjadi pembantu di rumah Misha Takanashi, gadis kecil campuran Rusia-Jepang, dan terus mencoba memeluk Misha meski selalu ditolak.",
        "rating": 7.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/1543/97038.jpg",
        "genres": ["Comedy", "Slice of Life", "Seinen"]
    },
    {
        "title": "Hinamatsuri",
        "synopsis": "Kapsul berisi anak perempuan berkekuatan telekinesis jatuh di kepala anggota Yakuza Yoshifumi Nitta. Ia terpaksa merawatnya dan kehidupan anehnya pun dimulai.",
        "rating": 8.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/1923/90082.jpg",
        "genres": ["Comedy", "Drama", "Sci-Fi", "Seinen", "Slice of Life", "Supernatural"]
    },
    {
        "title": "Mairimashita! Iruma-kun",
        "synopsis": "Iruma Suzuki dijual oleh orang tuanya ke iblis dan diadopsi oleh kakek iblis yang baik hati. Ia harus bertahan hidup di sekolah iblis tanpa ketahuan bahwa ia manusia.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1840/97736.jpg",
        "genres": ["Comedy", "Fantasy", "School", "Supernatural", "Shounen"]
    },
    {
        "title": "The God of High School",
        "synopsis": "Jin Mori berpartisipasi dalam turnamen martial arts skala nasional yang ternyata menyimpan rahasia yang jauh lebih besar dari sekadar kompetisi biasa.",
        "rating": 7.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/1241/108127.jpg",
        "genres": ["Action", "Adventure", "Fantasy", "Martial Arts", "Supernatural", "Shounen"]
    },
    {
        "title": "Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru",
        "synopsis": "Ryuuguin Seiya dipanggil menjadi pahlawan tapi ia sangat berhati-hati hingga berlebihan, menggunakan kekuatan penuh bahkan untuk musuh lemah sekalipun.",
        "rating": 7.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/1629/97963.jpg",
        "genres": ["Adventure", "Comedy", "Fantasy", "Parody", "Isekai"]
    },
    {
        "title": "Uchi no Ko no Tame naraba, Ore wa Moshikashitara Maou mo Taoseru kamo Shirenai",
        "synopsis": "Dale, adventurer terkenal, menemukan anak iblis kecil bernama Latina sendirian di hutan dan memutuskan untuk mengadopsinya sebagai putrinya.",
        "rating": 7.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/1553/98079.jpg",
        "genres": ["Adventure", "Fantasy", "Slice of Life", "Seinen"]
    },
    {
        "title": "Mushoku Tensei: Isekai Ittara Honki Dasu",
        "synopsis": "Seorang pria pengangguran 34 tahun bereinkarnasi di dunia sihir fantasi sebagai Rudeus Greyrat dan bertekad menjalani hidupnya tanpa penyesalan kali ini.",
        "rating": 8.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/1530/117776.jpg",
        "genres": ["Adventure", "Drama", "Fantasy", "Magic", "Romance", "Isekai", "Seinen"]
    },
    {
        "title": "Ijiranaide, Nagatoro-san",
        "synopsis": "Nagatoro, siswi aktif dan jail, senang menggoda dan menjahili senpai-nya yang pemalu dan penyendiri. Namun lambat laun keduanya mulai saling peduli.",
        "rating": 7.6,
        "image_url": "https://cdn.myanimelist.net/images/anime/1197/110449.jpg",
        "genres": ["Comedy", "Romance", "School", "Slice of Life", "Ecchi", "Seinen"]
    },
    {
        "title": "Maou Gakuin no Futekigousha",
        "synopsis": "Anos Voldigoad, Raja Iblis dari 2000 tahun lalu, bereinkarnasi di masa depan hanya untuk menemukan bahwa legenda tentang dirinya telah diputarbalikkan.",
        "rating": 7.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/1474/108224.jpg",
        "genres": ["Action", "Adventure", "Fantasy", "Magic", "School", "Harem", "Supernatural", "Shounen"]
    },
    {
        "title": "Rokudenashi Majutsu Koushi to Akashic Records",
        "synopsis": "Glenn Radars, guru pengganti yang malas, mengajar di akademi sihir bergengsi. Di balik kemalasannya tersimpan kemampuan dan rahasia masa lalu yang mengejutkan.",
        "rating": 7.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/4/37883.jpg",
        "genres": ["Action", "Comedy", "Fantasy", "Magic", "School", "Ecchi"]
    },
    {
        "title": "Jujutsu Kaisen",
        "synopsis": "Yuji Itadori menelan jari Raja Kutukan Ryoumen Sukuna untuk menyelamatkan temannya dan menjadi wadah kutukan terkuat. Ia direkrut untuk memakan semua jari Sukuna sebelum dieksekusi.",
        "rating": 8.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/1171/109222.jpg",
        "genres": ["Action", "Fantasy", "Horror", "School", "Supernatural", "Shounen"]
    },
    {
        "title": "Tensei Shitara Slime Datta Ken",
        "synopsis": "Mikami Satoru dibunuh dan bereinkarnasi sebagai slime di dunia fantasi. Dengan kemampuan menyerap kekuatan orang lain, ia membangun sebuah bangsa yang damai.",
        "rating": 8.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/10/94966.jpg",
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Isekai", "Magic", "Shounen"]
    },
    {
        "title": "Back Street Girls: Gokudolls",
        "synopsis": "Tiga anggota Yakuza yang mengecewakan bos mereka diberi pilihan: mati atau menjadi idol perempuan. Mereka terpaksa memilih operasi ganti kelamin dan berkarir sebagai idol.",
        "rating": 6.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1867/91551.jpg",
        "genres": ["Comedy", "Music", "Seinen"]
    },
    {
        "title": "Asobi Asobase",
        "synopsis": "Tiga siswi SMP membentuk 'Pastimer Club' untuk bermain berbagai permainan sepulang sekolah. Penuh ekspresi wajah ekstrem dan humor hitam yang tidak terduga.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1843/92959.jpg",
        "genres": ["Comedy", "School", "Slice of Life", "Seinen"]
    },
    {
        "title": "Xian Wang de Richang Shenghuo",
        "synopsis": "Wang Ling, siswa SMA biasa, sebenarnya memiliki kekuatan yang melampaui batas dewa. Ia hanya ingin menjalani kehidupan normal tapi kekuatannya selalu bocor secara tidak sengaja.",
        "rating": 7.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/1086/108218.jpg",
        "genres": ["Action", "Comedy", "Fantasy", "School", "Super Power"]
    },
    {
        "title": "Tenkuu Shinpan",
        "synopsis": "Yuri Honjo tiba-tiba terbangun di kota pencakar langit yang ditinggalkan, dikejar oleh pembunuh bertopeng aneh. Ia harus bertahan hidup dan mencari jalan pulang.",
        "rating": 6.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/1051/108756.jpg",
        "genres": ["Action", "Horror", "Mystery", "Psychological", "Thriller", "Seinen"]
    },
    {
        "title": "Grand Blue",
        "synopsis": "Iori Kitahara pindah ke kota pesisir untuk kuliah dan bergabung dengan klub menyelam. Kehidupan kampusnya ternyata dipenuhi minum-minum, ketelanjangan, dan kekacauan.",
        "rating": 8.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/1788/92908.jpg",
        "genres": ["Comedy", "Ecchi", "Romance", "Seinen", "Slice of Life", "Sports"]
    },
    {
        "title": "Kyou kara Ore wa!!",
        "synopsis": "Dua siswa SMA pindahan, Takashi Mitsuhashi dan Shinji Itou, memutuskan untuk menjadi berandalan dan delinquent di sekolah baru mereka dengan cara mereka sendiri.",
        "rating": 8.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/1069/114553.jpg",
        "genres": ["Action", "Comedy", "Romance", "School", "Seinen"]
    },
    {
        "title": "Ao no Exorcist",
        "synopsis": "Rin Okumura adalah putra Iblis Raja Lucifer. Setelah kematian ayah angkatnya, ia bergabung dengan akademi pengusir iblis dan bertekad mengalahkan Iblis itu sendiri.",
        "rating": 7.6,
        "image_url": "https://cdn.myanimelist.net/images/anime/1280/130562.jpg",
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "School", "Supernatural", "Shounen"]
    },
    {
        "title": "Saiki Kusuo no Ψ-nan",
        "synopsis": "Kusuo Saiki adalah psikik dengan kekuatan luar biasa yang hanya ingin hidup biasa dan makan dessert favoritnya. Sayangnya orang-orang aneh terus berdatangan ke hidupnya.",
        "rating": 8.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/80480.jpg",
        "genres": ["Comedy", "School", "Slice of Life", "Super Power", "Supernatural", "Shounen"]
    },
    {
        "title": "Super Crooks",
        "synopsis": "Johnny Bolt, penjahat super berkekuatan listrik, mengumpulkan tim penjahat untuk merampok orang paling berbahaya di Las Vegas dalam satu misi besar terakhir.",
        "rating": 7.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/1545/118180.jpg",
        "genres": ["Action", "Adventure", "Comedy", "Sci-Fi", "Super Power", "Seinen"]
    },
    {
        "title": "Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta",
        "synopsis": "Katarina Claes tersadar bahwa ia bereinkarnasi sebagai penjahat di game otome favoritnya. Semua ending menuju bencana baginya, jadi ia berusaha mengubah takdirnya.",
        "rating": 7.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/1483/108194.jpg",
        "genres": ["Comedy", "Fantasy", "Romance", "Harem", "Magic", "School", "Isekai", "Shoujo"]
    },
    {
        "title": "Record of Ragnarok",
        "synopsis": "Para dewa dari berbagai mitologi memutuskan untuk memusnahkan manusia. Brunhild menantang mereka dalam turnamen Ragnarok di mana 13 manusia terkuat melawan 13 dewa.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1733/111514.jpg",
        "genres": ["Action", "Drama", "Fantasy", "Historical", "Martial Arts", "Supernatural", "Seinen"]
    },
    {
        "title": "Mob Psycho 100",
        "synopsis": "Shigeo 'Mob' Kageyama adalah anak SMP dengan kekuatan psikik luar biasa yang menekan emosinya. Saat emosi mencapai 100%, hasilnya tidak dapat diprediksi.",
        "rating": 8.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1134/75975.jpg",
        "genres": ["Action", "Comedy", "Drama", "Mystery", "Psychological", "School", "Slice of Life", "Super Power", "Supernatural", "Shounen"]
    },
    {
        "title": "Mahou Shoujo Ore",
        "synopsis": "Saki Uno ingin menjadi idol seperti ibunya dulu. Saat monster menyerang, ia menjadi Magical Girl... tapi dalam wujud pria berotot besar.",
        "rating": 6.6,
        "image_url": "https://cdn.myanimelist.net/images/anime/1077/90553.jpg",
        "genres": ["Comedy", "Magic", "Parody", "Romance", "Seinen"]
    },
    {
        "title": "Isekai Maou to Shoukan Shoujo no Dorei Majutsu",
        "synopsis": "Seorang gamer hikikomori ter-summon ke dunia fantasi dalam wujud karakter game-nya, Iblis Raja Diablo. Meski bingung, ia tetap memainkan peran karakternya yang dominan.",
        "rating": 7.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/1759/91687.jpg",
        "genres": ["Adventure", "Comedy", "Ecchi", "Fantasy", "Harem", "Magic", "Romance", "Isekai", "Seinen"]
    },
    {
        "title": "Hataraku Maou-sama!",
        "synopsis": "Iblis Raja Maou Sadao kabur ke dunia modern Jepang dan terpaksa bekerja paruh waktu di McRonalds. Musuh lamanya, Pahlawan Emilia, juga muncul di Tokyo.",
        "rating": 8.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/13/50900.jpg",
        "genres": ["Comedy", "Fantasy", "Romance", "Supernatural", "Seinen"]
    },
    {
        "title": "Boku no Kanojo ga Majimesugiru Sho-bitch na Ken",
        "synopsis": "Akiho Kousaka, gadis terpintar dan tersopan di sekolah, ternyata sangat serius dalam berusaha menjadi kekasih yang baik dengan cara yang jauh melampaui batas kesopanan.",
        "rating": 6.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/88081.jpg",
        "genres": ["Comedy", "Ecchi", "Romance", "School", "Seinen"]
    },
    {
        "title": "Kishuku Gakkou no Juliet",
        "synopsis": "Romio Inuzuka dan Juliet Persia, dua ketua asrama rival, diam-diam menjalin hubungan terlarang karena dua asrama mereka sudah lama bermusuhan.",
        "rating": 7.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/1554/97062.jpg",
        "genres": ["Comedy", "Romance", "School", "Shounen"]
    },
    {
        "title": "Noragami",
        "synopsis": "Yato, dewa pengangguran tanpa kuil, bermimpi memiliki jutaan pengikut. Setelah menyelamatkan Hiyori, ia terlibat dalam berbagai urusan dunia roh yang berbahaya.",
        "rating": 8.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/1357/104691.jpg",
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Supernatural", "Shounen"]
    },
    {
        "title": "Gabriel DropOut",
        "synopsis": "Gabriel White, malaikat terbaik yang dikirim ke bumi untuk memahami manusia, malah kecanduan game online dan menjadi malas. Sementara setan Vignette malah bertingkah seperti malaikat.",
        "rating": 7.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/5/84004.jpg",
        "genres": ["Comedy", "Fantasy", "School", "Slice of Life", "Seinen"]
    },
    {
        "title": "Senpai ga Uzai Kouhai no Hanashi",
        "synopsis": "Futaba Igarashi seringkali kesal dengan senpai-nya Harumi Takeda yang besar dan berisik. Tapi kebersamaan mereka perlahan-lahan menumbuhkan perasaan yang lebih dalam.",
        "rating": 7.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/1284/118408.jpg",
        "genres": ["Comedy", "Romance", "Slice of Life", "Seinen"]
    },
    {
        "title": "Busou Shoujo Machiavellianism",
        "synopsis": "Fudou Nomura masuk sekolah yang dikuasai oleh lima perempuan bersenjata. Ia harus mengalahkan mereka semua atau terpaksa berperilaku feminin seperti siswa laki-laki lainnya.",
        "rating": 7.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/4/37883.jpg",
        "genres": ["Action", "Comedy", "Romance", "School", "Ecchi", "Shounen"]
    },
    {
        "title": "Satsuriku no Tenshi",
        "synopsis": "Rachel, gadis 13 tahun, terbangun di gedung bawah tanah tanpa ingatan. Ia bertemu Zack, pembunuh berantai berpedang sabit, dan keduanya berjanji untuk membantu satu sama lain keluar.",
        "rating": 7.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/1715/91491.jpg",
        "genres": ["Action", "Drama", "Horror", "Mystery", "Psychological", "Thriller", "Supernatural"]
    },
    {
        "title": "Platinum End",
        "synopsis": "Mirai Kakehashi diselamatkan oleh malaikatnya saat mencoba bunuh diri. Ia kemudian terlibat dalam kompetisi antar 13 kandidat yang dipilih dewa untuk menentukan Tuhan selanjutnya.",
        "rating": 6.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/1482/113488.jpg",
        "genres": ["Drama", "Mystery", "Psychological", "Supernatural", "Thriller", "Shounen"]
    },
    {
        "title": "Level E",
        "synopsis": "Alien pangeran dari planet jauh yang sangat cerdas namun super jahil datang ke bumi. Kisah konyol dan penuh akal-akalan pun terjadi pada orang-orang di sekitarnya.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1535/91203.jpg",
        "genres": ["Comedy", "Mystery", "Sci-Fi", "Seinen", "Supernatural"]
    },
    {
        "title": "Fantasy Bishoujo Juniku Ojisan to",
        "synopsis": "Dua sahabat laki-laki dipanggil ke dunia fantasi. Salah satunya berubah menjadi gadis cantik karena kutukan. Mereka berpetualang sambil menghadapi kutukan yang terus memperkuat efeknya.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1085/119706.jpg",
        "genres": ["Adventure", "Comedy", "Fantasy", "Romance", "Magic", "Isekai", "Shounen"]
    },
    {
        "title": "Sewayaki Kitsune no Senko-san",
        "synopsis": "Salaryman lelah bernama Nakano tiba-tiba didatangi Senko-san, rubah setengah dewa yang ingin merawat dan memanjakan hidupnya yang penuh tekanan.",
        "rating": 7.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/1796/96604.jpg",
        "genres": ["Comedy", "Fantasy", "Romance", "Seinen", "Slice of Life", "Supernatural"]
    },
    {
        "title": "Kobayashi-san Chi no Maid Dragon",
        "synopsis": "Kobayashi, programmer wanita, secara tidak sengaja mengundang Tohru, naga kuat dari dunia lain, untuk tinggal bersamanya sebagai pembantu. Kehidupan unik bersama para naga pun dimulai.",
        "rating": 8.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/5/85434.jpg",
        "genres": ["Comedy", "Fantasy", "Slice of Life", "Supernatural", "Seinen"]
    },
    {
        "title": "Yuru Yuri",
        "synopsis": "Empat siswi SMP merebut kembali ruang klub dan mendirikan 'Amusement Club'. Keseharian mereka yang ceria, konyol, dan penuh interaksi menggemaskan pun mengalir tanpa henti.",
        "rating": 7.6,
        "image_url": "https://cdn.myanimelist.net/images/anime/8/39813.jpg",
        "genres": ["Comedy", "School", "Slice of Life", "Seinen"]
    },
    {
        "title": "One Piece",
        "synopsis": "Monkey D. Luffy bercita-cita menjadi Raja Bajak Laut dengan menemukan harta karun terbesar One Piece. Bersama nakama-nakamanya yang beragam, ia menjelajahi Grand Line yang penuh bahaya.",
        "rating": 8.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/6/73245.jpg",
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Supernatural", "Shounen"]
    },
    {
        "title": "Chainsaw Man",
        "synopsis": "Denji, pemuda miskin yang berhutang pada yakuza, menyatu dengan anjingnya yang berubah menjadi iblis gergaji. Ia menjadi Chainsaw Man dan bekerja untuk organisasi pemburu iblis.",
        "rating": 8.6,
        "image_url": "https://cdn.myanimelist.net/images/anime/1806/126216.jpg",
        "genres": ["Action", "Adventure", "Fantasy", "Horror", "Supernatural", "Seinen"]
    },
    {
        "title": "Sentouin, Hakenshimasu!",
        "synopsis": "Agen elit organisasi jahat dikirim ke dunia fantasi sebagai 'agen penyusup'. Ia harus membantu sang pahlawan wanita meski bertentangan dengan sifat jahatnya.",
        "rating": 7.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/1498/115592.jpg",
        "genres": ["Action", "Comedy", "Fantasy", "Ecchi", "Isekai", "Seinen"]
    },
    {
        "title": "Nanbaka",
        "synopsis": "Empat tahanan paling ahli kabur yang selalu berhasil melarikan diri dari penjara manapun kini ditahan di Penjara Nanba yang sangat ketat. Petualangan kocak pun terjadi.",
        "rating": 7.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/10/81879.jpg",
        "genres": ["Action", "Comedy", "Mystery", "Seinen"]
    },
    {
        "title": "Mirai Nikki",
        "synopsis": "Yukiteru Amano menerima 'Future Diary' yang merekam masa depan. Ia terpaksa bertarung dengan 11 pemegang diary masa depan lainnya dalam game survival untuk menjadi Tuhan.",
        "rating": 7.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/13/23970.jpg",
        "genres": ["Action", "Drama", "Horror", "Mystery", "Psychological", "Romance", "Shounen", "Supernatural", "Thriller"]
    },
    {
        "title": "Kill la Kill",
        "synopsis": "Ryuuko Matoi tiba di akademi Honnouji untuk mencari pembunuh ayahnya sambil bersenjatakan setengah gunting raksasa. Ia melawan Satsuki Kiryuuin dan pasukan seragam ajaibnya.",
        "rating": 8.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/8/60579.jpg",
        "genres": ["Action", "Comedy", "Ecchi", "Fantasy", "School", "Super Power", "Seinen"]
    },
    {
        "title": "Masamune-kun no Revenge",
        "synopsis": "Masamune Makabe yang dulu gemuk dan dipermalukan gadis cantik kini kembali sebagai pemuda tampan dan berusaha membalas dendam dengan membuat gadis itu jatuh cinta lalu ditolak.",
        "rating": 7.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/4/83491.jpg",
        "genres": ["Comedy", "Romance", "School", "Shounen"]
    },
    {
        "title": "Oniichan wa Oshimai!",
        "synopsis": "Mahiro Oyama, gamer hikikomori, terbangun sebagai perempuan karena percobaan adiknya. Ia harus menjalani kehidupan sebagai perempuan sementara adiknya terus mencatat perkembangannya.",
        "rating": 7.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/1796/131522.jpg",
        "genres": ["Comedy", "Slice of Life", "School", "Seinen"]
    },
    {
        "title": "Maoujou de Oyasumi",
        "synopsis": "Putri Syalis diculik oleh Raja Iblis dan dipenjara di kastilnya. Tapi alih-alih menangis, ia justru lebih khawatir soal tidur nyenyak dan mencuri bahan-bahan untuk tempat tidurnya.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1572/104882.jpg",
        "genres": ["Comedy", "Fantasy", "Romance", "Slice of Life", "Shounen"]
    },
    {
        "title": "Tokyo Ghoul",
        "synopsis": "Ken Kaneki bertahan hidup setelah diserang ghoul dan menjadi setengah ghoul. Ia harus menyeimbangkan sisi manusia dan ghoul-nya sambil bertahan di antara dua dunia yang bermusuhan.",
        "rating": 7.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/5/64449.jpg",
        "genres": ["Action", "Drama", "Fantasy", "Horror", "Mystery", "Psychological", "Supernatural", "Seinen"]
    },
    {
        "title": "Mahou Shoujo Madoka★Magica",
        "synopsis": "Madoka Kaname ditawari menjadi Magical Girl oleh makhluk bernama Kyubey. Di balik tawaran menarik itu tersimpan kebenaran gelap tentang dunia Magical Girl yang sesungguhnya.",
        "rating": 8.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/9/77985.jpg",
        "genres": ["Drama", "Horror", "Magic", "Mystery", "Psychological", "Thriller", "Sci-Fi", "Supernatural", "Shoujo"]
    },
    {
        "title": "Musaigen no Phantom World",
        "synopsis": "Di dunia di mana hantu menjadi hal nyata akibat virus, Haruhiko Ichijo dan timnya dari Klub Perburuan Phantom berpetualang menyegel para phantom.",
        "rating": 6.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/7/79990.jpg",
        "genres": ["Action", "Comedy", "Fantasy", "Magic", "School", "Ecchi"]
    },
    {
        "title": "To LOVE-Ru",
        "synopsis": "Rito Yuuki yang pemalu ingin menyatakan perasaannya pada Haruna, tapi tiba-tiba alien putri cantik bernama Lala Satalin Deviluke muncul dan mengharapkan Rito menikahinya.",
        "rating": 7.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/1335/93373.jpg",
        "genres": ["Comedy", "Ecchi", "Fantasy", "Harem", "Romance", "School", "Sci-Fi", "Shounen"]
    },
    {
        "title": "Maria†Holic",
        "synopsis": "Kanako Miyamae bersekolah di sekolah Katolik campuran untuk mencari jodoh karena kursusnya. Tapi ia jatuh cinta pada murid yang ternyata adalah laki-laki yang menyamar sebagai perempuan.",
        "rating": 7.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/5/73655.jpg",
        "genres": ["Comedy", "Romance", "School", "Seinen"]
    },
    {
        "title": "Yofukashi no Uta",
        "synopsis": "Kou Yamori, siswa yang insomnia, berkeliaran malam hari dan bertemu Nazuna Nanakusa, vampir yang tinggal di malam hari. Ia ingin menjadi vampir, tapi syaratnya ia harus jatuh cinta pada Nazuna.",
        "rating": 7.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/1659/120866.jpg",
        "genres": ["Action", "Mystery", "Romance", "Supernatural", "Seinen"]
    },
    {
        "title": "Monogatari Series",
        "synopsis": "Koyomi Araragi, mantan vampir, bertemu berbagai gadis yang mengalami kelainan supernatural. Setiap arc mengikuti kisah unik masing-masing karakter dengan dialog dan visual yang unik.",
        "rating": 8.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/11/75225.jpg",
        "genres": ["Action", "Comedy", "Drama", "Mystery", "Psychological", "Romance", "Supernatural", "Seinen"]
    },
    {
        "title": "Isekai Quartet",
        "synopsis": "Karakter dari berbagai dunia isekai (Overlord, Re:Zero, KonoSuba, Tanya) tiba-tiba dipindahkan ke sekolah yang sama dan harus bersekolah bersama.",
        "rating": 7.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/1756/98458.jpg",
        "genres": ["Comedy", "Fantasy", "Isekai", "Parody", "School", "Seinen"]
    },
    {
        "title": "Koe no Katachi",
        "synopsis": "Shouya Ishida dulu membully siswi tuli Shouko Nishimiya hingga ia sendiri menjadi korban bully. Bertahun-tahun kemudian, ia mencoba menebus kesalahannya dan menemukan kembali Shouko.",
        "rating": 9.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/1619/92533.jpg",
        "genres": ["Drama", "Romance", "School", "Slice of Life", "Shounen"]
    },
    {
        "title": "Isekai Ojisan",
        "synopsis": "Paman Takafumi baru sadar setelah 17 tahun koma. Ternyata ia hidup di dunia fantasi selama itu dan pulang dengan berbagai kekuatan ajaib. Kini ia membuat konten YouTube sambil bernostalgia.",
        "rating": 8.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/1045/124990.jpg",
        "genres": ["Comedy", "Fantasy", "Isekai", "Seinen"]
    },
    {
        "title": "Tokyo Ravens",
        "synopsis": "Harutora Tsuchimikado, keturunan keluarga onmyoji tapi tak punya kekuatan, terpaksa memenuhi janjinya untuk menjadi shikigami bagi Natsume, saudaranya yang powerful.",
        "rating": 7.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/4/36530.jpg",
        "genres": ["Action", "Fantasy", "Magic", "Romance", "School", "Supernatural", "Shounen"]
    },
    {
        "title": "Mangaka-san to Assistant-san to The Animation",
        "synopsis": "Mangaka ecchi bernama Aito Yuuki selalu meminta asisten wanitanya, Ashisu Sahoto, menjadi model untuk karya-karyanya, sering dengan pose yang tidak nyaman.",
        "rating": 6.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/4/61891.jpg",
        "genres": ["Comedy", "Ecchi", "Romance", "Seinen", "Slice of Life"]
    },
    {
        "title": "Dagashi Kashi",
        "synopsis": "Kokonotsu Shikada, anak pemilik toko snack tradisional, didatangi Hotaru Shidare yang fanatik dengan snack tradisional (dagashi) dan ingin merekrut ayahnya.",
        "rating": 7.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/77201.jpg",
        "genres": ["Comedy", "Romance", "School", "Seinen", "Slice of Life"]
    },
    {
        "title": "Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka",
        "synopsis": "Bell Cranel, adventurer pemula di kota dungeon Orario, bercita-cita menjadi pahlawan terhebat. Setelah diselamatkan oleh Ais Wallenstein, ia berjuang keras untuk mengejar sang gadis pedang.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1549/93591.jpg",
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Romance", "Shounen"]
    },
    {
        "title": "Gakkougurashi!",
        "synopsis": "Sekilas terlihat seperti anime sekolah yang menyenangkan dan ceria, namun tersimpan kebenaran gelap bahwa para siswi ini sebenarnya bertahan hidup di sekolah yang dipenuhi zombie.",
        "rating": 7.6,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/73178.jpg",
        "genres": ["Drama", "Horror", "Mystery", "Psychological", "School", "Slice of Life", "Seinen"]
    },
    {
        "title": "Hentai Ouji to Warawanai Neko",
        "synopsis": "Youto Yokodera membuat permintaan pada patung kucing agar bisa mengungkapkan pikirannya dengan bebas. Permintaannya terkabul tapi juga membawa berbagai komplikasi lucu.",
        "rating": 7.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/50581.jpg",
        "genres": ["Comedy", "Romance", "School", "Supernatural", "Seinen"]
    },
    {
        "title": "High School of the Dead",
        "synopsis": "Sekelompok siswa SMA dan guru bimbingan berjuang bertahan hidup saat wabah zombie mendadak menyerang Jepang, sambil berhadapan dengan konflik antar sesama survivor.",
        "rating": 7.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/7/22066.jpg",
        "genres": ["Action", "Drama", "Ecchi", "Horror", "Supernatural", "Seinen", "School"]
    },
    {
        "title": "Akame ga Kill!",
        "synopsis": "Tatsumi bergabung dengan Night Raid, kelompok pembunuh bayaran yang melawan kekaisaran korup. Setiap pertarungan bisa menjadi yang terakhir bagi siapa pun.",
        "rating": 7.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/1460/110463.jpg",
        "genres": ["Action", "Adventure", "Drama", "Fantasy", "Horror", "Mystery", "Shounen"]
    },
    {
        "title": "Kamisama ni Natta Hi",
        "synopsis": "Seorang gadis misterius bernama Hina mengklaim bahwa kiamat akan datang dalam 30 hari dan mengganggu kehidupan Youta Narukami dengan cara-cara yang penuh teka-teki.",
        "rating": 7.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/1789/109442.jpg",
        "genres": ["Comedy", "Drama", "Fantasy", "Romance", "Sci-Fi", "Supernatural"]
    },
    {
        "title": "Sousou no Frieren",
        "synopsis": "Frieren, penyihir elf berumur panjang, melanjutkan perjalanan setelah para sahabat petualangannya menjadi tua dan meninggal. Ia mulai memahami arti hubungan dengan manusia yang berumur pendek.",
        "rating": 9.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
        "genres": ["Adventure", "Drama", "Fantasy", "Mystery", "Shounen"]
    },
    {
        "title": "Summertime Render",
        "synopsis": "Shinpei kembali ke pulau kampung halamannya untuk menghadiri pemakaman sahabat masa kecilnya. Ia menemukan misteri gelap tentang 'bayangan' yang membunuh orang dan kemampuannya untuk kembali ke masa lalu.",
        "rating": 8.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1443/120222.jpg",
        "genres": ["Action", "Drama", "Horror", "Mystery", "Psychological", "Romance", "Supernatural", "Thriller", "Shounen"]
    },
    {
        "title": "Binbougami ga!",
        "synopsis": "Ichiko Sakura, gadis yang sangat beruntung dan cantik, harus menghadapi Momiji, Dewa Kemiskinan yang bertugas menyeimbangkan keberuntungannya yang berlebihan.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/9/40060.jpg",
        "genres": ["Action", "Comedy", "Parody", "Romance", "Supernatural", "Shounen"]
    },
    {
        "title": "Kotoura-san",
        "synopsis": "Haruka Kotoura bisa membaca pikiran orang lain tapi hal itu justru menghancurkan semua hubungannya. Di sekolah baru, ia bertemu Manabe yang justru tidak keberatan pikirannya terbaca.",
        "rating": 7.5,
        "image_url": "https://cdn.myanimelist.net/images/anime/12/47273.jpg",
        "genres": ["Comedy", "Drama", "Romance", "School", "Supernatural", "Seinen"]
    },
    {
        "title": "Kage no Jitsuryokusha ni Naritakute!",
        "synopsis": "Minoru Kagenou terobsesi menjadi penguasa bayangan dan berlatih keras. Setelah bereinkarnasi, impiannya menjadi kenyataan tanpa disadarinya — semua yang ia karang ternyata nyata.",
        "rating": 8.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/1415/120334.jpg",
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Mystery", "Isekai", "Harem", "Seinen"]
    },
    {
        "title": "Ple Ple Pleiades × Kagejitsu!",
        "synopsis": "Crossover parodi pendek antara karakter Overlord dan The Eminence in Shadow dalam situasi sehari-hari yang konyol dan menggelikan.",
        "rating": 7.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/1806/126216.jpg",
        "genres": ["Comedy", "Fantasy", "Parody", "Seinen"]
    },
    {
        "title": "Blood Lad",
        "synopsis": "Staz Charlie Blood, vampir otaku berkuasa yang terobsesi dengan Jepang, bertemu gadis Jepang sungguhan yang kemudian mati dan menjadi hantu. Ia berjanji menghidupkannya kembali.",
        "rating": 7.3,
        "image_url": "https://cdn.myanimelist.net/images/anime/1069/71995.jpg",
        "genres": ["Action", "Comedy", "Fantasy", "Romance", "Supernatural", "Seinen"]
    },
    {
        "title": "Nu Wushen de Canzhuo",
        "synopsis": "Dewa wanita membuka restoran di perbatasan dunia manusia dan dewa. Berbagai pelanggan dari kalangan dewa, iblis, dan manusia datang dengan masalah masing-masing yang diselesaikan lewat makanan.",
        "rating": 8.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/1200/84006.jpg",
        "genres": ["Fantasy", "Slice of Life", "Mystery", "Supernatural"]
    },
    {
        "title": "Happy Sugar Life",
        "synopsis": "Satou Matsuzaka, gadis populer, jatuh cinta pada anak kecil bernama Shio dan rela melakukan segalanya — termasuk hal-hal mengerikan — demi melindungi 'kehidupan manis' mereka bersama.",
        "rating": 7.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/1726/91413.jpg",
        "genres": ["Drama", "Horror", "Mystery", "Psychological", "Romance", "Thriller", "Seinen"]
    },
    {
        "title": "Endro~!",
        "synopsis": "Para pahlawan perempuan yang gagal membunuh Iblis Raja justru mengirimnya kembali ke masa lalu. Iblis Raja kini menyamar sebagai guru di sekolah pahlawan yang sama.",
        "rating": 7.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/1300/99423.jpg",
        "genres": ["Adventure", "Comedy", "Fantasy", "Magic", "School", "Slice of Life", "Seinen"]
    },
    {
        "title": "Seitokai no Ichizon",
        "synopsis": "Ken Sugisaki bergabung dengan dewan siswa yang semuanya cantik dengan cara meraih nilai tertinggi. Ia bermimpi membangun harem seperti di game galge favoritnya.",
        "rating": 7.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/7/21990.jpg",
        "genres": ["Comedy", "Parody", "Romance", "School", "Seinen", "Harem"]
    },
    {
        "title": "Baka to Test to Shoukanjuu",
        "synopsis": "Di sekolah yang memisahkan siswa berdasarkan nilai, kelas F yang diisi siswa paling bodoh berjuang naik kelas dengan menggunakan 'Shoukanjuu', avatar pertempuran yang kekuatannya sesuai nilai ujian.",
        "rating": 7.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/9/25538.jpg",
        "genres": ["Comedy", "Fantasy", "Romance", "School", "Shounen"]
    },
    {
        "title": "D-Frag!",
        "synopsis": "Kenji Kazama, ketua geng sekolah yang ingin terlihat keren, terpaksa bergabung dengan Game Creation Club yang diisi anggota-anggota perempuan dengan kepribadian aneh dan kuat.",
        "rating": 7.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/52951.jpg",
        "genres": ["Comedy", "Game", "School", "Seinen"]
    },
    {
        "title": "Seto no Hanayome",
        "synopsis": "Nagasumi Michishio hampir tenggelam dan diselamatkan oleh putri duyung. Menurut hukum duyung, ia harus menikahi Sun atau salah satunya harus dibunuh.",
        "rating": 7.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/4/5199.jpg",
        "genres": ["Action", "Comedy", "Fantasy", "Romance", "School", "Shounen"]
    },
    {
        "title": "Denki-gai no Honya-san",
        "synopsis": "Kehidupan sehari-hari para karyawan di toko buku/komik di distrik Akihabara. Penuh momen lucu, canggung, dan menggemaskan antara rekan kerja yang unik.",
        "rating": 7.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/8/59992.jpg",
        "genres": ["Comedy", "Romance", "Seinen", "Slice of Life"]
    },
    {
        "title": "Maou no Ore ga Dorei Elf wo Yome ni Shitanda ga, Dou Medereba Ii?",
        "synopsis": "Zagan, penyihir muda yang ditakuti, membeli seorang budak elf cantik di lelang. Masalahnya, ia sama sekali tidak tahu cara berinteraksi dengan orang lain apalagi memperlakukan sang elf dengan baik.",
        "rating": 7.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/1301/117406.jpg",
        "genres": ["Comedy", "Fantasy", "Magic", "Romance", "Seinen"]
    },
    {
        "title": "Astarotte no Omocha!",
        "synopsis": "Putri Succubus kecil yang benci laki-laki terpaksa membentuk 'harem' karena aturan kerajaan. Satu-satunya laki-laki yang mau bergabung adalah manusia dari dunia lain beserta anaknya.",
        "rating": 6.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/9/23740.jpg",
        "genres": ["Comedy", "Fantasy", "Romance", "Seinen", "Slice of Life"]
    },
    {
        "title": "Princess Connect! Re:Dive",
        "synopsis": "Yuuki, pria yang kehilangan ingatannya, tiba di dunia fantasi Astraea. Ia bertemu Kokkoro yang siap memandunya, Pecorine yang ceria dan rakus, serta Karyl yang kucing misterius.",
        "rating": 7.6,
        "image_url": "https://cdn.myanimelist.net/images/anime/1510/106036.jpg",
        "genres": ["Action", "Adventure", "Comedy", "Fantasy", "Game", "Harem", "Slice of Life"]
    },
    {
        "title": "Bokusatsu Tenshi Dokuro-chan",
        "synopsis": "Kusakabe Sakura kedatangan malaikat pembunuh bernama Dokuro-chan yang seharusnya membunuhnya tapi malah memilih tinggal bersamanya — dan terus membunuhnya lalu menghidupkannya kembali.",
        "rating": 6.7,
        "image_url": "https://cdn.myanimelist.net/images/anime/9/9716.jpg",
        "genres": ["Comedy", "Ecchi", "Fantasy", "Romance", "School", "Seinen", "Supernatural"]
    },
    {
        "title": "Bokura wa Minna Kawai-sou",
        "synopsis": "Kazunari Usa pindah ke kos-kosan unik yang dihuni orang-orang dengan kepribadian eksentrik. Di sana ia bertemu Ritsu Kawai, gadis pendiam yang terobsesi dengan buku.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/8/55802.jpg",
        "genres": ["Comedy", "Romance", "School", "Seinen", "Slice of Life"]
    },
    {
        "title": "Arakawa Under the Bridge",
        "synopsis": "Kou Ichinomiya, pria kaya yang pantang berhutang, diselamatkan oleh Nino, gadis yang tinggal di bawah jembatan Arakawa. Untuk membayar hutangnya, ia harus tinggal di sana dan menjadi kekasihnya.",
        "rating": 7.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/7/22066.jpg",
        "genres": ["Comedy", "Romance", "Seinen", "Slice of Life"]
    },
    {
        "title": "Ore no Nounai Sentakushi ga, Gakuen Love Comedy wo Zenryoku de Jama Shiteiru",
        "synopsis": "Kanade Amakusa menderita kutukan 'Absolute Choice' yang memaksanya memilih antara dua opsi memalukan di tempat umum. Kutukan itu bisa hilang jika ia menemukan seorang gadis berambut pirang.",
        "rating": 7.1,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/51621.jpg",
        "genres": ["Comedy", "Romance", "School", "Supernatural", "Harem", "Shounen"]
    },
    {
        "title": "Rewrite",
        "synopsis": "Kotarou Tennouji memiliki kemampuan 'Rewrite' untuk menulis ulang fisik tubuhnya. Ia bergabung dengan Occult Research Club dan menemukan rahasia besar tentang kota dan masa depan bumi.",
        "rating": 7.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/1/82302.jpg",
        "genres": ["Action", "Comedy", "Drama", "Fantasy", "Mystery", "Romance", "School", "Supernatural", "Seinen"]
    },
    {
        "title": "Dan Da Dan",
        "synopsis": "Momo Ayase dan Ken Takakura bertaruh soal eksistensi alien vs hantu. Keduanya malah terseret langsung ke dalam petualangan supranatural dan alien yang berbahaya sekaligus kacau.",
        "rating": 8.6,
        "image_url": "https://cdn.myanimelist.net/images/anime/1801/141392.jpg",
        "genres": ["Action", "Comedy", "Horror", "Mystery", "Romance", "Sci-Fi", "Supernatural", "Shounen"]
    },
    {
        "title": "Hoshizora e Kakaru Hashi",
        "synopsis": "Kazuma Hoshi pindah ke desa pegunungan dan tidak sengaja mencium gadis desa bernama Ui Nakatsugawa saat pertama bertemu. Kehidupan baru yang penuh gadis-gadis manis pun dimulai.",
        "rating": 6.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/3/28286.jpg",
        "genres": ["Comedy", "Harem", "Romance", "School", "Seinen", "Slice of Life"]
    },
    {
        "title": "Ouran Koukou Host Club",
        "synopsis": "Haruhi Fujioka secara tidak sengaja bergabung dengan Host Club sekolah elit setelah memecahkan vas mahal. Ia harus bekerja sebagai host untuk melunasi hutangnya.",
        "rating": 8.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/9/35726.jpg",
        "genres": ["Comedy", "Drama", "Romance", "School", "Shoujo", "Slice of Life"]
    },
    {
        "title": "Toaru Series",
        "synopsis": "Di kota Academy City yang penuh esper, Touma Kamijou memiliki tangan kanan yang bisa membatalkan segala kekuatan supernatural. Ia terlibat dalam konflik besar antara sains dan sihir.",
        "rating": 7.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/5/22975.jpg",
        "genres": ["Action", "Adventure", "Fantasy", "Magic", "Romance", "Sci-Fi", "Supernatural", "Shounen"]
    },
    {
        "title": "Zom 100: Zombie ni Naru made ni Shitai 100 no Koto",
        "synopsis": "Akira Tendou, karyawan yang lelah kerja, justru bahagia saat zombie apocalypse terjadi karena ia tidak perlu kerja lagi. Ia pun membuat bucket list 100 hal ingin dilakukan sebelum jadi zombie.",
        "rating": 7.9,
        "image_url": "https://cdn.myanimelist.net/images/anime/1863/136791.jpg",
        "genres": ["Action", "Adventure", "Comedy", "Horror", "Shounen"]
    },
    {
        "title": "Himegoto",
        "synopsis": "Hime Arikawa yang berhutang diselamatkan oleh dewan siswa dengan syarat ia harus memakai seragam perempuan dan menjadi 'pelayan' dewan siswa selama SMA.",
        "rating": 6.8,
        "image_url": "https://cdn.myanimelist.net/images/anime/10/62036.jpg",
        "genres": ["Comedy", "School", "Seinen", "Slice of Life"]
    },
    {
        "title": "Henjin no Salad Bowl",
        "synopsis": "Seorang putri dari dunia fantasi jatuh ke dunia modern Jepang dan bertemu detektif yang membantu orang-orang bermasalah. Perpaduan elemen fantasi dan kehidupan modern yang unik.",
        "rating": 7.2,
        "image_url": "https://cdn.myanimelist.net/images/anime/1086/108218.jpg",
        "genres": ["Comedy", "Fantasy", "Slice of Life", "Seinen"]
    },
    {
        "title": "Oroka na Tenshi wa Akuma to Odoru",
        "synopsis": "Iblis bernama Akutsu Lily gagal merasuki malaikat dan malah terjebak dalam hubungan aneh di mana sang malaikat Ainosuke justru berusaha keras memenangkan hati si iblis.",
        "rating": 7.4,
        "image_url": "https://cdn.myanimelist.net/images/anime/1806/126216.jpg",
        "genres": ["Comedy", "Romance", "Supernatural", "Shounen"]
    },
    {
        "title": "Koisuru One Piece",
        "synopsis": "Spin-off romantis dari One Piece yang mengikuti kisah cinta para karakter ikonik di Grand Line dengan twist komedi dan momen-momen menggemaskan.",
        "rating": 7.0,
        "image_url": "https://cdn.myanimelist.net/images/anime/6/73245.jpg",
        "genres": ["Comedy", "Fantasy", "Romance", "Adventure", "Shounen"]
    }
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
            image_url TEXT
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
            "INSERT INTO anime (title, synopsis, rating, image_url) VALUES (?, ?, ?, ?)",
            (anime["title"], anime["synopsis"], anime["rating"], anime["image_url"])
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