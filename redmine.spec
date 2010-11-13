Name:       redmine
Version:    1.0.3
Release:    %mkrel 4
Summary:    A flexible project management web application
Group:      Networking/WWW
License:    GPLv2+
URL:        http://www.redmine.org
Source0:    http://rubyforge.org/frs/download.php/73140/%{name}-%{version}.tar.gz
Source101:  %{name}.logrotate
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root

# It can only work with webserver that have a plugin for passenger
# ie: apache or nginx
Requires:   webserver
Requires:   rubygem-passenger
Requires:   rubygems
Requires:   %{name}-db
Suggests:   ruby-RMagick
Suggests:   rubygem-ruby-openid
Suggests:   %{name}-scm

BuildArch:  noarch

%description
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

Redmine is open source and released under the terms of the GNU General Public
License v2 (GPL).

Overview

 * Multiple projects support
 * Flexible role based access control
 * Flexible issue tracking system
 * Gantt chart and calendar
 * News, documents & files management
 * Feeds & email notifications
 * Per project wiki
 * Per project forums
 * Time tracking
 * Custom fields for issues, time-entries, projects and users
 * SCM integration (SVN, CVS, Git, Mercurial, Bazaar and Darcs)
 * Issue creation via email
 * Multiple LDAP authentication support
 * User self-registration support
 * Multilanguage support
 * Multiple databases support

#-------------------------------------------------------------------------------
%package pg
Summary:    A flexible project management web application - pgsql connector
Group:      Networking/WWW
Requires:   rubygem-pg
Provides:   %{name}-pg = %{version}-%{release}
Provides:   %{name}-db = %{version}-%{release}

%description pg
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use postgresql as redmine's
database backend.

%files pg
%defattr(-,root,root,-)
#-------------------------------------------------------------------------------
%package mysql
Summary:    A flexible project management web application - mysql connector
Group:      Networking/WWW
Requires:   ruby-mysql
Provides:   %{name}-mysql = %{version}-%{release}
Provides:   %{name}-db    = %{version}-%{release}
%description mysql
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use mysql as redmine's
database backend.

%files mysql
%defattr(-,root,root,-)
#-------------------------------------------------------------------------------
%package sqlite
Summary:    A flexible project management web application - sqlite connector
Group:      Networking/WWW
Requires:   ruby-sqlite3
Provides:   %{name}-sqlite = %{version}-%{release}
Provides:   %{name}-db     = %{version}-%{release}

%description sqlite
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use sqlite as redmine's
database backend.

%files sqlite
%defattr(-,root,root,-)
#-------------------------------------------------------------------------------
%package git
Summary:    A flexible project management web application - git backend
Group:      Networking/WWW
Requires:   git-core
Provides:   %{name}-git = %{version}-%{release}
Provides:   %{name}-scm = %{version}-%{release}

%description git
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use git as redmine's
version control system backend

%files git
%defattr(-,root,root,-)
#-------------------------------------------------------------------------------
%package svn
Summary:    A flexible project management web application - subversion backend
Group:      Networking/WWW
Requires:   subversion
Provides:   %{name}-svn = %{version}-%{release}
Provides:   %{name}-scm = %{version}-%{release}

%description svn
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use subversion as redmine's
version control system backend

%files svn
%defattr(-,root,root,-)
#-------------------------------------------------------------------------------
%package hg
Summary:    A flexible project management web application - mercurial backend
Group:      Networking/WWW
Requires:   mercurial
Provides:   %{name}-hg  = %{version}-%{release}
Provides:   %{name}-scm = %{version}-%{release}

%description hg
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use mercurial as redmine's
version control system backend

%files hg
%defattr(-,root,root,-)
#-------------------------------------------------------------------------------
%package bzr
Summary:    A flexible project management web application - bzr backend
Group:      Networking/WWW
Requires:   bzr
Provides:   %{name}-bzr = %{version}-%{release}
Provides:   %{name}-scm = %{version}-%{release}

%description bzr
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use bazaar as redmine's
version control system backend

%files bzr
%defattr(-,root,root,-)
#-------------------------------------------------------------------------------
%package cvs
Summary:    A flexible project management web application - cvs backend
Group:      Networking/WWW
Requires:   cvs
Provides:   %{name}-cvs = %{version}-%{release}
Provides:   %{name}-scm = %{version}-%{release}

%description cvs
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use cvs as redmine's
version control system backend

%files cvs
%defattr(-,root,root,-)
#-------------------------------------------------------------------------------

%prep
%setup -q

%build
find . -name ".gitignore" -exec rm {} \;
perl -pi -e 's!/usr/local/bin/ruby!/usr/bin/env ruby!' lib/faster_csv.rb

%install
rm -rf %buildroot
install -d %{buildroot}%{_var}/www/%{name}
cp -rf * %{buildroot}%{_var}/www/%{name}
rm -rf %{buildroot}%{_var}/www/%{name}/vendor/rails

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -D -m644 %{SOURCE101} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{_sysconfdir}/logrotate.d/%{name}
%doc %{_var}/www/%{name}/README.rdoc
%dir %{_var}/www/%{name}/
%{_var}/www/%{name}/app/
%{_var}/www/%{name}/config/
%{_var}/www/%{name}/db/
%{_var}/www/%{name}/doc/
%{_var}/www/%{name}/extra/
%{_var}/www/%{name}/files/
%{_var}/www/%{name}/lib/
%{_var}/www/%{name}/log/
%{_var}/www/%{name}/public/
%{_var}/www/%{name}/Rakefile
%{_var}/www/%{name}/script/
%{_var}/www/%{name}/test/
%{_var}/www/%{name}/tmp/
%{_var}/www/%{name}/vendor/
