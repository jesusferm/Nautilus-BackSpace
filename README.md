# BackSpace in Nautilus on Gnome

The script BackSpaceGnome31-46.py its for fedora version 31 to 40 and Gnome 43 to 46.

The script BackSpaceGnome47.py its for fedora version 41 and Gnome 47.

## Install dependencies package

Installa rpmfusion repositorie

```
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
```
```
sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

### Install package necessary

```
sudo dnf install nautilus-python python3-gobject gtk3 python3 python2 gobject-introspection-devel pkg-config python3-devel
```

## Download python script and save into 

```
~/.local/share/nautilus-python/extensions
```
## Restart nautilus

```
nautilus -q
```

- I test this on Fedora 37, 38 BETA, with kernel >= 6.0.7, 6.2, it's works

License: MIT

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

#### Developed By
----------------
 * linuxitos - <contact@linuxitos.com>