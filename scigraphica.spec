%define		_prefix /usr/X11R6
Summary:	Open Source clone of Microcal Origin, data analysis and visualisation tool
Summary(pl):	Klon Open Source programu Microcal Origin, narzêdzia do analizy i wizualizacji danych
Name:		scigraphica
Version:	0.8.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Science
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
#Source2:	zterm.desktop
URL:		http://scigraphica.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel >= 4.0
BuildRequires:	ncurses-devel
BuildRequires:	imlib-devel >= 1.9.7
BuildRequires:	libxml-devel
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gtk+extra-devel >= 0.99.17
BuildRequires:	gnome-libs-devel
BuildRequires:	bonobo-devel >= 0.18
BuildRequires:	gnome-print-devel >= 0.1.0
BuildRequires:	/usr/bin/python
BuildRequires:  python-devel
BuildRequires:	python-numpy-devel
Requires:	python-sg = %{version}
Patch0:		%{name}-ac_am.patch
Patch1:		%{name}-sgso.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%package examples
Summary:	Examples of SciGraphica's possibilities
Summary(pl):	Przyk³ady pokazuj±ce mo¿liwo¶ci programu SciGraphica
Group:		X11/Applications/Science
Requires:	scigraphica

%description examples

%description examples -l pl

%package -n python-sg
Summary:	Python interface to SciGraphica routines
Summary(pl):	Interfejs python do procedur SciGraphica
Group:		Development/Languages/Python
Version:	%{version}
Requires:	python
Requires:	python-pygtk-gtk

%description -n python-sg

%description -n python-sg -l pl

#%package -n zterm
#Summary:	Pretty light-weight "yet another virtual terminal" program
#Summary(pl):	Kolejny wirtualny terminal, tym razem ca³kiem niewielki
#Group:		X11/Applications

#%description -n zterm

#%description -n zterm -l pl

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I /usr/share/aclocal/gnome
%{__autoconf}
%{__automake}

%configure --with-bonobo --with-python-script-prefix=/usr/lib/python2.2/site-packages/sg
%{__make}
# build sg.so in src/python
cd src
%{__make} python/sg.so

%install

rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir},%{_desktopdir},/usr/lib/python2.2/site-packages/sg
mv -f $RPM_BUILD_ROOT%{_datadir}/scigraphica/examples \
	$RPM_BUILD_ROOT%{_examplesdir}/scigraphica
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install src/python/sg.so $RPM_BUILD_ROOT/usr/lib/python2.2/site-packages/sg/sg.so

install zvt/zterm $RPM_BUILD_ROOT%{_bindir}
#install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Terminals/zterm.desktop

echo "sg" > $RPM_BUILD_ROOT/usr/lib/python2.2/site-packages/sg.pth

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/scigraphica
%{_datadir}/gnome/help/scigraphica
%{_pixmapsdir}/*
%{_desktopdir}/*
%doc docs/*.html docs/TODO

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/scigraphica

%files -n python-sg
%defattr(644,root,root,755)
%dir /usr/lib/python2.2/site-packages/sg
%attr(755,root,root) /usr/lib/python2.2/site-packages/sg/*.so
/usr/lib/python2.2/site-packages/sg/*.py
/usr/lib/python2.2/site-packages/*.pth

#%files -n zterm
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/zterm
#%{_applnkdir}/Terminals/zterm.desktop
#%doc zvt/README
