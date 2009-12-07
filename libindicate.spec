
Summary:	Libindicate
Summary(pl.UTF-8):	Libindicate
Name:		libindicate
Version:	0.2.3
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	http://launchpad.net/libindicate/0.2/0.2.3/+download/%{name}-%{version}.tar.gz
# Source0-md5:	c32f2cdd85534feea4a5ebd532ede641
Patch0:		%{name}-am.patch
URL:		https://launchpad.net/libindicate/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
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
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-gobject-introspection \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate.so.3.*.*
%attr(755,root,root) %ghost %{_libdir}/libindicate.so.3
%attr(755,root,root) %{_libdir}/libindicate-gtk.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/libindicate-gtk.so.1

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate.a
%attr(755,root,root) %{_libdir}/libindicate-gtk.a

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate.la
%attr(755,root,root) %{_libdir}/libindicate.so
%attr(755,root,root) %{_libdir}/libindicate-gtk.la
%attr(755,root,root) %{_libdir}/libindicate-gtk.so
%attr(755,root,root) %{_pkgconfigdir}/indicate.pc
%attr(755,root,root) %{_pkgconfigdir}/indicate-gtk.pc
%{_includedir}/libindicate-0.2

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libindicate
