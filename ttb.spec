Summary: TTB Teletekst Browser
Name: ttb
Version: 0.9.5
Release: 
Group: Misc
URL: http://www.djcbsoftware.nl/code/ttb
Packager: 
License: GPL
BuildArch: noarch

%description
TTB Teletekst Browser is a small browser for the teletekst system
as used in The Netherlands, and provides a convenient way to stay
up to date with news, sports, weather, stock exchange and what not

%files
/usr/bin/ttb
/usr/share/applications/ttb.desktop
/usr/share/pixmaps/ttb.png
/usr/share/ttb/ttb.glade

%post
chmod 755 /usr/bin/ttb

%postun
rm -f /usr/share/ttb

