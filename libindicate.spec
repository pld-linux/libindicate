#
# Conditional build:
%bcond_without	apidocs	# API documentation build
%bcond_without	gtk2	# GTK+ 2.x version
%bcond_without	gtk3	# GTK+ 3.x version
%bcond_without	dotnet	# .NET/Mono bindings
%bcond_without	python	# Python bindings
#
%if %{without gtk2}
# .NET bindings depend on gtk-sharp2 and use GTK+ 2.x variant of libindicate-gtk
%undefine	with_dotnet
%endif
%ifarch x32
%undefine	with_dotnet
%endif
Summary:	Libindicate library
Summary(pl.UTF-8):	Biblioteka libindicate
Name:		libindicate
Version:	12.10.1
Release:	5
License:	LGPL v2+
Group:		Libraries
Source0:	https://launchpad.net/libindicate/12.10/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	aeed68ec8047a3325b4aa4aef38f010a
Patch0:		%{name}-am.patch
Patch1:		%{name}-doc.patch
URL:		https://launchpad.net/libindicate/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.76
%{?with_dotnet:BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.1}
BuildRequires:	gdk-pixbuf2-devel >= 2.12
BuildRequires:	glibc-misc
BuildRequires:	glib2-devel >= 1:2.18
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel >= 0.6.7
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	gtk-doc-automake >= 1.4
BuildRequires:	libdbusmenu-devel >= 0.3.97
BuildRequires:	libtool
BuildRequires:	libxml2-devel
%{?with_dotnet:BuildRequires:	mono-csharp >= 1.0}
%{?with_dotnet:BuildRequires:	mono-devel >= 1.0}
BuildRequires:	pkgconfig
%if %{with python}
BuildRequires:	python-devel >= 2.3.5
BuildRequires:	python-pygobject-devel >= 0.22
BuildRequires:	python-pygtk-devel >= 2:2.14.0
%endif
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	vala
%if %{with doc}
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gtk-doc >= 1.4
%endif
Requires:	glib2 >= 1:2.18
Requires:	libdbusmenu >= 0.3.97
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%description -l pl.UTF-8
Mała biblioteka pozwalająca aplikacjom podnosić "flagi" na magistrali
DBus, aby inne komponenty środowiska mogły je odebrać i zwizualizować.
Obecnie jest używana przez wskaźnik komunikacji.

%package devel
Summary:	Header files for libindicate library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libindicate
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.18
Requires:	libdbusmenu-devel >= 0.3.97

%description devel
Header files for libindicate library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libindicate.

%package static
Summary:	Static libindicate library
Summary(pl.UTF-8):	Statyczna biblioteka libindicate
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libindicate library.

%description static -l pl.UTF-8
Statyczna biblioteka libindicate.

%package apidocs
Summary:	libindicate library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libindicate
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libindicate library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libindicate.

%package -n dotnet-indicate-sharp
Summary:	indicate library for .NET
Summary(pl.UTF-8):	Biblioteka indicate dla .NET
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gtk-sharp2 >= 2.12.1

%description -n dotnet-indicate-sharp
indicate library for .NET.

%description -n dotnet-indicate-sharp -l pl.UTF-8
Biblioteka indicate dla .NET.

%package -n dotnet-indicate-sharp-devel
Summary:	Development files for .NET indicate library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki .NET indicate
Group:		Development/Libraries
Requires:	dotnet-gtk-sharp2-devel >= 2.12.1
Requires:	dotnet-indicate-sharp = %{version}-%{release}

%description -n dotnet-indicate-sharp-devel
Development files for .NET indicate library.

%description -n dotnet-indicate-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki .NET indicate.

%package -n python-indicate
Summary:	Python binding for libindicate library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki libindicate
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygobject >= 0.22
Requires:	python-pygtk-gtk >= 2:2.14.0

%description -n python-indicate
Python binding for libindicate library.

%description -n python-indicate -l pl.UTF-8
Wiązanie Pythona do biblioteki libindicate.

%package -n python-indicate-devel
Summary:	Development file for Python libindicate binding
Summary(pl.UTF-8):	Plik programistyczny wiązania Pythona do biblioteki libindicate
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	python-indicate = %{version}-%{release}
Requires:	python-pygtk-devel >= 2:2.14.0

