Name:           clr-ignore-mod-sig
Version:        1
Release:        3
License:        GPL-2.0
Summary:        Append kernel command line to disable module signature verification
Group:          kernel
Source0:        clr-ignore-mod-sig.conf
Source1:        clr-ignore-mod-sig.motd

%description
Append kernel command line to disable module signature verification

%prep
mkdir configs
cp %{SOURCE0} configs/
mkdir motd
cp %{SOURCE1} motd/

%build

%install
mkdir -p %{buildroot}/usr/share/kernel/cmdline.d
install -m 0644 -Dt %{buildroot}/usr/share/kernel/cmdline.d configs/*
mkdir -p %{buildroot}/usr/lib/motd.d
install -m 0644 -Dt %{buildroot}/usr/lib/motd.d motd/*

%files
%dir /usr/share/kernel/cmdline.d
/usr/share/kernel/cmdline.d/*
%dir /usr/lib/motd.d
/usr/lib/motd.d/*
