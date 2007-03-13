Summary:	Documentation utilities for GNOME
Summary(pl.UTF-8):	Narzędzia do budowania dokumentacji dla GNOME
Name:		gnome-doc-utils
Version:	0.10.1
Release:	1
License:	GPL v2+/LGPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-doc-utils/0.10/%{name}-%{version}.tar.bz2
# Source0-md5:	208775a4b6c6d9ea0478a84afb36701f
Patch0:		%{name}-no_scrollkeeper_update.patch
URL:		http://www.gnome.org/
BuildRequires:	libxslt-devel >= 1.1.20
BuildRequires:	python >= 2.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires:	libxslt-progs
Requires:	python-libxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of documentation utilities for GNOME.

%description -l pl.UTF-8
Zestaw narzędzi do budowania dokumentacji dla GNOME.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

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
%{_datadir}/xml2po
%{_datadir}/xml/gnome
%{_mandir}/man1/xml2po.1*
%{_omf_dest_dir}/gnome-doc-make
%{_omf_dest_dir}/gnome-doc-xslt
%{_pkgconfigdir}/gnome-doc-utils.pc
%{_pkgconfigdir}/xml2po.pc
