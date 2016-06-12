window.App.deviceViewModel = (function (ko, datacontext) {
    /// <field name="devices" value="[new datacontext.device()]"></field>
    
    var devices = ko.observableArray(),    
        error = ko.observable(),
        addDevice = function () {
            var device = datacontext.createDevice();
            
            datacontext.saveNewDevice(device)
                .then(addSucceeded)
                .fail(addFailed);

            function addSucceeded() {
                
            }
            function addFailed() {
                error("Save of new device failed");
            }
        },
        deleteDevice = function (device) {
            devices.remove(device);
            datacontext.deleteDevice(device)
                .fail(deleteFailed);

            function deleteFailed() {
                
            }
        };
    
    datacontext.getDevices(devices, error); // load devices
        
    return {
        devices: devices,
        error: error,
        addDevice: addDevice,
        deleteDevice: deleteDevice
    };
    
})(ko, window.App.datacontext);

// Initiate the Knockout bindings
ko.applyBindings(window.App.deviceViewModel);
