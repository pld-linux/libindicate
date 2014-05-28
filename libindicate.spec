# TODO:
# - python, sharp subpackages
%bcond_without	doc
Summary:	Libindicate
Summary(pl.UTF-8):	Libindicate
Name:		libindicate
Version:	12.10.1
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	https://launchpad.net/libindicate/12.10/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	aeed68ec8047a3325b4aa4aef38f010a
Patch0:		%{name}-am.patch
Patch1:		%{name}-doc.patch
URL:		https://launchpad.net/libindicate/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	glibc-misc
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc-automake
BuildRequires:	libdbusmenu-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
%if %{with doc}
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gtk-doc
%endif
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

#%description -l pl.UTF-8

%package devel
Summary:	Header files for libindicate
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki indicate
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libindicate.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki indicate.

%package static
Summary:	Static indicate library
Summary(pl.UTF-8):	Statyczna biblioteka indicate
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static indicate library.

%description static -l pl.UTF-8
Statyczna biblioteka indicate.

%package apidocs
Summary:	indicate library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki indicate
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
indicate library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki indicate.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%if %{with doc}
%{__gtkdocize}
%endif
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	%{__enable_disable doc gtk-doc} \
	--with-html-dir=%{_gtkdocdir}

# without -j1 introspection tries to link with system -lindicate
%{__make} -j1 \
	PKG_CONFIG_PATH=$(pwd)/libindicate:$(pwd)/libindicate-gtk

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libindicate.so.5
%attr(755,root,root) %{_libdir}/libindicate-gtk3.so.3.*.*
%attr(755,root,root) %ghost %{_libdir}/libindicate-gtk3.so.3
%{_libdir}/girepository-1.0/Indicate-*.typelib
%{_libdir}/girepository-1.0/IndicateGtk3-*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate.so
%attr(755,root,root) %{_libdir}/libindicate-gtk3.so
%{_pkgconfigdir}/indicate-0.7.pc
%{_pkgconfigdir}/indicate-gtk3-0.7.pc
%{_includedir}/libindicate-0.7
%{_includedir}/libindicate-gtk3-0.7
%{_datadir}/gir-1.0/Indicate-*.gir
%{_datadir}/gir-1.0/IndicateGtk3-*.gir

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate.a
%attr(755,root,root) %{_libdir}/libindicate-gtk3.a

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libindicate
%endif
