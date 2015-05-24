Name:           ros-indigo-robot-controllers
Version:        0.4.0
Release:        0%{?dist}
Summary:        ROS robot_controllers package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-kdl-parser
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-orocos-kdl
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-robot-controllers-interface
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-tf-conversions
Requires:       ros-indigo-trajectory-msgs
Requires:       ros-indigo-urdf
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-kdl-parser
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-orocos-kdl
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-robot-controllers-interface
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-tf-conversions
BuildRequires:  ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-urdf

%description
Some basic robot controllers for use with robot_controllers_interface.

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
* Sat May 23 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.4.0-0
- Autogenerated by Bloom

* Sat Mar 28 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.3.1-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.3.0-0
- Autogenerated by Bloom

* Fri Mar 13 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.1.4-0
- Autogenerated by Bloom

* Wed Jan 28 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.1.3-0
- Autogenerated by Bloom

* Tue Jan 06 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.1.2-0
- Autogenerated by Bloom

* Mon Jan 05 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.1.1-0
- Autogenerated by Bloom

