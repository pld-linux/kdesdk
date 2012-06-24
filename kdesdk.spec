# TODO:
#   * grouping scripts from scripts/ subdir
#   * installing emacs and shell advancements

%define         _state          unstable
%define         _kdever         kde-3.1-beta2

Summary:	KDESDK - Software Development Kit for KDE
Summary(pl):	KDESDK - Wsparcie programistyczne dla KDE
Name:		kdesdk
Version:	3.0.8
Release:	1
Epoch:		2
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# translations are  generated from kde-i18n.spec now
# Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-kbabel_am.patch
BuildRequires:	bison
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
Pakiet wspomagaj�cy programowanie w �rodowisku KDE.

%package extractrc
Summary:	extracts the strings from .rc files
Summary(pl):	odnajduje stringi w plikach .rc
Group:		X11/Development/Tools
Requires:	/usr/bin/perl

%description extractrc
A Perl script, it extracts the strings in an application�s .rc file,
e.g. testappui.rc, and writes into the pot file where the translations
are build with (po-files)

%description extractrc -l pl
Skrypt napisany w Perlu, kt�ry odnajduje stringi w plikach .rc aplikacji,
np. testappgui.rc i zapisuje je do plik�w pot

%package devel
Summary:	Header files for kdesdk
Summary(pl):	Pliki nag��wkowe dla kdesdk
Group:		X11/Development/Libraries

%description devel
Header files for kdesdk.

%description devel -l pl
Pliki nag��wkowe dla kdesdk.

%package static
Summary:	Static libraries for kdesdk
Summary(pl):	Statyczne biblioteki dla kdesdk
Group:		X11/Development/Tools

%description static
Static libraries for kdesdk.

%description static -l pl
Statyczne biblioteki dla kdesdk.

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
Modularny skrypt, kt�r potrafi automagicznie wygenerowa� 
szkielet katalog�w dla zwyk�ej aplikacji pod KDE 3.x, aplikacji
KPart lub skonwertowa� istniej�c� aplikacji.

%package kbabel
Summary:        An advanced and easy to use PO-file editor
Summary(pl):    Rozbudowany i �atwy w obs�udze edytor plik�w PO
Group:          X11/Development/Tools
Requires:	gettext-devel

%description kbabel
KBabel is a tool, that allows easy management, edition and upkeep of 
gettext .po files.

%description kbabel -l pl
KBabel jest narz�dziem, kt�re pozwala na �atwe zarz�dzanie, edycj� i 
utrzymanie plik�w po.

%package kbugbuster
Summary:        A tools that allows cooperation with bugs.kde.org
Summary(pl):    Narz�dzie wsp�pracuj�ce z bugs.kde.org
Group:          X11/Development/Tools

%description kbugbuster
KBugBuster allows easy bug management on bugs.kde.org

%description kbugbuster -l pl
KBugBuster u�atwia wyszukwianie i zarz�dzanie b��dami na bugs.kde.org

%package kaddressbook-kdeaccounts
Summary:        A kdeaccounts plugin for the KDE adressbook
Summary(pl):    Plugin do ksi��ki adresowej KDE dodaj�cy obs�ug� kdeaccounts
Group:          X11/Applications
Requires:	kdepim-kaddressbook >= 3.0.8

%description kaddressbook-kdeaccounts
A kdeaccounts plugin for the KDE adressbook. What is does is adding the people from kde's cvs accounts file
to the addressbook.

%description kaddressbook-kdeaccounts -l pl
Plugin do ksi��ki adresowej KDE dodaj�cy obs�ug� kdeaccounts. Dodaje on osoby posiadaj�ce konta w cvs kde do 
ksi�zki adresowej.

%package pallette-gimp
Summary:        Adds the KDE Default pallette to GIMP
Summary(pl):    Dodaje domy�ln� palet� kolor�w KDE do GIMPa
Group:          X11/Applications/Graphics
Requires:	gimp

%description pallette-gimp
Adds the KDE Default pallette to GIMP

%description pallette-gimp -l pl
Dodaje domy�ln� palet� kolor�w KDE do GIMPa

%package pallette-xpaint
Summary:        Adds the KDE Default pallette to XPaint
Summary(pl):    Dodaje domy�ln� palet� kolor�w KDE do Xpainta
Group:          X11/Applications/Graphics
Requires:       xpaint

