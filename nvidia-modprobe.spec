Name:           nvidia-modprobe
Version:        375.39
Release:        1%{?dist}
Summary:        NVIDIA kernel module loader

License:        GPLv2+
URL:            http://www.nvidia.com/object/unix.html
Source0:        ftp://download.nvidia.com/XFree86/nvidia-modprobe/nvidia-modprobe-%{version}.tar.bz2

BuildRequires:  m4


%description
An utility to load the NVIDIA kernel module and create NVIDIA character device
files.


%prep
%setup -q


%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} NV_VERBOSE=1 STRIP_CMD="/bin/true"


%install
rm -rf %{buildroot}
%make_install INSTALL="install -p" PREFIX=%{_prefix}


%files
%doc COPYING
%attr(4755, root, root) %{_bindir}/nvidia-modprobe
%{_mandir}/man1/nvidia-modprobe.1.*


%changelog
* Fri Feb 17 2017 Jajauma's Packages <jajauma@yandex.ru> - 375.39-1
- Update to latest upstream release

* Fri Feb 17 2017 Jajauma's Packages <jajauma@yandex.ru> - 375.26-1
- Update to latest upstream release

* Sun Nov 27 2016 Jajauma's Packages <jajauma@yandex.ru> - 375.20-1
- Update to latest upstream release

* Thu Oct 20 2016 Jajauma's Packages <jajauma@yandex.ru> - 367.57-1
- Update to latest upstream version

* Sun Oct 02 2016 Jajauma's Packages <jajauma@yandex.ru> - 367.44-1
- Public release
