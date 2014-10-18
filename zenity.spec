Summary:	The GNOME port of dialog
Name:		zenity
Version:	3.14.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/zenity/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	144712f5f29a71bf5969525052e75d1c
URL:		http://freshmeat.net/projects/zenity/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-webkit-devel
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libnotify-devel
BuildRequires:	perl-base
BuildRequires:	pkg-config
BuildRequires:	yelp-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zenity is a rewrite of gdialog, the GNOME port of dialog which allows
you to display dialog boxes from the commandline and shell scripts.

%prep
%setup -q
# kill gnome common deps
%{__sed} -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

