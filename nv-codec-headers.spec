Name:           nv-codec-headers
Version:        13.0.19.0
Release:        1%{?dist}
Summary:        FFmpeg version of Nvidia Codec SDK headers
License:        MIT
URL:            https://github.com/FFmpeg/nv-codec-headers
BuildArch:      noarch
       
Source0:        %url/archive/n%{version}/%{name}-n%{version}.tar.gz

BuildRequires:  make

%description
FFmpeg version of headers required to interface with Nvidias codec APIs.

%prep
%autosetup -n %{name}-n%{version}
sed -i -e 's@/include@/include/ffnvcodec@g' ffnvcodec.pc.in

# Extract license
sed -n '4,25p' include/ffnvcodec/nvEncodeAPI.h > LICENSE
sed -i '1,22s/^.\{,3\}//' LICENSE

%build
%make_build PREFIX=%{_prefix} LIBDIR=/share

%install
%make_install PREFIX=%{_prefix} LIBDIR=/share

%files
%doc README
%license LICENSE
%{_includedir}/ffnvcodec/
%{_datadir}/pkgconfig/ffnvcodec.pc

%changelog
* Thu Mar 13 2025 Simone Caronni <negativo17@gmail.com> - 13.0.19.0-1
- Update to 13.0.19.0.

* Thu Sep 26 2024 Simone Caronni <negativo17@gmail.com> - 12.2.72.0-1
- Update to 12.2.72.0.
- Trim changelog.

* Mon Oct 09 2023 Simone Caronni <negativo17@gmail.com> - 12.1.14.0-1
- Update to 12.1.14.0.

* Tue Mar 14 2023 Simone Caronni <negativo17@gmail.com> - 12.0.16.0-1
- Update to 12.0.16.0.

* Wed Jan 12 2022 Leigh Scott <leigh123linux@gmail.com> - 11.1.5.1-1
- Update to 11.1.5.1

* Wed Dec 08 2021 Leigh Scott <leigh123linux@gmail.com> - 11.1.5.0-1
- Update to 11.1.5.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 21 2021 Leigh Scott <leigh123linux@gmail.com> - 11.0.10.1-1
- Update to 11.0.10.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
