
Summary:	kbtsco is a kommander script that help connection with bluetooth headset
Summary(pl):	kbtsco to skrypt kommandera, który pomaga ³±czyæ zestaw s³uchawkowy Bluetooth
Name:		kbtsco
Version:	1.4.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.kde-apps.org/content/files/45427-%{name}.kmdr.tar.bz2
# Source0-md5:	18d2ea8064561c568ab4d19c5ad6d6d6
Source1:	%{name}.desktop
Patch0:		%{name}-path.patch
URL:		http://www.kde-apps.org/content/show.php?content=45427
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	bluez-hcidump
Requires:	bluez-utils
Requires:	btsco
Requires:	kdebase-kdialog
Requires:	kdewebdev-kommander
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kbtsco is a kommander script that help connection with bluetooth
headset (tested with sony ericsson HBH-600) to use with xmms,audacity
or skype. The features of this GUI included the starting daemon
sdpd,hcid and rfcomm and scan MAC address to use with BTSCO in order
to select headphone as sound device.

%description -l pl
kbtsco to skrypt kommandera, który pomaga ³±czyæ zestaw s³uchawkowy
Bluetooth (testowane z sony ericsson HBH-600) z oprogramowaniem. Mo¿na
go u¿yæ z xmms, audacity lub skype. Mo¿liwo¶ci interfejsu graficznego
zawieraj±: uruchomienie demona sdpd, hcid i rfcomm oraz skanowanie
adresów MAC aby u¿ywaæ ich z BTSCO w celu wyboru zestawu s³uchawkowego
jako urz±dzenia d¼wiêkowego.

%prep
%setup -q -c
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir},%{_desktopdir}/kde}
install kbtsco.kmdr $RPM_BUILD_ROOT%{_datadir}/%{name}
install %SOURCE1 $RPM_BUILD_ROOT%{_desktopdir}/kde

cat > $RPM_BUILD_ROOT%{_bindir}/kbtsco <<EOF
#!/bin/sh

if [ ! -x %{_bindir}/kmdr-executor ]; then
exec %{_bindir}/kdialog --error "Package kdewebdev-kommander is missing.\nYou need to install it."
exit 0
fi
exec %{_bindir}/kmdr-executor %{_datadir}/%{name}/%{name}.kmdr

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbtsco
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/kbtsco.kmdr
%{_desktopdir}/kde/%{name}.desktop
