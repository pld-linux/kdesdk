
%define		_state		stable
%define		_ver		3.1.4

Summary:	KDESDK - Software Development Kit for KDE
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	%{_ver}
Release:	0.1
Epoch:		8
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	ed343cedeab6c6dc814fa8b4e164e4ec
# translations are generated from kde-i18n.spec now
Source1:	ftp://blysk.ds.pg.gda.pl/linux/kde-i18n-package/%{version}/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	3afe212bf8a89f8a51a991d8ad3ae552
BuildRequires:	bison
BuildRequires:	ed
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel
BuildRequires:	kdebase-devel = %{epoch}:%{version}
BuildRequires:	libltdl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kdesdk-devel

%define		_htmldir	/usr/share/doc/kde/HTML
%define		_gimpdir	%(gimptool --gimpdatadir)
%define		_appdefdir	/usr/X11R6/lib/X11/app-defaults
%define		_emacspkgdir	/usr/share/emacs/21.2
%define		_xemacspkgdir	/usr/share/xemacs-packages
%define		_zshfcdir	/usr/share/zsh/latest/functions

%description
Software Development Kit for KDE.

%description -l pl
Pakiet wspomagaj±cy programowanie w ¶rodowisku KDE.

%package static
Summary:	Static libraries for kdesdk
Summary(pl):	Statyczne biblioteki dla kdesdk
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description static
Static libraries for kdesdk.

%description static -l pl
Statyczne biblioteki dla kdesdk.

%package cervisia
Summary:	A KDE cvs frontend
Summary(pl):	Frontend CVS pod KDE
Group:		X11/Development/Tools
Requires:	cvs >= 1.10
Obsoletes:	%{name}-devel

%description cervisia
A KDE cvs frontend.

%description cervisia -l pl
Frontend CVS pod KDE.

%package completions-bash
Summary:	Autocomplete definitions for bash
Summary(pl):	Definicje autouzupe³niania dla basha
Group:		Applications/Shells
Requires:	bash-completion
Obsoletes:	%{name}-devel

%description completions-bash
Autocomplete definitions for bash.

%description completions-bash -l pl
Definicje autouzupe³niania dla basha.

%package completions-zsh
Summary:	Autocomplete definitions for zsh
Summary(pl):	Definicje autouzupe³niania dla zsh
Group:		Applications/Shells
Requires:	zsh >= 4.0.6-2
Obsoletes:	%{name}-devel

%description completions-zsh
Autocomplete definitions for zsh.

%description completions-zsh -l pl
Definicje autouzupe³niania dla zsh.

%package emacs
Summary:	A set of macros for emacs
Summary(pl):	Zestaw makr do emacsa
Group:		X11/Development/Tools
Requires:	emacs-common
Obsoletes:	%{name}-devel

%description emacs
A set of macros for emacs.

%description emacs -l pl
Zestaw makr do emacsa.

%package kaddressbook-kdeaccounts
Summary:	A kdeaccounts plugin for the KDE adressbook
Summary(pl):	Wtyczka do ksi±¿ki adresowej KDE dodaj±ca obs³ugê kdeaccounts
Group:		X11/Applications
Requires:	kdepim-kaddressbook >= 3.0.8
Obsoletes:	%{name}-devel

%description kaddressbook-kdeaccounts
A kdeaccounts plugin for the KDE adressbook. What is does is adding
the people from KDE's CVS accounts file to the addressbook.

%description kaddressbook-kdeaccounts -l pl
Wtyczka do ksi±¿ki adresowej KDE dodaj±ca obs³ugê kdeaccounts. Dodaje
ona osoby posiadaj±ce konta w CVS KDE do ksi±¿ki adresowej.

%package kapptemplate
Summary:	KDE application framework generator
Summary(pl):	Generator szkieletu dla aplikacji KDE
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description kapptemplate
Modular shell script that will automatically create a framework for
either a normal KDE 3.x application, a KPart application, a KPart
plugin, or convert an existing application.

