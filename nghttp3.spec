#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x7E8403D5D673C366 (tatsuhiro.t@gmail.com)
#
Name     : nghttp3
Version  : 0.13.0
Release  : 1
URL      : https://github.com/ngtcp2/nghttp3/releases/download/v0.13.0/nghttp3-0.13.0.tar.xz
Source0  : https://github.com/ngtcp2/nghttp3/releases/download/v0.13.0/nghttp3-0.13.0.tar.xz
Source1  : https://github.com/ngtcp2/nghttp3/releases/download/v0.13.0/nghttp3-0.13.0.tar.xz.asc
Summary  : nghttp3 library
Group    : Development/Tools
License  : MIT
Requires: nghttp3-lib = %{version}-%{release}
Requires: nghttp3-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : pkgconfig(cunit)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description


%package dev
Summary: dev components for the nghttp3 package.
Group: Development
Requires: nghttp3-lib = %{version}-%{release}
Provides: nghttp3-devel = %{version}-%{release}
Requires: nghttp3 = %{version}-%{release}

%description dev
dev components for the nghttp3 package.


%package doc
Summary: doc components for the nghttp3 package.
Group: Documentation

%description doc
doc components for the nghttp3 package.


%package lib
Summary: lib components for the nghttp3 package.
Group: Libraries
Requires: nghttp3-license = %{version}-%{release}

%description lib
lib components for the nghttp3 package.


%package license
Summary: license components for the nghttp3 package.
Group: Default

%description license
license components for the nghttp3 package.


%prep
%setup -q -n nghttp3-0.13.0
cd %{_builddir}/nghttp3-0.13.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689259900
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1689259900
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nghttp3
cp %{_builddir}/nghttp3-%{version}/COPYING %{buildroot}/usr/share/package-licenses/nghttp3/4d9bde9ffbec8d7737496c973a08b1799dfb9a63 || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/nghttp3/nghttp3.h
/usr/include/nghttp3/version.h
/usr/lib64/libnghttp3.so
/usr/lib64/pkgconfig/libnghttp3.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/nghttp3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnghttp3.so.8
/usr/lib64/libnghttp3.so.8.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nghttp3/4d9bde9ffbec8d7737496c973a08b1799dfb9a63
