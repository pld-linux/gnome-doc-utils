Summary:	Documentation utilities for GNOME
Summary(pl):	Narzêdzia do budowania dokumentacji dla GNOME
Name:		gnome-doc-utils
Version:	0.2.0
Release:	1
License:	GPL v2+/LGPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-doc-utils/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	c72f2a974e4f05210d2736e92399c58e
URL:		http://www.gnome.org/
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	libxslt-devel >= 1.1.14
BuildRequires:	python >= 2.0
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
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

%post
/usr/bin/scrollkeeper-update -q

%postun
if [ $1 = 0 ]; then
	/usr/bin/scrollkeeper-update -q
fi

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
%{_mandir}/man1/xml2po.1*
