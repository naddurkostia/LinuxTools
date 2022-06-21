pkgname=LinuxTools
pkgver=1.0.0
pkgrel=1
pkgdesc="A script for comfortable package installation."
arch=('x86_64')
url="https://github.com/naddurkostia/${pkgname}"
license=('MIT')
depends=('bash')
source=("https://github.com/naddurkostia/${pkgname}/archive/${pkgver}.tar.gz")
md5sums=('SKIP')

package() {
  install -Dm755 "$srcdir/$pkgname-$pkgver/_main_.py" "$pkgdir/usr/bin/$pkgname"
  install -Dm644 "$srcdir/$pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
