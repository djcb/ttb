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
%if 0%{?fedora} <= 8 && 0%{?rhel} <= 5
BuildRequires: python-setuptools
%else
BuildRequires: python-setuptools-devel
%endif

%description
TTB Teletekst Browser is a small browser for the teletekst system
as used in The Netherlands, and provides a convenient way to stay
up to date with news, sports, weather, stock exchange and what not

#%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%prep
%setup -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} -c 'import setuptools; execfile("setup.py")' build

%install
%{__python} -c 'import setuptools; execfile("setup.py")' install --skip-build --root $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/usr/share/doc/%{name}-%{version}
cp -av [ALMP]* ${RPM_BUILD_ROOT}/usr/share/doc/%{name}-%{version}

%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && %{__rm} -rf ${RPM_BUILD_ROOT}
rm -rf ${RPM_BUILD_DIR}/%{name}-%{version}

%files
%defattr(-,root,root,-)
/usr/bin/ttb
/usr/share/applications/ttb.desktop
/usr/share/pixmaps/ttb.png
/usr/share/ttb
/usr/share/doc/%{name}-%{version}
%{python_sitelib}/*
#%if 0%{?fedora} >= 9
#%{python_sitelib}/%{name}-%{version}-*.egg-info
#%endif

%post
chmod 755 /usr/bin/ttb

%changelog
* Wed Aug 12 2009 Marco Hartgring <marco.hartgring@gmail.com>
- Updated spec file to add python egg support
