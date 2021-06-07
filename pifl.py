#!/usr/bin/env python3
import argparse
import sys
import os

AUTHOR = "Arnav Ghosh"

banner = f"""
{AUTHOR}
 ____ ___ _____ _
|  _ \_ _|  ___| |      _ __  _   _
| |_) | || |_  | |     | '_ \| | | |
|  __/| ||  _| | |___ _| |_) | |_| |
|_|  |___|_|   |_____(_) .__/ \__, |
                       |_|    |___/
"""
print(banner)

parser = argparse.ArgumentParser(description="Usually Pkg managers Don't Come with List Based Install, So here a Plugin for you ")
parser.add_argument('--package_manager', help="Select your Package Manager", default="apt")
parser.add_argument('--list', help="The List file to Look for Packages List")
parser.add_argument('--verbose', help="Check Verbosity", default="False")
args = parser.parse_args()

pkg_man = args.package_manager
pkg_man_location = os.popen(f"which {pkg_man}")
pkg_man_location = str(pkg_man_location.read()).replace('\n', '')

user = str(os.popen('whoami').read()).replace('\n', '')

if user != 'root':
	print("[-]Please Run this as root, or as sudo")
	sys.exit()

install_command = None
bypass_command = None

if args.list:
	if args.verbose == 'True':
		print(args.list)
	if os.path.exists(pkg_man_location):
		print(f"[+]Searching for {pkg_man}")
		print(f"[|]Found at {pkg_man_location}")

if 'apt' in pkg_man_location:
	install_command = "install"
	os.system(f"sh -c '{pkg_man_location} moo'")
	bypass_command = '-y'
elif 'pacman' in pkg_man_location:
	install_command = "-Sy"
	os.system(f"sh -c '{pkg_man_location} -Sy sl'")
	os.system(f"sl")
	bypass_command = "--noconfirm"
else:
	print(f"[!]It seems Like You are not Running a Debian or Arch Based Distro, So It will be Difficult for me to Install Packages")
	print("[*]Please Enter the Install Command for your Package Manager")
	print("[-]Example: \nAPT - apt install <package>\nPACMAN - pacman -Sy <package>")
	install_command = input("[+]Command: ")
	bypass_command = input("[+]Bypass Argument (Example: apt install <package> -y or pacman -Sy <package> --noconfirm): ")

print(f"{pkg_man_location} {install_command} <AnyPackage>")

packages = []

try:
	with open(args.list) as file:
		for package in file:
			package = str(package).replace('\n', '')
			if arg.verbose == "False":
				print(package)
			packages.append(package)
except:
	print("[!]There was a Error Opening the File")
	if os.path.exists(args.list):
		print("[!]Error Opening the File, Please check the Permissions")
	else:
		print("[!]Path doesn't exist!")

for package in packages:
	try:
		os.system(f"{pkg_man_location} {install_command} {package} {bypass_command}")
	except Exception as E:
		if args.verbose == 'True':
			print(E)
		print("[+]Some Error Occured!")
		newline = '\n'
		log = open(f'{os.system("date").read().replace(newline, "")}', 'w+')
		log.write(str(E))
		log.close()
		print("[-]Error Written to Log file in Current Directory")
