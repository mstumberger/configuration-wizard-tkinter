from Tkinter import *
from subprocess import Popen, PIPE
import socket


class SampleApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.wm_title("iDisplay Configuration Wizard")

        # Hostname frame
        self.row_hostname = Frame(self)
        self.hostname = StringVar()
        self.hostname.set(socket.gethostname())
        self.lab_hostname = Label(self.row_hostname, width=15, text="Hostname", anchor='w')
        self.ent_hostname = Entry(self.row_hostname, textvariable=self.hostname)

        self.row_hostname.pack(side=TOP, fill=X, padx=5, pady=5)
        self.lab_hostname.pack(side=LEFT)
        self.ent_hostname.pack(side=RIGHT, expand=YES, fill=X)

        # IP Address frame
        self.row_ip_address = Frame(self)
        self.lab_address = Label(self.row_ip_address, width=15, text="IP Address", anchor='w')
        self.start_ip = StringVar()
        self.start_ip.set('192.168.1.')
        self.ent_address = Entry(self.row_ip_address, width=15, textvariable=self.start_ip)
        self.ip = StringVar()
        self.ip.set('120')
        self.ip.trace('w', self.ping_ip)
        self.mywidget = Entry(self.row_ip_address, textvariable=self.ip, width=4, bd=5)
        # IP Address frame pack
        self.row_ip_address.pack(side=TOP, fill=X, padx=5, pady=5)
        self.lab_address.pack(side=LEFT)
        self.mywidget.pack(side=RIGHT, expand=YES, fill=X)
        self.ent_address.pack(side=RIGHT, expand=YES, fill=X)

        # Subnet frame
        self.row_subnet = Frame(self)
        self.lab_subnet = Label(self.row_subnet, width=15, text="Subnet", anchor='w')
        self.ent_subnet = Entry(self.row_subnet)

        self.row_subnet.pack(side=TOP, fill=X, padx=5, pady=5)
        self.lab_subnet.pack(side=LEFT)
        self.ent_subnet.pack(side=RIGHT, expand=YES, fill=X)

        # Gateway
        self.row_gateway = Frame(self)
        self.lab_gateway = Label(self.row_gateway, width=15, text="Gateway", anchor='w')
        self.ent_gateway = Entry(self.row_gateway)

        self.row_gateway.pack(side=TOP, fill=X, padx=5, pady=5)
        self.lab_gateway.pack(side=LEFT)
        self.ent_gateway.pack(side=RIGHT, expand=YES, fill=X)

        # Nameserver
        self.row_nameserver = Frame(self)
        self.lab_nameserver = Label(self.row_nameserver, width=15, text="Nameserver", anchor='w')
        self.ent_nameserver = Entry(self.row_nameserver)

        self.row_nameserver.pack(side=TOP, fill=X, padx=5, pady=5)
        self.lab_nameserver.pack(side=LEFT)
        self.ent_nameserver.pack(side=RIGHT, expand=YES, fill=X)

        # Apply settings button frame
        self.button_apply_frame = Frame(self)
        self.button_apply = Button(self.button_apply_frame, text="Apply settings", bg="green", command=self.quit)
        # Apply settings button frame
        self.button_apply_frame.pack(side=BOTTOM, fill=Y, padx=2, pady=2)
        self.button_apply.pack(side=LEFT)

        # Put on center of the screen
        self.center(self)

    def ping_ip(self, a, b, c):
        if host_is_available('192.168.1.'+self.ip.get()):
            self.mywidget.config(bg='red')
        else:
            self.mywidget.config(bg='green')
        self.mywidget.update_idletasks()

    # Move to center of the screen
    def center(self, win):
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()


def host_is_available(ip):
    cmd = ['ping', '-c', '1', '-t', '1', ip]
    process = Popen(cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return process.returncode == 0 # code=0 means available

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
