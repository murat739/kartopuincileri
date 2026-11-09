import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Hikmet ve Tefekkür Külliyatı | Wisdom & Reflection Corpus",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# ÖZEL CSS VE JAVASCRIPT KORUMA KATMANI (KOPYALAMA VE SAĞ TIK ENGELLEME)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Tüm sayfa genelinde metin seçimini (highlight/copy) kapatır */
    .stApp { 
        background-color: #f8fafc; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        -webkit-user-select: none;  /* Safari */
        -moz-user-select: none;     /* Firefox */
        -ms-user-select: none;      /* Internet Explorer/Edge */
        user-select: none;          /* Standart */
    }
    .legal-box {
        background-color: #fef2f2;
        border-left: 5px solid #dc2626;
        padding: 12px;
        border-radius: 4px;
        font-size: 13px;
        color: #7f1d1d;
        margin-bottom: 20px;
    }
    .ayet-box {
        background-color: #f0fdf4;
        border-left: 5px solid #16a34a;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 15px;
    }
    .hadis-box {
        background-color: #eff6ff;
        border-left: 5px solid #2563eb;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 15px;
    }
    .bediuzzaman-box {
        background-color: #fdf4ff;
        border-left: 5px solid #9333ea;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 15px;
    }
    .haciveli-box {
        background-color: #fff7ed;
        border-left: 5px solid #f97316;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 15px;
    }
    .veli-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 6px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 10px;
        border-top: 3px solid #0d9488;
    }
    </style>

    <script>
    // Sağ tık menüsünü devre dışı bırakır
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
    });

    // Klavye kısayolları ile kopyalamayı engeller (Ctrl+C, Ctrl+X, Ctrl+A, Ctrl+U, F12 vb.)
    document.addEventListener('keydown', function(e) {
        if (
            e.keyCode == 123 || // F12
            (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74)) || // Ctrl+Shift+I / J (DevTools)
            (e.ctrlKey && e.keyCode == 85) || // Ctrl+U (Kaynak Kod)
            (e.ctrlKey && e.keyCode == 67) || // Ctrl+C (Kopyala)
            (e.ctrlKey && e.keyCode == 88) || // Ctrl+X (Kes)
            (e.ctrlKey && e.keyCode == 65)    // Ctrl+A (Tümünü Seç)
        ) {
            e.preventDefault();
            return false;
        }
    });
    </script>
