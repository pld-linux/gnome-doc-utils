Summary:	Documentation utilities for GNOME
Summary(pl.UTF-8):	Narzędzia do budowania dokumentacji dla GNOME
Name:		gnome-doc-utils
Version:	0.20.9
Release:	1
License:	GPL v2+/LGPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-doc-utils/0.20/%{name}-%{version}.tar.xz
# Source0-md5:	dd58f8dd10fb90299ae009dd0faf5270
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd44-xml
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.37.0
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	libxml2-progs >= 1:2.6.31
BuildRequires:	libxslt-devel >= 1.1.22
BuildRequires:	libxslt-progs >= 1.1.22
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	python-libxml2 >= 1:2.6.31
BuildRequires:	rarian-compat
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	rarian-compat
Requires:	libxslt-progs >= 1.1.22
Requires:	python-libxml2 >= 1:2.6.31
Requires:	python-modules >= 1:2.4
Requires:	which
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of documentation utilities for GNOME.

%description -l pl.UTF-8
Zestaw narzędzi do budowania dokumentacji dla GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4 -I tools
%{__autoconf}
%{__automake}
%configure \
	--disable-scrollkeeper
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%find_lang %{name} --all-name --with-omf --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-doc-prepare
%attr(755,root,root) %{_bindir}/gnome-doc-tool
%attr(755,root,root) %{_bindir}/xml2po
%{_aclocaldir}/gnome-doc-utils.m4
%{_datadir}/%{name}
%{_datadir}/xml/gnome
%{_datadir}/xml/mallard
%{_mandir}/man1/xml2po.1*
%dir %{py_sitescriptdir}/xml2po
%{py_sitescriptdir}/xml2po/*.py[co]
%dir %{py_sitescriptdir}/xml2po/modes
%{py_sitescriptdir}/xml2po/modes/*.py[co]
%{_npkgconfigdir}/gnome-doc-utils.pc
%{_npkgconfigdir}/xml2po.pc
