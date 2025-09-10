import bluetooth
from Foundation import NSObject, NSRunLoop, NSDate
import CoreBluetooth
import objc

CBCentralManagerDelegate = objc.protocolNamed("CBCentralManagerDelegate")

class ScanDelegate(NSObject, protocols=[CBCentralManagerDelegate]):
    def init(self):
        self = objc.super(ScanDelegate, self).init()
        self.devices = set()
        return self

    def centralManagerDidUpdateState_(self, manager):
        if manager.state() == 5:  # 5 == PoweredOn
            manager.scanForPeripheralsWithServices_options_(None, None)

    def centralManager_didDiscoverPeripheral_advertisementData_RSSI_(
        self, manager, peripheral, advData, RSSI
    ):
        name = peripheral.name() or "Unknown"
        addr = peripheral.identifier().UUIDString()
        if addr not in self.devices:
            self.devices.add(addr)
            print(f"Found: {name} [{addr}]")

def main():
    delegate = ScanDelegate.alloc().init()
    manager = CoreBluetooth.CBCentralManager.alloc().initWithDelegate_queue_options_(
        delegate, None, None
    )
    print("Scanning for Bluetooth devices (BLE)...")
    NSRunLoop.currentRunLoop().runUntilDate_(NSDate.dateWithTimeIntervalSinceNow_(8.0))

if __name__ == "__main__":
    main()