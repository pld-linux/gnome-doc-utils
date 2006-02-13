Summary:	Documentation utilities for GNOME
Summary(pl):	Narzêdzia do budowania dokumentacji dla GNOME
Name:		gnome-doc-utils
Version:	0.5.5
Release:	1
License:	GPL v2+/LGPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-doc-utils/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	ce9a4787afb9aac91ce55bbee2127d43
Patch0:		%{name}-no_scrollkeeper_update.patch
URL:		http://www.gnome.org/
BuildRequires:	libxslt-devel >= 1.1.15
BuildRequires:	python >= 2.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires:	python-libxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of documentation utilities for GNOME.

%description -l pl
Zestaw narzêdzi do budowania dokumentacji dla GNOME.

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
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}/*.m4
%{_datadir}/%{name}
%{_datadir}/xml2po
%{_datadir}/xml/gnome
%{_mandir}/man1/xml2po.1*
%{_omf_dest_dir}/*
%{_pkgconfigdir}/*.pc
