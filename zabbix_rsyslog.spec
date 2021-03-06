%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define module_name zabbix_rsyslog 

Name:           %{module_name}
Version:        1.0.2
Release:        1
Group:          Applications/System
Summary:        Send rsyslog queue stats to Zabbix

License:        Apache 2.0
URL:            https://github.com/facastagnini/zabbix-rsyslog
Source0:        %{module_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools
Requires:       python-setuptools rsyslog python-argparse
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Takes rsyslog's impstats, which shows various stats for all the action queues,
and sends them to Zabbix for monitoring.

%prep
%setup -q -n %{module_name}-%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT

%files
%doc README.md
%{python_sitelib}/*
%attr(0755,-,-) %{_bindir}/
%config %{_sysconfdir}/rsyslog.d/10-impstats.conf
%config %{_sysconfdir}/logrotate.d/rsyslogd-impstats
%config %{_sysconfdir}/zabbix_agentd.d/rsyslogdiscovery.conf

%changelog
* Thu Oct 29 2015 Micah Yoder
- Increase rsyslog queue size to 100000 from 1000
- Increase tail analysis from 30 to 500

* Wed Jun 17 2015 Micah Yoder
- Add argparse dependency

* Wed Jun 10 2015  Micah Yoder
- Initial spec
