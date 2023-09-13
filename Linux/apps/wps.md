

## Installation

1. Go [here](linux.wps.com) and download the proper package (mine was `.deb`).

2. Where it is downloaded, install it using `dpkg`:

```
sudo dpkg -i <filename>
```

To run, search wps from the start menu.

### A more reliable way

When installed from using the above instructions, sometimes it would not open. This way it has no problem:

```
sudo snap install wps-office-multilang
sudo snap connect wps-office-multilang:removable-media
```

To run,

```
# for ppt
wps-office-multilang.wpp
# for doc
wps-office-multilang.wps
# for spreadsheets
wps-office-multilang.et
```
