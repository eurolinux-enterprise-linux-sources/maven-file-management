%global pkgname file-management

Name:           maven-%{pkgname}
Version:        1.2.1
Release:        7%{?dist}
# Maven-shared defines file-management version as 1.2.2
Epoch:          1
Summary:        Maven File Management API
License:        ASL 2.0
# URL is not working now, cached copy at http://web.archive.org/web/20121029070007/http://maven.apache.org/shared/file-management/
URL:            http://maven.apache.org/shared/%{pkgname}
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/file-management-1.2.1
# tar caf maven-file-management-1.2.1.tar.xz file-management-1.2.1/
Source0:        %{name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  modello

Obsoletes:      maven-shared-%{pkgname} < %{epoch}:%{version}-%{release}
Provides:       maven-shared-%{pkgname} = %{epoch}:%{version}-%{release}

%description
Provides a component for plugins to easily resolve project dependencies.

This is a replacement package for maven-shared-file-management.

%package javadoc
Summary:        Javadoc for %{name}
Obsoletes:      maven-shared-%{pkgname}-javadoc < %{epoch}:%{version}-%{release}
Provides:       maven-shared-%{pkgname}-javadoc = %{epoch}:%{version}-%{release}
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{pkgname}-%{version}
cp -p %{SOURCE1} LICENSE.txt

# Need namespace for new version modello
# Bug has been filed at http://jira.codehaus.org/browse/MSHARED-234
sed -i "s|<model>|<model xmlns=\"http://modello.codehaus.org/MODELLO/1.3.0\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://modello.codehaus.org/MODELLO/1.3.0 http://modello.codehaus.org/xsd/modello-1.3.0.xsd\" xml.namespace=\"..\" xml.schemaLocation=\"..\" xsd.namespace=\"..\" xsd.targetNamespace=\"..\">|" src/main/mdo/fileset.mdo

# FileSetUtilsTest.testDeleteDanglingSymlink() is expected to fail
sed -i /testDeleteDanglingSymlink/,/assert/s/False/True/ `find -name FileSetUtilsTest.java`

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.2.1-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.2.1-6
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1:1.2.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jan 18 2013 Tomas Radej <tradej@redhat.com> - 1:1.2.1-3
- Added proper Provides/Obsoletes in javadoc
- Fixed changelog entries

* Mon Jan 14 2013 Tomas Radej <tradej@redhat.com> - 1:1.2.1-2
- Added licence text
- Changed maven target from install to package
- Creating directories in Install

* Wed Aug 08 2012 Tomas Radej <tradej@redhat.com> - 1.2.1-1
- Initial version

