# TODO:
#   * scripts from scripts/ subdirectory are not installed.
Summary:	KDESDK - Software Development Kit for KDE
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	2.2.2
Release:	1
License:	GPL
Group:		X11/Development/Tools
Group(de):	X11/Entwicklung/Werkzeuge
Group(fr):	X11/Development/Outils
Group(pl):	X11/Programowanie/Narzêdzia
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	kdebase-devel = %{version}
BuildRequires:	gettext-devel
BuildRequires:	db2-devel
# kmtrace need /usr/lib/libiberty.a (path hardcoded into configure).
BuildRequires:	binutils-static
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Software Development Kit for KDE.

%description -l pl
Pakiet wspomagaj±cy programowanie w ¶rodowisku KDE.

%package devel
Summary:	Header files for kdesdk
Summary(pl):	Pliki nag³ówkowe dla kdesdk
Group:		X11/Applications/Developement

%description devel
Header files for kdesdk.

%description devel -l pl
Pliki nag³ówkowe dla kdesdk.

%package static
Summary:	Static libraries for kdesdk
Summary(pl):	Statyczne biblioteki dla kdesdk
Group:		X11/Libraries

%description static
Static libraries for kdesdk.

%description static
Statyczne biblioteki dla kdesdk.

%prep
%setup -q

%build

kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--enable-nls \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

gzip -9fn README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/kde2/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/lib*.la
%{_mandir}/*/*
%{_applnkdir}/*/*
%{_datadir}/mimelnk/*/*
%{_datadir}/services/*
%{_datadir}/apps/*
%{_pixmapsdir}/*/*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/lib*so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* %{date} PLD Team <pld-list@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: kdesdk.spec,v $
Revision 1.8  2001-11-26 21:35:13  mkochano
- Release 1.
- Updated to 2.2.2.
- Removed subpackages (they are in other packages now).
- Added static and devel subpackages.

Revision 1.7  2001/09/28 12:54:14  qboosh
- fixed Groups, added Source0 URL (note: current stable version is 2.2.1)

Revision 1.6  2001/05/02 21:51:21  qboosh
- adapterized and made spec %%debug ready or added using %%rpm*flags macros

Revision 1.5  2000/12/03 02:46:37  agaran
Just adapterized

* Sun Jun 13  1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [19990609]
- update to last version.

* Tue Jun  1 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [19990531]
- update to last version.
 
* Sat May 29 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [19990529]
- updating to last version.
 
* Thu May  6 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [0.9-1]
- separating package.

* Wed May  5 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- build RPM.
