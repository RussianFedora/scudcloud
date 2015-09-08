Summary:	Slack
Name:		scudcloud
Version:	1.0.62
Release:	2%{?dist}

URL:		https://github.com/raelgc/scudcloud/
Group:		Applications/Internet
Source:		%{name}-%{version}.tar.gz
License:	MIT

BuildRequires:	desktop-file-utils
BuildRequires:	python

Requires:	python3
Requires:	python3-PyQt4

Requires(post):	xdg-utils
Requires(postun):	xdg-utils

BuildArch: noarch

%description
Slack Client

%prep
%setup -q

%build

%install
INSTALL="/opt/scudcloud"
mkdir -p ${RPM_BUILD_ROOT}/$INSTALL/lib
mkdir -p ${RPM_BUILD_ROOT}/$INSTALL/resources
mkdir -p ${RPM_BUILD_ROOT}/usr/share/applications/
mkdir -p ${RPM_BUILD_ROOT}/usr/share/icons/hicolor/scalable/apps
mkdir -p ${RPM_BUILD_ROOT}/usr/share/icons/mono-dark/scalable/apps
mkdir -p ${RPM_BUILD_ROOT}/usr/share/icons/mono-light/scalable/apps
mkdir -p ${RPM_BUILD_ROOT}/usr/bin

cd scudcloud-1.0
cp lib/*.py ${RPM_BUILD_ROOT}/$INSTALL/lib
cp resources/* ${RPM_BUILD_ROOT}/$INSTALL/resources
cp scudcloud ${RPM_BUILD_ROOT}/$INSTALL
cp LICENSE ${RPM_BUILD_ROOT}/$INSTALL
cp scudcloud.desktop ${RPM_BUILD_ROOT}/usr/share/applications/
cp systray/hicolor/* ${RPM_BUILD_ROOT}/usr/share/icons/hicolor/scalable/apps
cp systray/mono-dark/* ${RPM_BUILD_ROOT}/usr/share/icons/mono-dark/scalable/apps
cp systray/mono-light/* ${RPM_BUILD_ROOT}/usr/share/icons/mono-light/scalable/apps
ln -sf $INSTALL/scudcloud ${RPM_BUILD_ROOT}/usr/bin/scudcloud

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/scudcloud.desktop

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
xdg-desktop-menu forceupdate 2> /dev/null || :

%postun
xdg-desktop-menu forceupdate 2> /dev/null || :

%files
%defattr(-,root,root)
/opt/scudcloud
%{_datadir}/applications/scudcloud.desktop
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/icons/mono-dark/scalable/apps/*
%{_datadir}/icons/mono-light/scalable/apps/*
%{_bindir}/scudcloud

%changelog
* Mon May 18 2015 Marcin Trendota <moonwolf@poczta.onet.pl>
- First version
