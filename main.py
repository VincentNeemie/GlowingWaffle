import logging
from GlowingWaffle import GlowingWaffle


def main(target_ip):
    # Configure logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('pen_test.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Create a GlowingWaffle object with the target IP address or hostname
    with GlowingWaffle(target_ip) as gw:
        # Perform an Nmap scan
        gw.nmap_scan()
        logger.info('Nmap scan results:')
        logger.info(gw.nmap_results)

        # Capture packets using Wireshark
        gw.wireshark_capture()
        logger.info('Packet capture complete')

        # Exploit the target using Metasploit
        gw.metasploit_exploit()
        logger.info('Metasploit exploit results:')
        logger.info(gw.metasploit_results)

        # Generate a PDF report
        pdf_name = gw.create_report()
        logger.info(f'PDF report generated: {pdf_name}')


if __name__ == '__main__':
    # Get the target IP address from user input
    target_ip = input('Enter the target IP address: ')
    main(target_ip)