# Script generated with Bloom
pkgdesc="ROS - Applications for NAO using the NAOqi API"


pkgname='ros-kinetic-nao-apps'
pkgver='0.5.15_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-trajectory-msgs'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-geometry-msgs'
'ros-kinetic-humanoid-nav-msgs'
'ros-kinetic-naoqi-bridge'
'ros-kinetic-naoqi-bridge-msgs'
'ros-kinetic-naoqi-driver'
'ros-kinetic-naoqi-driver-py'
'ros-kinetic-naoqi-pose'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
)

conflicts=()
replaces=()

_dir=nao_apps
source=()
md5sums=()

prepare() {
    cp -R $startdir/nao_apps $srcdir/nao_apps
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

