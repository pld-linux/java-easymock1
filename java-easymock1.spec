%define		srcname		easymock1
Summary:	easymock
Name:		java-easymock1
Version:	1.2
Release:	0.1
License:	MIT
Group:		Libraries/Java
Source0:	http://downloads.sourceforge.net/project/easymock/EasyMock/1.2/easymock%{version}_Java1.5.zip
# Source0-md5:	828a04a6b901917cb995c316ee542f2f
Source1:	easymock.pom
URL:		http://easymock.org
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.555
BuildRequires:	unzip
Requires(post):	jpackage-utils >= 0:1.7.2
Requires(postun):	jpackage-utils >= 0:1.7.2
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
easymock

%package javadoc
Summary:	Online manual for %{srcname}
Summary(pl.UTF-8):	Dokumentacja online do %{srcname}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{srcname}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{srcname}.

%description javadoc -l fr.UTF-8
Javadoc pour %{srcname}.

%package demo
Summary:	Demo for %{srcname}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu %{srcname}
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{srcname}.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{srcname}.

%package manual
Summary:	Tutorial for %{srcname}
Group:		Documentation

%description manual
Manual for %{srcname}.

%package source
Summary:	Source code of %{srcname}
Summary(pl.UTF-8):	Kod źródłowy %{srcname}
Group:		Documentation
Requires:	jpackage-utils >= 1.7.5-2

%description source
Source code of %{srcname}.

%description source -l pl.UTF-8
Kod źródłowy %{srcname}.

%prep
%setup -q -n easymock%{version}_Java1.5

mkdir demo
cd demo
unzip ../samples.zip

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a easymock.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/easymock-%{version}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink

# demo
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# source
install -d $RPM_BUILD_ROOT%{_javasrcdir}
cp -a src.zip $RPM_BUILD_ROOT%{_javasrcdir}/%{srcname}.src.jar

# maven stuff
install -d $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{srcname}.pom
%add_to_maven_depmap easymock easymock %{version} JPP %{srcname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_maven_depmap

%postun
%update_maven_depmap

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%{_javadir}/%{srcname}.jar
%{_javadir}/%{srcname}-%{version}.jar
%{_javadir}/easymock-%{version}.jar
%{_datadir}/maven2/poms/JPP.%{srcname}.pom
%{_mavendepmapfragdir}/%{name}

%files demo
%defattr(644,root,root,755)
%doc Documentation.html easymock.css news.txt
%{_examplesdir}/%{name}-%{version}

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}

%files source
%defattr(644,root,root,755)
%{_javasrcdir}/%{srcname}.src.jar
