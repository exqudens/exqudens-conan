from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration


class ConanConfiguration(ConanFile):
    name = "glm"
    version = "0.9.9.8"
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
        self.copy("*")
        if (
            self.settings.arch == "x86"
            and self.settings.os == "Windows"
            and self.settings.compiler == "Visual Studio"
            and self.settings.compiler.version == 16
            and self.settings.compiler.runtime == "MD"
            and self.settings.build_type == "Release"
            and self.options.type == "interface"
        ):
            self.copy(src="build/glm", pattern="*.*", dst="include")
        elif (
            self.settings.arch == "x86_64"
            and self.settings.os == "Windows"
            and self.settings.compiler == "Visual Studio"
            and self.settings.compiler.version == 16
            and self.settings.compiler.runtime == "MD"
            and self.settings.build_type == "Release"
            and self.options.type == "interface"
        ):
            self.copy(src="build/glm", pattern="*.*", dst="include")
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


if __name__ == "__main__":
    pass
