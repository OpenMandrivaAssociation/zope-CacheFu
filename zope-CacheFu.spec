%define product		CacheFu
%define version		1.0.2
%define release		1

%define zope_minver	2.7
%define plone_minver	2.0

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Summary:	CacheFu speeds up Plone dramatically
Name:		zope-%{product}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Group:		System/Servers
Source:		http://plone.org/products/cachefu/releases/%{version}/CacheFu-%{version}.tar.bz2
URL:		http://plone.org/products/cachefu/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver}
Requires:	plone >= %{plone_minver}

Provides:	plone-Faq == %{version}
Obsoletes:	zope-Faq


%description
CacheFu speeds up plone sites transparently using a combination of memory,
proxy, and browser caching. CacheFu can be used by itself or with squid
and/or apache. CacheFu generates configuration files for squid or squid
behind apache (if you are using apache by itself, no special configuration
is needed).

%prep
%setup -c

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a %{product} %{buildroot}%{software_home}/Products/%{product}


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
%defattr(0644, root, root, 0755)
%{software_home}/Products/*


