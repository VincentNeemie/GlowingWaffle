from GlowingWaffle import GlowingWaffle
import subprocess
import pytest

# Tests that the nmap_scan() method raises an exception when called with an invalid target IP address. 
def test_nmap_scan_invalid_ip(self):
    # Test that the nmap_scan() method raises an exception when called with an invalid target IP address
    target = 'invalid_ip_address'
    gw = GlowingWaffle(target)
    with pytest.raises(subprocess.CalledProcessError):
        gw.nmap_scan()