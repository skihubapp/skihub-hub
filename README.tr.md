[English](README.md) · Türkçe

<!-- content-version: 2026-10-22.4 -->

# SkiHub

SkiHub, kayak yapmak isteyenleri eğitmenler ve ekipman kiralama noktalarıyla buluşturan, rezervasyon ve güven süreçlerine odaklanan bir girişimdir. Bu merkez; ürünü tanımak, katkı vermek, davetli geliştirici olarak başlamak ve yazılı ticari bilgi istemek için başlangıç noktasıdır.

**Katkı durumu:** **Ready (Hazır)** görevler için public dokümantasyon katkıları [yayımlanan lisanslar](LICENSE.md) kapsamında açıktır. Başlamadan önce görevi üstlenmek istediğini bildir ve bakım sorumlusunun onayını al. Bu merkezin yayımlanması, canlı ürün akışının doğrulandığı anlamına gelmez.

<!-- section: start -->
## Başlangıç yolunu seç

| Amacım… | Başlangıç noktası | Sonraki adım |
| --- | --- | --- |
| SkiHub'ı tanımak | [Ürün](docs/product.md), [güncel durum](docs/status-and-roadmap.md) | Ürün kapsamını ve mevcut kanıtların sınırını oku. |
| Teknik katkı vermek | [Katkı yolları](docs/contribution-paths.md), [katkı rehberi](CONTRIBUTING.md) | Hazır bir dokümantasyon görevi seç, kapsamı bakım sorumlusuyla doğrula ve odaklı bir PR gönder. |
| Davetli geliştirici olarak başlamak | [Davetli geliştirici yolu](CONTRIBUTING.md#invited-developers) | Şirket iletişim adresinden atanmış kapsamı ve başlangıç bilgilerini iste. Erişim kişi bazında onaylanır. |
| İş birliği, sponsorluk veya yatırımı değerlendirmek | [Ticari iletişim](docs/partners.md) | [info@skihub.com.tr](mailto:info@skihub.com.tr) adresine kısa, yazılı bir talep gönder. |

<!-- section: product -->
## Ürün ve markalar

SkiHub ana markadır. KayakHocam.com ve KiralıkKayak.com müşteri ve hizmet sağlayıcı giriş noktaları olarak konumlandırılır. Teknik bağlantıları ve canlı davranışları doğrulama gerektirir. Kurucu Baran Bayran'ın Uludağ'da kayak odası, ekipman kiralama ve dağ operasyonu deneyimi vardır.

SkiHub Core; kimlik, uygunluk, müsaitlik, rezervasyon, ödeme, kiralama ve yorumların esas kaynağı olmalıdır. Bu bir mimari kuraldır; bu merkez, her entegrasyonun bugün bu kurala uyduğunu kanıtlamaz. [Genel mimariyi](docs/architecture.md) incele.

<!-- section: status -->
## Bugün ne doğrulandı?

Güncel kaynak incelemesi, eğitmen başvurusu ve işlem akışlarıyla ilgili kodun bulunduğunu doğruladı. Bu hazırlıkta başvuru arayüzünün küçük bir modülü de izole testlerle kontrol edildi. Eğitmen başvurusu, giriş, eğitmen onayı, AI Match, rezervasyon, ödeme, kiralama ve Camp için canlı uçtan uca doğrulama beklenmektedir. Burada kullanıcı, gelir, iş ortağı, güvenlik denetimi veya operasyon büyüklüğü iddiası yer almaz.

Dört açık durum kullanırız: **Doğrulandı**, **Geliştirme aşamasında**, **Planlanıyor** ve **Doğrulama bekliyor**. Bir not veya yalnızca kod incelemesi, çalışan canlı akışın kanıtı değildir. Her durumun kapsamı için [durum ve yol haritasını](docs/status-and-roadmap.md) incele.

<!-- section: contribute -->
## Kapsamı belli bir işe katkı ver

[İlk görev listesinde](docs/contribution-paths.md), yalnız public dosyalarla yapılabilecek dört dokümantasyon işi bulunur. **HUB-01** (okunabilirlik ve dil eşliği) ile **HUB-03** (katkıcı başlangıcı) üstlenilmeye hazırdır; dış katkıları Baran Bayran inceler. HUB-02 ve HUB-04, teknik inceleyici atanana kadar **Prepared (Hazırlanmış)** durumundadır. Ürün kodu üzerinde çalışma, ayrıca onaylanmış kapsam ve uygun erişim gerektirir.

Özgün merkez metinleri **CC BY 4.0**; denetim aracı, CI ve katkı şablonları **MIT** lisanslıdır. Kesin dosya kapsamı [LICENSE.md](LICENSE.md) içindedir. Geçerli lisansın bildirim ve atıf koşullarıyla ticari yeniden kullanım mümkündür. Ürün kodu, markalar, logolar ve üçüncü taraf materyal bu izinlerin dışındadır. Katkıcı haklarını korur; yalnız aynı dosya lisansıyla paylaşabileceği özgün içeriği gönderir. Bu, hak sahipliğinin devri değildir.

Katkı gönüllüdür. Ücret, hisse, işe alım, ortaklık veya gelecekte iş garantisi verilmez. Kabul edilen katkılara PR geçmişinde atıf yapılır.

Katılmadan önce [CONTRIBUTING.md](CONTRIBUTING.md), [davranış kuralları](CODE_OF_CONDUCT.md) ve [güvenlik bildirim rehberini](SECURITY.md) oku. Varsayılan iletişim yazılıdır; görüşmeler isteğe bağlıdır.

<!-- section: boundaries -->
## Bilgi ve inceleme sınırları

Bu merkez paylaşılabilir dokümantasyon içerir. Ticari ürün kaynağı, müşteri kayıtları, erişim bilgileri veya özel geliştirici başlangıç ayrıntıları içermez. Branch, klasör veya CODEOWNERS kaydı bir depoyu kimlerin okuyabileceğini sınırlamaz.

İlk bakım sorumlusu Baran Bayran'dır; dış katkıcıların dokümantasyon PR'larını inceler. PR yazarı için başka bir yetkili inceleyici gerekir. Ürün kodu değişiklikleri için yetkili teknik inceleyici atanmalıdır. CODEOWNERS incelemeyi yönlendirir; tek başına onayı veya branch korumasını zorunlu kılmaz.

<!-- section: maintain -->
## İki dili birlikte güncelle

Bu README değiştiğinde [README.md](README.md) aynı PR'da güncellenmelidir. Bölüm sırası, anlam, durumlar, iletişim bilgileri, bağlantılar ve `content-version` işareti eş kalmalıdır. Sürüm işareti içerik eşliğini gösterir; ürün sürümü değildir.

Depo kökünde `python tools/check_hub.py` çalıştır. Bu çevrimdışı kontrol; yerel bağlantıları, İngilizce/Türkçe yapı eşliğini ve public kapsam kurallarını denetler. Başarılı sonuç ürün davranışını, çevirinin tüm anlam doğruluğunu veya yayına hazır olmayı kanıtlamaz; bunları inceleyici ayrıca kontrol eder.

<!-- section: contact -->
## İletişim

Yazılı talepler, davetli geliştirici erişim istekleri ve özel güvenlik bildirimleri için [info@skihub.com.tr](mailto:info@skihub.com.tr) adresini kullan. İlk mesajda parola, token, kimlik belgesi, müşteri verisi veya istismar ayrıntısı gönderme. Asgari güvenlik bildirimi için [SECURITY.md](SECURITY.md) rehberini izle.
