Summary:	Open Source clone of Microcal Origin, data analysis and visualisation tool
Summary(pl):	Klon Open Source programu Microcal Origin, narzêdzia do analizy i wizualizacji danych
Name:		scigraphica
Version:	0.8.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/scigraphica/%{name}-%{version}.tar.gz
# Source0-md5:	8527c80fe75bc4f72c14548c7a2b0b71
Source1:	%{name}.desktop
#Source2:	zterm.desktop
Patch0:		%{name}-ac_am.patch
Patch1:		%{name}-sgso.patch
URL:		http://scigraphica.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel >= 0.18
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.1.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gtk+extra-devel >= 0.99.17
BuildRequires:	imlib-devel >= 1.9.7
BuildRequires:	libxml-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel >= 4.0
BuildRequires:	python
BuildRequires:	python-Numeric-devel
BuildRequires:	python-devel
Requires:	python-sg = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open Source clone of Microcal Origin, data analysis and visualisation
tool.

%description -l pl
Klon Open Source programu Microcal Origin, narzêdzia do analizy i
wizualizacji danych.

%package examples
Summary:	Examples of SciGraphica's possibilities
Summary(pl):	Przyk³ady pokazuj±ce mo¿liwo¶ci programu SciGraphica
Group:		X11/Applications/Science
Requires:	%{name} = %{version}-%{release}

%description examples
Examples of SciGraphica's possibilities.

%description examples -l pl
Przyk³ady pokazuj±ce mo¿liwo¶ci programu SciGraphica.

%package -n python-sg
Summary:	Python interface to SciGraphica routines
Summary(pl):	Interfejs python do procedur SciGraphica
Group:		Development/Languages/Python
Requires:	python
Requires:	python-pygtk-gtk

%description -n python-sg
Python interface to SciGraphica routines.

%description -n python-sg -l pl
Interfejs python do procedur SciGraphica.

#%package -n zterm
#Summary:	Pretty light-weight "yet another virtual terminal" program
#Summary(pl):	Kolejny wirtualny terminal, tym razem ca³kiem niewielki
#Group:		X11/Applications
#
#%description -n zterm
#Pretty light-weight "yet another virtual terminal" program
#
#%description -n zterm -l pl
#Kolejny wirtualny terminal, tym razem ca³kiem niewielki

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I /usr/share/aclocal/gnome
%{__autoconf}
%{__automake}

%configure \
	--with-bonobo \
	--with-python-script-prefix=%{py_sitedir}/sg
%{__make}
# build sg.so in src/python
%{__make} -C src python/sg.so

%install

rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir},%{_desktopdir},%{py_sitedir}/sg}
mv -f $RPM_BUILD_ROOT%{_datadir}/scigraphica/examples \
	$RPM_BUILD_ROOT%{_examplesdir}/scigraphica
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install src/python/sg.so $RPM_BUILD_ROOT%{py_sitedir}/sg/sg.so

install zvt/zterm $RPM_BUILD_ROOT%{_bindir}
#install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/zterm.desktop

echo "sg" > $RPM_BUILD_ROOT%{py_sitedir}/sg.pth

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.html docs/TODO
%attr(755,root,root) %{_bindir}/scigraphica
%{_datadir}/gnome/help/scigraphica
%{_pixmapsdir}/*
%{_desktopdir}/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/scigraphica

%files -n python-sg
%defattr(644,root,root,755)
%dir %{py_sitedir}/sg
%attr(755,root,root) %{py_sitedir}/sg/*.so
%{py_sitedir}/sg/*.py
%{py_sitedir}/*.pth

#%files -n zterm
#%defattr(644,root,root,755)
#%doc zvt/README
#%attr(755,root,root) %{_bindir}/zterm
#%{_desktopdir}/zterm.desktop
