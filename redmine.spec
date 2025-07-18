Name:           redmine
Version:        2.3.2
Release:        2
Summary:        A flexible project management web application
Group:          Networking/WWW
License:        GPLv2+
URL:            https://www.redmine.org
Source0:        http://rubyforge.org/frs/download.php/75597/%{name}-%{version}.tar.gz
Source101:      %{name}.logrotate
Source102:      %{name}.httpd
Source103:      %{name}-pg-database.yml

BuildRequires:  ruby >= 1.8.7
BuildRequires:  ruby-RubyGems
Requires:       webserver
Requires:       rails >= 2.3.14
Requires:       ruby-rack >= 1.1.1
Requires:       rubygems
Requires:       %{name}-db
Requires:       ruby-ruby-debug
# Only suggests rubygem-passenger, after all, it can work with fcgi too
Suggests:       rubygem-passenger
Suggests:       ruby-RMagick
Suggests:       rubygem-ruby-openid
Suggests:       %{name}-scm

BuildArch:      noarch

%description
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

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
Summary:        A flexible project management web application - pgsql connector
Group:          Networking/WWW
Requires:       rubygem-pg
Provides:       %{name}-pg = %{version}-%{release}
Provides:       %{name}-db = %{version}-%{release}

%description pg
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use postgresql as redmine's
database backend.


%files pg
%{_var}/www/%{name}/config/database.postgres.yml
#-------------------------------------------------------------------------------
%package mysql
Summary:        A flexible project management web application - mysql connector
Group:          Networking/WWW
Requires:       ruby-mysql
Provides:       %{name}-mysql = %{version}-%{release}
Provides:       %{name}-db    = %{version}-%{release}

%description mysql
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use mysql as redmine's
database backend.


%files mysql
%config(noreplace) %{_var}/www/%{name}/config/database.yml
#-------------------------------------------------------------------------------
%package sqlite
Summary:        A flexible project management web application - sqlite connector
Group:          Networking/WWW
Requires:       ruby-sqlite3
Provides:       %{name}-sqlite = %{version}-%{release}
Provides:       %{name}-db     = %{version}-%{release}

%description sqlite
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use sqlite as redmine's
database backend.


%files sqlite
#-------------------------------------------------------------------------------
%package git
Summary:        A flexible project management web application - git backend
Group:          Networking/WWW
Requires:       git-core
Provides:       %{name}-git = %{version}-%{release}
Provides:       %{name}-scm = %{version}-%{release}

%description git
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use git as redmine's
version control system backend


%files git
#-------------------------------------------------------------------------------
%package svn
Summary:        A flexible project management web application - subversion backend
Group:          Networking/WWW
Requires:       subversion
Provides:       %{name}-svn = %{version}-%{release}
Provides:       %{name}-scm = %{version}-%{release}

%description svn
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use subversion as redmine's
version control system backend


%files svn
#-------------------------------------------------------------------------------
%package hg
Summary:        A flexible project management web application - mercurial backend
Group:          Networking/WWW
Requires:       mercurial
Provides:       %{name}-hg  = %{version}-%{release}
Provides:       %{name}-scm = %{version}-%{release}

%description hg
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use mercurial as redmine's
version control system backend


%files hg
#-------------------------------------------------------------------------------
%package bzr
Summary:        A flexible project management web application - bzr backend
Group:          Networking/WWW
Requires:       bzr
Provides:       %{name}-bzr = %{version}-%{release}
Provides:       %{name}-scm = %{version}-%{release}

%description bzr
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use bazaar as redmine's
version control system backend


%files bzr
#-------------------------------------------------------------------------------
%package cvs
Summary:        A flexible project management web application - cvs backend
Group:          Networking/WWW
Requires:       cvs
Provides:       %{name}-cvs = %{version}-%{release}
Provides:       %{name}-scm = %{version}-%{release}

%description cvs
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use cvs as redmine's
version control system backend


%files cvs
#-------------------------------------------------------------------------------

%prep
%setup -q

%build
find . -name ".gitignore" -exec rm {} \;
perl -pi -e 's!/usr/local/bin/ruby!/usr/bin/env ruby!' lib/faster_csv.rb

%install
install -d %{buildroot}%{_var}/www/%{name}
cp -rf * %{buildroot}%{_var}/www/%{name}

# Don’t include bundled rails
rm -rf %{buildroot}%{_var}/www/%{name}/vendor/rails

# Copy database.yml.example as it’s mandatory to run redmine
cp %{buildroot}%{_var}/www/%{name}/config/database.yml.example %{buildroot}%{_var}/www/%{name}/config/database.yml
# Likewise, add postgresql conf
install -D -m644 %{SOURCE103} %{buildroot}%{_var}/www/%{name}/config/database.postgres.yml

# Add Logrotate script
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -D -m644 %{SOURCE101} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Add httpd default conf
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -D -m644 %{SOURCE102} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

%files
%{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%doc %{_var}/www/%{name}/README.rdoc
%dir %{_var}/www/%{name}/
%{_var}/www/%{name}/app/
%dir %{_var}/www/%{name}/config/
%doc %{_var}/www/%{name}/config/*.example
%{_var}/www/%{name}/config/environments/
%{_var}/www/%{name}/config/locales/
%{_var}/www/%{name}/config/initializers/
%{_var}/www/%{name}/config/routes.rb
%{_var}/www/%{name}/config/boot.rb
%{_var}/www/%{name}/config/environment.rb
%{_var}/www/%{name}/config/settings.yml
%{_var}/www/%{name}/db/
%{_var}/www/%{name}/doc/
%{_var}/www/%{name}/extra/
# Directory has to be owned by the user under which the webserver runs
# Since apache is the preferred webserver for many people simplify the
# process for those users, but it sucks, all webservers should belong
# to the same user :-(
%attr(0755,apache,apache) %{_var}/www/%{name}/files/
%{_var}/www/%{name}/lib/
%attr(0755,apache,apache) %{_var}/www/%{name}/log/
%{_var}/www/%{name}/public/
%{_var}/www/%{name}/Rakefile
%{_var}/www/%{name}/script/
%{_var}/www/%{name}/test/
%attr(0755,apache,apache) %{_var}/www/%{name}/tmp/
%{_var}/www/%{name}/vendor/
%{_var}/www/%{name}/Gemfile
%{_var}/www/%{name}/config.ru
%{_var}/www/%{name}/config/application.rb
%{_var}/www/%{name}/config/preinitializer.rb
%{_var}/www/%{name}/plugins/README
