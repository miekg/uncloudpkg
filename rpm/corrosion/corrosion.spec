Name:           uncloud-corrosion
Version:        0.17.1
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
%ifarch aarch64
curl -L
https://github.com/psviderski/corrosion/releases/download/v%{version}/corrosion-arm64-unknown-linux-gnu.tar.gz > %{name}.tar.gz
%endif
%ifarch x86_64
curl -L https://github.com/psviderski/corrosion/releases/download/v%{version}/corrosion-amd64-unknown-linux-gnu.tar.gz > %{name}.tar.gz
%endif
tar xf %{name}.tar.gz

%install
cp %{_topdir}corrosion.service %{buildroot}/../corrosion.service

install -D -m 0755 corrosion          %{buildroot}/%{_bindir}/corrosion
install -D -m 0644 corrosion.service  %{buildroot}/%{_unitdir}/corrosion.service

install -D -m 0640 docker-daemon.json  %{buildroot}%{_sysconfdir}/docker/docker-daemon.json

%files
%{_bindir}/%{name}d
%{_unitdir}/corrosion.service
