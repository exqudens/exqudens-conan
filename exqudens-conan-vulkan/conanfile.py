from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration


class ConanConfiguration(ConanFile):
    name = "vulkan"
    version = "1.2.182.0"
    settings = {
        "arch": ["x86_64", "x86"],
        "os": ["Windows"],
        "compiler": {
            "Visual Studio": {
                "version": ["16"],
                "runtime": ["MD", "MT"]
            }
        },
        "build_type": ["Release"]
    }
    options = {"type": ["interface", "static", "shared"]}

    def package(self):
        if (
            self.settings.arch == "x86"
            and self.settings.os == "Windows"
            and self.settings.compiler == "Visual Studio"
            and self.settings.compiler.version == 16
            and self.settings.compiler.runtime == "MD"
            and self.settings.build_type == "Release"
            and self.options.type == "shared"
        ):
            self.copy(src="1.2.182.0/Include", pattern="*.*", dst="include")
            self.copy(src="1.2.182.0/Lib32", pattern="*.*", dst="lib")
            self.copy(src="1.2.182.0/Bin32", pattern="*.*", dst="bin")
            self.copy(src="1.2.182.0/Tools32", pattern="*.*", dst="tools")
        elif (
            self.settings.arch == "x86"
            and self.settings.os == "Windows"
            and self.settings.compiler == "Visual Studio"
            and self.settings.compiler.version == 16
            and self.settings.compiler.runtime == "MT"
            and self.settings.build_type == "Release"
            and self.options.type == "static"
        ):
            self.copy(src="1.2.182.0/Include", pattern="*.*", dst="include")
            self.copy(src="1.2.182.0/Lib32", pattern="*.*", dst="lib")
            self.copy(src="1.2.182.0/Bin32", pattern="*.*", dst="bin")
            self.copy(src="1.2.182.0/Tools32", pattern="*.*", dst="tools")
        elif (
            self.settings.arch == "x86_64"
            and self.settings.os == "Windows"
            and self.settings.compiler == "Visual Studio"
            and self.settings.compiler.version == 16
            and self.settings.compiler.runtime == "MD"
            and self.settings.build_type == "Release"
            and self.options.type == "shared"
        ):
            self.copy(src="1.2.182.0/Include", pattern="*.*", dst="include")
            self.copy(src="1.2.182.0/Lib", pattern="*.*", dst="lib")
            self.copy(src="1.2.182.0/Bin", pattern="*.*", dst="bin")
            self.copy(src="1.2.182.0/Tools", pattern="*.*", dst="tools")
        elif (
            self.settings.arch == "x86_64"
            and self.settings.os == "Windows"
            and self.settings.compiler == "Visual Studio"
            and self.settings.compiler.version == 16
            and self.settings.compiler.runtime == "MT"
            and self.settings.build_type == "Release"
            and self.options.type == "static"
        ):
            self.copy(src="1.2.182.0/Include", pattern="*.*", dst="include")
            self.copy(src="1.2.182.0/Lib", pattern="*.*", dst="lib")
            self.copy(src="1.2.182.0/Bin", pattern="*.*", dst="bin")
            self.copy(src="1.2.182.0/Tools", pattern="*.*", dst="tools")
        else:
            raise ConanInvalidConfiguration(
                "Unsupported"
                + " 'self.settings.arch' = '" + str(self.settings.arch) + "'"
                + " 'self.settings.os' = '" + str(self.settings.os) + "'"
                + " 'self.settings.compiler' = '" + str(self.settings.compiler) + "'"
                + " 'self.settings.compiler.version' = '" + str(self.settings.compiler.version) + "'"
                + " 'self.settings.compiler.runtime' = '" + str(self.settings.compiler.runtime) + "'"
                + " 'self.settings.build_type' = '" + str(self.settings.build_type) + "'"
                + " 'self.options.type' = '" + str(self.options.type) + "'"
            )

    def package_info(self):
        if self.options.type == "interface":
            self.cpp_info.libs = []
        else:
            self.cpp_info.libs = ["vulkan-1.lib"]


if __name__ == "__main__":
    pass
