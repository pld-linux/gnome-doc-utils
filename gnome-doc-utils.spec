Summary:	Documentation utilities for GNOME
Summary(pl.UTF-8):	Narzędzia do budowania dokumentacji dla GNOME
Name:		gnome-doc-utils
Version:	0.12.0
Release:	2
License:	GPL v2+/LGPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-doc-utils/0.12/%{name}-%{version}.tar.bz2
# Source0-md5:	5934c08d12407d8233416343cd73df24
Patch0:		%{name}-no_scrollkeeper_update.patch
URL:		http://www.gnome.org/
BuildRequires:	libxslt-devel >= 1.1.22
BuildRequires:	python >= 2.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	rarian-compat
Requires(post,postun):	rarian-compat
Requires:	libxslt-progs
Requires:	python-libxml2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
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
