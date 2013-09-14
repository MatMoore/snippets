Dumb Archive eXtractor
======================
§2.8.4 of the tar man page (https://www.gnu.org/software/tar/manual/html_section/extract.html#SEC29) has
this to say about extracting files from the internet:
> Extracting files from archives can overwrite files that already exist.
> If you receive an archive from an untrusted source, you should make a new directory
> and extract into that directory, so that you don't have to worry about the extraction
> overwriting one of your existing files.
> For example, if ‘untrusted.tar’ came from somewhere else on the Internet, and you don't
> necessarily trust its contents, and you don't necessarily trust its contents, you can extract it as follows: 

    $ mkdir newdir
    $ cd newdir
    $ tar -xvf ../untrusted.tar

This basically does that, for files that can be extracted with tar and unzip.

* If the archive constains a parent directory that can be safely extracted into
the current directory, it will be.
* If the archive can't be extracted to the current directory, it will be extracted
to a directory sharing the same name as the archive.
* If the directory already exists, the archive will be skipped.
