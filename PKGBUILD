# Script generated with Bloom
pkgdesc="ROS - <p>The nao_robot metapackage contains some useful nodes to integrate the Nao humanoid robot into ROS. Check out the <a href="http://www.ros.org/wiki/nao_extras">nao_extras stack</a> for more functionality. The <a href="http://www.ros.org/wiki/humanoid_navigation"> humanoid_navigation stack</a> contains some more general packages for humanoid/biped robots.</p>"
url='http://www.ros.org/wiki/nao_robot'

pkgname='ros-kinetic-nao-robot'
pkgver='0.5.15_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-nao-apps'
'ros-kinetic-nao-bringup'
'ros-kinetic-nao-description'
)

conflicts=()
replaces=()

_dir=nao_robot
source=()
md5sums=()

prepare() {
    cp -R $startdir/nao_robot $srcdir/nao_robot
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

