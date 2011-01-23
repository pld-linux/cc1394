Summary:	AVT CC1394 Viewer application
Summary(pl.UTF-8):	Aplikacja do podglądu AVT CC1394
Name:		cc1394
Version:	3.0
Release:	1
License:	BSD
Group:		X11/Applications/Multimedia
Source0:	http://www.alliedvisiontec.com/fileadmin/content/PDF/Software/AVT_software/zip_files/AVTFire4Linux3v0.src.tar
# Source0-md5:	72b16f6d8e0f482d1b057ee84bb78430
URL:		http://www.alliedvisiontec.com/us/products/software/linux/avt-fire4linux.html
BuildRequires:	QtCore-devel >= 4.1
BuildRequires:	QtGui-devel >= 4.1
BuildRequires:	QtXml-devel >= 4.1
BuildRequires:	SDL-devel
BuildRequires:	libdc1394-devel(avt) >= 2.1.2
BuildRequires:	qt4-build >= 4.1
BuildRequires:	qt4-qmake >= 4.1
Requires:	libdc1394(avt) >= 2.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CC1394 is a demo viewer for IIDC cameras, based on the libdc1394_avt
control library. The supported camera feature set focuses on AVT
camera families. However, third-party cameras should also be usable.

%description -l pl.UTF-8
CC1394 to demonstracyjna aplikacja do podglądu z kamer IIDC, oparta na
bibliotece sterującej libdc1394_avt. Zbiór obsługiwanych możliwości 
skupia się na rodzinach kamer AVT, ale kamery innych firm także mogą
być używalne.

%prep
%setup -q -n AVTFire4Linux3v0_src

tar xzf %{name}-%{version}.tar.gz

%build
cd %{name}

qmake-qt4 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C %{name} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AVT_F4L_Readme_Source.txt ReleaseNotes.txt cc1394/{COPYING,README}
%attr(755,root,root) %{_bindir}/cc1394
