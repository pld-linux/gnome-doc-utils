Summary:	Documentation utilities for GNOME
Summary(pl):	Narzêdzia do budowania dokumentacji dla GNOME
Name:		gnome-doc-utils
Version:	0.1.2
Release:	1
License:	LGPL
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-doc-utils/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	7164538a4a56418328f9bfde0313ac6b
URL:		http://www.gnome.org/
BuildRequires:	libxml2-devel >= 2.6.12
BuildRequires:	libxslt-devel >= 1.1.8
BuildRequires:	python >= 2.0
BuildRequires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of documentation utilities for GNOME.

%description -l pl
Zestaw narzêdzi do budowania dokumentacji dla GNOME.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}/*.pc
%{_aclocaldir}/*.m4
%{_datadir}/%{name}
%{_omf_dest_dir}/*
%{_datadir}/xml/gnome
%{_datadir}/xml2po
