#!/bin/bash
# Manual Release Script - Tag ve Release Oluşturma

set -e  # Hata durumunda dur

echo "🚀 OpenCV Chessboard Generator - Release Script"
echo "================================================"
echo ""

# Mevcut versiyonu al
CURRENT_VERSION=$(grep "version = " pyproject.toml | head -1 | cut -d'"' -f2)
echo "📦 Mevcut versiyon: $CURRENT_VERSION"
echo ""

# Yeni versiyon sor
read -p "🔢 Yeni versiyon numarası (örn: 1.0.1): " NEW_VERSION

if [ -z "$NEW_VERSION" ]; then
    echo "❌ Versiyon numarası boş olamaz!"
    exit 1
fi

echo ""
echo "📝 Versiyon güncelleniyor: $CURRENT_VERSION → $NEW_VERSION"

# Dosyaları güncelle
sed -i "s/version = \"$CURRENT_VERSION\"/version = \"$NEW_VERSION\"/" pyproject.toml
sed -i "s/version=\"$CURRENT_VERSION\"/version=\"$NEW_VERSION\"/" setup.py
sed -i "s/__version__ = \"$CURRENT_VERSION\"/__version__ = \"$NEW_VERSION\"/" chessboard_generator/__init__.py

echo "✅ Dosyalar güncellendi"

# Commit ve tag
echo ""
read -p "📋 Release notları (bir satırda): " RELEASE_NOTES

if [ -z "$RELEASE_NOTES" ]; then
    RELEASE_NOTES="Version $NEW_VERSION"
fi

echo ""
echo "💾 Değişiklikler commit ediliyor..."
git add pyproject.toml setup.py chessboard_generator/__init__.py
git commit -m "chore: bump version to $NEW_VERSION [skip ci]"

echo "🏷️  Tag oluşturuluyor: v$NEW_VERSION"
git tag -a "v$NEW_VERSION" -m "Version $NEW_VERSION"

echo "☁️  GitHub'a push ediliyor..."
git push origin main
git push origin "v$NEW_VERSION"

echo ""
echo "✅ Git tag oluşturuldu ve push edildi!"
echo ""
echo "📦 Şimdi package build ediliyor..."
rm -rf dist/ build/ *.egg-info/
python3 -m build

echo ""
echo "🎉 İşlem tamamlandı!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 Sonraki Adımlar:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1️⃣  GitHub Release Oluştur:"
echo "   gh release create v$NEW_VERSION --title \"Version $NEW_VERSION\" \\"
echo "     --notes \"$RELEASE_NOTES\" \\"
echo "     dist/opencv_chessboard_generator-$NEW_VERSION-py3-none-any.whl \\"
echo "     dist/opencv_chessboard_generator-$NEW_VERSION.tar.gz"
echo ""
echo "2️⃣  PyPI'ya Yükle:"
echo "   python3 -m twine upload dist/*"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
