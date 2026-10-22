[English](README.md) · Türkçe

<!-- content-version: 2026-10-22.2 -->

# SkiHub

SkiHub, kayak yapmak isteyenleri eğitmenler ve ekipman kiralama noktalarıyla buluşturan, rezervasyon ve güven süreçlerine odaklanan bir girişimdir. Bu merkez; ürünü tanımak, katkı vermek, davetli geliştirici olarak başlamak ve yazılı ticari bilgi istemek için başlangıç noktasıdır.

**Hazırlık durumu:** bu içerik public yayına adaydır. Yayın ve katkı koşulları kurucunun onayını beklemektedir. Bu kararlar kayda geçene kadar katkı kabulü kapalıdır. Bu belgelerin hazırlanması, canlı ürün akışının doğrulandığı anlamına gelmez.

<!-- section: start -->
## Başlangıç yolunu seç

| Amacım… | Başlangıç noktası | Sonraki adım |
| --- | --- | --- |
| SkiHub'ı tanımak | [Ürün](docs/product.md), [güncel durum](docs/status-and-roadmap.md) | Ürün kapsamını ve mevcut kanıtların sınırını oku. |
| Teknik katkı vermek | [Katkı yolları](docs/contribution-paths.md), [katkı rehberi](CONTRIBUTING.md) | Sınırları belirli bir görevi incele; çalışma göndermeden önce katkı kabulünün açılmasını bekle. |
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

[İlk görev listesinde](docs/contribution-paths.md), yayın ve katkı koşulları onaylandıktan sonra yalnız public dosyalarla yapılabilecek dört dokümantasyon işi bulunur. Bunlar hazırlanmış adaylardır; henüz katkıya açılmış görevler değildir. Ürün kodu üzerinde çalışma, ayrıca onaylanmış kapsam ve uygun erişim gerektirir.

Katkı gönüllüdür. Ücret, hisse, işe alım veya ortaklık garantisi verilmez. İçeriğin yayımlanması ve PR gönderilmesi tek başına hakları veya ticari kullanım koşullarını belirlemez. Bu aday için lisans seçilmemiştir; katkı kabulü açılmadan önce geçerli koşulları kurucu onaylamalıdır. Katkı sahibi farklı bir talepte bulunmadıkça, kabul edilen PR geçmişinde kendisine atıf yapılır.

Katılmadan önce [CONTRIBUTING.md](CONTRIBUTING.md), [davranış kuralları](CODE_OF_CONDUCT.md) ve [güvenlik bildirim rehberini](SECURITY.md) oku. Varsayılan iletişim yazılıdır; görüşmeler isteğe bağlıdır.

<!-- section: boundaries -->
## Bilgi ve inceleme sınırları

Bu merkez paylaşılabilir dokümantasyon içerir. Ticari ürün kaynağı, müşteri kayıtları, erişim bilgileri veya özel geliştirici başlangıç ayrıntıları içermez. Branch, klasör veya CODEOWNERS kaydı bir depoyu kimlerin okuyabileceğini sınırlamaz.

İlk inceleme sorumlusu Baran Bayran'dır. Teknik değişiklikler veya mevcut tek inceleyicinin yazdığı PR için ikinci teknik inceleyici atanmalıdır. Yazar kendi PR'ını onaylayamaz. CODEOWNERS, incelemeyi yönlendiren dosyadır; tek başına onayı veya branch korumasını zorunlu kılmaz.

<!-- section: maintain -->
## İki dili birlikte güncelle

Bu README değiştiğinde [README.md](README.md) aynı PR'da güncellenmelidir. Bölüm sırası, anlam, durumlar, iletişim bilgileri, bağlantılar ve `content-version` işareti eş kalmalıdır. Sürüm işareti içerik eşliğini gösterir; ürün sürümü değildir.

Depo kökünde `python tools/check_hub.py` çalıştır. Bu çevrimdışı kontrol; yerel bağlantıları, İngilizce/Türkçe yapı eşliğini ve public kapsam kurallarını denetler. Başarılı sonuç ürün davranışını, çevirinin tüm anlam doğruluğunu veya yayına hazır olmayı kanıtlamaz; bunları inceleyici ayrıca kontrol eder.

<!-- section: contact -->
## İletişim

Yazılı talepler, davetli geliştirici erişim istekleri ve özel güvenlik bildirimleri için [info@skihub.com.tr](mailto:info@skihub.com.tr) adresini kullan. İlk mesajda parola, token, kimlik belgesi, müşteri verisi veya istismar ayrıntısı gönderme. Asgari güvenlik bildirimi için [SECURITY.md](SECURITY.md) rehberini izle.