%description -n python-indicate-devel
Development file for Python libindicate binding>

%description -n python-indicate-devel -l pl.UTF-8
Plik programistyczny wiązania Pythona do biblioteki libindicate.

%package -n vala-libindicate
Summary:	Vala API for libindicate library
Summary(pl.UTF-8):	API języka Vala do biblioteki libindicate
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala

%description -n vala-libindicate
Vala API for libindicate library.

%description -n vala-libindicate -l pl.UTF-8
API języka Vala do biblioteki libindicate.

%package gtk
Summary:	Helpers for libindicate that require GTK+ (2.x) dependencies
Summary(pl.UTF-8):	Funkcje pomocnicze libindicate zależne od GTK+ (2.x)
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.12

%description gtk
Helpers for libindicate that require GTK+ (2.x) dependencies.

%description gtk -l pl.UTF-8
Funkcje pomocnicze libindicate zależne od GTK+ (2.x).

%package gtk-devel
Summary:	Header files for libindicate-gtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libindicate-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.12

%description gtk-devel
Header files for libindicate-gtk library.

%description gtk-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libindicate-gtk.

%package gtk-static
Summary:	Static libindicate-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka libindicate-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-gtk-devel = %{version}-%{release}

%description gtk-static
Static libindicate-gtk library.

%description gtk-static -l pl.UTF-8
Statyczna biblioteka libindicate-gtk.

%package -n dotnet-indicate-gtk-sharp
Summary:	indicate-gtk library for .NET
Summary(pl.UTF-8):	Biblioteka indicate-gtk dla .NET
Group:		Libraries
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	dotnet-indicate-sharp = %{version}-%{release}
Requires:	dotnet-gtk-sharp2 >= 2.12.1

%description -n dotnet-indicate-gtk-sharp
indicate-gtk library for .NET.

%description -n dotnet-indicate-gtk-sharp -l pl.UTF-8
Biblioteka indicate-gtk dla .NET.

%package -n dotnet-indicate-gtk-sharp-devel
Summary:	Development files for .NET indicate-gtk library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki .NET indicate-gtk
Group:		Development/Libraries
Requires:	dotnet-gtk-sharp2-devel >= 2.12.1
Requires:	dotnet-indicate-sharp-devel = %{version}-%{release}
Requires:	dotnet-indicate-gtk-sharp = %{version}-%{release}

%description -n dotnet-indicate-gtk-sharp-devel
Development files for .NET indicate-gtk library.

%description -n dotnet-indicate-gtk-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki .NET indicate-gtk.

%package -n vala-libindicate-gtk
Summary:	Vala API for libindicate-gtk library
Summary(pl.UTF-8):	API języka Vala do biblioteki libindicate-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-gtk-devel = %{version}-%{release}
Requires:	vala-libindicate = %{version}-%{release}

%description -n vala-libindicate-gtk
Vala API for libindicate-gtk library.

%description -n vala-libindicate-gtk -l pl.UTF-8
API języka Vala do biblioteki libindicate-gtk.

%package gtk3
Summary:	Helpers for libindicate that require GTK+ (3.x) dependencies
Summary(pl.UTF-8):	Funkcje pomocnicze libindicate zależne od GTK+ (3.x)
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3 >= 3.0.0

%description gtk3
Helpers for libindicate that require GTK+ (3.x) dependencies.

%description gtk3 -l pl.UTF-8
Funkcje pomocnicze libindicate zależne od GTK+ (3.x).

%package gtk3-devel
Summary:	Header files for libindicate-gtk3 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libindicate-gtk3
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk3 = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0.0

%description gtk3-devel
Header files for libindicate-gtk3 library.

%description gtk3-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libindicate-gtk3.

%package gtk3-static
Summary:	Static libindicate-gtk3 library
Summary(pl.UTF-8):	Statyczna biblioteka libindicate-gtk3
Group:		X11/Development/Libraries
Requires:	%{name}-gtk3-devel = %{version}-%{release}

%description gtk3-static
Static libindicate-gtk3 library.

%description gtk3-static -l pl.UTF-8
Statyczna biblioteka libindicate-gtk3.

