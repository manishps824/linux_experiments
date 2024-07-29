import dbus

class SystemdManager:

    def __init__(self):
        self.sysbus = dbus.SystemBus()
        self.systemd1 = self.sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        self.manager = dbus.Interface(self.systemd1, 'org.freedesktop.systemd1.Manager')
    
    def list_systemctl_services(self):
        for service in self.sysbus.list_names():
            print(service)

    def list_unit_files(self):
        unit_files = self.manager.ListUnitFiles()
        for unit in unit_files:
            print(unit)

    def stop_unit(self, unit_name):
        res = self.manager.StopUnit(unit_name, 'fail')

    def start_unit(self, unit_name):
        res = self.manager.StartUnit(unit_name, 'fail')

if __name__ == "__main__":
    sysman = SystemdManager()
#    sysman.list_unit_files()
    sysman.stop_unit('postgresql.service')
    sysman.start_unit('postgresql.service')

