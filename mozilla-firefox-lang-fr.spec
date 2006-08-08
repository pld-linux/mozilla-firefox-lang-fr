Summary:	French resources for Mozilla-firefox
Summary(pl):	Francuskie pliki jêzykowe dla Mozilli-firefox
Name:		mozilla-firefox-lang-fr
Version:	1.5.0.6
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source0-md5:	a77ec6225ece78fa9f711090fcb5b529
URL:		http://www.mozilla.org/
BuildRequires:	unzip
Requires(post,postun):	mozilla-firefox >= %{version}
Requires(post,postun):	textutils
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_firefoxdir	%{_libdir}/mozilla-firefox
%define		_chromedir	%{_firefoxdir}/chrome

%description
French resources for Mozilla-firefox.

%description -l pl
Francuskie pliki jêzykowe dla Mozilli-firefox.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_firefoxdir}/defaults/profile}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/* $RPM_BUILD_ROOT%{_chromedir}
sed -e 's@chrome/fr\.jar@fr.jar@' $RPM_BUILD_ROOT%{_libdir}/chrome.manifest \
	> $RPM_BUILD_ROOT%{_chromedir}/fr.manifest
mv -f $RPM_BUILD_ROOT%{_libdir}/*.rdf $RPM_BUILD_ROOT%{_firefoxdir}/defaults/profile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/fr.jar
%{_chromedir}/fr.manifest
# file conflict:
#%{_firefoxdir}/defaults/profile/*.rdf