%description pallette-xpaint
Adds the KDE Default pallette to XPaint

%description pallette-xpaint -l pl
Dodaje domy�ln� palet� kolor�w KDE do XPainta

%package kmtrace
Summary:        An mtrace to full backtrace conversion tool
Summary(pl):    Narz�dzie do konwersji z mtrace do pe�nego backtrace'a
Group:          X11/Development/Tools
BuildRequires:  binutils-static

%description kmtrace
Converts glibc's mtrace log into a full backtrace.

%description kmtrace -l pl 
Konwertuje mtrace glibca do pe�nego backtrace'a.

%package kompare
Summary:	Kompare is a program to view the differences between files.
Summary(pl):	Kompare to program s�u��cy do por�wnywania zmian mi�dzy plikami.
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
Kompare to program s�u��cy do por�wnywania zmian mi�dzy plikami. Aktualnie dost�pne funkcje:
  * por�wnanie plik�w lub katalog�w poprzez graficzny interfejs
  * przedstawienie �r�d�a i celu za pomoc� krzywej beziera
  * graficzne przegl�danie paczy w formatach diff, unidiff, context i zwyk�ym
  * interaktywne wprowadzanie zmian
  * prze�roczysto�� sieciowa
  * mo�liwo�� ogl�dania wyj�cia diff w wewn�trznej przegl�darce
  * �atwa nawigacja mi�dzy wieloplikowymi diffami wraz z dokowalnym drzewem
  * zamiana �rod�a i celu za pomoc� pojedy�czej komendy
  * statystyki diff�w


%package kspy 
Summary:        A utility for egzamining the internal state of a QT/KDE application.
Summary(pl):    Narz�dzie do badania stanu aplikacji QT/KDE
Group:          X11/Development/Tools

%description kspy
KSpy is a utility intended to help developers examine the internal
state of a Qt/KDE application. KSpy graphically displays all the
QObjects in use, and allows you to browse their properties. Using KSpy
is very simple, include kspy.h and call KSpy::invoke() when you want
to looks inside your app. The KSpy function is inline and the main
part of KSpy is dynamically loaded, so you may even want to leave this
in the release build of an application.

%description kspy -l pl
KSpy to nar�edzie maj�ce u�atwi� programisto badanie wewn�trznego stanu aplikacji
QT/KDE. KSpy ilustruje graficznie wszystkie Qobjects jakie s� w u�yciu i pozwala
na �atwe przegl�danie ich w�a�ciwo�ci. Korzystanie z KSpy jest bardzo proste (wystarczy
do��czy� plik kspy.h i wywo�a� KSpy::invoke() w miejscu, kt�?e chcemy obejrze� w naszej 
aplikacji. Funkcja KSpy jest inline, wi�c mo�esz nawet zostawi� j� nawet w wydaniu stabilnym.

%package kstartperf
Summary:	A tool to measure startup time for KDE applications.
Summary(pl):	Narz�dzie s�u��ce do pomiaru czasu �adowania aplikacji KDE.
Group:          X11/Development/Tools

%description kstartperf
kstartperf measures startup time for KDE applications.

%description kstartperf -l pl
Narz�dzie s�u��ce do pomiaru czasu �adowania aplikacji KDE.

%package po2xml
Summary:	An xml2po and vice versa converters.
Summary(pl):	Konwertery po2xml i vice versa.
Group:          X11/Development/Tools

%description po2xml
An xml2po and vice versa converters.

%description po2xml -l pl
Konwertery po2xml i vice versa.

%prep
%setup -q
%patch0 -p1

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
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

cd kstartperf
%{__make} install DESTDIR="$RPM_BUILD_ROOT"
cd ..


%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files 
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/[!e]*
%attr(755,root,root) %{_bindir}/extend_dmalloc
%attr(755,root,root) %{_libdir}/kde3/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/lib*.la
%{_mandir}/*/*
%{_applnkdir}/*/*
%{_datadir}/mimelnk/*/*
%{_datadir}/services/*
%{_datadir}/apps/*
%{_pixmapsdir}/*/*/*

%files extractrc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/extractrc

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/lib*so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files kapptemplate
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kapptemplate
%{_datadir}/apps/kapptemplate
