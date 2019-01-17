Name:           clr-ignore-mod-sig
Version:        1
Release:        1
License:        GPL-2.0
Summary:        Append kernel command line to disable module signature verification
Group:          kernel
Source0:        clr-ignore-mod-sig.conf

%description
Append kernel command line to disable module signature verification

%prep
mkdir configs
cp %{SOURCE0} configs/

%build

%install
mkdir -p %{buildroot}/usr/share/kernel/cmdline.d
install -m 0644 -Dt %{buildroot}/usr/share/kernel/cmdline.d configs/*

%files
%dir /usr/share/kernel/cmdline.d
/usr/share/kernel/cmdline.d/*
