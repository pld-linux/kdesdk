%define	date	19990713
Summary:	KDESDK - Software Development Kit for KDE.
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE.
Name:		kdesdk
Version: 	%{date}
Release:	1
Copyright:	GPL
Group:		X11/KDE/Development
Group(pl):	X11/KDE/Programowanie
#ftp:		ftp.kde.org
#patch:		/pub/kde/snapshots
Source:		%{name}-%{version}.tar.bz2
Patch:		kdesdk-fix.patch
Patch1:		kdesdk-scripts-fix.patch
Requires:	qt >= 1.44, kdelibs >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix	/usr/X11R6
%define	_mandir	/usr/X11R6/man

%description
Software Development Kit for KDE

%description -l pl
Pakiet wspomagaj±cy programowanie w ¶rodowisku KDE.

%package kdesgmltools
Summary:	SGML-tools for KDE. 
Summary(pl):	Narzêdzie SGML-u dla KDE
Group:		X11/KDE/Development
Group(pl):	X11/KDE/Narzêdzia

%description kdesgmltools

%description -l pl kdesgmltools

%package ktranslator
Summary:	KDE Translator Tools
Summary(pl):	Prosty tlumacz dla KDE
Group:		X11/KDE/Development
Group(pl):	X11/KDE/Narzêdzia

%description ktranslator

%description -l pl ktranslator
Program wspomagaj±cy tworzenie t³umaczeñ dla aplikacji tworzonych w
¶rodowisku KDE.

%package kdoc
Summary:	K documantation tools
Summary(pl):	Kdoc
Group:		X11/KDE/Development
Group(pl):	X11/KDE/Narzêdzia

%description kdoc
KDE documentation tools.

%description -l pl kdoc
Narzêdzia do tworzenia dokumentacji dla KDE.

%package kappgen
Summary:	kappgen
Summary(pl):	kappgen
Group:		X11/KDE/Development
Group(pl):	X11/KDE/Narzêdzia

%description kappgen
This program make abasic KDE application.
 
%description -l pl kappgen
Program do tworzenia prostego szkieletu aplikacji dla KDE.

%prep
%setup -q -n %{name}
%patch -p0
%patch1 -p0

%build
export KDEDIR=%{_prefix}
CXXFLAGS="$RPM_OPT_FLAGS -Wall -fno-rtti -fno-exceptions" \
CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target} \
	--prefix=$KDEDIR \
	--enable-nls \
	--with-install-root=$RPM_BUILD_ROOT

make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/kde/toolbar

export KDEDIR=%{_prefix}
make \
	prefix=$RPM_BUILD_ROOT$KDEDIR \
	sgml_prefix=$RPM_BUILD_ROOT/usr/lib/sgml-tools \
	kde_prefix=$RPM_BUILD_ROOT$KDEDIR \
	INSTALL=/usr/bin/install \
	install

%find_lang ktranslator
%find_lang kappgen

gzip -9 $RPM_BUILD_ROOT/usr/X11R6/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files kdesgmltools 
#-f kdesgmltools.lang
%defattr(644, root, root, 755)
#%doc
%attr(755,root,root) %{_bindir}/ksgml2html
%attr(755,root,root) %{_bindir}/kniceinc
%{_datadir}/apps/niceSgml2Html/
/usr/lib/sgml-tools
%lang(en) %{_datadir}/doc/HTML/en/ksgml2html/*

%files ktranslator -f ktranslator.lang
%defattr(644, root, root, 755)
#%doc
%config(missingok) /etc/X11/kde/ktranslatorrc
%config(missingok) /etc/X11/kde/applnk/Applications/ktranslator.kdelnk

%attr(755,root,root) %{_bindir}/ktranslator
%lang(en) %{_datadir}/kde/doc/HTML/en/ktranslator

%files kdoc
%defattr(644, root, root, 755)
#%doc
%attr(755,root,root) %{_bindir}/kdoc
%attr(755,root,root) %{_bindir}/qt2kdoc
%{_datadir}/kdoc
/usr/X11R6/man/man1/kdoc.1.gz
/usr/X11R6/man/man1/qt2kdoc.1.gz

%files kappgen
%defattr(644, root, root, 755)
#%doc
%attr(755,root,root) %{_bindir}/kappgen
%{_datadir}/kde/apps/kappgen

%files
%defattr(644, root, root, 755)
#%doc
%attr(755,root,root) %{_bindir}/cvs*
%attr(755,root,root) %{_bindir}/cxxmetric
%attr(644,root,root) /usr/X11R6/man/man1/cvs*.1.gz

%changelog
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
