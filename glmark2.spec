%define ver	2017.07
%define gitdate	20190327
%define githash	eaa7088
%define rel	4

Name:		glmark2
Version:	%{ver}
Release:	%mkrel %rel%{?gitdate:.%{gitdate}}
Summary:	OpenGL and ES 2.0 Benchmark
License:	GPLv3
URL:		https://github.com/glmark2/glmark2
Group:		Development/X11
# From https://github.com/glmark2/glmark2.git
# Use the included glmark2-getfromgit.sh script to generate the latest archive
Source0:	glmark2-%{ver}-%{gitdate}.git.%{githash}.tar.xz
Source1:	glmark2-getfromgit.sh
Source2:	glmark2-software
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng12)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	python

%description
Glmark2 is a benchmark for OpenGL 2.0 and ES 2.0.

%prep
%setup -q

# Remove internal jpeg libraries
rm -rv src/libjpeg-turbo src/libpng

%build
# Fix incorrect sRGB profile (from suse)
convert data/textures/effect-2d.png -strip data/textures/effect-2d.png

./waf configure	\
	--with-flavors="drm-gl,drm-glesv2,x11-gl,x11-glesv2,wayland-gl,wayland-glesv2" \
	--prefix=%{_usr}
./waf -v


%install
./waf install -v --destdir=%{buildroot}
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}

%files
# the x11 opengl benchmark
%doc NEWS README COPYING COPYING.SGI
%{_bindir}/%{name}
%{_bindir}/%{name}-drm
%{_bindir}/%{name}-es2
%{_bindir}/%{name}-es2-drm
%{_bindir}/%{name}-software
%{_bindir}/%{name}-wayland
%{_mandir}/man1/%{name}-wayland.1*
%{_bindir}/%{name}-es2-wayland
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-drm.1*
%{_mandir}/man1/%{name}-es2.1*
%{_mandir}/man1/%{name}-es2-drm.1*
%{_mandir}/man1/%{name}-es2-wayland.1*
%{_datadir}/%{name}/
