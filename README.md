# Antistealer - Güvenlik ve Dosya Erişimi Kısıtlama Aracı

## 🎯 Proje Özeti

**AntiStealer**, kullanıcıların bilgisayarlarına yönelik **uzaktan erişim yazılımlarına (RAT)** karşı güvenlik sağlamak amacıyla geliştirilmiş bir **Python** tabanlı koruma programıdır. Bu yazılım, **kritik dosyaların** kilitlenmesini sağlayarak kötü amaçlı yazılımların bu dosyalara erişmesini engeller.

**AntiStealer**, özellikle popüler uygulamalarda, **Discord**, **Chrome**, **Opera**, **Brave** gibi programlardaki kritik dosyaların güvenliğini sağlamayı hedefler.

## 👥 Takım Bilgileri

| İsim            | Öğrenci No   | Rol              |
| --------------- | ------------ | ---------------- |
| [Emirhan Yavuz] | [2320191077] | Proje Lideri     |
| [Hakan Akkaya]  | [2320191089] | Proje Yardımcısı |

## 📅 Önemli Tarihler

- **Başlangıç:** 2025-01-22
- **Teslim:** 2025-01-25
- **Son Güncelleme:** 2025-01-25

## 🎬 Demo Video

Projenin çalışır demo videosu aşağıdaki bağlantıda bulunmaktadır:

[Demo Video Linki](#) _(1-3 dakika)_

**Video içeriği:**

- Projenin temel özellikleri
- Örnek kullanım senaryosu
- Çıktıların gösterimi

# 🎯 Hedefler ve Kapsam

- **Kritik Dosya Yolları:** Discord, Chrome, Opera, Brave, Edge gibi yaygın uygulamaların verileri hedef alınacaktır.
- **Dosya Erişim Kontrolü:** `icacls` komutu kullanılarak dosya erişim izinleri üzerinde değişiklik yapılacak.
- **Kapsamlı GUI:** PyQt5 kullanılarak, kullanıcının işlem yapabilmesi için bir arayüz tasarlanacaktır.
- **Hedef Sistem:** Bu yazılım Windows işletim sistemi üzerinde çalışacak şekilde tasarlanacaktır.
- **Kilitleme ve Kilit Açma:** Kullanıcı, belirli dosyaları kilitleyip açabilme yeteneğine sahip olacak.
- **Hedef Kullanıcılar:** Sistem yöneticileri veya güvenlik uzmanları, kullanıcıların cihazlarında olası zararlı yazılımlara karşı önlem almasını sağlayacak.


## 🔧 Teknik Gereksinimler

### Yazılım Gereksinimleri

- **Python >= 3.8:** Proje Python 3.8 veya daha yeni bir sürüm ile çalışır.
- **Git:** Proje kodlarının yönetimi ve sürüm kontrolü için Git gereklidir. GitHub gibi bir platformda projenin kaynak kodları depolanabilir.

### Python Kütüphaneleri

- **subprocess:** Komut satırı işlemlerini başlatmak ve yönetmek için kullanılır.
- **os:** Dosya ve dizin işlemleri yapmak için kullanılır.
- **ctypes:** C tarzı işlevleri Python'da çağırmak için kullanılır.
- **PyQt5:** Grafik kullanıcı arayüzü (GUI) oluşturmak için kullanılır.
- **sys:** Python betiğiyle ilgili sistem özelliklerini almak için kullanılır.


## 📂 Proje Yapısı

```plaintext
Antistealer/
│
├── antistealer.py               # Ana Python betiği
├── requirements.txt             # Proje bağımlılıkları
├── README.md                    # Proje açıklaması
├── LICENSE                      # Proje lisansı

```

## 💻 Kullanım

### Gerekli Bağımlılıkları Yükleyin:

İlk olarak, proje klasörüne gidin ve gerekli Python kütüphanelerini yüklemek için terminal üzerinden aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
```

### Ağ Tarama Başlatın:

#### ***Önemli Not: Programı Yönetici Haklarıyla Çalıştırınız.***.

antistealer.py dosyasını çalıştırarak Grafiksel arayüze Erişebilirsiniz.

İsterseniz [Releases](https://github.com/emirhannyvz/Antistealer/releases "Exe dosyasını indirebilirsiniz.") butonuna tıkayarak Exe olarak çalıştırabilirsiniz.

Açılan ekranda ***Lock Files*** butonuna tıklandığında Rat salıdırlarında çalınabilecek olan verilerinizin olduğu klasörler kilitlenerek ***verilerinizi koruma altına alırsınız***.

Kilitlenen Klasör ve Dosyalarınızın kilidini kaldırmak için ***Unlock Files*** butonuna tıklayabilirsiniz.

### Sonuçları Görüntüleyin:

Yapılan işlemler programdaki ***Console ekranında*** sırasıyla yazdırılacaktır.
