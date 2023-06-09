/* Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. */

#pragma once

#include <map>
#include <memory>
#include <string>
#include <unordered_map>
#include <vector>

#include "paddle/phi/common/place.h"
#include "paddle/phi/core/enforce.h"
#ifdef PADDLE_WITH_CUDA
#include "paddle/phi/backends/dynload/cuda_driver.h"
#include "paddle/phi/backends/dynload/nvrtc.h"
#endif
#ifdef PADDLE_WITH_HIP
#include "paddle/phi/backends/dynload/hiprtc.h"
#include "paddle/phi/backends/dynload/rocm_driver.h"
#endif

namespace phi {

class DeviceCode {
 public:
  virtual ~DeviceCode() {}
  virtual bool Compile(bool include_path = false) = 0;
  virtual void Launch(const size_t n, std::vector<void*>* args) const = 0;

  Place GetPlace() const { return place_; }
  std::string GetName() const { return name_; }

 protected:
  Place place_;
  std::string name_;
  std::string kernel_;
};

#if defined(PADDLE_WITH_CUDA) || defined(PADDLE_WITH_HIP)
class GPUDeviceCode : public DeviceCode {
 public:
  explicit GPUDeviceCode(const Place& place,
                         const std::string& name,
                         const std::string& kernel);
  bool Compile(bool include_path = false) override;
  void Launch(const size_t n, std::vector<void*>* args) const override;

  void SetNumThreads(int num_threads) { num_threads_ = num_threads; }
  void SetWorkloadPerThread(int workload_per_thread) {
    workload_per_thread_ = workload_per_thread;
  }

  static void CheckAvailableStatus();
  static bool IsAvailable() { return available_; }

 private:
#ifdef PADDLE_WITH_HIP
  bool CheckNVRTCResult(hiprtcResult result, std::string function);
#else
  bool CheckNVRTCResult(nvrtcResult result, std::string function);
#endif

  static bool available_;

  bool is_compiled_{false};
  int max_threads_{0};
  int num_threads_{1024};
  int workload_per_thread_{1};
  std::vector<char> ptx_;
#ifdef PADDLE_WITH_HIP
  hipModule_t module_;
  hipFunction_t function_;
#else
  CUmodule module_;
  CUfunction function_;
#endif
};
#endif

class DeviceCodePool {
 public:
  using DeviceCodeMap =
      std::unordered_map<std::string, std::unique_ptr<DeviceCode>>;

  explicit DeviceCodePool(const std::vector<Place>& places);

  static DeviceCodePool& Instance() {
    PADDLE_ENFORCE_NOT_NULL(
        pool,
        errors::NotFound("Need to create DeviceCodePool first, by calling "
                         "DeviceCodePool::Init(places)!"));
    return *pool;
  }

  static DeviceCodePool& Init(const std::vector<Place>& places) {
    if (pool == nullptr) {
      pool = new DeviceCodePool(places);
    }
    return *pool;
  }

  void Set(std::unique_ptr<DeviceCode>&& code);

  DeviceCode* Get(const Place& place, const std::string& name);

  size_t size(const Place& place) const {
    auto iter = device_codes_.find(place);
    if (iter == device_codes_.end()) {
      return 0;
    }
    return iter->second.size();
  }

 private:
  static DeviceCodePool* pool;
  std::map<Place, DeviceCodeMap> device_codes_;
  DISABLE_COPY_AND_ASSIGN(DeviceCodePool);
};

}  // namespace phi
