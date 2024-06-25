%global debug_package %{nil}

Name:           difftastic
Version:        0.58.0
Release:        1%{?dist}
Summary:        a structural diff that understands syntax
Group:          Applications/System
License:        MIT
URL:            https://github.com/wilfred/%{name}
BuildRequires:  cmake
BuildRequires:  cargo, rust, clang-devel, clang-libs
Source:         https://github.com/wilfred/%{name}/archive/refs/tags/%{version}.tar.gz

%description
Difftastic is a CLI diff tool that compares files based on
their syntax, not line-by-line. Difftastic produces accurate
diffs that are easier for humans to read.

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp target/release/difft %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE* *.md
/usr/bin/difft

%changelog
* Tue Jun 25 2024 Jamie Curnow <jc@jc21.com> - 0.58.0-1
- v0.58.0

* Fri Mar 22 2024 Jamie Curnow <jc@jc21.com> - 0.56.1-1
- v0.56.1
