#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtgraphicaleffects
Version  : 5.12.0
Release  : 12
URL      : https://download.qt.io/official_releases/qt/5.12/5.12.0/submodules/qtgraphicaleffects-everywhere-src-5.12.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.12/5.12.0/submodules/qtgraphicaleffects-everywhere-src-5.12.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtgraphicaleffects-lib = %{version}-%{release}
Requires: qtgraphicaleffects-license = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Test)

%description
No detailed description available

%package lib
Summary: lib components for the qtgraphicaleffects package.
Group: Libraries
Requires: qtgraphicaleffects-license = %{version}-%{release}

%description lib
lib components for the qtgraphicaleffects package.


%package license
Summary: license components for the qtgraphicaleffects package.
Group: Default

%description license
license components for the qtgraphicaleffects package.


%prep
%setup -q -n qtgraphicaleffects-everywhere-src-5.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1544049315
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtgraphicaleffects
cp LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtgraphicaleffects/LICENSE.FDL
cp LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtgraphicaleffects/LICENSE.GPL2
cp LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtgraphicaleffects/LICENSE.GPL3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtgraphicaleffects/LICENSE.GPL3-EXCEPT
cp LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtgraphicaleffects/LICENSE.LGPL3
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/qml/QtGraphicalEffects/Blend.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/BrightnessContrast.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/ColorOverlay.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/Colorize.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/ConicalGradient.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/Desaturate.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/DirectionalBlur.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/Displace.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/DropShadow.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/FastBlur.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/GammaAdjust.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/GaussianBlur.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/Glow.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/HueSaturation.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/InnerShadow.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/LevelAdjust.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/LinearGradient.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/MaskedBlur.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/OpacityMask.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/RadialBlur.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/RadialGradient.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/RectangularGlow.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/RecursiveBlur.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/ThresholdMask.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/ZoomBlur.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/libqtgraphicaleffectsplugin.so
/usr/lib64/qt5/qml/QtGraphicalEffects/plugins.qmltypes
/usr/lib64/qt5/qml/QtGraphicalEffects/private/DropShadowBase.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/private/DropShadowBase.qmlc
/usr/lib64/qt5/qml/QtGraphicalEffects/private/FastGlow.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/private/FastGlow.qmlc
/usr/lib64/qt5/qml/QtGraphicalEffects/private/FastInnerShadow.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/private/FastInnerShadow.qmlc
/usr/lib64/qt5/qml/QtGraphicalEffects/private/FastMaskedBlur.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/private/FastMaskedBlur.qmlc
/usr/lib64/qt5/qml/QtGraphicalEffects/private/GaussianDirectionalBlur.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/private/GaussianDirectionalBlur.qmlc
/usr/lib64/qt5/qml/QtGraphicalEffects/private/GaussianGlow.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/private/GaussianGlow.qmlc
/usr/lib64/qt5/qml/QtGraphicalEffects/private/GaussianInnerShadow.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/private/GaussianInnerShadow.qmlc
/usr/lib64/qt5/qml/QtGraphicalEffects/private/GaussianMaskedBlur.qml
/usr/lib64/qt5/qml/QtGraphicalEffects/private/GaussianMaskedBlur.qmlc
/usr/lib64/qt5/qml/QtGraphicalEffects/private/libqtgraphicaleffectsprivate.so
/usr/lib64/qt5/qml/QtGraphicalEffects/private/qmldir
/usr/lib64/qt5/qml/QtGraphicalEffects/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtgraphicaleffects/LICENSE.FDL
/usr/share/package-licenses/qtgraphicaleffects/LICENSE.GPL2
/usr/share/package-licenses/qtgraphicaleffects/LICENSE.GPL3
/usr/share/package-licenses/qtgraphicaleffects/LICENSE.GPL3-EXCEPT
/usr/share/package-licenses/qtgraphicaleffects/LICENSE.LGPL3
