Summary:	Kbtsco
Summary(pl):	Kbtsco
Name:		kbtsco
Version:	1.4.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.kde-apps.org/content/files/45427-%{name}.kmdr.tar.bz2
# Source0-md5:	762fcde7683eb666dfe7300ae83af828
URL:		http://www.kde-apps.org/content/show.php?content=45427
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdewebdev-kommander
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kbtsco is a kommander script that help connection with bluetooth
headset(tested with sony ericsson HBH-600)to use with xmms,audacity or
skype The features of this gui included the starting daemon sdpd,hcid
and rfcomm and scan MAC address to use with BTSCO in order to select
headphone as device

#%description -l pl

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir}}
install kbtsco.kmdr $RPM_BUILD_ROOT%{_datadir}/%{name}

cat > $RPM_BUILD_ROOT%{_bindir}/kbtsco <<EOF
#!/bin/sh

exec %{_bindir}/kmdr-executor %{_datadir}/%{name}/%{name}.kmdr

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbtsco
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/kbtsco.kmdr
