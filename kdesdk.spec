%define	date	19990713
Summary:	KDESDK - Software Development Kit for KDE
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	%{date}
Release:	1
License:	GPL
Group:		X11/Development/Tools
Group(de):	X11/Entwicklung/Werkzeuge
Group(fr):	X11/Development/Outils
Group(pl):	X11/Programowanie/Narzêdzia
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-fix.patch
Patch1:		%{name}-scripts-fix.patch
Requires:	qt >= 1.44, kdelibs >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Software Development Kit for KDE.

%description -l pl
Pakiet wspomagaj±cy programowanie w ¶rodowisku KDE.

%package kdesgmltools
Summary:	SGML-tools for KDE
Summary(pl):	Narzêdzie SGML-u dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje

%description kdesgmltools

%description kdesgmltools -l pl

%package ktranslator
Summary:	KDE Translator Tools
Summary(pl):	Prosty t³umacz dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje

%description ktranslator
Tool supporting translation of KDE applications.

%description ktranslator -l pl
Program wspomagaj±cy tworzenie t³umaczeñ dla aplikacji tworzonych w
¶rodowisku KDE.

%package kdoc
Summary:	K documentation tools
Summary(pl):	Narzêdzia do dokumentacji KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje

%description kdoc
KDE documentation tools.

%description kdoc -l pl
Narzêdzia do tworzenia dokumentacji dla KDE.

%package kappgen
Summary:	kappgen
Summary(pl):	kappgen
Group:		X11/Development/Tools
Group(de):	X11/Entwicklung/Werkzeuge
Group(fr):	X11/Development/Outils
Group(pl):	X11/Programowanie/Narzêdzia

%description kappgen
This program makes a basic KDE application.

%description kappgen -l pl
Program do tworzenia prostego szkieletu aplikacji dla KDE.

%prep
%setup -q -n %{name}
%patch -p0
%patch1 -p0

%build
KDEDIR=%{_prefix} ; export KDEDIR
CXXFLAGS="%{rpmcflags} -Wall -fno-rtti -fno-exceptions" \
CFLAGS="%{rpmcflags} -Wall" \
./configure %{_target} \
	--prefix=$KDEDIR \
	--enable-nls \
	--with-install-root=$RPM_BUILD_ROOT

%{__make} KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/kde/toolbar

export KDEDIR=%{_prefix}
%{__make} \
	prefix=$RPM_BUILD_ROOT$KDEDIR \
	sgml_prefix=$RPM_BUILD_ROOT/usr/lib/sgml-tools \
	kde_prefix=$RPM_BUILD_ROOT$KDEDIR \
	INSTALL=/usr/bin/install \
	install

%find_lang ktranslator
%find_lang kappgen

%clean
rm -rf $RPM_BUILD_ROOT

%files kdesgmltools 
%defattr(644,root,root,755)
#-f kdesgmltools.lang
%defattr(644, root, root, 755)
#%doc
%attr(755,root,root) %{_bindir}/ksgml2html
%attr(755,root,root) %{_bindir}/kniceinc
%{_datadir}/apps/niceSgml2Html/
/usr/lib/sgml-tools
%lang(en) %{_datadir}/doc/HTML/en/ksgml2html/*

%files ktranslator -f ktranslator.lang
%defattr(644,root,root,755)
#%doc
%config(missingok) %{_sysconfdir}/X11/kde/ktranslatorrc
%config(missingok) %{_sysconfdir}/X11/kde/applnk/Applications/ktranslator.kdelnk

%attr(755,root,root) %{_bindir}/ktranslator
%lang(en) %{_datadir}/kde/doc/HTML/en/ktranslator

%files kdoc
%defattr(644,root,root,755)
#%doc
%attr(755,root,root) %{_bindir}/kdoc
%attr(755,root,root) %{_bindir}/qt2kdoc
%{_datadir}/kdoc
%{_mandir}/man1/kdoc.1*
%{_mandir}/man1/qt2kdoc.1*

%files kappgen
%defattr(644,root,root,755)
#%doc
%attr(755,root,root) %{_bindir}/kappgen
%{_datadir}/kde/apps/kappgen

%files
%defattr(644,root,root,755)
#%doc
%attr(755,root,root) %{_bindir}/cvs*
%attr(755,root,root) %{_bindir}/cxxmetric
%attr(644,root,root) %{_mandir}/man1/cvs*.1*

%changelog
* %{date} PLD Team <pld-list@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: kdesdk.spec,v $
Revision 1.7  2001-09-28 12:54:14  qboosh
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