%description kapptemplate -l pl
Modularny skrypt, który potrafi automatycznie wygenerowaæ szkielet
katalogów dla zwyk³ej aplikacji pod KDE 3.x, aplikacji KPart, wtyczki
KPart lub skonwertowaæ istniej±c± aplikacjê.

%package kbabel
Summary:	An advanced and easy to use PO-file editor
Summary(pl):	Rozbudowany i ³atwy w obs³udze edytor plików PO
Group:		X11/Development/Tools
Requires:	gettext-devel
Obsoletes:	%{name}-devel

%description kbabel
KBabel is a tool, that allows easy management, edition and upkeep of
gettext .po files.

%description kbabel -l pl
KBabel jest narzêdziem, które pozwala na ³atwe zarz±dzanie, edycjê i
utrzymanie plików po.

%package kbabel-devel
Summary:	Kbabel headers
Summary(pl):	Pliki nag³ówkowe KBabel
Group:		X11/Development
Requires:	gettext-devel
Requires:	%{name}-kbabel = %{epoch}:%{version}
Requires:	%{name}-kbabel-catalog = %{epoch}:%{version}
Requires:	%{name}-kbabel-dictionary = %{epoch}:%{version}
Obsoletes:	%{name}-devel

%description kbabel-devel
KBabel headers.

%description kbabel-devel -l pl
Pliki nag³ówkowe KBabel.

%package kbabel-dictionary
Summary:	Plugin that supports dictionaries made from po compendia
Summary(pl):	Wtyczka kbabel obs³uguj±ca s³owniki z kompendiów po
Group:		X11/Development
Requires:	gettext-devel
Requires:	%{name}-kbabel = %{epoch}:%{version}
Obsoletes:	%{name}-devel

%description kbabel-dictionary
Plugin that supports dictionaries made from po compendia.

%description kbabel-dictionary -l pl
Wtyczka kbabel obs³uguj±ca s³owniki z kompendiów po.

%package kbabel-catalog
Summary:	A KBabel catalog manager
Summary(pl):	Zarz±dca zbiorów plików po zintegrowany z KBabel
Group:		X11/Development
Requires:	gettext-devel
Requires:	%{name}-kbabel = %{epoch}:%{version}
Obsoletes:	%{name}-devel

%description kbabel-catalog
A KBabel catalog manager.

%description kbabel-catalog -l pl
Zarz±dca zbiorów plików po zintegrowany z KBabel.

%package kbugbuster
Summary:	A tools that allows cooperation with bugs.kde.org
Summary(pl):	Narzêdzie wspó³pracuj±ce z bugs.kde.org
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description kbugbuster
KBugBuster allows easy bug management on bugs.kde.org.

%description kbugbuster -l pl
KBugBuster u³atwia wyszukwianie i zarz±dzanie b³êdami na bugs.kde.org.

%package kmtrace
Summary:	A mtrace to full backtrace conversion tool
Summary(pl):	Narzêdzie do konwersji z mtrace do pe³nego backtrace'a
Group:		X11/Development/Tools
BuildRequires:	binutils-static
Obsoletes:	%{name}-devel

%description kmtrace
Converts glibc's mtrace log into a full backtrace.

%description kmtrace -l pl
Konwertuje mtrace glibca do pe³nego backtrace'a.

%package kompare
Summary:	Kompare is a program to view the differences between files
Summary(pl):	Kompare to program s³u¿±cy do porównywania zmian miêdzy plikami
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description kompare
Kompare is a program to view the differences between files. Features
include:

  * comparison of files or directories via a graphical interface
  * bezier-based connection widget lets you see both source and destination
    as they really appear
  * graphical viewing of patch files in normal, context, unified and
    diff formats
  * interactive application of differences
  * full network transparency
  * ability to view plain-text diff output in embedded viewer
  * easy navigation of multiple-file diffs with dockable navigation tree
  * graphical interface to commonly used diff command line options
  * switch source and destination with one command
  * diff statistics