%package -n vala-libindicate-gtk3
Summary:	Vala API for libindicate-gtk3 library
Summary(pl.UTF-8):	API języka Vala do biblioteki libindicate-gtk3
Group:		X11/Development/Libraries
Requires:	%{name}-gtk3-devel = %{version}-%{release}
Requires:	vala-libindicate = %{version}-%{release}

%description -n vala-libindicate-gtk3
Vala API for libindicate-gtk3 library.

%description -n vala-libindicate-gtk3 -l pl.UTF-8
API języka Vala do biblioteki libindicate-gtk3.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%if %{with apidocs}
%{__gtkdocize}
%endif
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%if %{with gtk2}
install -d build-gtk2
cd build-gtk2
../%configure \
	%{!?with_python:--disable-python} \
	--disable-silent-rules \
	%{__enable_disable apidocs gtk-doc} \
	--with-gtk=2 \
	--with-html-dir=%{_gtkdocdir}

# without -j1 introspection tries to link with system -lindicate
%{__make} -j1
cd ..
%endif

%if %{with gtk3}
install -d build-gtk3
cd build-gtk3
../%configure \
	%{!?with_python:--disable-python} \
	--disable-silent-rules \
	%{__enable_disable apidocs gtk-doc} \
	--with-gtk=3 \
	--with-html-dir=%{_gtkdocdir}

# without -j1 introspection tries to link with system -lindicate
%{__make} -j1
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with gtk2}
%{__make} -j1 -C build-gtk2 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with gtk3}
%{__make} -j1 -C build-gtk3 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%if %{with python}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/indicate/_indicate.{la,a}
%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%post	gtk3 -p /sbin/ldconfig
%postun	gtk3 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libindicate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libindicate.so.5
%{_libdir}/girepository-1.0/Indicate-0.7.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate.so
%{_includedir}/libindicate-0.7
%{_datadir}/gir-1.0/Indicate-0.7.gir
%{_pkgconfigdir}/indicate-0.7.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libindicate
%endif

%if %{with dotnet}
%files -n dotnet-indicate-sharp
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/indicate-sharp

%files -n dotnet-indicate-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/indicate
%{_libdir}/indicate-sharp-0.1
%{_pkgconfigdir}/indicate-sharp-0.1.pc
%endif

%if %{with python}
%files -n python-indicate
%defattr(644,root,root,755)
%dir %{py_sitedir}/indicate
%attr(755,root,root) %{py_sitedir}/indicate/_indicate.so
%{py_sitedir}/indicate/__init__.py[co]

%files -n python-indicate-devel
%defattr(644,root,root,755)
%{_datadir}/pygtk/2.0/defs/indicate.defs
%endif

%files -n vala-libindicate
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/Indicate-0.7.vapi

%if %{with gtk2}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libindicate-gtk.so.3
%{_libdir}/girepository-1.0/IndicateGtk-0.7.typelib

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate-gtk.so
%{_includedir}/libindicate-gtk-0.7
%{_datadir}/gir-1.0/IndicateGtk-0.7.gir
%{_pkgconfigdir}/indicate-gtk-0.7.pc

%files gtk-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate-gtk.a

%if %{with dotnet}
%files -n dotnet-indicate-gtk-sharp
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/indicate-gtk-sharp

%files -n dotnet-indicate-gtk-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/indicate-gtk
%{_libdir}/indicate-gtk-sharp-0.1
%{_pkgconfigdir}/indicate-gtk-sharp-0.1.pc
%endif

%files -n vala-libindicate-gtk
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/IndicateGtk-0.7.vapi
%endif

%if %{with gtk3}
%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate-gtk3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libindicate-gtk3.so.3
%{_libdir}/girepository-1.0/IndicateGtk3-0.7.typelib

%files gtk3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate-gtk3.so
%{_includedir}/libindicate-gtk3-0.7
%{_datadir}/gir-1.0/IndicateGtk3-0.7.gir
%{_pkgconfigdir}/indicate-gtk3-0.7.pc

%files gtk3-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate-gtk3.a

%files -n vala-libindicate-gtk3
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/IndicateGtk3-0.7.vapi
%endif
