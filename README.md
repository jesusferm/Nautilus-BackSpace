# BackSpace in Nautilus on Gnome

Versión for Gnome before 41, 42 to 48, and for gnome 49


## Install dependencies package for all versión

Install rpmfusion repositorie

```
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
```
```
sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

### Install package

```
sudo dnf install nautilus-python python3-gobject gtk3 python3 gobject-introspection-devel pkg-config python3-devel gtk-murrine-engine  kernel-headers kernel-devel dkms elfutils-libelf-devel qt5-qtx11extras gcc make perl bzip2 meson ninja-build gcc python3-devel python3-pip gobject-introspection-devel glib2-devel nautilus-devel
```

## Download python script and save into 


```
~/.local/share/nautilus-python/extensions
```



## Restart nautilus

```
nautilus -q
```

- Tested on Fedora with Gnome (41-49)

License: MIT

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

#### Developed By
----------------
 * linuxitos - <contact@linuxitos.com>