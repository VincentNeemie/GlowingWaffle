from GlowingWaffle import GlowingWaffle
# Tests that a GlowingWaffle object is created successfully with a valid target IP address. 
def test_create_glowing_waffle_object(self):
    # Test that a GlowingWaffle object is created successfully with a valid target IP address
    target = '192.168.1.1'
    gw = GlowingWaffle(target)
    assert gw.target == target
    assert gw.nmap_results is None
    assert gw.wireshark_results is None
    assert gw.metasploit_results is None