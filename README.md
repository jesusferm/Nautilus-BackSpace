# BackSpace Nautilus 43

Use key backspace to back directory in nautilus 43, only for Fedora >= 37, if any use distro based debian ajust the packge

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

- I test this on fedora 37 beta, with kernel 6.0.7, it's works