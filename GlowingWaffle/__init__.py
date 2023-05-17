import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
class GlowingWaffle:
    """
    This class represents a GlowingWaffle object that performs penetration testing and generates a PDF report.
     Attributes
    ----------
    target : str
        The target IP address or hostname.
    nmap_results : str
        The results of the Nmap scan.
    wireshark_results : str
        The results of the Wireshark capture.
    metasploit_results : str
        The results of the Metasploit exploit.
    """
    def __init__(self, target):
        """
        Initializes the GlowingWaffle object.
         Parameters
        ----------
        target : str
            The target IP address or hostname.
        """
        self.target = target
        self.nmap_results = None
        self.wireshark_results = None
        self.metasploit_results = None
    def nmap_scan(self):
        """
        This method performs an Nmap scan and saves the results in the nmap_results attribute.
        """
        nmap_command = ['nmap', '-sS', '-sV', self.target]
        self.nmap_results = subprocess.run(nmap_command, stdout=subprocess.PIPE).stdout.decode('utf-8')
    def wireshark_capture(self):
        """
        This method captures packets using Wireshark and saves the results in a pcap file.
        """
        wireshark_command = ['tshark', '-i', 'eth0', '-f', 'tcp port 80', '-w', 'output.pcap']
        subprocess.run(wireshark_command)
    def metasploit_exploit(self):
        """
        This method exploits the target using Metasploit and saves the results in the metasploit_results attribute.
        """
        metasploit_command = ['msfconsole', '-q', '-x', 'use auxiliary/scanner/http/dir_scanner; set RHOSTS ' + self.target + '; run; exit']
        self.metasploit_results = subprocess.run(metasploit_command, stdout=subprocess.PIPE).stdout.decode('utf-8')
    def create_report(self):
        """
        This method generates a PDF report using ReportLab library.
        """
        # Use ReportLab to create a PDF report
        pdf_name = 'pen_test_report.pdf'
        c = canvas.Canvas(pdf_name, pagesize=letter)
        c.drawString(100, 750, 'Penetration Testing Report')
        c.drawString(100, 700, 'Nmap Results:')
        c.drawString(100, 650, self.nmap_results)
        c.drawString(100, 550, 'Wireshark Results:')
        c.drawString(100, 500, self.wireshark_results)
        c.drawString(100, 400, 'Metasploit Results:')
        c.drawString(100, 350, self.metasploit_results)
        c.save()
        # Return the name of the PDF report
        return pdf_name