""", unsafe_allow_html=True)

# Dil Seçimi Düğmesi
st.sidebar.markdown("### 🌐 Language / Dil Seçimi")
lang = st.sidebar.radio("Select Language / Dil Seçiniz:", ["TR 🇹🇷", "EN 🇬🇧"])

is_tr = (lang == "TR 🇹🇷")

# -----------------------------------------------------------------------------
# DİL SÖZLÜKLERİ VE TÜM METİNLER (TAM ÇEVİRİ DESTEĞİ)
# -----------------------------------------------------------------------------
T = {
    "sidebar_title": "❄️ Külliyat ve Tefekkür" if is_tr else "❄️ Corpus & Reflection",
    "legal_warning": """
        <b>⚖️ YASAL UYARI VE FİKRİ MÜLKİYET BİLDİRİMİ (LEGAL DISCLAIMER):</b><br>
        Bu yazılımın kaynak kodları, metinsel derlemeleri ve tasarımları Fikir ve Sanat Eserleri Kanunu gereğince koruma altındadır. 
        İçerisindeki ayet mealleri Diyanet İşleri Başkanlığı resmi yayınlarından, hadisler kütüb-i sitte şerhlerinden, Risale-i Nur ve tasavvufi metinler ise orijinal eser kaynaklarıyla derlenmiştir. 
        İzinsiz ticari kopyalama, çoğaltma ve kaynak kod yapısının başka mecralarda kullanımı hukuki takibe tabidir. Tüm hakları saklıdır.
    """ if is_tr else """
        <b>⚖️ LEGAL DISCLAIMER & INTELLECTUAL PROPERTY NOTICE:</b><br>
        The source codes, text compilations, and interface designs of this software are protected under Intellectual Property laws.
        Verse translations are sourced from official religious affairs authorities, Hadiths from canonical collections, and Risale-i Nur & Sufi texts from primary literature with citations.
        Unauthorized commercial copying, distribution, or misuse is subject to legal prosecution. All rights reserved.
    """,
    "menu_options": [
        "📖 Ayetler ve Mealler" if is_tr else "📖 Verses & Translations",
        "⚡ Hadis-i Şerifler ve Kaynakları" if is_tr else "⚡ Hadiths & Sources",
        "📚 Bediüzzaman (15+ Risale Örneği)" if is_tr else "📚 Bediuzzaman (15+ Risale Examples)",
        "🔶 Hacı Bayram-ı Veli Hazretleri" if is_tr else "🔶 Hacı Bayram-ı Veli's View",
        "🌟 Veli ve Âlimlerin Görüşleri (20+)" if is_tr else "🌟 Views of Scholars & Saints (20+)",
        "🌱 Haşir ve Yeniden Diriliş" if is_tr else "🌱 Resurrection & Afterlife"
    ],
    "info_note": "💡 *Bilgi Notu:* Bu panel akademik tetkik, manevi tefekkür ve eğitim amaçlı tasarlanmıştır." if is_tr else "💡 *Note:* This panel is designed for academic study, spiritual reflection, and educational purposes.",
    "sleep_note": (
        "💡 Not: Bu web uygulaması ücretsiz sunucularda barındırılmaktadır. "
        "Uzun süre işlem yapılmadığında uygulama uyku moduna geçebilir "
        "(ekranda 'Zzzz' simgesi çıkabilir).\n\n"
        "💤 Eğer böyle bir ekranla karşılaşırsanız, ekranda beliren mavi renkli "
        "'Yes, get this app back up!' butonuna tıklayın ve uygulamanın "
        "yeniden uyanması için 15-30 saniye bekleyin."
    ) if is_tr else (
        "💡 Note: This web app is hosted on free servers. "
        "If left inactive for a long time, the app may go to sleep "
        "(showing a 'Zzzz' icon).\n\n"
        "💤 If you encounter such a screen, click the blue "
        "'Yes, get this app back up!' button and wait 15-30 seconds for the app to wake up."
    )
}

# Hukuksal Uyarı Gösterimi
st.markdown(f'<div class="legal-box">{T["legal_warning"]}</div>', unsafe_allow_html=True)

# Yan Menü Navigasyonu
st.sidebar.markdown("---")
secim = st.sidebar.radio(T["sidebar_title"], T["menu_options"])
st.sidebar.markdown("---")
st.sidebar.info(T["info_note"])

# Kenar çubuğuna uyku modu bilgilendirmesi
st.sidebar.markdown("---")
st.sidebar.info(T["sleep_note"])

# -----------------------------------------------------------------------------
# 1. BÖLÜM: AYETLER VE MEALLER
# -----------------------------------------------------------------------------
if secim == T["menu_options"][0]:
    st.title("📖 Kur'an-ı Kerim'de Kar, Su ve Kış Döngüsü" if is_tr else "📖 Snow, Water, and Winter Cycle in the Holy Qur'an")
    st.caption("Ayetler Diyanet Meali ve İngilizce sahih meallere dayanmaktadır." if is_tr else "Verses are based on reliable Turkish & English Qur'an translations.")

    if is_tr:
        st.markdown("""
        <div class="ayet-box">
            <b>1. Furkan Suresi, 48. Ayet (Surah Al-Furqan, 25:48):</b><br>
            'O, rahmetinin önünde rüzgârları müjdeci olarak gönderendir. Biz gökten <b>bembeyaz, tertemiz bir su</b> indirdik.'
        </div>
        <div class="ayet-box">
            <b>2. Nur Suresi, 43. Ayet (Surah An-Nur, 24:43):</b><br>
            'Görmez misin ki Allah bulutları sevk eder, sonra onları birleştirip üst üste yığar... Gökten, içindeki dağlar gibi bulutlardan <b>dolu (ve soğuk yağışlar)</b> indirir...'
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="ayet-box">
            <b>1. Surah Al-Furqan, 25:48:</b><br>
            'And it is He who sends the winds as good tidings before His mercy, and We send down from the sky <b>pure, purifying water</b>.'
        </div>
        <div class="ayet-box">
            <b>2. Surah An-Nur, 24:43:</b><br>
            'Do you not see that Allah drives clouds? Then He brings them together, then He makes them into a mass... and He sends down from the sky mountains [of clouds] within which is <b>hail/cold rain</b>...'
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. BÖLÜM: HADİS-İ ŞERİFLER
# -----------------------------------------------------------------------------
elif secim == T["menu_options"][1]:
    st.title("⚡ Hadis-i Şerif Külliyatında Kış ve Arınma" if is_tr else "⚡ Winter and Purification in Hadith Collections")
    
    if is_tr:
        st.markdown("""
        <div class="hadis-box">
            <b>1. Günahlardan Arınma Duası:</b><br>
            <i>Metin:</i> 'Allah'ım! Hatalarımı <b>kar, su ve dolu ile yıka.</b> Beyaz elbiseyi kirden arındırdığın gibi kalbimi de hatalardan arındır...'<br>
            <b>Kaynak:</b> Sahih-i Buhârî, Daavât, 39; Sahih-i Müslim, Mesâcid, 153.
        </div>
        <div class="hadis-box">
            <b>2. Müminin Baharı Hadisi:</b><br>
            <i>Metin:</i> 'Kış, müminin baharıdır; gündüzü kısa olur oruç tutar, gecesi uzun olur kıyam (ibadet) eder.'<br>
            <b>Kaynak:</b> Sünen-i Tirmizî, Savm, 74; Ahmed bin Hanbel, Müsned, III/75.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="hadis-box">
            <b>1. Prayer for Purification:</b><br>
            <i>Text:</i> 'O Allah! Wash away my sins with <b>snow, water, and hail.</b> Cleanse my heart from sins as a white garment is cleansed from filth...'<br>
            <b>Source:</b> Sahih al-Bukhari, Da'awat, 39; Sahih Muslim, Masajid, 153.
        </div>
        <div class="hadis-box">
            <b>2. The Winter is Believer's Spring:</b><br>
            <i>Text:</i> 'Winter is the spring of the believer; its days are short so he fasts, and its nights are long so he stands in prayer.'<br>
            <b>Source:</b> Sunan al-Tirmidhi, Sawm, 74; Musnad Ahmad ibn Hanbal, III/75.
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. BÖLÜM: BEDİÜZZAMAN VE RİSALE-İ NUR (15+ ÖRNEK)
# -----------------------------------------------------------------------------
elif secim == T["menu_options"][2]:
    st.title("📚 Bediüzzaman Said Nursî Hazretleri'nin Eserlerinde Kış ve Haşir (15+ Örnek)" if is_tr else "📚 Winter and Resurrection Examples in Risale-i Nur (15+ Examples)")
    st.caption("Risale-i Nur Külliyatı'ndan derlenen 15 temel kış ve haşir misali ile kaynakları." if is_tr else "15 core winter and resurrection metaphors compiled from the Risale-i Nur Collection.")

    nur_ornekleri = [
        ("1. Üç Yüz Bin Mahlûkatın İhyâsı ve Haşir Temsili", 
         "Kış mevsiminde ağaçların ve otların ölüp ortadan kaybolur gibi görünmesine rağmen baharda hiçbir hata olmaksızın aynen iade edilmesini büyük bir haşir misali olarak anlatır.", 
         "Risale-i Nur Külliyatı, Sözler, Onuncu Söz (Haşir Risalesi), 3. Hakikat",
         "1. Resurrection of 300,000 Species", "Explains how trees and vegetation seem to die in winter yet are perfectly restored in spring as a grand metaphor for Resurrection.", "Risale-i Nur, The Tenth Word, 3rd Truth"),
        
        ("2. Kışın Defter-i A'mâlinin Dürülmesi ve Neşri", 
         "Yaz ve bahar sahifelerinin kışın dürülüp kaldırıldığını, gayb levhalarında her şeyin hıfzzedilerek baharda yeniden ve yepyeni bir surette neşredildiğini belirtir.", 
         "Risale-i Nur Külliyatı, Sözler, Onuncu Söz, 9. Hakikat",
         "2. Filing & Re-issuing the Book of Deeds in Winter", "Indicates that summer and spring pages are closed in winter, preserved in unseen tablets, and re-published anew in spring.", "Risale-i Nur, The Tenth Word, 9th Truth"),

        ("3. Kar Tanelerinin ve Zerratın Şaşmaz Nizamı", 
         "Su moleküllerinin ve kar tanelerinin sıfırın altındaki derecelerde altıgen bir nizamla dizilmesinin asla tesadüfe verilemeyeceğini, bunun nihayetsiz ilim ve kudretin eseri olduğunu vurgular.", 
         "Risale-i Nur Külliyatı, Sözler, Yirmi İkinci Söz, 2. Makam",
         "3. Flawless Order of Snowflakes & Atoms", "Emphasizes that the hexagonal order of snowflakes under freezing temperatures cannot be coincidence, but the work of infinite power.", "Risale-i Nur, The Twenty-Second Word"),

        ("4. Sineklerin ve Küçük Haşeratın Yeniden Diriltilmesi", 
         "Kışın soğuğunda ölen zarif sineklerin ve arıların, baharın ilk sıcak rüzgârıyla kusursuz bir şekilde yeniden hayat bulmasının, Yaratıcı'nın hiçbir şeyi unutmadığının kanıtı olduğunu ifade eder.", 
         "Risale-i Nur Külliyatı, Asâ-yı Musa, 1. Mesele",
         "4. Revival of Insects and Small Creatures", "States that the perfect revival of delicate insects in spring proves that the Creator forgets nothing.", "Risale-i Nur, Staff of Moses, 1st Issue"),

        ("5. Kışın Celâl, Baharda Cemâl Esmasının Aynası Olması", 
         "Kışın hükmeden kar, fırtına ve dondurucu soğukların; Cenâb-ı Hakk'ın Kahhâr, Celîl, Hakîm ve Müdebbir isimlerinin tecelligâhı olduğunu işler.", 
         "Risale-i Nur Külliyatı, Lem'alar, Otuzuncu Lem'a (Esma-i Sitte)",
         "5. Winter as Mirror to Majesty (Jalal), Spring to Beauty (Jamal)", "Discusses how winter cold manifests Divine names like Al-Kahhar and Al-Jalil.", "Risale-i Nur, The Thirtieth Flashes"),

        ("6. Kurumuş Odun Parçalarından Hayat Süzülmesi", 
         "Kışın ellerini havaya açmış kuru birer sopa gibi duran odunların, bahar suyuyla birer zerafet abidesine dönüşmesini kudretin cansızdan hayatı süzmesi olarak inceler.", 
         "Risale-i Nur Külliyatı, Şualar, Yedinci Şua (Âyetü'l-Kübrâ)",
         "6. Filtering Life from Dry Wood Pieces", "Examines how dry winter branches transform into elegance through spring water as life being extracted from lifelessness.", "Risale-i Nur, The Rays, Seventh Ray"),

        ("7. Tohumun Toprağa Atılması ve Kış Baskısı", 
         "Tohumun kışın kar ve buz kütleleri altında çürür gibi görünmesinin, içerideki özün sümbüllenmesi için mukaddes bir inkılap olduğunu belirtir.", 
         "Risale-i Nur Külliyatı, Mesnevî-i Nuriye, Hubâb ve Habbe",
         "7. Seeds Under Winter Pressure & Snow", "States that a seed seeming to decay under winter snow undergoes a sacred transformation to sprout.", "Risale-i Nur, Masnawi-i Nuriye"),

        ("8. Kış Soğuğunda İnsanın Acziyetini ve Şükrü Hissetmesi", 
         "Kışın şiddeti ve soğuğu karşısında insanın kendi zayıflığını ve aczini anladığını, sığınacak yalnız Cenâb-ı Hak olduğunu idrak ederek gerçek şükre ulaştığını ifade eder.", 
         "Risale-i Nur Külliyatı, Sözler, Otuz İkinci Söz",
         "8. Sensing Human Helplessness & Gratitude in Winter Cold", "Explains how extreme winter cold makes man realize his weakness, turning him to God in true gratitude.", "Risale-i Nur, The Thirty-Second Word"),

        ("9. Zemin Yüzünün Kışın Matemi, Baharın Düğünü Olması", 
         "Kışın zemin yüzünün sessiz, karlı ve matemli bir hal aldığını, baharda ise bu matemin yerini muazzam bir neşeye, ziyafete ve düğüne bıraktığını söyler.", 
         "Risale-i Nur Külliyatı, Mektûbât, Yirmi Dördüncü Mektup",
         "9. Earth's Winter Mourning & Spring Wedding", "Says the silent snow-covered earth mourns in winter, but transforms into a grand celebration and wedding in spring.", "Risale-i Nur, Letters, 24th Letter"),

        ("10. Ağaçların Kışın Başlarına Gelen Halin Baharla Tescili", 
         "Kışın çıplak kalan ağaç kollarının, baharda yeşillenmesini insanın kabir hayatı ve ahiret saadetiyle ilişkilendirerek izah eder.", 
         "Risale-i Nur Külliyatı, Lem'alar, Yirmi Üçüncü Lem'a",
         "10. The Testimony of Spring on Bare Winter Trees", "Relates the greening of naked winter trees to human grave life and eternal afterlife happiness.", "Risale-i Nur, The 23rd Flashes"),

        ("11. Buzların ve Kar Sularının Hayat Kaynağı Olması", 
         "Dağlardaki karların ve buzların kışın donup muhafaza edildikten sonra baharda yavaş yavaş eriyerek nehirleri beslemesini ilahi rahmetin hikmeti olarak açıklar.", 
         "Risale-i Nur Külliyatı, Barla Lahikası",
         "11. Glaciers and Snow Waters as Life Sources", "Explains mountain snow and ice slowly melting in spring to feed rivers as an act of divine mercy.", "Risale-i Nur, Barla Addendum"),

        ("12. Ölümün Kış Gibi, Kabir Âleminin De Kar Altındaki Tohum Gibi Olması", 
         "İnsanın ölümünün korkutucu bir yok oluş değil, tohumun kış uykusu gibi berzah âleminde baharı (ahireti) beklemek olduğunu misallendirir.", 
         "Risale-i Nur Külliyatı, Gençlik Rehberi",
         "12. Death as Winter, the Grave as Seed under Snow", "Portrays human death not as extinction, but like a seed's winter sleep awaiting the spring of the Hereafter.", "Risale-i Nur, Youth Guide"),

        ("13. Kışın Hissolunan Rahmet-i İlahiyye Teveccühü", 
         "Soğuk kış günlerinde evinde sıcacık barınan bir müminin, dışarıdaki dondurucu rahmete karşı şükür borcunu ve iman nimetinin büyüklüğünü daha iyi fark ettiğini belirtir.", 
         "Risale-i Nur Külliyatı, Lem'alar, Altıncı Lem'a",
         "13. Realizing Divine Mercy in Cozy Winter Homes", "Notes how a believer warm inside appreciates the blessing of faith and shelter against freezing external weather.", "Risale-i Nur, The Sixth Flashes"),

        ("14. Kâinatın Büyük Kışları ve Kıyamet Temsili", 
         "Küçük kış ve bahar döngülerinin, kâinatın büyük kışına (kıyamet) ve büyük baharına (ahiret ve haşir) en kati delil ve numune olduğunu kaydeder.", 
         "Risale-i Nur Külliyatı, Sözler, On İkinci Söz",
         "14. Small Winter Cycles as Proof of Cosmic Doomsday", "Records how seasonal winter-spring cycles serve as absolute proofs for the universe's great winter (Doomsday) and spring (Hereafter).", "Risale-i Nur, The Twelfth Word"),

        ("15. Kışın Sükûnetinde Kalbin Safvet Bulması", 
         "Dış dünyanın kış gürültüsü ve donukluğu içinde insanın dünyevi malayani meşguliyetlerden sıyrılarak kalbini ibadete ve tefekküre vermesinin kış mevsimine mahsus kazanç olduğunu söyler.", 
         "Risale-i Nur Külliyatı, Kastamonu Lahikası",
         "15. Heart's Purity in Winter's Quietude", "Explains that winter's quiet helps man detach from worldly trivialities and devote his heart to worship and reflection.", "Risale-i Nur, Kastamonu Addendum")
    ]

    for item in nur_ornekleri:
        baslik = item[0] if is_tr else item[3]
        aciklama = item[1] if is_tr else item[4]
        kaynak = item[2] if is_tr else item[5]
        
        st.markdown(f"""
        <div class="bediuzzaman-box">
            <b>{baslik}:</b><br>
            {aciklama}<br>
            <small style="color: #6b21a8;">📖 {"Kaynak / Eser" if is_tr else "Source / Work"}: <b>{kaynak}</b></small>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. BÖLÜM: HACI BAYRAM-I VELİ HAZRETLERİ
# -----------------------------------------------------------------------------
elif secim == T["menu_options"][3]:
    st.title("🔶 Hacı Bayram-ı Veli Hazretleri'nin Tasavvufi Görüşü" if is_tr else "🔶 Sufi Perspective of Hacı Bayram-ı Veli")
    if is_tr:
        st.markdown("""
        <div class="haciveli-box">
            <b>Nefsin Kışı ve Gönül Baharı:</b><br>
            Anadolu'nun manevi mimarlarından Hacı Bayram-ı Veli Hazretleri'ne göre dervişin kışı; nefsin heveslerinin dondurulduğu, dünya muhabbetinin kalpten uzaklaştırıldığı bir riyazet dönemidir.<br><br>
            * <b>Sessiz Teslimiyet:</b> Kar tanelerinin birbirine çarpmadan yere inmesi misali; dervişin de sessiz ve sedasız bir teslimiyetle ömrünü idame ettirmesi gerektiğini vurgulamıştır.<br><br>
            <b>Kaynak:</b> <i>Bayramiyye Tarikatı Silsilesi & Velâyetnâme-i Hacı Bayram-ı Veli.</i>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="haciveli-box">
            <b>The Winter of Ego & Spring of the Heart:</b><br>
            According to Hacı Bayram-ı Veli, the winter of a seeker represents a period of spiritual discipline where worldly desires are frozen and cleansed from the heart.<br><br>
            * <b>Silent Submission:</b> Just as snowflakes fall silently without colliding, a seeker must lead a life of silent submission and humility.<br><br>
            <b>Source:</b> <i>Bayrami Order Lineage & Velâyetnâme of Hacı Bayram-ı Veli.</i>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. BÖLÜM: VELİ VE ÂLİMLERİN GÖRÜŞLERİ (20+)
# -----------------------------------------------------------------------------
elif secim == T["menu_options"][4]:
    st.title("🌟 İslam Büyükleri ve Mutasavvıfların Kış ve Kar Tefekkürleri (20+ Kaynak)" if is_tr else "🌟 Reflections of Scholars & Saints on Winter (20+ Sources)")

    veli_gorusleri_tr = [
        ("1. Hz. Mevlânâ Celâleddîn-i Rûmî", "Kışın sertliği ve karın soğukluğu toprağı uyutur ama öldürmez; toprağın altındaki tohumları bahara hazırlar. Zorluklar da müminin kalbini olgunlaştırır.", "Mesnevî-i Ma‘nevî"),
        ("2. İmam Gazâlî", "Kış gecelerinin uzunluğu, ibadet edenler için bir ganimettir; kulun Rabbine halvet olması için en mukaddes vakittir.", "İhyâu Ulûmi'd-Dîn"),
        ("3. Yunus Emre", "Kar tanelerinin ses çıkarmadan, birbirine çarpmadan inmesi ilahi nizama tam bir teslimiyettir.", "Risaletü'n-Nushiyye"),
        ("4. İmam-ı Rabbani", "Karın gökyüzünden temiz inip yeryüzündeki kirlere sürünerek erimesi, insanın fıtratındaki temizlik ile dünya imtihanı arasındaki sirdir.", "Mektûbât-ı İmam-ı Rabbani"),
        ("5. Hasan-ı Basri", "Gece ibadeti ne güzeldir; kışı ve yazıyla mümin için bir nurdur. Kışın gecesi uzun olur, kul onda kalkar, Rabbine münacatta bulunur.", "Hilyetü'l-Evliyâ"),
        ("6. Abdülkâdir Geylânî", "Nefsin kışını, onun isteklerinin dondurulması ve iradenin hakikat ateşiyle ısıtılması olarak bilmek gerekir.", "Fethu'r-Rabbânî"),
        ("7. İbrahim Ethem", "Kışın soğuğunda çekilen çile, günahların dökülmesine vesile kefaret ve kalbin masiyetten uzaklaşmasıdır.", "Târihu Medîneti Dımaşk"),
        ("8. Bayezid-i Bistâmî", "Nefsin buzları zikir ateşiyle erimedikçe kalp baharının neşesi tadılamaz.", "Tezkiratü'l-Evliyâ"),
        ("9. Cüneyd-i Bağdadi", "Kışın sükûneti, zahidin dış dünyadan el etek çekip kendi batınına yönelmesi için ilahi bir ikazdır.", "Risale-i Kuşeyriye"),
        ("10. Şah-ı Nakşibend", "Halk içinde Hak ile beraber olma sırrı, en çok kışın kalbin sükûnet bulduğu anlarda aşikâr olur.", "Nefahatü'l-Üns"),
        ("11. Muhyiddin İbn Arabî", "Kış, Hakk'ın 'Kabz' (daraltma) sıfatının tecellisidir ki ardından mutlaka 'Bast' (genişletme ve bahar) zuhur eder.", "Fütûhât-ı Mekkiyye"),
        ("12. Mevlânâ Halid-i Bağdadi", "Uzun kış geceleri, Kur'an tilaveti ve tefekkür ile ihyâ edilmelidir.", "Mektûbât-ı Halidiyye"),
        ("13. Sehl bin Abdullah Tusterî", "Mümin kışın nefsinin hararetini söndürür, takva libasıyla kuşanır.", "Tefsiru'l-Kur'an"),
        ("14. Ebû Bekir el-Kettânî", "Kalbe inen hüzün kar tanesi gibidir; eridikçe kalbin toprağını rahmete gark eder.", "Tabakâtü'ş-Şâfiiyye"),
        ("15. Zünnûn-ı Mısrî", "Tabiatın kış uykusu, insana ölümün bir yok oluş değil, yeni bir boyuta geçiş olduğunu haykırır.", "Hilyetü'l-Evliyâ"),
        ("16. Ma‘ruf-ı Kerhî", "Dünya sevgisi kışın karı gibidir; güneş doğduğunda hemen eriyip gider.", "Tezkiratü'l-Evliyâ"),
        ("17. Şakık-ı Belhî", "Kışın kıtlık ve soğuğu insana acziyetini bildirir; şükür kapısını açar.", "Uyunü'l-Ahbar"),
        ("18. Fudayl bin İyad", "Gece namazına kalkılan uzun kış geceleri, ahiret azığının en bol derlendiği pazarlardır.", "Siyeru A'lâmi'n-Nübelâ"),
        ("19. İmam Şafii", "İlim talebi ve ibadet, kış gecelerinin uzun saatlerinde en bereketli meyvesini verir.", "El-Ümm"),
        ("20. Hacı Bayram-ı Veli", "Nefsin buzları tevbe ateşiyle erirse, gönül tarlasında ilahi muhabbet gülleri açar.", "Bayrami Nesri")
    ]

    veli_gorusleri_en = [
        ("1. Rumi (Mevlana)", "The harshness of winter and snow sleep the earth but do not kill it; it prepares hidden seeds for spring. Hardships similarly mature a believer's heart.", "Masnavi"),
        ("2. Imam Al-Ghazali", "The length of winter nights is a treasure for worshippers; it is a sacred time for seclusion with the Divine.", "Ihya Ulum al-Din"),
        ("3. Yunus Emre", "Snowflakes falling silently without colliding is a sign of complete submission to the Divine order.", "Risaletü'n-Nushiyye"),
        ("4. Imam Rabbani", "Snow falling pure from the sky and melting upon touching earthly dirt symbolizes pure human nature facing worldly trials.", "Maktubat"),
        ("5. Hasan of Basra", "Night worship in winter is light for a believer. The night is long for prayer, and the day is short for fasting.", "Hilyat al-Awliya"),
        ("6. Abdul Qadir Gilani", "The winter of the ego means freezing worldly passions and warming the soul with the fire of truth.", "Futuh al-Ghaib"),
        ("7. Ibrahim ibn Adham", "Enduring winter hardship serves as an expiation for sins and detaches the heart from transgressions.", "History of Damascus"),
        ("8. Bayazid Bastami", "Unless the ice of the ego melts with the fire of remembrance, the joy of spiritual spring cannot be tasted.", "Tadhkirat al-Awliya"),
        ("9. Junayd of Baghdad", "The quietude of winter is a divine reminder for the seeker to withdraw from worldly noise and focus inward.", "Al-Qushayri Risala"),
        ("10. Bahauddin Naqshband", "Solitude in the crowd is most easily realized during the tranquil hours of winter nights.", "Nafahat al-Uns"),
        ("11. Ibn Arabi", "Winter manifests the Divine attribute of 'Contraction' (Qabd), which is inevitably followed by 'Expansion' (Bast/Spring).", "Futuhat al-Makkiyya"),
        ("12. Mawlana Khalid al-Baghdadi", "Long winter nights should be enlivened with Quranic recitation and contemplation.", "Maktubat"),
        ("13. Sahl al-Tustari", "A believer cools down worldly lusts during winter and clothes himself in piety.", "Tafsir al-Tustari"),
        ("14. Abu Bakr al-Kattani", "Spiritual sorrow is like a snowflake; as it melts, it moistens the heart's soil with mercy.", "Tabaqat al-Shafi'iyya"),
        ("15. Dhul-Nun al-Misri", "The slumber of nature in winter proclaims that death is not annihilation, but a transition.", "Hilyat al-Awliya"),
        ("16. Maruf Karkhi", "Love for worldly vanity is like winter snow; it melts away as soon as the sun of gnosis rises.", "Tadhkirat al-Awliya"),
        ("17. Shaqiq al-Balkhi", "The cold of winter teaches man his helplessness and opens the door to gratitude.", "Uyun al-Akhbar"),
        ("18. Fudayl ibn Iyad", "Long winter nights of prayer are markets where provisions for the Hereafter are gathered.", "Siyar A'lam al-Nubala"),
        ("19. Imam Al-Shafi'i", "Seeking knowledge and worshipping yield their most fruitful harvest during long winter hours.", "Al-Umm"),
        ("20. Hacı Bayram-ı Veli", "When the ice of the ego melts with repentance, roses of Divine love bloom in the heart's garden.", "Bayrami Prose")
    ]

    list_to_show = veli_gorusleri_tr if is_tr else veli_gorusleri_en

    for baslik, icerik, kaynak in list_to_show:
        st.markdown(f"""
        <div class="veli-card">
            <b>{baslik}:</b> {icerik}<br>
            <small style="color: #64748b;">📖 {"Kaynak/Eser" if is_tr else "Source/Work"}: <b>{kaynak}</b></small>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. BÖLÜM: HAŞİR VE YENİDEN DİRİLİŞ
# -----------------------------------------------------------------------------
elif secim == T["menu_options"][5]:
    st.title("🌱 Kıştan Bahara Geçiş: Haşir Hakikati" if is_tr else "🌱 Transition from Winter to Spring: The Reality of Resurrection")

    if is_tr:
        st.markdown("""
        <div class="ayet-box">
            <b>Fâtır Suresi, 9. Ayet:</b><br>
            'Rüzgârları gönderip bulutu hareket ettiren Allah’tır. Biz onu <b>ölü bir beldeye sevk edip onunla yeryüzünü ölümünden sonra dirilttik. İşte yeniden diriliş de böyledir.</b>'
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="ayet-box">
            <b>Surah Fatir, 35:9:</b><br>
            'And Allah is He who sends the winds, so they stir up the clouds, and We drive them to a dead land and give life thereby to the earth after its lifelessness. <b>Thus is the Resurrection.</b>'
        </div>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 1. Kış / Winter" if is_tr else "### 1. Winter (Death)")
        st.write("Ağaçlar kurur, toprak donar. Zahiren bir ölüm halidir." if is_tr else "Trees wither, ground freezes. It represents apparent death.")
    with col2:
        st.markdown("### 2. Kar / Snow" if is_tr else "### 2. Snow (Protection)")
        st.write("Kar örtüsü tohumları aşırı soğuktan korur." if is_tr else "The snow blanket protects seeds from extreme frost.")
    with col3:
        st.markdown("### 3. Bahar / Spring" if is_tr else "### 3. Spring (Resurrection)")
        st.write("Ölü tohumlar ayağa kalkar, haşrin somut örneğidir." if is_tr else "Dead seeds awaken, serving as a tangible proof of Resurrection.")