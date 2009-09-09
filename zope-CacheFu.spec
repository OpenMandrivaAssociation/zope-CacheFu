%define Product CacheFu
%define product cachefu
%define name    zope-%{Product}
%define version 1.1
%define release %mkrel 5

%define zope_minver     2.7
%define zope_home       %{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	CacheFu speeds up Plone dramatically
License:	GPL
Group:		System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tgz
Requires:	zope >= %{zope_minver}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}


%description
CacheFu speeds up plone sites transparently using a combination of memory,
proxy, and browser caching. CacheFu can be used by itself or with squid
and/or apache. CacheFu generates configuration files for squid or squid
behind apache (if you are using apache by itself, no special configuration
is needed).

%prep
%setup -q -n %{Product}-%{version}

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a CMFSquidTool CacheSetup PageCacheManager PolicyHTTPCacheManager \
    %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
