# PyPI Yayınlama Rehberi

Bu rehber, paketinizi PyPI'ya (Python Package Index) nasıl yükleyeceğinizi adım adım gösterir.

## 📋 Ön Gereksinimler

### 1. PyPI Hesabı Oluşturun

- **Test PyPI** (test için): https://test.pypi.org/account/register/
- **Gerçek PyPI**: https://pypi.org/account/register/

### 2. Gerekli Araçları Yükleyin

```bash
pip install --upgrade pip setuptools wheel twine build
```

## 🔧 Paket Hazırlığı

### 1. Bilgileri Güncelleyin

Aşağıdaki dosyalarda **kendi bilgilerinizi** girin:

**setup.py** ve **pyproject.toml** dosyalarında:
- `author="Your Name"` → Adınız
- `author_email="your.email@example.com"` → E-postanız
- `url="https://github.com/yourusername/..."` → GitHub URL'niz

**chessboard_generator/__init__.py** dosyasında:
- `__author__` ve `__email__` değerlerini güncelleyin

### 2. Paket Adı Kontrolü

PyPI'da paket adınızın müsait olup olmadığını kontrol edin:
- https://pypi.org/project/chessboard-calibration-generator/

Eğer alınmışsa, `setup.py` ve `pyproject.toml` dosyalarında farklı bir isim seçin.

## 🏗️ Paket Oluşturma

### 1. Proje Dizinine Gidin

```bash
cd /home/anzatsan/Kodlar/fusionV4/chessboard-calibration-generator
```

### 2. Paketi Build Edin

```bash
python -m build
```

Bu komut `dist/` klasöründe iki dosya oluşturur:
- `chessboard_calibration_generator-1.0.0.tar.gz` (source distribution)
- `chessboard_calibration_generator-1.0.0-py3-none-any.whl` (wheel)

## 🧪 Test PyPI'da Test Etme (ÖNERİLİR)

Önce Test PyPI'da test etmenizi şiddetle öneriyoruz!

### 1. Test PyPI'ya Yükleyin

```bash
python -m twine upload --repository testpypi dist/*
```

Kullanıcı adı ve şifrenizi girin (Test PyPI hesabınız).

### 2. Test PyPI'dan Yükleyip Test Edin

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ chessboard-calibration-generator
```

### 3. Test Edin

```bash
# CLI'yı test edin
chessboard-generator

# Python'dan test edin
python -c "from chessboard_generator import ChessboardGenerator; print('Success!')"
```

## 🚀 Gerçek PyPI'ya Yükleme

Her şey test'te çalışıyorsa, gerçek PyPI'ya yükleyin:

```bash
python -m twine upload dist/*
```

## 🔐 API Token Kullanımı (Önerilir)

Şifre yerine API token kullanmak daha güvenlidir:

### 1. PyPI'da Token Oluşturun

- PyPI'a giriş yapın
- Account Settings → API tokens → Add API token
- Scope: "Entire account" veya specific project
- Token'ı kopyalayın (bir daha gösterilmeyecek!)

### 2. Token ile Yükleme

```bash
python -m twine upload --username __token__ --password <your-token> dist/*
```

### 3. ~/.pypirc Dosyası Oluşturun (Opsiyonel)

```ini
[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcC...your-token-here...

[testpypi]
username = __token__
password = pypi-AgENdGVzdC5weXBpLm9yZw...your-token-here...
```

## 📦 Yeni Versiyon Yükleme

Güncellemeler için:

### 1. Versiyon Numarasını Artırın

**setup.py**, **pyproject.toml** ve **__init__.py** dosyalarında:
```python
version="1.0.1"  # veya 1.1.0, 2.0.0 vb.
```

### 2. Eski Build Dosyalarını Temizleyin

```bash
rm -rf build/ dist/ *.egg-info/
```

### 3. Yeniden Build ve Upload

```bash
python -m build
python -m twine upload dist/*
```

## ✅ Doğrulama

Paket yüklendikten sonra:

```bash
# Yükleyin
pip install chessboard-calibration-generator

# CLI'yı test edin
chessboard-generator

# Veya Python'dan
python -c "from chessboard_generator import ChessboardGenerator"
```

## 📊 İstatistikler ve Yönetim

- Paket sayfanız: `https://pypi.org/project/chessboard-calibration-generator/`
- İndirme istatistikleri: https://pypistats.org/
- Yönetim: PyPI hesabınızdan

## 🐛 Yaygın Hatalar ve Çözümleri

### "The user '...' isn't allowed to upload to project"
→ Paket adı zaten alınmış, farklı bir isim seçin

### "File already exists"
→ O versiyon zaten yüklenmiş, versiyon numarasını artırın

### "Invalid distribution"
→ `rm -rf dist/ build/ *.egg-info/` çalıştırıp tekrar build edin

### ImportError
→ `__init__.py` dosyasının doğru olduğundan emin olun

## 📚 Ek Kaynaklar

- PyPI Packaging Tutorial: https://packaging.python.org/tutorials/packaging-projects/
- Semantic Versioning: https://semver.org/
- Python Packaging User Guide: https://packaging.python.org/

## 🎉 Tebrikler!

Paketinizi başarıyla yüklediyseniz, artık herkes şu şekilde kullanabilir:

```bash
pip install chessboard-calibration-generator
```

İyi şanslar! 🚀
