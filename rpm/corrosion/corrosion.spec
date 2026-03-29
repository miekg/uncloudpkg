Name:           uncloud-corrosion
Version:        0.2.2
Release:        1.0
Summary:        Uncloud gossip-based distributed store
License:        ASL-2.0
URL:            https://uncloud.run
Source0:        %{name}-%{version}.tar.gz
Source1:        corrosion.service
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}

%description
Corrosion is a Rust program that propagates a SQLite database with a gossip protocol.

%define services corrosion.service
%define _topdir %(echo $PWD)/

%prep

%build
curl -L https://github.com/psviderski/corrosion/releases/download/v%{version}/corrosion-%{_arch}-unknown-linux-gnu.tar.gz > %{name}.tar.gz
tar xf %{name}.tar.gz

%install
cp %{_topdir}corrosion.service %{buildroot}/../corrosion.service

install -D -m 0755 corrosion          %{buildroot}/%{_bindir}/corrosion
install -D -m 0644 corrosion.service  %{buildroot}/%{_unitdir}/corrosion.service

%files
%{_bindir}/corrosion
%{_unitdir}/corrosion.service
