Name:		glmark2
Version:	2021.12
Release:	1
Summary:	OpenGL and ES 2.0 Benchmark
License:	GPLv3
URL:		https://github.com/glmark2/glmark2
Group:		Development/X11
Source0:	https://github.com/glmark2/glmark2/releases/archive/%{name}-%{version}.tar.gz
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
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	meson

%description
Glmark2 is a benchmark for OpenGL 2.0 and ES 2.0.

%prep
%autosetup -p1

# Remove internal jpeg libraries
rm -rv src/libjpeg-turbo src/libpng

%build
# Fix incorrect sRGB profile (from suse)
convert data/textures/effect-2d.png -strip data/textures/effect-2d.png
%meson \
    -Dflavors="drm-gl,drm-glesv2,x11-gl,x11-glesv2,wayland-gl,wayland-glesv2"

%meson_build

%install
%meson_install -C build

%files
# the x11 opengl benchmark
%doc NEWS README COPYING COPYING.SGI
%{_bindir}/%{name}
%{_bindir}/%{name}-drm
%{_bindir}/%{name}-es2
%{_bindir}/%{name}-es2-drm
%{_bindir}/%{name}-wayland
%{_bindir}/%{name}-es2-wayland
%doc %{_mandir}/man1/%{name}-wayland.1*
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/man1/%{name}-drm.1*
%doc %{_mandir}/man1/%{name}-es2.1*
%doc %{_mandir}/man1/%{name}-es2-drm.1*
%doc %{_mandir}/man1/%{name}-es2-wayland.1*
%{_datadir}/%{name}/