%description kompare -l pl
Kompare to program s³u¿±cy do porównywania zmian miêdzy plikami.
Aktualnie dostêpne funkcje:
  * porównanie plików lub katalogów poprzez graficzny interfejs
  * przedstawienie ¼ród³a i celu za pomoc± krzywej Beziera
  * graficzne przegl±danie ³at w formatach diff, unidiff, context i
    zwyk³ym
  * interaktywne wprowadzanie zmian
  * przezroczysto¶æ sieciowa
  * mo¿liwo¶æ ogl±dania wyj¶cia diff w wewnêtrznej przegl±darce
  * ³atwa nawigacja miêdzy wieloplikowymi diffami wraz z dokowalnym drzewem
  * zamiana ¼ród³a i celu za pomoc± pojedynczej komendy
  * statystyki diffów

%package kprofilemethod
Summary:	Kprofilemethod is a set of macros which help profiling using QTime
Summary(pl):	Kprofilemethod to zestaw makr u³atwiaj±cych profilowanie z wykorzystaniem QTime
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description kprofilemethod
Kprofilemethod is a set of macros which help profiling using QTime.

%description kprofilemethod -l pl
Kprofilemethod to zestaw makr u³atwiaj±cych profilowanie z
wykorzystaniem QTime.

%package kspy
Summary:	A utility for egzamining the internal state of a QT/KDE application.
Summary(pl):	Narzêdzie do badania stanu aplikacji QT/KDE
Group:		X11/Development/Tools
Obsoletes:	kdiff
Obsoletes:	kdiff2
Obsoletes:	%{name}-devel

%description kspy
KSpy is a utility intended to help developers examine the internal
state of a Qt/KDE application. KSpy graphically displays all the
QObjects in use, and allows you to browse their properties. Using KSpy
is very simple, include kspy.h and call KSpy::invoke() when you want
to looks inside your app. The KSpy function is inline and the main
part of KSpy is dynamically loaded, so you may even want to leave this
in the release build of an application.

