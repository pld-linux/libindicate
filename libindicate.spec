
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
#BuildRequires:	gir-repository-devel
BuildRequires:	libtool
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

%prep
%setup -q
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
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
%attr(755,root,root) %ghost %{_libdir}/libindicate-gtk.so.1
%attr(755,root,root) %{_libdir}/libindicate-gtk.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libindicate.so.3
%attr(755,root,root) %{_libdir}/libindicate.so.3.0.2

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate-gtk.a
%attr(755,root,root) %{_libdir}/libindicate.a

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate-gtk.la
%attr(755,root,root) %{_libdir}/libindicate-gtk.so
%attr(755,root,root) %{_libdir}/libindicate.la
%attr(755,root,root) %{_libdir}/libindicate.so
%attr(755,root,root) %{_pkgconfigdir}/indicate-gtk.pc
%attr(755,root,root) %{_pkgconfigdir}/indicate.pc
%{_includedir}/libindicate-0.2
