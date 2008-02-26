#
# TODO:
# - add doc and readme
# - add desc and pl desc.
Summary:	World of Padman - the biggest Q3A-Funmod project
Summary(pl.UTF-8):	World of Padman - największa modyfikacja projektu Q3A
Name:		worldofpadman
Version:	1.2
Release:	0.5
License:	GPL v2
Group:		X11/Applications/Games
Source0:	ftp://ftp.snt.utwente.nl/pub/games/worldofpadman/linux/%{name}.run
# Source0-md5:	c7650414d7865ddac26ada6b3f7b8cc9
Source1:	ftp://ftp.snt.utwente.nl/pub/games/worldofpadman/linux/wop_patch_1_2.run
# Source1-md5:	3468fc91889795471bc68e35ea334614
Source2:	%{name}.desktop
URL:		http://www.worldofpadman.com
BuildRequires:	/bin/sh
BuildRequires:	tar
Requires:	worldofpadman-data
ExclusiveArch:	%{ix86} %{x8664} ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.

#% description -l pl.UTF-8

%prep
%setup -q -T -c -n %{name}
sh %{SOURCE0} --noexec --target .
sh %{SOURCE1} --noexec --target .

tar xf readme.tar
tar xf extras.tar

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

%ifarch i?86 athlon
tar xf wop-engine.i386.tar -C $RPM_BUILD_ROOT%{_datadir}/%{name}
%endif
%ifarch ppc ppc64
tar xf wop-engine.ppc.tar -C $RPM_BUILD_ROOT%{_datadir}/%{name}
%endif
%ifarch %{x8664}
tar xf wop-engine.x86_64.tar -C $RPM_BUILD_ROOT%{_datadir}/%{name}
%endif

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install wop.png $RPM_BUILD_ROOT%{_pixmapsdir}
install bin/Linux/x86/WoP $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -sf %{_datadir}/%{name}/WoP $RPM_BUILD_ROOT%{_bindir}/WoP

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README README_de copyright_de.txt copyright_en.txt wop_patch_1_2.txt gpl.txt
#%doc readme readme.html *.cfg
%attr(755,root,root) %{_bindir}/WoP
%attr(755,root,root) %{_datadir}/%{name}/wopded.*
%attr(755,root,root) %{_datadir}/%{name}/wop-engine.*
%attr(755,root,root) %{_datadir}/%{name}/WoP
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
