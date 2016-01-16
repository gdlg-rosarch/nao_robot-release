Name:           ros-indigo-nao-apps
Version:        0.5.13
Release:        0%{?dist}
Summary:        ROS nao_apps package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-indigo-catkin

%description
Applications for NAO using the NAOqi API

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Jan 16 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.13-0
- Autogenerated by Bloom

* Fri Jan 01 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.12-0
- Autogenerated by Bloom

* Tue Aug 11 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.11-0
- Autogenerated by Bloom

* Fri Jul 31 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.10-0
- Autogenerated by Bloom

* Thu Jul 30 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.9-0
- Autogenerated by Bloom

* Tue Apr 28 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.7-0
- Autogenerated by Bloom

* Fri Feb 27 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.6-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.5-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.4-0
- Autogenerated by Bloom

