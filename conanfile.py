from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps

class MyProjectConan(ConanFile):
    name = "MyProject"
    version = "0.1"
    settings = "os", "arch", "compiler", "build_type"
    
    requires = [
        "boost/1.86.0",
        "fmt/7.1.3",  # Downgraded to 7.1.3
        "nlohmann_json/3.10.5",
        "spdlog/1.8.5"
    ]
    
    generators = "CMakeDeps", "CMakeToolchain"

    def layout(self):
        self.folders.source = "src"
        self.folders.build = "build"

    def generate(self):
        # Remove this line; CMakeToolchain is handled by the generator
        pass  # Not needed as `CMakeToolchain` is automatically handled

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*my_project.lib", dst="lib", keep_path=False)

    def exports_sources(self):
        return "src/*"  # Make sure source files in 'src' are included