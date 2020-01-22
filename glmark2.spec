%define gitdate	25.12.2019
#rel to bump
%define rel	1

Name:		glmark2
Version:	%{gitdate}
Release:	1.%{gitdate}.%{rel}
Summary:	OpenGL and ES 2.0 Benchmark
License:	GPLv3
URL:		https://github.com/glmark2/glmark2
Group:		Development/X11
# From https://github.com/glmark2/glmark2.git
Source0:	glmark2-25.12.2019.zip

BuildRequires:	imagemagick
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	python

%description
Glmark2 is a benchmark for OpenGL 2.0 and ES 2.0.

%prep
%setup -qn glmark2-master

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
#install -m 755 %{SOURCE2} %{buildroot}%{_bindir}

%files
# the x11 opengl benchmark
%doc NEWS README COPYING COPYING.SGI
%{_bindir}/%{name}
%{_bindir}/%{name}-drm
%{_bindir}/%{name}-es2
%{_bindir}/%{name}-es2-drm
%{_bindir}/%{name}-software
#{_bindir}/%{name}-wayland
%{_mandir}/man1/%{name}-wayland.1*
%{_bindir}/%{name}-es2-wayland
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-drm.1*
%{_mandir}/man1/%{name}-es2.1*
%{_mandir}/man1/%{name}-es2-drm.1*
%{_mandir}/man1/%{name}-es2-wayland.1*
%{_datadir}/%{name}/
