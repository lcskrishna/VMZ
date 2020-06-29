wget https://github.com/opencv/opencv/archive/3.4.0.zip -O opencv-3.4.0.zip
unzip opencv-3.4.0.zip
cd opencv-3.4.0
mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local -DBUILD_SHARED_LIBS=ON ..
make -j
make install
ldconfig
