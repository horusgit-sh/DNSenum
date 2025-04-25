#!/usr/bin/env python3

# Dependencies:
# python3-dnspython

# Used Modules:
import dns.zone as dz
import dns.query as dq
import dns.resolver as dr
import argparse

# Initialize Resolver-Class from dns.resolver as "NS"
NS = dr.Resolver()

# Target domain
Domain = 'inlanefreight.com'

# Set the nameservers that will be used
NS.nameservers = ['ns1.inlanefreight.com', 'ns2.inlanefreight.com']

Subdomains = []

def AXFR(domain, nameserver):

        try:
                axfr = dz.from_xfr(dq.xfr(nameserver, domain))

                if axfr:
                        print('[*] Successful Zone Transfer from {}'.format(nameserver))

                        for record in axfr:
                            sub = '{}.{}'.format(record.to_text(), domain)
                            if sub not in Subdomains:
                                Subdomains.append(sub)

        # If zone transfer fails
        except Exception as error:
                print(error)
                pass

# Main
if __name__=="__main__":

        # For each nameserver
        for nameserver in NS.nameservers:

                #Try AXFR
                AXFR(Domain, nameserver)

        # Print the results
        if Subdomains is not None:
                print('-------- Found Subdomains:')

                # Print each subdomain
                for subdomain in Subdomains:
                        print('{}'.format(subdomain))

        else:
                print('No subdomains found.')
                exit()         