%description kspy -l pl
KSpy to narzêdzie maj±ce u³atwiæ programistom badanie wewnêtrznego
stanu aplikacji QT/KDE. KSpy ilustruje graficznie wszystkie QObjects
jakie s± w u¿yciu i pozwala na ³atwe przegl±danie ich w³a¶ciwo¶ci.
Korzystanie z KSpy jest bardzo proste (wystarczy do³±czyæ plik kspy.h
i wywo³aæ KSpy::invoke() w miejscu, które chcemy obejrzeæ w naszej
aplikacji. Funkcja KSpy jest inline, wiêc mo¿na zostawiæ j± nawet w
wydaniu stabilnym.

%package kstartperf
Summary:	A tool to measure startup time for KDE applications
Summary(pl):	Narzêdzie s³u¿±ce do pomiaru czasu ³adowania aplikacji KDE
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description kstartperf
kstartperf measures startup time for KDE applications.

%description kstartperf -l pl
Narzêdzie s³u¿±ce do pomiaru czasu ³adowania aplikacji KDE.

%package pallette-gimp
Summary:	Adds the KDE Default pallette to GIMP
Summary(pl):	Dodaje domy¶ln± paletê kolorów KDE do GIMP-a
Group:		X11/Applications/Graphics
Requires:	gimp
Obsoletes:	%{name}-devel

%description pallette-gimp
Adds the KDE Default pallette to GIMP.

%description pallette-gimp -l pl
Dodaje domy¶ln± paletê kolorów KDE do GIMP-a.

%package pallette-xpaint
Summary:	Adds the KDE Default pallette to XPaint
Summary(pl):	Dodaje domy¶ln± paletê kolorów KDE do XPainta
Group:		X11/Applications/Graphics
Requires:	xpaint
Obsoletes:	%{name}-devel

%description pallette-xpaint
Adds the KDE Default pallette to XPaint.

%description pallette-xpaint -l pl
Dodaje domy¶ln± paletê kolorów KDE do XPainta.

%package po2xml
Summary:	An xml2po and vice versa converters
Summary(pl):	Konwertery po2xml i vice versa
Group:		X11/Development/Tools
Requires:	/usr/bin/python
Obsoletes:	%{name}-devel

%description po2xml
An xml2po and vice versa converters.

%description po2xml -l pl
Konwertery po2xml i vice versa.

%package scripts-build
Summary:	A set of scripts useful for building KDE
Summary(pl):	Zestaw skryptów do kompilowania KDE
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	%{name}-devel

%description scripts-build
A set of scripts useful for building KDE.

%description scripts-build -l pl
Zestaw skryptów do kompilowania KDE.

%package scripts-cxxmetric
Summary:	Statistic meter for c/c++ files
Summary(pl):	Plik do tworzenia statystyki plików c/c++
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	%{name}-devel

%description scripts-cxxmetric
Counts lines of code, comments and blank space in C and C++ source
files.

%description scripts-cxxmetric -l pl
Zlicza linijki kodu, komentarzy i znaków bia³ych w plikach ¼ród³owych
C i C++.

%package scripts-cvs
Summary:	A set of scripts for maintaining KDE from CVS
Summary(pl):	Zestaw skryptów do zarz±dzania KDE z CVS
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	%{name}-devel

%description scripts-cvs
A set of scripts for maintaining KDE from CVS.

%description scripts-cvs -l pl
Zestaw skryptów do zarz±dzania KDE z CVS.

%package scripts-doc
Summary:	A set of scripts for quick access to qt/KDE documentation
Summary(pl):	Zestaw skryptów szybkiego dostêpu do dokumentacji qt/KDE
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description scripts-doc
A set of scripts for quick access to qt/KDE documentation.

%description scripts-doc -l pl
Zestaw skryptów szybkiego dostêpu do dokumentacji qt/KDE.

%package scripts-extractrc
Summary:	Extracts the strings from .rc files
Summary(pl):	Wyci±ga ³añcuchy z plików .rc
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	%{name}-extractrc
Obsoletes:	%{name}-devel

%description scripts-extractrc
A Perl script, it extracts the strings in an application's .rc file,
e.g. testappui.rc, and writes into the pot file where the translations
are build with (po-files).

%description scripts-extractrc -l pl
Skrypt napisany w Perlu, który wyci±ga ³añcuchy z plików .rc
aplikacji, np. testappgui.rc i zapisuje je do plików pot, z których
tworzy siê t³umaczenia (pliki po).

%package scripts-kdekillall
Summary:	A script for killing KDE apps started with kdeinit
Summary(pl):	Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description scripts-kdekillall
A script for killing KDE apps started with kdeinit.

%description scripts-kdekillall -l pl
Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit.

%package scripts-kdelnk2desktop
Summary:	A kdelnk to desktop converter
Summary(pl):	Konwerter plików kdelnk na desktop
Group:		X11/Development/Tools
Obsoletes:	%{name}-devel

%description scripts-kdelnk2desktop
A kdelnk to desktop converter.

%description scripts-kdelnk2desktop -l pl
Konwerter plików kdelnk na desktop.

%package scripts-zonetab2pot
Summary:	A zone.tab to .pot converter
Summary(pl):	Konwerter plików zone.tab na .pot
Group:		X11/Development/Tools
Requires:	/usr/bin/python
Requires:	gettext-devel
Obsoletes:	%{name}-devel

%description scripts-zonetab2pot
This script reads timezone list as its first argument or from
/usr/share/zoneinfo/zone.tab, and converts it to a PO file template.

%description scripts-zonetab2pot -l pl
Ten skrypt wczytuje listê stref czasowych z linii poleceñ lub pliku
/usr/share/zoneinfo/zone.tab i konwertuje je na plik POT.

%package xemacs
Summary:	A set of macros for xemacs
Summary(pl):	Zestaw makr do xemacsa
Group:		X11/Development/Tools
Requires:	xemacs-common
Obsoletes:	%{name}-devel

%description xemacs
A set of macros for xemacs.

%description xemacs -l pl
Zestaw makr do xemacsa.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

for plik in `find ./ -name *.desktop | grep -l '\[nb\]'` ; do
	echo $plik
	echo -e ',s/\[nb\]/[no]/\n,w' | ed $plik
done

%configure \
	--enable-final \
	--enable-nls
%{__make}

%{__make} -C kstartperf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefdir},%{_emacspkgdir}/kde} \
	$RPM_BUILD_ROOT{%{_xemacspkgdir}/kde,%{_zshfcdir},%{_sysconfdir}/bash_completion.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C kstartperf install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf `find . -name CVS`

install ./kdepalettes/KDE_Gimp	$RPM_BUILD_ROOT%{_gimpdir}/palettes/
cp ./kdepalettes/kde_xpaintrc	$RPM_BUILD_ROOT%{_appdefdir}/XPaint.kde
cp ./scripts/kde-emacs/*.*	$RPM_BUILD_ROOT%{_emacspkgdir}/kde
cp ./scripts/kde-emacs/*.*	$RPM_BUILD_ROOT%{_xemacspkgdir}/kde
cp ./scripts/completions/zsh/*	$RPM_BUILD_ROOT%{_zshfcdir}
cp ./scripts/completions/bash/* $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/

cd $RPM_BUILD_ROOT%{_pixmapsdir}
mv {locolor,crystalsvg}/32x32/apps/kbugbuster.png
mv {locolor,crystalsvg}/32x32/apps/kompare.png
cd -

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang	cervisia	--with-kde
%find_lang	kbabel		--with-kde
%find_lang	kbugbuster	--with-kde
%find_lang	kompare		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%{_libdir}/kde3/kfile_[!p]*.la
%attr(755,root,root) %{_libdir}/kde3/kfile_[!p]*.so
%{_datadir}/mimelnk
%{_datadir}/services/kfile_c*
%{_datadir}/services/kfile_d*
%{_datadir}/services/kfile_h*
%{_pixmapsdir}/[!l]*/*/*/*gettext*.png

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/lib*.a

%files cervisia -f cervisia.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cervisia
%{_libdir}/libcervisia.la
%attr(755,root,root) %{_libdir}/libcervisia.so*
%{_mandir}/man1/cervisia*
%{_datadir}/apps/cervisia*
%{_applnkdir}/Development/cervisia.desktop
%{_pixmapsdir}/*/*/*/cervisia.png

%files completions-bash
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d

%files completions-zsh
%defattr(644,root,root,755)
%{_zshfcdir}/*

%files emacs
%defattr(644,root,root,755)
%{_emacspkgdir}/kde

%files kapptemplate
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kapptemplate
%dir %{_datadir}/apps/kapptemplate
%{_datadir}/apps/kapptemplate/[!b]*
%dir %{_datadir}/apps/kapptemplate/bin
%attr(755,root,root) %{_datadir}/apps/kapptemplate/bin/*

%files kaddressbook-kdeaccounts
%defattr(644,root,root,755)
%{_libdir}/kde3/kabcformat_kdeaccounts.la
%attr(755,root,root) %{_libdir}/kde3/kabcformat_kdeaccounts.so
%{_datadir}/apps/kabc/formats/*

%files kbabel -f kbabel.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbabel
%{_libdir}/libkbabelcommon.la
%attr(755,root,root) %{_libdir}/libkbabelcommon.so*
%{_libdir}/libkbabel.la
%attr(755,root,root) %{_libdir}/libkbabel.so*
%{_libdir}/kde3/kfile_po.la
%attr(755,root,root) %{_libdir}/kde3/kfile_po.so
%{_libdir}/kde3/pothumbnail.la
%attr(755,root,root) %{_libdir}/kde3/pothumbnail.so
%{_datadir}/apps/kbabel
%{_datadir}/services/*po*
%{_applnkdir}/Development/kbabel.desktop
%{_pixmapsdir}/[!l]*/*/*/kbabel.png

%files kbabel-catalog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/catalogmanager
%{_libdir}/libcatalogmanager.la
%attr(755,root,root) %{_libdir}/libcatalogmanager.so*
%{_libdir}/kde3/libpoauxiliary.la
%attr(755,root,root) %{_libdir}/kde3/libpoauxiliary.so
%{_libdir}/kde3/libpocompendium.la
%attr(755,root,root) %{_libdir}/kde3/libpocompendium.so
%{_datadir}/apps/catalogmanager
%{_applnkdir}/Development/catalogmanager.desktop
%{_pixmapsdir}/[!l]*/*/*/catalogmanager.png

%files kbabel-dictionary
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbabeldict
#%{_libdir}/kde3/libdbsearchengine.la
#%attr(755,root,root) %{_libdir}/kde3/libdbsearchengine.so
%{_libdir}/libkbabeldict*.la
%attr(755,root,root) %{_libdir}/libkbabeldict*.so*
%{_applnkdir}/Development/kbabeldict.desktop
%{_datadir}/apps/kbabeldict
%{_pixmapsdir}/[!l]*/*/*/kbabeldict.png

%files kbabel-devel
%defattr(644,root,root,755)
%{_includedir}/kbabel

%files kbugbuster -f kbugbuster.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbugbuster
%{_datadir}/apps/kbugbuster
%{_applnkdir}/Development/kbugbuster.desktop
%{_pixmapsdir}/[!l]*/*/*/kbugbuster.png

#%files kmtrace
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kmtrace
#%attr(755,root,root) %{_bindir}/kminspector
#%attr(755,root,root) %{_bindir}/demangle
#%attr(755,root,root) %{_bindir}/match
#%{_libdir}/libktrace*.la
#%attr(755,root,root) %{_libdir}/libktrace*.so*
#%{_includedir}/ktrace.h
#%{_datadir}/apps/kmtrace

%files kompare -f kompare.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kompare
%{_libdir}/kde3/libkompare*.la
%attr(755,root,root) %{_libdir}/kde3/libkompare*.so
%{_datadir}/apps/kompare*
%{_datadir}/service*/kompare*
%{_applnkdir}/Development/kompare.desktop
%{_pixmapsdir}/[!l]*/*/*/kompare.png

%files kprofilemethod
%defattr(644,root,root,755)
%{_includedir}/kprofilemethod.h

%files kspy
%defattr(644,root,root,755)
%{_libdir}/libkspy.la
%attr(755,root,root) %{_libdir}/libkspy.so*
%{_includedir}/kspy.h

%files kstartperf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kstartperf
%{_libdir}/libkstartperf.la
%attr(755,root,root) %{_libdir}/libkstartperf.so*

%files pallette-gimp
%defattr(644,root,root,755)
%{_gimpdir}/palettes

%files pallette-xpaint
%defattr(644,root,root,755)
%{_appdefdir}

%files po2xml
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fixsgml
%attr(755,root,root) %{_bindir}/po2xml
%attr(755,root,root) %{_bindir}/split2po
%attr(755,root,root) %{_bindir}/swappo
%attr(755,root,root) %{_bindir}/transxx
%attr(755,root,root) %{_bindir}/xml2pot

%files scripts-build
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/adddebug
%attr(755,root,root) %{_bindir}/create*
%attr(755,root,root) %{_bindir}/extend*
%attr(755,root,root) %{_bindir}/makeobj
%attr(755,root,root) %{_bindir}/licensecheck
%attr(755,root,root) %{_bindir}/includemocs
%attr(755,root,root) %{_bindir}/fixincludes
%attr(755,root,root) %{_bindir}/kde-build
%attr(755,root,root) %{_bindir}/cheatmake
%{_mandir}/man1/kde-build*

%files scripts-cvs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cvs*
%attr(755,root,root) %{_bindir}/noncvslist
%attr(755,root,root) %{_bindir}/pruneemptydirs
%{_mandir}/man1/*cvs*

%files scripts-doc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtdoc
%attr(755,root,root) %{_bindir}/kdedoc

%files scripts-extractrc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/extractrc

%files scripts-cxxmetric
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cxxmetric

%files scripts-kdekillall
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdekillall

%files scripts-kdelnk2desktop
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdelnk2desktop.py

%files scripts-zonetab2pot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zonetab2pot.py

%files xemacs
%defattr(644,root,root,755)
%{_xemacspkgdir}/kde
