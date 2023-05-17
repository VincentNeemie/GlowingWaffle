 # GlowingWaffle
 GlowingWaffle is a Python class that allows you to perform basic penetration testing on a target system and generate a PDF report of the test results.
 ## Features
 The GlowingWaffle class currently supports the following features:
- Nmap scan of the target system
- Packet capture using Wireshark
- Exploitation of the target using Metasploit
- Generation of a PDF report of the test results using ReportLab
 ## Dependencies
 To use the GlowingWaffle class, you need to have the following dependencies installed:
- Python 3.x
- Nmap
- Wireshark
- Metasploit Framework
- python-nmap module
- PyShark module
- msfrpc module
- reportlab module
 ## Usage
 To use the GlowingWaffle class, follow these steps:
1. Clone the repository or download the source code.
2. Import the GlowingWaffle class in your Python script:
from GlowingWaffle import GlowingWaffle
1. Create an instance of the GlowingWaffle class with the IP address or hostname of the target you want to test:
target = "192.168.1.1"
   waffle = GlowingWaffle(target)
1. Call the  `nmap_scan()` ,  `wireshark_capture()` , and  `metasploit_exploit()`  methods of the  `waffle`  instance to perform the respective tests:
waffle.nmap_scan()
   waffle.wireshark_capture()
   waffle.metasploit_exploit()
1. Call the  `create_report()`  method of the  `waffle`  instance to generate a PDF report of the test results:
waffle.create_report()
1. The PDF report will be saved in the same directory as the Python script. You can customize the layout of the report by modifying the  `report()`  method in the  `GlowingWaffle`  class.
 ## Example
 Here's an example usage of the GlowingWaffle class:
from GlowingWaffle import GlowingWaffle
 target = "192.168.1.1"
waffle = GlowingWaffle(target)
 waffle.nmap_scan()
waffle.wireshark_capture()
waffle.metasploit_exploit()
 waffle.create_report()
This will generate a PDF report of the security test results for the target system.
 ## License
 GlowingWaffle is available under the MIT License. See the LICENSE file for more information.
 ## Contributing
 If you find any issues with GlowingWaffle or have suggestions for new features, please open an issue or submit a pull request on GitHub. We welcome contributions from the community!
 ## Contact
 For any questions or comments, please feel free to contact me.

 ## Disclaimer of Liability:
The software provided "as is", with no warranty, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The author will not be liable for any special, incidental, consequential, or indirect damages due to loss of data or any other reason. You use this software at your own risk and you assume full responsibility and risk of loss resulting from the use or inability to use this software.