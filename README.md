# Ghat
A "Wabi Sabi" created Visual Music Displaying LED G-hat  
<html>
<body>
<h1> Welcome to setting up your Wifi controlled Led Awesome Hat </h1>

<h2> Part 1 </h2>
<h3> Installing the Unicorn Led Hat library to run the led and talk to the neo pixels</h3>

<code>
curl https://get.pimoroni.com/unicornhathd | bash
</code>
<br>

<h2>Part 2 Install the server</h2> 

<code>
wget https://gist.github.com/isc30/aa80d81df44de8a91dc0a82d55806381/raw/install.bash
<br>
sudo bash install.bash
</code>
<h3>Server script installs PHP7 + Nginx + MySQL + PhpMyAdmin 
(set florets as password) </h3>

<h2>Part 3 </h2> <h3>Set root permision to run code / sudo commands using php website 
Add sudo abilities to websites by this </h3>
must be root
<br>
<code> sudo su </code>
<code>  sudo visudo </code> <br>
(then add this under the root line) <br> <code>
www-data ALL = NOPASSWD: ALL </code>
<br>
When done the part should look like...
<br>

# User privilege specification <br>
root    ALL=(ALL:ALL) ALL <br>
www-data ALL = NOPASSWD: ALL <br>

<h2>Part 4</h2><h3>Copy My Website  and python linked php code folder to this directory </h3>

/var/www/default/public



<h2>Part 5</h2> <h3> Setup the Access point / Hotspot networking </h3> 

https://github.com/mellow-hype/wifi-berry
<br>
Before installing, install these dependencies if they have not been installed already.<br>
<code>
sudo apt-get install python3 python3-setuptools git
</code><br>
<h4>Installation</h4>


git clone https://github.com/mellow-hype/wifi-berry.git <br>
cd wifi-berry <br>
sudo python3 setup.py install <br>
<h2>Part 5B</h2> <h3> Tweek network interfaces by adding ethernet to connect to internet via dhcp</h3> 
<i>add this to network  interface configuration
</i><br>
<b>
sudo nano /etc/network/interfaces <br>
auto eth0<br>
allow-hotplug eth0<br>
iface eth0 inet dhcp <br>
</b>

whole file looks like <br> <p>
  GNU nano 2.7.4            File: /etc/network/interfaces                       

# wifi-berry static IP settings (/etc/network/interfaces)
auto lo
iface lo inet loopback

auto eth0
allow-hotplug eth0
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet static
    address 172.24.1.1
    netmask 255.255.255.0
    network 172.24.1.0
    broadcast 172.24.1.255
#    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

allow-hotplug wlan1
iface wlan1 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
</p>

</body>

</html>
