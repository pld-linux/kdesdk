# TODO:
#   * grouping scripts from scripts/ subdir
#   * installing emacs and shell advancements

%define         _state          unstable
%define         _kdever         kde-3.1-rc5

Summary:	KDESDK - Software Development Kit for KDE
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	3.1
Release:	1
Epoch:		2
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# translations are  generated from kde-i18n.spec now
# Source1:	kde-i18n-%{name}-%{version}.tar.bz2
#Patch0:		%{name}-kbabel_am.patch
BuildRequires:	bison
BuildRequires:	db2-devel
BuildRequires:	db4-devel
BuildRequires:	gettext-devel
BuildRequires:	kdebase-devel = %{version}
# required by kbabel:
#Requires:	gettext-devel
# kmtrace need /usr/lib/libiberty.a (path hardcoded into configure).
#Requires:	kdelibs = %{version}
#Requires:	%{name}-extractrc = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML
%define		_mandir		%{_prefix}/man

%description
Software Development Kit for KDE.

%description -l pl
Pakiet wspomagaj±cy programowanie w ¶rodowisku KDE.

%package devel
Summary:	Header files for kdesdk
Summary(pl):	Pliki nag³ówkowe dla kdesdk
Group:		X11/Development/Libraries

%description devel
Header files for kdesdk.

%description devel -l pl
Pliki nag³ówkowe dla kdesdk.

%package static
Summary:	Static libraries for kdesdk
Summary(pl):	Statyczne biblioteki dla kdesdk
Group:		X11/Development/Tools

%description static
Static libraries for kdesdk.

%description static -l pl
Statyczne biblioteki dla kdesdk.

%package cervisia
Summary:        A KDE cvs frontend.
Summary(pl):    Frontend CVS pod KDE.
Group:            X11/Development/Tools
Requires:	cvs >= 1.10

%description cervisia
A KDE cvs frontend.

%description cervisia -l pl
Frontend CVS pod KDE.

%package completions-bash
Summary:        Autocomplete definitions for bash.
Summary(pl):    Definicje autouzupe³niania dla basha.
Group:		Applications/Shells
Requires:	bash-completion

%description completions-bash
Autocomplete definitions for bash.

%description completions-bash -l pl
Definicje autouzupe³niania dla basha.

%package completions-zsh
Summary:        Autocomplete definitions for zsh.
Summary(pl):    Definicje autouzupe³niania dla zsh.
Group:          Applications/Shells
Requires:       zsh >= 4.0.6-2

%description completions-zsh
Autocomplete definitions for zsh.

%description completions-zsh -l pl
Definicje autouzupe³niania dla zsh.

%package emacs
Summary:	A set of macros for emacs
Summary(pl):	Zestaw makr do emacs.
Group:		X11/Development/Tools
Requires: 	emacs

%description emacs
A set of macros for emacs

%description emacs -l pl
Zestaw makr do emacs.

%package kaddressbook-kdeaccounts
Summary:        A kdeaccounts plugin for the KDE adressbook
Summary(pl):    Plugin do ksi±¿ki adresowej KDE dodaj±cy obs³ugê kdeaccounts
Group:          X11/Applications
Requires:	kdepim-kaddressbook >= 3.0.8

%description kaddressbook-kdeaccounts
A kdeaccounts plugin for the KDE adressbook. What is does is adding the people from kde's cvs accounts file
to the addressbook.

%description kaddressbook-kdeaccounts -l pl
Plugin do ksi±¿ki adresowej KDE dodaj±cy obs³ugê kdeaccounts. Dodaje on osoby posiadaj±ce konta w cvs kde do 
ksi±zki adresowej.

%package kapptemplate
Summary:        KDE application framework generator
Summary(pl):    Generator szkieletu do aplikacji KDE
Group:          X11/Development/Tools

%description kapptemplate
Modular shell script that will automatically create a
framework for either a normal KDE 3.x application, a
KPart application, a KPart plugin, or convert an
existing application.

%description kapptemplate -l pl
Modularny skrypt, któr potrafi automagicznie wygenerowaæ 
szkielet katalogów dla zwyk³ej aplikacji pod KDE 3.x, aplikacji
KPart lub skonwertowaæ istniej±c± aplikacji.

%package kbabel
Summary:        An advanced and easy to use PO-file editor
Summary(pl):    Rozbudowany i ³atwy w obs³udze edytor plików PO
Group:          X11/Development/Tools
Requires:	gettext-devel

