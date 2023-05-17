from GlowingWaffle import GlowingWaffle
    # Tests that the create_report() method generates a PDF report with the correct information from the nmap_results, wireshark_results, and metasploit_results attributes. 
def test_create_report(self, mocker):
    # Set up mock attributes for GlowingWaffle object
    target = '192.168.1.1'
    nmap_results = 'Nmap scan results'
    wireshark_results = 'Wireshark capture results'
    metasploit_results = 'Metasploit exploit results'
    gw = GlowingWaffle(target)
    gw.nmap_results = nmap_results
    gw.wireshark_results = wireshark_results
    gw.metasploit_results = metasploit_results

    # Set up mock for ReportLab canvas
    mock_canvas = mocker.Mock()
    mocker.patch('reportlab.pdfgen.canvas.Canvas', return_value=mock_canvas)

    # Call create_report() method and assert that PDF is generated with correct information
    pdf_name = gw.create_report()
    assert pdf_name == 'pen_test_report.pdf'
    mock_canvas.drawString.assert_any_call(100, 750, 'Penetration Testing Report')
    mock_canvas.drawString.assert_any_call(100, 700, 'Nmap Results:')
    mock_canvas.drawString.assert_any_call(100, 650, nmap_results)
    mock_canvas.drawString.assert_any_call(100, 550, 'Wireshark Results:')
    mock_canvas.drawString.assert_any_call(100, 500, wireshark_results)
    mock_canvas.drawString.assert_any_call(100, 400, 'Metasploit Results:')
    mock_canvas.drawString.assert_any_call(100, 350, metasploit_results)
    mock_canvas.save.assert_called_once()