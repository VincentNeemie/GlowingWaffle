from GlowingWaffle import GlowingWaffle
target = "192.168.1.1"
report = GlowingWaffle(target)
report.nmap_scan()
report.wireshark_capture()
report.metasploit_exploit()
report.create_report()