%description kbabel
KBabel is a tool, that allows easy management, edition and upkeep of 
gettext .po files.

%description kbabel -l pl
KBabel jest narzêdziem, które pozwala na ³atwe zarz±dzanie, edycjê i 
utrzymanie plików po.

%package kbabel-devel
Summary:        Kbabel headers.
Summary(pl):    Pliki nag³owkowe KBabel.
Group:          X11/Development
Requires:       gettext-devel
Requires:	%{name}-kbabel = %{version} 
Requires:       %{name}-kbabel-catalog = %{version}
Requires:       %{name}-kbabel-dictionary = %{version}

%description kbabel-devel
KBabel headers.

%description kbabel-devel -l pl
Pliki nag³owkowe KBabel.

%package kbabel-dictionary
Summary:        Plugin that supports dictionaries made from po compendia.
Summary(pl):    Plugin kbabel obs³uguj±cy s³owniki z kompendiów po.
Group:          X11/Development
Requires:       gettext-devel
Requires:	%{name}-kbabel = %{version}

%description kbabel-dictionary
Plugin that supports dictionaries made from po compendia.

%description kbabel-dictionary -l pl
Plugin kbabel obs³uguj±cy s³owniki z kompendiów po.

%package kbabel-catalog
Summary:        A KBabel catalog manager.
Summary(pl):    Mened¿er zbiorów plików po zintegrowany z KBabel.
Group:          X11/Development
Requires:       gettext-devel
Requires:	%{name}-kbabel = %{version}

%description kbabel-catalog
A KBabel catalog manager.

%description kbabel-catalog -l pl
Mened¿er zbiorów plików po zintegrowany z KBabel.

%package kbugbuster
Summary:        A tools that allows cooperation with bugs.kde.org
Summary(pl):    Narzêdzie wspó³pracuj±ce z bugs.kde.org
Group:          X11/Development/Tools

%description kbugbuster
KBugBuster allows easy bug management on bugs.kde.org

%description kbugbuster -l pl
KBugBuster u³atwia wyszukwianie i zarz±dzanie b³êdami na bugs.kde.org

%package kmtrace
Summary:        An mtrace to full backtrace conversion tool
Summary(pl):    Narzêdzie do konwersji z mtrace do pe³nego backtrace'a
Group:          X11/Development/Tools
BuildRequires:  binutils-static

%description kmtrace
Converts glibc's mtrace log into a full backtrace.

%description kmtrace -l pl 
Konwertuje mtrace glibca do pe³nego backtrace'a.

%package kompare
Summary:	Kompare is a program to view the differences between files.
Summary(pl):	Kompare to program s³u¿±cy do porównywania zmian miêdzy plikami.
Group:		X11/Development/Tools

%description kompare
Kompare is a program to view the differences between files. Features include:

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
Kompare to program s³u¿±cy do porównywania zmian miêdzy plikami. Aktualnie dostêpne funkcje:
  * porównanie plików lub katalogów poprzez graficzny interfejs
  * przedstawienie ¼ród³a i celu za pomoc± krzywej beziera
  * graficzne przegl±danie paczy w formatach diff, unidiff, context i zwyk³ym
  * interaktywne wprowadzanie zmian
  * prze¼roczysto¶æ sieciowa
  * mo¿liwo¶æ ogl±dania wyj¶cia diff w wewnêtrznej przegl±darce
  * ³atwa nawigacja miêdzy wieloplikowymi diffami wraz z dokowalnym drzewem
  * zamiana ¼rod³a i celu za pomoc± pojedyñczej komendy
  * statystyki diffów

%package kprofilemethod
Summary:	Kprofilemethod is a set of macros which help profiling using QTime.
Summary(pl):	Kprofilemethod to zestaw makr u³atwiaj±cych profilowanie z wykorzystaniem QTime.
Group:		X11/Development/Tools

%description kprofilemethod
Kprofilemethod is a set of macros which help profiling using QTime.

%description kprofilemethod -l pl
Kprofilemethod to zestaw makr u³atwiaj±cych profilowanie z wykorzystaniem QTime.

%package kspy 
Summary:        A utility for egzamining the internal state of a QT/KDE application.
Summary(pl):    Narzêdzie do badania stanu aplikacji QT/KDE
Group:          X11/Development/Tools
Obsoletes:	kdiff
Obsoletes:	kdiff2

