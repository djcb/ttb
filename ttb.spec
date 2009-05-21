%define name    ttb
%define version 1.0.1
%define release 1

Summary: TTB Teletekst Browser
Name: %{name}
Version: %{version}
Release: %{release}
Group: Misc
Source0:  %{name}-%{version}.tar.gz
URL: http://www.djcbsoftware.nl/code/ttb
License: GPL
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
Vendor: Dirk-Jan C. Binnema

%description
TTB Teletekst Browser is a small browser for the teletekst system
as used in The Netherlands, and provides a convenient way to stay
up to date with news, sports, weather, stock exchange and what not

%prep
%setup -n %{name}-%{version}

%install
./setup.py -v install --prefix="${RPM_BUILD_ROOT}/usr"
mkdir -p ${RPM_BUILD_ROOT}/usr/share/doc/%{name}-%{version}
cp -av [ALMP]* ${RPM_BUILD_ROOT}/usr/share/doc/%{name}-%{version}

%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && %{__rm} -rf ${RPM_BUILD_ROOT}
rm -rf ${RPM_BUILD_DIR}/%{name}-%{version}

%files
/usr/bin/ttb
/usr/share/applications/ttb.desktop
/usr/share/pixmaps/ttb.png
/usr/share/ttb
/usr/share/doc/%{name}-%{version}

%post
chmod 755 /usr/bin/ttb

