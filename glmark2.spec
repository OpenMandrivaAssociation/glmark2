Summary:	OpenGL and ES 2.0 Benchmark
Name:		glmark2
Version:	2023.01
Release:	2
License:	GPLv3
Group:		Development/X11
URL:		https://github.com/glmark2/glmark2
Source0:	https://github.com/glmark2/glmark2/archive/refs/tags/%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-es2.desktop
Source3:	%{name}-es2-wayland.desktop
Source4:	%{name}-wayland.desktop
Source5:	%{name}.png
Source6:	%{name}-es2.png
Source7:	%{name}-es2-wayland.png
Source8:	%{name}-wayland.png
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

# Remove internal libraries
rm -r src/libjpeg-turbo src/libpng src/zlib
rm -r waf waflib

%build
# Fix incorrect sRGB profile (from suse)
convert data/textures/effect-2d.png -strip data/textures/effect-2d.png
%meson \
    -Dflavors="drm-gl,drm-glesv2,wayland-gl,wayland-glesv2,x11-gl,x11-glesv2"

%meson_build

%install
%meson_install -C build

for i in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4}; do
    desktop-file-install --dir=%{buildroot}%{_datadir}/applications $i
done

install -d %{buildroot}%{_datadir}/pixmaps/
install -p %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{buildroot}%{_datadir}/pixmaps/

%files
# the x11 opengl benchmark
%doc NEWS README COPYING COPYING.SGI
%{_bindir}/%{name}
%{_bindir}/%{name}-drm
%{_bindir}/%{name}-es2
%{_bindir}/%{name}-es2-drm
%{_bindir}/%{name}-wayland
%{_bindir}/%{name}-es2-wayland
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/pixmaps/*.png
%doc %{_mandir}/man1/%{name}-wayland.1*
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/man1/%{name}-drm.1*
%doc %{_mandir}/man1/%{name}-es2.1*
%doc %{_mandir}/man1/%{name}-es2-drm.1*
%doc %{_mandir}/man1/%{name}-es2-wayland.1*
%{_datadir}/%{name}/
