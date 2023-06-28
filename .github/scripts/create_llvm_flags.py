import sys

lookup_build_flags= {
    "Release" : "-DBUILD_TYPE=Release",
    "ReleaseAssert" : "-DBUILD_TYPE=Release -DLLVM_ENABLE_ASSERTIONS=ON",
    "Release" : "-DBUILD_TYPE=Release",
}
print(sys.argv)