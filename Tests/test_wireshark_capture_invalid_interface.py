from GlowingWaffle import GlowingWaffle
import pytest
import subprocess
# Tests that the wireshark_capture() method raises an exception when called with an invalid interface name. 
def test_wireshark_capture_invalid_interface(self):
    # Test that the wireshark_capture() method raises an exception when called with an invalid interface name
    target = '192.168.1.1'
    gw = GlowingWaffle(target)
    with pytest.raises(subprocess.CalledProcessError):
        gw.wireshark_capture()