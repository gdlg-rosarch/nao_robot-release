Name:           ros-jade-nao-description
Version:        0.5.13
Release:        0%{?dist}
Summary:        ROS nao_description package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/nao_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-message-filters
Requires:       ros-jade-robot-state-publisher
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf
Requires:       ros-jade-urdf
Requires:       ros-jade-xacro
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-urdf
BuildRequires:  ros-jade-xacro

%description
Description of the Nao robot model that can be used with robot_state_publisher
to display the robot's state of joint angles.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Jan 16 2016 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.13-0
- Autogenerated by Bloom

* Fri Jan 01 2016 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.12-0
- Autogenerated by Bloom

* Tue Aug 11 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.11-0
- Autogenerated by Bloom

* Fri Jul 31 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.10-1
- Autogenerated by Bloom

* Fri Jul 31 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.10-0
- Autogenerated by Bloom

* Thu Jul 30 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.9-0
- Autogenerated by Bloom

* Fri May 01 2015 Séverin Lemaignan <severin.lemaignan@epfl.ch> - 0.5.7-0
- Autogenerated by Bloom

