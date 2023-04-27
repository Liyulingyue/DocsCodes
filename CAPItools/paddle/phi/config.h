// Header file generated by paddle/phi/CMakeLists.txt

// Generate a compilation configuration to avoid compilation errors or
// incompatibilities caused by using phi without defining a phi compilation
// macro. At the same time, configuration file definition macros are more
// readable than those defined through the compilation option `-D`.

#pragma once

#undef ON
#undef OFF
#define ON 1
#define OFF 0

// WITH_MKLDNN
#if ON
#undef PADDLE_WITH_MKLDNN
#define PADDLE_WITH_MKLDNN
#endif

// WITH_CUSTOM_DEVICE
#if OFF
#undef PADDLE_WITH_CUSTOM_DEVICE
#undef PADDLE_WITH_CUSTOM_KERNEL
#define PADDLE_WITH_CUSTOM_DEVICE
#define PADDLE_WITH_CUSTOM_KERNEL
#endif

// WITH_ARM
#if OFF
#undef PADDLE_WITH_ARM
#define PADDLE_WITH_ARM
#endif

#undef ON
#undef OFF