%description kspy
KSpy is a utility intended to help developers examine the internal
state of a Qt/KDE application. KSpy graphically displays all the
QObjects in use, and allows you to browse their properties. Using KSpy
is very simple, include kspy.h and call KSpy::invoke() when you want
to looks inside your app. The KSpy function is inline and the main
part of KSpy is dynamically loaded, so you may even want to leave this
in the release build of an application.

%description kspy -l pl
KSpy to nar¿edzie maj±ce u³atwiæ programisto badanie wewnêtrznego stanu aplikacji
QT/KDE. KSpy ilustruje graficznie wszystkie Qobjects jakie s± w u¿yciu i pozwala
na ³atwe przegl±danie ich w³a¶ciwo¶ci. Korzystanie z KSpy jest bardzo proste (wystarczy
do³±czyæ plik kspy.h i wywo³aæ KSpy::invoke() w miejscu, któ?e chcemy obejrzeæ w naszej 
aplikacji. Funkcja KSpy jest inline, wiêc mo¿esz nawet zostawiæ j± nawet w wydaniu stabilnym.

%package kstartperf
Summary:	A tool to measure startup time for KDE applications.
Summary(pl):	Narzêdzie s³u¿±ce do pomiaru czasu ³adowania aplikacji KDE.
Group:          X11/Development/Tools

%description kstartperf
kstartperf measures startup time for KDE applications.

%description kstartperf -l pl
Narzêdzie s³u¿±ce do pomiaru czasu ³adowania aplikacji KDE.

%package pallette-gimp
Summary:        Adds the KDE Default pallette to GIMP
Summary(pl):    Dodaje domy¶ln± paletê kolorów KDE do GIMPa
Group:          X11/Applications/Graphics
Requires:	gimp >= 1.2

%description pallette-gimp
Adds the KDE Default pallette to GIMP

%description pallette-gimp -l pl
Dodaje domy¶ln± paletê kolorów KDE do GIMPa

%package pallette-xpaint
Summary:        Adds the KDE Default pallette to XPaint
Summary(pl):    Dodaje domy¶ln± paletê kolorów KDE do Xpainta
Group:          X11/Applications/Graphics
Requires:       xpaint

%description pallette-xpaint
Adds the KDE Default pallette to XPaint

%description pallette-xpaint -l pl
Dodaje domy¶ln± paletê kolorów KDE do XPainta

%package po2xml
Summary:	An xml2po and vice versa converters.
Summary(pl):	Konwertery po2xml i vice versa.
Group:          X11/Development/Tools
Requires:	/usr/bin/python

%description po2xml
An xml2po and vice versa converters.

%description po2xml -l pl
Konwertery po2xml i vice versa.

%package scripts-build
Summary:        An set of scripts useful for building kde.
Summary(pl):    Zestaw skryptów do kompilowania kde.
Group:          X11/Development/Tools
Requires:	/usr/bin/perl

%description scripts-build
A set of scripts useful for building kde.

%description scripts-build -l pl
Zestaw skryptów do kompilowania kde.

%package scripts-cxxmetric
Summary:	Statistic meter for c/c++ files.
Summary(pl):	Plik do tworzenia statystyki plików c/c++.
Group:		X11/Development/Tools
Requires:	/usr/bin/perl

%description scripts-cxxmetric
Counts lines of code, comments and blank space in C and C++ source files.

%description scripts-cxxmetric -l pl
Zlicza linijki kodu, komentarzy i znaków bia³ych w plikach ¼ród³owych C i C++.

%package scripts-cvs
Summary:        A set of scripts for mainatining kde from cvs.
Summary(pl):    Zestaw skryptów do zarz±dzania kde z cvs.
Group:          X11/Development/Tools
Requires:	/usr/bin/perl

%description scripts-cvs 
A set of scripts for mainatining kde from cvs.

%description scripts-cvs -l pl
Zestaw skryptów do zarz±dzania kde z cvs.

%package scripts-doc
Summary:        A set of scripts forquick access to qt/kde documentation.
Summary(pl):    Zestaw skryptów szybkiego dostêpu do dokumentacji qt/kde.
Group:          X11/Development/Tools

%description scripts-doc
A set of scripts forquick access to qt/kde documentation.

%description scripts-doc -l pl
Zestaw skryptów szybkiego dostêpu do dokumentacji qt/kde.

%package scripts-extractrc
Summary:	Extracts the strings from .rc files
Summary(pl):	Odnajduje stringi w plikach .rc
Group:		X11/Development/Tools
Requires:	/usr/bin/perl
Obsoletes:	kdesdk-extractrc

%description scripts-extractrc
A Perl script, it extracts the strings in an application´s .rc file,
e.g. testappui.rc, and writes into the pot file where the translations
are build with (po-files)

%description scripts-extractrc -l pl
Skrypt napisany w Perlu, który odnajduje stringi w plikach .rc aplikacji,
np. testappgui.rc i zapisuje je do plików pot

%package scripts-kdekillall
Summary:        A script for killing KDE appsstarted with kdeinit.
Summary(pl):   Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit.
Group:          X11/Development/Tools

%description scripts-kdekillall
A script for killing KDE appsstarted with kdeinit.

%description scripts-kdekillall -l pl
Skrypt do unicestwiania aplikacji KDE uruchomionych przez kdeinit.

%package scripts-kdelnk2desktop
Summary:        A kdelnk to desktop converter.
Summary(pl):   Konwerter plików kdelnk na desktop.
Group:          X11/Development/Tools

%description scripts-kdelnk2desktop
A kdelnk to desktop converter.

%description scripts-kdelnk2desktop -l pl
Konwerter plików kdelnk na desktop.

%package scripts-zonetab2pot
Summary:        A zone.tab to .pot converter.
Summary(pl):    Konwerter plików zone.tab na .pot
Group:          X11/Development/Tools
Requires:	/usr/bin/python
Requires:	gettext-devel

%description scripts-zonetab2pot
This script reads timezone list as its first argument
or from /usr/share/zoneinfo/zone.tab, and converts it
to a PO file template.

%description scripts-zonetab2pot -l pl
Ten skrypt wczytuje listê stref czasowych z linii 
poleceñ lub pliku /usr/share/zoneinfo/zone.tab i konwertuje je
na plik POT.

%package xemacs
Summary:	A set of macros for xemacs
Summary(pl):	Zestaw makr do xemacs.
Group:		X11/Development/Tools
Requires: 	xemacs

%description xemacs
A set of macros for xemacs

%description xemacs -l pl
Zestaw makr do xemacs.


%prep
%setup -q
#%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        CPPFLAGS="`pkg-config libpng12 --cflags`"
fi

%configure \
	--enable-nls \
	--with-db-name=db4 \
	--enable-final

%{__make}

cd kstartperf
%{__make}
cd ../kbugbuster
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

cd kstartperf
%{__make} install DESTDIR="$RPM_BUILD_ROOT"
cd ..
cd kbugbuster
%{__make} install DESTDIR="$RPM_BUILD_ROOT"
cd ..
rm -rf `find . -name CVS`

install -d $RPM_BUILD_ROOT/%{_libdir}/X11/
install -d $RPM_BUILD_ROOT/%{_libdir}/X11/app-defaults
install -d $RPM_BUILD_ROOT/%{_usr}/share/emacs-packages/
install -d $RPM_BUILD_ROOT/%{_usr}/share/zsh/
install -d $RPM_BUILD_ROOT/%{_usr}/share/zsh/latest
install -d $RPM_BUILD_ROOT/%{_usr}/share/zsh/latest/functions
install -d $RPM_BUILD_ROOT/%{_usr}/share/emacs-packages/kde
install -d $RPM_BUILD_ROOT/%{_usr}/share/xemacs-packages/
install -d $RPM_BUILD_ROOT/%{_usr}/share/xemacs-packages/kde
install -d $RPM_BUILD_ROOT/%{_datadir}/gimp
install -d $RPM_BUILD_ROOT/%{_datadir}/gimp/1.2
install -d $RPM_BUILD_ROOT/%{_datadir}/gimp/1.2/palettes
install -d $RPM_BUILD_ROOT/%{_sysconfdir}
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d



install ./kdepalettes/KDE_Gimp	$RPM_BUILD_ROOT/%{_datadir}/gimp/1.2/palettes/
cp ./kdepalettes/kde_xpaintrc	$RPM_BUILD_ROOT/%{_libdir}/X11/app-defaults/XPaint.kde
cp ./scripts/kde-emacs/*.*	$RPM_BUILD_ROOT/%{_usr}/share/emacs-packages/kde
cp ./scripts/kde-emacs/*.*	$RPM_BUILD_ROOT/%{_usr}/share/xemacs-packages/kde
cp ./scripts/completions/bash/* $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/
cp ./scripts/completions/zsh/*	$RPM_BUILD_ROOT/%{_usr}/share/zsh/latest/functions

%find_lang	cervisia	--with-kde
%find_lang	kbabel		--with-kde
%find_lang	kbugbuster	--with-kde
%find_lang	kompare		--with-kde

%clean
%{!?_without_clean:rm -rf $RPM_BUILD_ROOT}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files 
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/kde3/kfile_c*
%attr(755,root,root) %{_libdir}/kde3/kfile_d*
%{_datadir}/mimelnk
%{_datadir}/services/kfile_c*
%{_datadir}/services/kfile_d*
%{_datadir}/services/kfile_h*
%{_pixmapsdir}/*/*/*/*gettext*.png

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files cervisia -f cervisia.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cervisia
%attr(755,root,root) %{_libdir}/libcervisia*
%{_mandir}/man1/cervisia*
%{_datadir}/apps/cervisia*
%{_pixmapsdir}/*/*/*/cervisia.png
%{_applnkdir}/Development/cervisia.desktop

%files completions-bash
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d

%files completions-zsh
%defattr(644,root,root,755)
%{_usr}/share/zsh/latest/functions

%files emacs
%defattr(644,root,root,755)
%{_usr}/share/emacs-packages/kde

%files kapptemplate
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kapptemplate
%dir %{_datadir}/apps/kapptemplate
%{_datadir}/apps/kapptemplate/[!b]*
%dir %{_datadir}/apps/kapptemplate/bin
%attr(755,root,root) %{_datadir}/apps/kapptemplate/bin/*

%files kaddressbook-kdeaccounts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kabc*
%{_datadir}/apps/kabc/formats/*

%files kbabel -f kbabel.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbabel
%attr(755,root,root) %{_libdir}/libkbabelcommon*
%attr(755,root,root) %{_libdir}/libkbabel.*
%attr(755,root,root) %{_libdir}/kde3/kfile_po.*
%attr(755,root,root) %{_libdir}/kde3/pothumbnail*
%{_datadir}/apps/kbabel
%{_datadir}/services/*po*
%{_pixmapsdir}/*/*/*/kbabel.png
%{_applnkdir}/Development/kbabel.desktop

%files kbabel-catalog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/catalogmanager
%attr(755,root,root) %{_libdir}/libcatalog*
%attr(755,root,root) %{_libdir}/kde3/libpoaux*
%attr(755,root,root) %{_libdir}/kde3/libpocomp*
%attr(755,root,root) %{_libdir}/kde3/libdbsearchengine.*
%{_datadir}/apps/catalogmanager
%{_pixmapsdir}/*/*/*/catalogmanager.png
%{_applnkdir}/Development/catalogmanager.desktop

%files kbabel-dictionary
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbabeldict
%attr(755,root,root) %{_libdir}/libkbabeldict*
%{_applnkdir}/Development/kbabeldict.desktop
%{_datadir}/apps/kbabeldict
%{_pixmapsdir}/*/*/*/kbabeldict.png

%files kbabel-devel
%defattr(644,root,root,755)
%{_includedir}/kbabel

%files kbugbuster -f kbugbuster.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbugbuster
%{_datadir}/apps/kbugbuster
%{_pixmapsdir}/*/*/*/kbugbuster.png
%{_applnkdir}/Development/kbugbuster.desktop

%files kmtrace
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmtrace
%attr(755,root,root) %{_bindir}/kminspector
%attr(755,root,root) %{_bindir}/demangle
%attr(755,root,root) %{_bindir}/match
%attr(755,root,root) %{_libdir}/libktrace*.so*
%attr(755,root,root) %{_libdir}/libktrace*.la
%{_includedir}/ktrace.h
%{_datadir}/apps/kmtrace

%files kompare -f kompare.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kompare
%attr(755,root,root) %{_libdir}/kde3/libkompare*
%attr(755,root,root) %{_libdir}/libdiff*
%{_datadir}/apps/kompare*
%{_datadir}/service*/kompare*
%{_pixmapsdir}/*/*/*/kompare.png
%{_applnkdir}/Development/kompare.desktop

%files kprofilemethod
%defattr(644,root,root,755)
%{_includedir}/kprofilemethod.h

%files kspy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkspy*
%{_includedir}/kspy.h

%files kstartperf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kstartperf
%attr(755,root,root) %{_libdir}/libkstartperf*

%files pallette-gimp
%defattr(644,root,root,755)
%{_datadir}/gimp/1.2/palettes

%files pallette-xpaint
%defattr(644,root,root,755)
%{_libdir}/X11/app-defaults

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
%{_usr}/share/xemacs-packages/kde
