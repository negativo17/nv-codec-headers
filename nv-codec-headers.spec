Name:           nv-codec-headers
Version:        8.2.15.6
Release:        1%{?dist}
Summary:        FFmpeg version of Nvidia Codec SDK headers
License:        MIT
URL:            https://github.com/FFmpeg/nv-codec-headers
Source0:        %url/archive/n%{version}/%{name}-n%{version}.tar.gz

BuildArch:      noarch
       

%description
FFmpeg version of headers required to interface with Nvidias codec APIs.


%prep
%autosetup -n %{name}-n%{version}


%build
%make_build PREFIX=%{_prefix} LIBDIR=/share


%install
%make_install PREFIX=%{_prefix} LIBDIR=/share


%files
%doc README
%{_includedir}/ffnvcodec/
%{_datadir}/pkgconfig/ffnvcodec.pc


%changelog
* Sat Jan 05 2019 Leigh Scott <leigh123linux@googlemail.com> - 8.2.15.6-1
- Update to 8.2.15.6

* Tue Nov 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 8.2.15.5-1
- Update to 8.2.15.5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Leigh Scott <leigh123linux@googlemail.com> - 8.1.24.2-1
- Update to 8.1.24.2

* Sun Apr 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 8.1.24.1-1
- Update to 8.1.24.1

* Tue Feb 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 8.0.14.1-1
- First build
