# O'Reilly downloader

> Downloads the free ebooks offered by O'Reilly. They can be downloaded by 
categories in different formats.

# Installation
Download the script. It requires `python`. Version `3.x` is advised although it 
should work on version `2.7.x` too. You can execute using:

After downloading it, you need to give it execution permissions:
```
$ chmod +x oreilly_downloader
```

After that, you can execute using:
```
$ ./oreilly_downloader

# If it is in your PATH
$ oreilly_downloader
```

# Usage
```
usage: oreilly_downloader [-h] [-e] [-m] [-p] [-v]
                             [<category> [<category> ...]]

Downloads the free ebooks offered by OReilly. They can be downloaded by
categories in different formats.

positional arguments:
  <category>     category of the books. Choose between: programming business
                 data iot security web-platform webops-perf

optional arguments:
  -h, --help     show this help message and exit
  -e, --epub     download the book in ePub format.
  -m, --mobi     download the book in Mobi format.
  -p, --pdf      download the book in PDF format.
  -v, --version  show program's version number and exit
```

# Meta
- **Author:** Alberto Martinez de Murga ([@threkk](https://threkk.com))   
- **License:** BSD-3. See `LICENSE` for more information.
- **Repository:** https://github.com/threkk/scripts/oreilly_downloader
