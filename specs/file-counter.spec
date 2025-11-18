Name:           file-counter
Version:        1.0
Release:        1%{?dist}
Summary:        Script to count files in /etc
License:        GPL
BuildArch:      noarch
Source0:        count_files.sh
Requires:       bash, findutils

%description
Counts files in /etc directory excluding links and dirs.

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 %{SOURCE0} %{buildroot}/usr/local/bin/file-counter

%files
/usr/local/bin/file-counter

%changelog
* Tue Nov 18 2025 designerpromax <designerpromax@github.com> - 1.0-1
- Initial release
