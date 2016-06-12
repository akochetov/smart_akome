window.App = window.App || {};

window.App.datacontext = (function () {

    var datacontext = {
        getDevices: getDevices,
        createDevice: createDevice,
        createSignal: createSignal,
        saveNewDevice: saveNewDevice,
        saveChangedDevice: saveChangedDevice,
        deleteDevice: deleteDevice,
        triggerSignal: triggerSignal
    };

    return datacontext;

    function getDevices(devicesObservable, errorObservable) {
        return ajaxRequest("get", deviceUrl())
            .done(getSucceeded)
            .fail(getFailed);

        function getSucceeded(data) {
            var mappeddevices = $.map(data, function (list) { return new createDevice(list); });
            devicesObservable(mappeddevices);
        }

        function getFailed() {
            errorObservable("Error retrieving devices.");
        }
    }
    function createDevice(data) {
        return new datacontext.Device(data); 
    }
    function saveNewDevice(device) {
        clearErrorMessage(device);
        return ajaxRequest("post", deviceUrl(), device)
            .done(function (result) {
                device.ID = result.ID;
                device.Name = result.Name;
            })
            .fail(function () {
                device.errorMessage("Error adding a device.");
            });
    }
    function deleteDevice(device) {
        return ajaxRequest("delete", deviceUrl(device.ID))
            .fail(function () {
                device.errorMessage("Error removing device.");
            });
    }
    function saveChangedDevice(device) {
        clearErrorMessage(device);
        return ajaxRequest("put", deviceUrl(device.ID), device, "text")
            .fail(function () {
                device.errorMessage("Error updating the device. Please make sure it is non-empty.");
            });
    }


    function getSignals(devicesObservable, errorObservable) {
        
        return ajaxRequest("get", signalUrl())
            .done(getSucceeded)
            .fail(getFailed);

        function getSucceeded(data) {
            var mappedsignals = $.map(data, function (list) { return new createSignal(list); });
            devicesObservable(mappedsignals);
        }

        function getFailed() {        
            errorObservable("Error retrieving devices.");
        }
    }
    function createSignal(data) {
        return new datacontext.Signal(data);
    }
    function triggerSignal(signal) {
        clearErrorMessage(signal);
        
        return ajaxRequest("post", signalUrl(), signal)
            .done(function (result) {
                signal.ID = signal.ID;             
            })
            .fail(function () {
                signal.errorMessage("Error triggering a signal.");
            });
    }

    // Private
    function clearErrorMessage(entity) { entity.errorMessage(null); }    
    function ajaxRequest(type, url, data, dataType) { // Ajax helper
        var options = {
            dataType: dataType || "json",
            contentType: "application/json",
            cache: false,
            type: type,
            data: data ? data.toJson() : null
        };

        var antiForgeryToken = $("#antiForgeryToken").val();
        if (antiForgeryToken) {
            options.headers = {
                'RequestVerificationToken': antiForgeryToken
            }
        }

        return $.ajax(url, options);
    }
    // routes
    function deviceUrl(id) { return "/api/device/" + (id || ""); }
    function signalUrl(id) { return "/api/signaltrigger/" + (id || ""); }
})();