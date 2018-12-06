# Run tests in check section
# Disabled because https://github.com/marstr/goalias/issues/4
%bcond_with check

%global goipath         github.com/marstr/goalias
%global commit          8dff9a14db648bfdd58d45515d3eaaee23aad078

%global common_description %{expand:
This rather bizarre program will scour a Go package for all publicly exported 
entities then create a package that merely delegates the work to the original 
package.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Generates a Go package that acts as a ghost of another
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/marstr/collection)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git8dff9a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180628git8dff9a1
- Bump to commit 8dff9a14db648bfdd58d45515d3eaaee23aad078

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180416git3026ca7
- First package for Fedora


